# Formulário de entrada

O que o comercial joga na skill antes da proposta. **Não é para preencher em ordem nem de uma vez**
— jogue o que tem, em texto corrido, transcrição de reunião, print de conversa, o que for. A skill
lê, extrai o que consegue e pergunta o que falta, **uma coisa por vez**.

## Os quatro campos bloqueantes

Sem estes quatro não sai preço, e a skill não deve inventá-los.

| # | Campo | Por que bloqueia |
| --- | --- | --- |
| **1** | **O que o cliente pediu, item por item** | é a lista que decide a rota, e a rota decide a tabela inteira |
| **2** | **Quais sistemas do cliente a solução precisa consultar ou alimentar** | cada sistema de terceiro é uma integração com prazo próprio, e o prazo não é do NI |
| **3** | **Quantas pessoas vão usar, separando quem opera de quem é atendido** | são dois eixos de custo diferentes e confundi-los erra o preço nos dois sentidos |
| **4** | **Volume mensal esperado** — atendimentos, consultas ou mensagens | é o que define a banda da mensalidade e a estimativa do repasse de tokens e conversas, que o cliente paga direto e vai perguntar quanto é |

## O campo que o comercial escolhe: o modo de risco

Antes de calcular, a skill pergunta em qual **modo de risco** rodar: 🛡️ **conservador**,
⚖️ **padrão** ou 🔥 **agressivo**. O padrão é o default e não exige nada. **Conservador exige
motivo escrito** — sem isso vira o padrão pela porta dos fundos. **Agressivo exige duas coisas:**
a pergunta de ROI respondida pelo cliente **e** decisor identificado e acessível. Faltou uma, cai
para o padrão. Ver § O modo de risco em [`modelo.md`](modelo.md).

Sobre o campo 1: **concreto, não adjetivo.** "Quer algo mais personalizado" não é resposta.
"Quer que o lembrete saia 48 h antes em vez de 24 h" é. "Quer consultar quanto sobrou do
orçamento de viagem dele" é.

---

## A · Quem é

| Campo | Se não souber |
| --- | --- |
| Cliente, setor de atuação | — |
| Área e cargo de quem está pedindo | pergunte na próxima conversa; define o `f_área`, que vale 8% no preço |
| Produto candidato: Maísa · Ludi · Plum · não sei | "não sei" é resposta válida — a skill ajuda a decidir |

**Por que a área importa:** cliente de área core fala de receita, produto e cliente final; cliente
de função-meio fala de processo e operação. É o `f_área` do multiplicador, e o fator mais subjetivo
do modelo.

## B · O que ele pediu

| Campo | Se não souber |
| --- | --- |
| **Lista item por item** (bloqueante) | volte para o cliente. É o único campo sem substituto |
| Como ele resolve isso hoje — planilha, pessoa, sistema, ninguém | assuma "ninguém" e declare a premissa |
| **Sistemas a integrar, um por nome** (bloqueante) | pergunte o nome exato. "O ERP deles" não serve: ERP diferente é preço diferente |
| Ele topa mudar o processo, ou a solução tem que caber no processo atual | assuma que tem que caber, que é o caso caro |

⚠️ **Para cada sistema nomeado, a skill vai checar a família e o status de credencial em
§ Integrações de [`modelo.md`](modelo.md).** Provedor-gestor e credencial de `parceria` mudam a proposta antes de
qualquer conta.

## C · Tamanho

| Campo | Se não souber |
| --- | --- |
| **Quantas pessoas vão operar** a solução (U) | bloqueante |
| Quantas pessoas vão **ser atendidas ou perguntar** | estime pela operação e declare |
| **Volume mensal** de atendimentos, consultas ou mensagens (V) | bloqueante — se ele não sabe, estime junto com ele na reunião |
| Tamanho da operação atendida, em pessoas | use o nº de operadores × 10 como piso grosseiro e declare |
| Faturamento, se ele falou | deixe em branco; **não** use faturamento do grupo global |

⚠️ **Porte é da operação que vai usar a solução, não do grupo econômico.** Subsidiária brasileira
prevalece sobre receita global.

## D · O retorno

| Campo | Se não souber |
| --- | --- |
| O que ele disse que ganha: horas, pessoas ou dinheiro | vá para a linha de baixo |
| **Quem disse isso e quando** | obrigatório se houver número. Ganho sem autor não sobe preço |
| Se não declarou: qual o processo hoje, quantas pessoas, quanto tempo leva | dá para construir a conta **com ele**, na reunião seguinte |

**Nunca estime o ganho por conta própria e use o seu número para subir o preço.** Se o cliente não
sabe dizer, o modo ROI-âncora não está disponível e o `f_retorno` fica em 1,00. Isso é uma perda de
receita real — e é por isso que essa pergunta vale a pena ser feita na reunião.

Conta pronta para usar com ele:

```
horas poupadas por mês × custo-hora carregado × 12 = ganho anual
custo-hora carregado = salário mensal × 1,8 ÷ 160
```

## E · Restrições

| Campo | Se não souber |
| --- | --- |
| Prazo pedido, e **por quê** — evento, auditoria, safra, virada de ano | assuma sem prazo apertado |
| Exige SLA com multa? | assuma não; se sim, é gate |
| Exige repositório ou dado segregado? LGPD, isolamento por pessoa? | assuma não; se sim, muda o custo |
| Contrato de quanto tempo ele quer | assuma 12 meses |
| **Em nome de quem ficam as contas** de LLM, nuvem e WhatsApp | assuma no nome do cliente — tokens, infra e APIs pagas são **repasse**, fora do preço. Se ficarem com o NI, repassar vira cobrança e precisa estar escrito |
| Orçamento que ele deixou escapar | deixe em branco — **nunca** ancore a proposta no número dele |
| **Algum número que a casa já disse a ele** — faixa de setup ou de mensalidade falada na reunião | responda "nenhum" só se tiver certeza. Faixa dita antes do dimensionamento vira teto na cabeça do cliente |
| **Quem aprova, e se estava na reunião** | pergunte. Autoridade é uma das causas de perda mais comuns |
| **Se existe verba nesta janela, ou só no próximo ciclo** | pergunte. Timing é a outra |
| **Quantos projetos o núcleo terá em paralelo nesta janela** | assuma 4 — é o que define o rateio de PM e Tech Lead, e ele varia de +10% a +31% |
| **Quantos projetos cada pessoa da equipe vai carregar** | assuma **1**, que é o normal hoje. 2 acontece raramente e não muda o preço; se acontecer, é sinal de que a casa finalmente vendeu o suficiente — vale avisar quem cuida do modelo |

## F · O que você não sabe

Liste. Sem enfeite.

Esta seção é a mais importante do formulário e a que costuma vir vazia. Lacuna declarada entra na
proposta como premissa e protege o time; lacuna esquecida vira retrabalho não faturado no mês
três.

---

## O que a skill devolve

1. **Rota** — configuração, extensão ou motor + domínio — com o porquê
2. **Âncora ou seguidor**, e o que isso muda no contrato
3. **Dimensionamento** em PERT, por etapa, com o prior medido de onde vier
4. **O preço** — piso, referência, multiplicador e teto de payback — com as contas à vista
5. **Preço**: setup e mensalidade
6. **Gates disparados** e o que fazer com cada um
7. **O que assumi** — a lista de premissas que entram na proposta
8. **A linha da base de propostas** pronta para colar (formato no Passo 8 do [`SKILL.md`](SKILL.md))

## O que a skill NÃO faz

- Não escreve a proposta. Devolve os números e as premissas; o texto e o Canva são seus.
- Não decide desconto. Aponta o piso e a política; a concessão é do comercial.
- Não substitui o mapeamento técnico. Se a lista do campo 1 tiver item que ninguém sabe se dá
  para fazer, o preço sai com essa lacuna declarada — não sai resolvido.
