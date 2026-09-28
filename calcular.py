# -*- coding: utf-8 -*-
"""A conta do modelo.md em Python: o PRECO quando tudo esta respondido, a FAIXA enquanto falta.

Quem roda e o agente, no code execution do claude.ai (ou no Claude Code):

    python calcular.py '{"produto": "maisa", "sistemas_cliente": [0, 1], "conversas": 800}'
    python calcular.py caso.json            # o mesmo caso, lido de um arquivo
    python calcular.py --json '{...}'       # saida em JSON
    python calcular.py --teste              # confere contra os exemplos da skill

Cada campo do caso vem de um de tres jeitos:
    respondido    um valor                 "conversas": 800
    em aberto     as opcoes possiveis      "sistemas_cliente": [0, 1, 2]    "conversas": [800, 3000]
                  com palpite              {"opcoes": [0, 1], "provavel": 0}
                  sem nada                 "?"   (usa as opcoes padrao do campo)
Campo que decide o preco e nao veio conta como "?". Os outros, se nao vierem, valem o padrao
(nao / zero), e a saida diz que foi assumido.

Com algum campo em aberto sai a FAIXA — o menor e o maior preco possiveis com as opcoes dadas —,
o preco provavel (o palpite onde houver; onde nao houver, a opcao de baixo: "na duvida, fique no de
baixo") e o quanto cada resposta, sozinha, pode subir o ano 1. Com tudo respondido sai o preco, com
a conta linha a linha, o repasse, as conferencias e os gates que se decidem por numero.

Os numeros sao os do modelo.md. Quando um mudar la, mude aqui e rode --teste.
"""
import itertools
import json
import math
import sys
from pathlib import Path

# ---------------------------------------------------------------- comuns (modelo.md)
TAXA_CONSTRUCAO = 1600      # R$ por semana-analista de item novo
PACOTE_ENTERPRISE = 0.15    # sobre o setup, com 2+ requisitos formais
PISO_SW = 925               # R$ por semana-analista, conferido contra o ano 1
MRR_MIN = 0.25              # mensalidade x 12 >= 25% do ano 1 (gate 10)
CAPTURA_ALVO = (0.10, 0.20)
CAPTURA_MAX = 0.30          # gate 13
ROI_MIN, ROI_FATIA = 200000, 0.15
GATE1_ANO1, CAL_MIN = 120000, 6   # sem prazo maximo desde a v8
DESCONTO_MAX = 0.15         # acima disso, gate 11
GESTAO = 0.15               # taxa de gestao na opcao de consumo incluso
SUSTENTACAO_ANCORA = 1 / 3  # por ano, sobre o setup do ancora: fecha os 25% do gate 10

# ---------------------------------------------------------------- Maisa
MAISA = {"M1": (14000, 1100), "M2": (30000, 1900), "M3": (55000, 3200)}
MAISA_VOL_LIMIAR, MAISA_VOL_PASSO, MAISA_VOL_VALOR = 3000, 1000, 250
MAISA_INFRA, MAISA_TOKEN, META_UTILIDADE = 185, 0.111, 0.035

# ---------------------------------------------------------------- Plum
PLUM_NUCLEO, PLUM_SISTEMA, PLUM_FONTE, PLUM_ISOLAMENTO, PLUM_WEB = 20000, 10000, 4000, 12000, 15000
PLUM_CONECTOR = 400
PLUM_FRANQUIA = [(2000, 1800), (6000, 3000), (15000, 4800)]   # ate N perguntas/mes -> plataforma
SEMANAS_POR_MES = 4.3

# ---------------------------------------------------------------- Ludi
LUDI_MODULO = {"atendimento": 24, "pedagogico": 45}          # R$ por aluno por ano
LUDI_FAIXAS = [(2000, 0.00), (5000, 0.10), (20000, 0.20), (math.inf, 0.30)]
LUDI_PISO, LUDI_IMPL_MESES, LUDI_IMPL_MIN, LUDI_SISTEMA = 1200, 2, 5000, 10000


def _r100(x):
    return int(round(x, -2))


def brl(x):
    """27200 -> 'R$ 27.200'."""
    return "R$ " + f"{x:,.0f}".replace(",", ".")


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


# ================================================================ a conta de um cenario

def nivel_maisa(sistemas_cliente, fluxos_proprios=0, regras_por_unidade=False, multicanal=False):
    """As quatro perguntas do modelo.md, em ordem: sistemas do cliente, regras por unidade, outro
    canal, fluxo proprio. Conta so os sistemas DO CLIENTE (depois da decisao deles x nosso).
    fluxos_proprios = processos que a Maisa executa SOZINHA, com efeito fora da conversa (cobrar,
    campanha ativa, orcamento fechado). Teste do humano: se alguem da empresa recebe e decide, nao
    conta — e M1.
    """
    if sistemas_cliente >= 3 or multicanal or fluxos_proprios >= 2:
        return "M3"
    if sistemas_cliente >= 1 or fluxos_proprios == 1 or regras_por_unidade:
        return "M2"
    return "M1"


def _fechar(conta, setup_tabela, mensal, sw_novos, pacote, desconto, ganho_anual, alternativa_anual,
            sw, semanas):
    """Setup, ano 1 e conferencias — iguais nos tres produtos."""
    novos = sw_novos * TAXA_CONSTRUCAO
    setup = (setup_tabela + novos) * (1 + (PACOTE_ENTERPRISE if pacote else 0))
    setup = _r100(setup * (1 - desconto))
    if novos:
        conta += [("itens novos", f"{sw_novos} sw × {brl(TAXA_CONSTRUCAO)}", novos)]
    if pacote:
        conta += [("pacote enterprise", "× 1,15 no setup", None)]
    if desconto:
        conta += [("desconto no setup", pct(desconto), None)]
    ano1 = setup + 12 * mensal

    roi = False
    if ganho_anual >= ROI_MIN and ano1 / ganho_anual < CAPTURA_ALVO[0]:
        roi = True
        ano1 = _r100(ROI_FATIA * ganho_anual)
        setup = ano1 - 12 * mensal
        conta += [("modo ROI-âncora", f"ano 1 = 15% de {brl(ganho_anual)}; o setup absorve", None)]

    captura = ano1 / ganho_anual if ganho_anual else None
    piso = sw * PISO_SW if sw else None
    mrr = 12 * mensal / ano1
    gates = []
    if ano1 > GATE1_ANO1:
        gates.append(1)
    if roi:
        gates.append(9)
    if mrr < MRR_MIN - 1e-9:
        gates.append(10)
    if desconto > DESCONTO_MAX or (piso and ano1 < piso):
        gates.append(11)
    if captura and captura > CAPTURA_MAX:
        gates.append(13)
    avisos = []
    if alternativa_anual and alternativa_anual < ano1 / 2:
        avisos.append("a alternativa custa menos da metade do ano 1: diga em reais o que o NI entrega "
                      "além dela, ou não venda")
    if semanas and semanas < CAL_MIN:
        avisos.append("menos de 6 semanas: costuma faltar etapa (mobilização, acessos, go-live)")
    return {"conta": conta, "setup": setup, "mensalidade": mensal, "ano1": ano1, "captura": captura,
            "piso": piso, "mrr": mrr, "roi_ancora": roi, "gates": gates, "avisos": avisos,
            "ganho_anual": ganho_anual, "sw": sw}


def maisa(sistemas_cliente, conversas, fluxos_proprios=0, regras_por_unidade=False, multicanal=False,
          templates=0, sw_novos=0, pacote=False, desconto=0.0, ganho_anual=0, alternativa_anual=0,
          sw=0, semanas=0, nivel=None, provedor_gestor=False):
    nivel = nivel or nivel_maisa(sistemas_cliente, fluxos_proprios, regras_por_unidade, multicanal)
    setup_tab, mensal_tab = MAISA[nivel]
    extra = MAISA_VOL_VALOR * math.ceil((conversas - MAISA_VOL_LIMIAR) / MAISA_VOL_PASSO) \
        if conversas > MAISA_VOL_LIMIAR else 0
    mensal = mensal_tab + extra
    conta = [("nível", f"{sistemas_cliente} sistema(s) do cliente", nivel),
             ("setup da tabela", nivel, setup_tab),
             ("mensalidade da tabela", nivel, mensal_tab),
             ("adicional de volume", f"{conversas:,} conversas/mês".replace(",", "."), extra)]
    r = _fechar(conta, setup_tab, mensal, sw_novos, pacote, desconto, ganho_anual, alternativa_anual,
                sw, semanas)
    repasse = MAISA_INFRA + conversas * MAISA_TOKEN + templates * META_UTILIDADE
    r.update(produto="maisa", nivel=nivel, repasse=round(repasse),
             consumo_incluso={"mensalidade": round(mensal + repasse * (1 + GESTAO)),
                              "franquia_conversas": round(conversas * 1.2),
                              "excedente_por_conversa": round(MAISA_TOKEN * (1 + GESTAO), 3)})
    if provedor_gestor:
        r["gates"] = sorted(r["gates"] + [4])
    return r


def plum(sistemas, perguntas, fontes_extras=0, isolamento=False, plataforma_web=False, sw_novos=0,
         pacote=False, desconto=0.0, ganho_anual=0, alternativa_anual=0, sw=0, semanas=0):
    setup_tab = (PLUM_NUCLEO + sistemas * PLUM_SISTEMA + fontes_extras * PLUM_FONTE
                 + (PLUM_ISOLAMENTO if isolamento else 0) + (PLUM_WEB if plataforma_web else 0))
    faixa = next(((ate, v) for ate, v in PLUM_FRANQUIA if perguntas <= ate), None)
    plataforma = faixa[1] if faixa else PLUM_FRANQUIA[-1][1]
    mensal = plataforma + sistemas * PLUM_CONECTOR
    conta = [("núcleo", "", PLUM_NUCLEO),
             ("sistemas de terceiro", f"{sistemas} × {brl(PLUM_SISTEMA)}", sistemas * PLUM_SISTEMA),
             ("fontes próprias extras", f"{fontes_extras} × {brl(PLUM_FONTE)}", fontes_extras * PLUM_FONTE),
             ("isolamento por pessoa", "", PLUM_ISOLAMENTO if isolamento else 0),
             ("plataforma web", "", PLUM_WEB if plataforma_web else 0),
             ("plataforma mensal", f"{perguntas:,} perguntas/mês, usuários ilimitados".replace(",", "."),
              plataforma),
             ("conectores", f"{sistemas} × {brl(PLUM_CONECTOR)}/mês", sistemas * PLUM_CONECTOR)]
    r = _fechar(conta, setup_tab, mensal, sw_novos, pacote, desconto, ganho_anual, alternativa_anual,
                sw, semanas)
    if isolamento:
        r["gates"] = sorted(r["gates"] + [8])
    if not faixa:
        r["avisos"].append("acima de 15.000 perguntas/mês: plataforma sob medida — escale")
    r.update(produto="plum", nivel=f"{sistemas} sistema(s)", repasse=None)
    return r


def ludi_anual(alunos, preco):
    """Desconto por faixa, como imposto de renda: cada faixa so vale para os alunos dentro dela."""
    total, ini = 0.0, 0
    for ate, desc in LUDI_FAIXAS:
        n = max(0, min(alunos, ate) - ini)
        total += n * preco * (1 - desc)
        ini = ate
    return total


def ludi(alunos, atendimento=True, pedagogico=False, sistemas_academicos=0, sw_novos=0, pacote=False,
         desconto=0.0, ganho_anual=0, alternativa_anual=0, sw=0, semanas=0):
    anual = (ludi_anual(alunos, LUDI_MODULO["atendimento"]) if atendimento else 0) \
        + (ludi_anual(alunos, LUDI_MODULO["pedagogico"]) if pedagogico else 0)
    mensal = max(round(anual / 12), LUDI_PISO)
    impl = max(LUDI_IMPL_MESES * mensal, LUDI_IMPL_MIN)
    setup_tab = impl + sistemas_academicos * LUDI_SISTEMA
    conta = [("anual por aluno", f"{alunos:,} alunos".replace(",", "."), round(anual)),
             ("mensalidade", "o maior entre anual ÷ 12 e o piso", mensal),
             ("implantação", f"o maior entre 2 mensalidades e {brl(LUDI_IMPL_MIN)}", impl),
             ("sistemas acadêmicos", f"{sistemas_academicos} × {brl(LUDI_SISTEMA)}",
              sistemas_academicos * LUDI_SISTEMA)]
    r = _fechar(conta, setup_tab, mensal, sw_novos, pacote, desconto, ganho_anual, alternativa_anual,
                sw, semanas)
    r.update(produto="ludi", nivel="+".join(m for m, on in (("atendimento", atendimento),
                                                             ("pedagogico", pedagogico)) if on),
             anual=round(anual), repasse=None)
    return r


def ancora(sw_construcao, pacote=False, piso_mensal=0, ganho_anual=0, sw=0, semanas=0):
    """Produto inteiro novo para o cliente: construcao + sustentacao (setup / 36 por mes), sem tabela
    por unidade. piso_mensal: no Ludi, R$ 1.200."""
    construcao = sw_construcao * TAXA_CONSTRUCAO
    setup = construcao * (1 + (PACOTE_ENTERPRISE if pacote else 0))
    mensal = max(math.ceil(SUSTENTACAO_ANCORA * setup / 12 / 100 - 1e-9) * 100, piso_mensal)
    conta = [("construção", f"{sw_construcao} sw × {brl(TAXA_CONSTRUCAO)}", construcao),
             ("sustentação", "setup ÷ 36, para cima a R$ 100", mensal)]
    r = _fechar(conta, construcao, mensal, 0, pacote, 0.0, ganho_anual, 0, sw or sw_construcao, semanas)
    r.update(produto="ancora", nivel="âncora", repasse=None)
    return r


# ================================================================ os campos de cada produto
# nome -> (rotulo para o comercial, opcoes quando vier "?", decide o preco?)
# "decide o preco" = se nao vier no caso, conta como em aberto, e aparece no painel como FALTA.
# opcoes None = nao existe faixa padrao: o agente tem de dar as opcoes.

NIVEL_4 = ("sistemas_cliente", "regras_por_unidade", "multicanal", "fluxos_proprios")
COMUNS = {
    "pacote": ("pacote enterprise (2+ requisitos formais: SSO, LGPD, homologação...)", [False, True], False),
    "sw_novos": ("equipe do item novo (semanas-analista, do PM)", None, False),
    "desconto": ("desconto no setup", None, False),
    "ganho_anual": ("ganho anual declarado pelo cliente", None, False),
    "alternativa_anual": ("custo anual da alternativa do cliente", None, False),
    "sw": ("dimensionamento (semanas-analista) para o piso", None, False),
    "semanas": ("semanas de calendário", None, False),
}
CAMPOS = {
    "maisa": {
        "nivel": ("nível M1 / M2 / M3", ["M1", "M2", "M3"], False),
        "sistemas_cliente": ("sistemas DO CLIENTE que a Maísa lê ou escreve", [0, 1, 3], True),
        "regras_por_unidade": ("unidades com regras diferentes", [False, True], True),
        "multicanal": ("outro canal além do WhatsApp", [False, True], True),
        "fluxos_proprios": ("processos que a Maísa faz sozinha, sem ninguém aprovar", [0, 1, 2], True),
        "conversas": ("conversas por mês", [0, 3000], True),
        "templates": ("mensagens de template por mês (só para o repasse)", None, False),
        "provedor_gestor": ("agenda em provedor-gestor (Booksy, Trinks...)", [False, True], False),
        **COMUNS,
    },
    "plum": {
        "sistemas": ("sistemas de terceiro lidos por API", [0, 1, 3], True),
        "perguntas": ("perguntas por mês", [2000, 6000, 15000], True),
        "pessoas": ("pessoas que vão perguntar", None, False),
        "perguntas_semana": ("perguntas por pessoa por semana", None, False),
        "isolamento": ("cada pessoa só vê o próprio dado", [False, True], True),
        "fontes_extras": ("outras bases próprias do cliente", [0, 1, 2], False),
        "plataforma_web": ("plataforma web (SSO, perfis, painel)", [False, True], False),
        **COMUNS,
    },
    "ludi": {
        "alunos": ("alunos ativos", None, True),
        "atendimento": ("módulo Atendimento", [False, True], False),
        "pedagogico": ("módulo Pedagógico", [False, True], True),
        "sistemas_academicos": ("sistemas acadêmicos integrados", [0, 1], True),
        **COMUNS,
    },
    "ancora": {
        "sw_construcao": ("construção (semanas-analista, do PM)", None, True),
        "piso_mensal": ("piso mensal (Ludi: 1.200)", None, False),
        **{k: v for k, v in COMUNS.items() if k in ("pacote", "ganho_anual", "sw", "semanas")},
    },
}
PADRAO = {"atendimento": True}   # o resto que nao decide o preco: nao / zero

# campos cuja faixa padrao nao tem teto: o que acontece acima dela
SEM_TETO = {
    ("maisa", "conversas"): "acima de 3.000 conversas/mês, +R$ 250/mês a cada 1.000 (R$ 3.000/ano)",
    ("maisa", "sistemas_cliente"): "3 ou mais sistemas já é M3; mais sistemas não mudam o nível",
    ("plum", "sistemas"): "cada sistema a mais soma R$ 10.000 de setup + R$ 400/mês (R$ 14.800 no ano 1)",
    ("plum", "perguntas"): "acima de 15.000 perguntas/mês é plataforma sob medida — escale",
}


class CasoInvalido(Exception):
    pass


def _norm(produto, nome, valor):
    """Devolve (opcoes, provavel, em_aberto) de um campo."""
    rotulo, padrao, _ = (CAMPOS[produto].get(nome) or (nome, None, False))
    if isinstance(valor, dict):
        opcoes, provavel = valor.get("opcoes", "?"), valor.get("provavel")
    else:
        opcoes, provavel = valor, None
    if opcoes == "?":
        if padrao is None:
            raise CasoInvalido(f"`{nome}` ({rotulo}): não tem faixa padrão — passe as opções, "
                               f"ex.: \"{nome}\": [300, 800]")
        opcoes = padrao
    if not isinstance(opcoes, list):
        return [opcoes], None, False
    if not opcoes:
        raise CasoInvalido(f"`{nome}`: lista de opções vazia")
    opcoes = sorted(set(opcoes), key=lambda v: (str(type(v)), v))
    if len(opcoes) == 1:
        return opcoes, None, False
    if provavel is not None and provavel not in opcoes:
        opcoes = sorted(set(opcoes) | {provavel}, key=lambda v: (str(type(v)), v))
    return opcoes, provavel, True


def _ler_caso(caso):
    produto = str(caso.get("produto", "")).lower().replace("í", "i").replace("â", "a")
    if produto not in CAMPOS:
        raise CasoInvalido("`produto` tem de ser maisa, plum, ludi ou ancora")
    campos = CAMPOS[produto]
    desconhecidos = [k for k in caso if k not in campos and k not in ("produto", "empresa")]
    if desconhecidos:
        raise CasoInvalido(f"campo(s) que o {produto} não conhece: {', '.join(desconhecidos)} — "
                           f"os que existem: {', '.join(campos)}")
    if "sw_novos" in caso and caso["sw_novos"] == "?":
        caso = dict(caso, sw_novos=0)
        itens_novos_pendentes = True
    else:
        itens_novos_pendentes = False
    for nome in ("desconto", "ganho_anual", "alternativa_anual", "sw", "semanas", "templates"):
        if isinstance(caso.get(nome), (list, dict)) or caso.get(nome) == "?":
            raise CasoInvalido(f"`{nome}` tem de ser um número só (ou ficar fora). Ganho em faixa: "
                               f"passe o de baixo")

    nivel_dado = produto == "maisa" and "nivel" in caso
    plum_estimado = produto == "plum" and "perguntas" not in caso and "pessoas" in caso
    fixos, abertos, assumidos = {}, {}, []
    for nome, (rotulo, padrao, decide) in campos.items():
        if nome in caso:
            opcoes, provavel, em_aberto = _norm(produto, nome, caso[nome])
            if em_aberto:
                abertos[nome] = (opcoes, provavel)
            else:
                fixos[nome] = opcoes[0]
        elif nome in ("nivel", "pessoas", "perguntas_semana") or (plum_estimado and nome == "perguntas"):
            continue
        elif decide and not (nivel_dado and nome in NIVEL_4):
            opcoes, _, _ = _norm(produto, nome, "?")
            abertos[nome] = (opcoes, None)
        elif nome in PADRAO:
            fixos[nome] = PADRAO[nome]
        else:
            fixos[nome] = False if padrao and isinstance(padrao[0], bool) else 0
            if nome in ("pacote", "provedor_gestor", "plataforma_web", "fontes_extras"):
                assumidos.append(f"{rotulo}: {'não' if fixos[nome] in (False, 0) else fixos[nome]}")
    if plum_estimado and "perguntas_semana" not in caso:
        raise CasoInvalido("para estimar as perguntas do Plum passe `pessoas` e `perguntas_semana`")
    if produto == "ludi" and not fixos.get("atendimento") and "pedagogico" in fixos and not fixos["pedagogico"]:
        raise CasoInvalido("o Ludi precisa de ao menos um módulo")
    return produto, fixos, abertos, assumidos, itens_novos_pendentes


def _avaliar(produto, v):
    """Roda a conta de UM cenario (todos os campos com um valor)."""
    base = {k: v.get(k, 0) for k in ("sw_novos", "desconto", "ganho_anual", "sw", "semanas")}
    if produto == "maisa":
        return maisa(v.get("sistemas_cliente", 0), v.get("conversas", 0), v.get("fluxos_proprios", 0),
                     v.get("regras_por_unidade", False), v.get("multicanal", False), v.get("templates", 0),
                     pacote=v.get("pacote", False), alternativa_anual=v.get("alternativa_anual", 0),
                     nivel=v.get("nivel"), provedor_gestor=v.get("provedor_gestor", False), **base)
    if produto == "plum":
        perguntas = v.get("perguntas")
        if perguntas is None:
            perguntas = round(v["pessoas"] * v["perguntas_semana"] * SEMANAS_POR_MES)
        return plum(v.get("sistemas", 0), perguntas, v.get("fontes_extras", 0), v.get("isolamento", False),
                    v.get("plataforma_web", False), pacote=v.get("pacote", False),
                    alternativa_anual=v.get("alternativa_anual", 0), **base)
    if produto == "ludi":
        return ludi(v["alunos"], v.get("atendimento", True), v.get("pedagogico", False),
                    v.get("sistemas_academicos", 0), pacote=v.get("pacote", False),
                    alternativa_anual=v.get("alternativa_anual", 0), **base)
    return ancora(v["sw_construcao"], v.get("pacote", False), v.get("piso_mensal", 0),
                  v.get("ganho_anual", 0), v.get("sw", 0), v.get("semanas", 0))


def _fmt_opcao(v):
    if isinstance(v, bool):
        return "sim" if v else "não"
    if isinstance(v, (int, float)):
        return f"{v:,.0f}".replace(",", ".")
    return str(v)


def calcular(caso):
    """O caso inteiro: preco (tudo respondido) ou faixa (algo em aberto). Devolve um dict."""
    produto, fixos, abertos, assumidos, pendente = _ler_caso(caso)
    # plum: pessoas x perguntas por semana em faixa vira faixa de perguntas
    if produto == "plum" and "perguntas" not in fixos and "perguntas" not in abertos:
        pessoas = abertos.pop("pessoas", ([fixos.pop("pessoas", 0)], None))[0]
        por_semana = abertos.pop("perguntas_semana", ([fixos.pop("perguntas_semana", 0)], None))[0]
        estimadas = sorted({round(p * q * SEMANAS_POR_MES) for p in pessoas for q in por_semana})
        if len(estimadas) == 1:
            fixos["perguntas"] = estimadas[0]
        else:
            abertos["perguntas"] = ([estimadas[0], estimadas[-1]], None)
    fixos.pop("pessoas", None)
    fixos.pop("perguntas_semana", None)

    saida = {"produto": produto, "assumido": assumidos, "itens_novos_pendentes": pendente}
    if not abertos:
        r = _avaliar(produto, fixos)
        saida.update(tipo="preco", resultado=r, entrada=fixos)
        return saida

    nomes = list(abertos)
    cenarios = []
    for combo in itertools.product(*(abertos[n][0] for n in nomes)):
        v = dict(fixos, **dict(zip(nomes, combo)))
        cenarios.append((v, _avaliar(produto, v)))
    minimo = min(cenarios, key=lambda c: c[1]["ano1"])
    maximo = max(cenarios, key=lambda c: c[1]["ano1"])
    baixo = dict(fixos, **{n: abertos[n][0][0] for n in nomes})
    r_baixo = _avaliar(produto, baixo)
    provavel = dict(fixos, **{n: (abertos[n][1] if abertos[n][1] is not None else abertos[n][0][0])
                              for n in nomes})
    r_prov = _avaliar(produto, provavel)

    impacto = []
    for n in nomes:
        variacoes =[(op, _avaliar(produto, dict(baixo, **{n: op}))) for op in abertos[n][0]]
        op_max, r_max = max(variacoes, key=lambda x: x[1]["ano1"])
        delta = r_max["ano1"] - r_baixo["ano1"]
        mudanca = ""
        if produto == "maisa" and r_max["nivel"] != r_baixo["nivel"]:
            mudanca = f"{r_baixo['nivel']} → {r_max['nivel']}"
        impacto.append({"campo": n, "rotulo": CAMPOS[produto][n][0],
                        "opcoes": [_fmt_opcao(o) for o in abertos[n][0]],
                        "ate": delta, "com": _fmt_opcao(op_max), "mudanca": mudanca,
                        "sem_teto": SEM_TETO.get((produto, n)) if caso.get(n, "?") == "?" else None})
    impacto.sort(key=lambda i: -i["ate"])

    # o que esta em aberto pode nao mexer no preco (ex.: ja e M2 por um sistema, e a outra pergunta
    # tambem so levaria a M2): ai o preco esta fechado, e o que falta vira nota, nao faixa
    if all(c[1]["setup"] == r_baixo["setup"] and c[1]["mensalidade"] == r_baixo["mensalidade"]
           for c in cenarios):
        saida.update(tipo="preco", resultado=r_baixo, entrada=baixo,
                     sem_efeito=[CAMPOS[produto][n][0] for n in nomes])
        return saida

    niveis = sorted({c[1]["nivel"] for c in cenarios})
    atencao = []
    if maximo[1]["ano1"] > GATE1_ANO1:
        atencao.append(f"no máximo da faixa o ano 1 passa de {brl(GATE1_ANO1)} (gate 1)")
    if any(8 in c[1]["gates"] for c in cenarios):
        atencao.append("se houver isolamento por pessoa, é o gate 8")
    if any(4 in c[1]["gates"] for c in cenarios):
        atencao.append("agenda em provedor-gestor é o gate 4")
    saida.update(tipo="faixa", abertos={n: [_fmt_opcao(o) for o in abertos[n][0]] for n in nomes},
                 minimo=minimo[1], maximo=maximo[1], provavel=r_prov,
                 provavel_entrada={n: _fmt_opcao(provavel[n]) for n in nomes},
                 palpites=[n for n in nomes if abertos[n][1] is not None],
                 setup=(min(c[1]["setup"] for c in cenarios), max(c[1]["setup"] for c in cenarios)),
                 mensalidade=(min(c[1]["mensalidade"] for c in cenarios),
                              max(c[1]["mensalidade"] for c in cenarios)),
                 niveis=niveis, impacto=impacto, atencao=atencao)
    return saida


# ================================================================ o texto

NOME = {"maisa": "MAÍSA", "plum": "PLUM", "ludi": "LUDI", "ancora": "ÂNCORA"}
CURTO = {"sistemas_cliente": "sistemas do cliente", "regras_por_unidade": "regras por unidade",
         "multicanal": "outro canal", "fluxos_proprios": "fluxos próprios", "conversas": "conversas/mês",
         "nivel": "nível", "pacote": "pacote enterprise", "provedor_gestor": "provedor-gestor",
         "sistemas": "sistemas", "perguntas": "perguntas/mês", "isolamento": "isolamento por pessoa",
         "fontes_extras": "fontes extras", "plataforma_web": "plataforma web", "alunos": "alunos",
         "pedagogico": "Pedagógico", "atendimento": "Atendimento",
         "sistemas_academicos": "sistemas acadêmicos", "sw_construcao": "construção (sw)"}


def _texto_faixa(s):
    p = s["produto"]
    n = len(s["abertos"])
    linhas = [f"{NOME[p]} · FAIXA PROVISÓRIA — {n} resposta(s) em aberto · interna: não diga faixa ao cliente",
              f"  setup        {brl(s['setup'][0])} a {brl(s['setup'][1])}",
              f"  mensalidade  {brl(s['mensalidade'][0])} a {brl(s['mensalidade'][1])}",
              f"  ANO 1        {brl(s['minimo']['ano1'])} a {brl(s['maximo']['ano1'])}"]
    if p == "maisa":
        niveis = s["niveis"]
        linhas.append(f"  nível        {niveis[0]}" + (f" a {niveis[-1]}" if len(niveis) > 1 else ""))
    pr = s["provavel"]
    com = ", ".join(f"{CURTO.get(k, k)} {v}" for k, v in s["provavel_entrada"].items())
    base = ("palpite onde houver, o de baixo no resto" if s["palpites"]
            else "tudo no de baixo (na dúvida, fique no de baixo)")
    linhas.append(f"  provável     {brl(pr['setup'])} + 12 × {brl(pr['mensalidade'])} = {brl(pr['ano1'])}"
                  f"{' · ' + pr['nivel'] if p == 'maisa' else ''}")
    linhas.append(f"               {base}: {com}")
    linhas.append("")
    linhas.append("O QUE MAIS MEXE NO ANO 1 — cada resposta sozinha, com o resto no de baixo (não somam)")
    for i, im in enumerate(s["impacto"], 1):
        quanto = f"até +{brl(im['ate'])}" if im["ate"] else "não muda o preço nesta faixa"
        extra = f"  {im['mudanca']}" if im["mudanca"] else ""
        linhas.append(f"  {i}. {im['rotulo']}  [{' · '.join(im['opcoes'])}]  {quanto}{extra}")
        if im["sem_teto"]:
            linhas.append(f"       {im['sem_teto']}")
    fora = []
    if s["itens_novos_pendentes"]:
        fora.append("itens novos sem dimensionamento: + R$ 1.600 por semana-analista no setup "
                    "(× 1,15 com pacote) — o PM dá a equipe; não estime")
    if fora or s["atencao"]:
        linhas.append("")
    if fora:
        linhas.append("FORA DA FAIXA")
        linhas += [f"  {f}" for f in fora]
    if s["atencao"]:
        linhas.append("ATENÇÃO")
        linhas += [f"  {a}" for a in s["atencao"]]
    if s["assumido"]:
        linhas.append("ASSUMIDO (não veio no caso)")
        linhas += [f"  {a}" for a in s["assumido"]]
    return "\n".join(linhas)


def _texto_preco(s):
    r = s["resultado"]
    p = s["produto"]
    linhas = [f"{NOME[p]} · PREÇO — tudo o que mexe no preço está respondido"]
    for rotulo, como, valor in r["conta"]:
        if rotulo in ("setup", "mensalidade", "ano 1"):
            continue
        v = brl(valor) if isinstance(valor, (int, float)) and not isinstance(valor, bool) else (valor or "")
        linhas.append(f"  {rotulo:<24} {v:<12} {como}")
    linhas.append(f"  {'SETUP':<24} {brl(r['setup'])}")
    linhas.append(f"  {'MENSALIDADE':<24} {brl(r['mensalidade'])}")
    linhas.append(f"  {'ANO 1':<24} {brl(r['setup'])} + 12 × {brl(r['mensalidade'])} = {brl(r['ano1'])}")
    if r.get("repasse"):
        ci = r["consumo_incluso"]
        linhas.append(f"  {'repasse (estimativa)':<24} ≈ {brl(r['repasse'])}/mês, fora do ano 1 · "
                      f"consumo incluso: {brl(ci['mensalidade'])}/mês, franquia de "
                      f"{_fmt_opcao(ci['franquia_conversas'])} conversas")
    elif p != "ancora":
        linhas.append(f"  {'repasse':<24} a medir no primeiro mês, fora do ano 1")
    linhas.append("CONFERÊNCIAS")
    if r["captura"] is not None:
        c = r["captura"]
        marca = "✓ alvo" if CAPTURA_ALVO[0] <= c <= CAPTURA_ALVO[1] else (
            "✓ aceitável" if CAPTURA_ALVO[1] < c <= CAPTURA_MAX else (
                "abaixo do alvo" if c < CAPTURA_ALVO[0] else "✗ gate 13"))
        linhas.append(f"  valor        {brl(r['ano1'])} ÷ {brl(r['ganho_anual'])} = captura {pct(c)} {marca}")
    else:
        linhas.append("  valor        sem ganho declarado — a pergunta tem de aparecer na saída")
    if r["piso"]:
        ok = "✓" if r["ano1"] >= r["piso"] else "✗ gate 11"
        linhas.append(f"  piso         {r['sw']} sw × {brl(PISO_SW)} = {brl(r['piso'])} {'≤' if ok == '✓' else '>'} ano 1 {ok}")
    else:
        linhas.append("  piso         não calculado — sem dimensionamento")
    ok = "✓" if r["mrr"] >= MRR_MIN - 1e-9 else "✗ gate 10"
    linhas.append(f"  recorrência  {brl(12 * r['mensalidade'])} ÷ {brl(r['ano1'])} = {pct(r['mrr'])} {ok}")
    for a in r["avisos"]:
        linhas.append(f"  aviso        {a}")
    linhas.append(f"GATES POR NÚMERO  {', '.join(map(str, r['gates'])) if r['gates'] else 'nenhum'}"
                  "  (os de julgamento — credencial, mantenedor, pesquisa — são do SKILL.md)")
    if s["itens_novos_pendentes"]:
        linhas.append("FALTA  itens novos sem dimensionamento: + R$ 1.600 por semana-analista no setup")
    if s.get("sem_efeito"):
        linhas.append("EM ABERTO, SEM EFEITO NO PREÇO — qualquer resposta dá este mesmo preço")
        linhas += [f"  {r}" for r in s["sem_efeito"]]
    if s["assumido"]:
        linhas.append("ASSUMIDO (não veio no caso)")
        linhas += [f"  {a}" for a in s["assumido"]]
    return "\n".join(linhas)


def texto(s):
    return _texto_faixa(s) if s["tipo"] == "faixa" else _texto_preco(s)


# ================================================================ conferencia

def testes():
    # preco: os casos do SKILL.md e dos exemplos resolvidos da skill
    r = maisa(sistemas_cliente=1, conversas=2400, templates=1500, ganho_anual=300000, sw=16, semanas=8)
    assert (r["nivel"], r["setup"], r["mensalidade"], r["ano1"]) == ("M2", 30000, 1900, 52800), r
    assert round(r["captura"], 3) == 0.176 and r["gates"] == [] and r["repasse"] == 504, r
    r = maisa(sistemas_cliente=0, conversas=800, templates=800, sw=12)
    assert (r["nivel"], r["ano1"], r["repasse"]) == ("M1", 27200, 302), r
    r = plum(sistemas=3, isolamento=True, perguntas=3000, sw=39)
    assert (r["setup"], r["mensalidade"], r["ano1"], r["gates"]) == (62000, 4200, 112400, [8]), r
    assert plum(sistemas=1, isolamento=True, perguntas=3000)["ano1"] == 82800
    r = ludi(alunos=1200, atendimento=True, sistemas_academicos=1, sw=12)
    assert (r["mensalidade"], r["setup"], r["ano1"]) == (2400, 15000, 43800), r
    assert ludi_anual(3000, 45) == 130500
    r = ancora(40, piso_mensal=LUDI_PISO)
    assert (r["mensalidade"], r["ano1"], r["gates"]) == (1800, 85600, []), r
    assert ancora(25)["gates"] == [], ancora(25)
    assert ancora(40, pacote=True)["gates"] == []
    assert plum(3, 3000, isolamento=True, semanas=13)["gates"] == [8]   # prazo longo nao e gate
    assert nivel_maisa(0) == "M1" and nivel_maisa(0, fluxos_proprios=1) == "M2"
    assert maisa(sistemas_cliente=0, conversas=5500)["mensalidade"] == 1100 + 3 * 250

    # o caso completo pela porta da frente da o mesmo preco
    s = calcular({"produto": "maisa", "sistemas_cliente": 1, "conversas": 2400, "regras_por_unidade": False,
                  "multicanal": False, "fluxos_proprios": 0, "templates": 1500, "ganho_anual": 300000, "sw": 16})
    assert s["tipo"] == "preco" and s["resultado"]["ano1"] == 52800, s
    s = calcular({"produto": "maisa", "nivel": "M1", "conversas": 800})
    assert s["tipo"] == "preco" and s["resultado"]["ano1"] == 27200, s

    # faixa: o que falta abre o intervalo, e a resposta que mais mexe vem primeiro
    s = calcular({"produto": "maisa", "sistemas_cliente": [0, 1], "conversas": 800,
                  "regras_por_unidade": False, "multicanal": False, "fluxos_proprios": 0})
    assert s["tipo"] == "faixa" and (s["minimo"]["ano1"], s["maximo"]["ano1"]) == (27200, 52800), s
    assert s["impacto"][0]["campo"] == "sistemas_cliente" and s["impacto"][0]["ate"] == 25600
    assert s["impacto"][0]["mudanca"] == "M1 → M2" and s["provavel"]["ano1"] == 27200
    s = calcular({"produto": "maisa", "sistemas_cliente": {"opcoes": [0, 1], "provavel": 1},
                  "conversas": 800, "regras_por_unidade": False, "multicanal": False, "fluxos_proprios": 0})
    assert s["provavel"]["ano1"] == 52800, s
    s = calcular({"produto": "maisa"})                      # nada respondido: a tabela inteira
    assert (s["minimo"]["ano1"], s["maximo"]["ano1"]) == (27200, 93400), s
    assert len(s["abertos"]) == 5
    s = calcular({"produto": "plum", "sistemas": 1, "perguntas": "?", "isolamento": "?"})
    assert (s["minimo"]["ano1"], s["maximo"]["ano1"]) == (56400, 104400), s
    s = calcular({"produto": "plum", "sistemas": 1, "isolamento": False, "pessoas": [20, 40],
                  "perguntas_semana": [5, 10]})
    assert s["tipo"] == "preco" and s["sem_efeito"] == ["perguntas por mês"], s   # 430 a 1.720: mesma faixa
    assert s["resultado"]["ano1"] == 56400, s
    s = calcular({"produto": "plum", "sistemas": 1, "isolamento": False, "pessoas": [20, 100],
                  "perguntas_semana": [5, 10]})
    assert s["abertos"] == {"perguntas": ["430", "4.300"]} and s["maximo"]["ano1"] == 70800, s
    s = calcular({"produto": "ludi", "alunos": [300, 800], "pedagogico": False, "sistemas_academicos": 0})
    assert (s["minimo"]["ano1"], s["maximo"]["ano1"]) == (19400, 24200), s
    s = calcular({"produto": "maisa", "sistemas_cliente": 1, "conversas": 1800, "regras_por_unidade": "?",
                  "multicanal": False, "fluxos_proprios": [0, 1]})     # ja e M2; o resto nao muda
    assert s["tipo"] == "preco" and s["resultado"]["ano1"] == 52800 and len(s["sem_efeito"]) == 2, s
    s = calcular({"produto": "maisa", "nivel": "M2", "conversas": 2400, "sw_novos": "?"})
    assert s["tipo"] == "preco" and s["itens_novos_pendentes"], s
    for ruim in ({"produto": "ludi"}, {"produto": "x"}, {"produto": "maisa", "ganho_anual": [1, 2]},
                 {"produto": "plum", "sistema": 1}):
        try:
            calcular(ruim)
        except CasoInvalido:
            continue
        raise AssertionError(f"devia recusar {ruim}")
    print("ok — bate com o SKILL.md e com os exemplos")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--teste":
        testes()
        return 0
    como_json = argv[0] == "--json"
    arg = argv[1] if como_json else argv[0]
    bruto = Path(arg).read_text(encoding="utf-8") if arg.endswith(".json") and Path(arg).is_file() else arg
    try:
        s = calcular(json.loads(bruto))
    except json.JSONDecodeError as e:
        print(f"o caso não é JSON válido: {e}")
        return 2
    except CasoInvalido as e:
        print(f"caso inválido: {e}")
        return 2
    print(json.dumps(s, ensure_ascii=False, indent=2, default=str) if como_json else texto(s))
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
