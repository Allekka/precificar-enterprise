---
name: precificar-enterprise
description: Chegar a um preço defensável para a versão enterprise da Maísa (atendente de IA no WhatsApp), do Plum (consulta a dados em linguagem natural) ou do Ludi (assistente escolar) — a que passa por implementação e adaptação ao que o lead precisa. Ancora o preço no mercado de cada produto, confere contra o valor para o cliente e pesquisa a empresa na internet antes de calcular. Use quando o comercial disser que precisa montar proposta, orçar um cliente, responder "quanto custa", ou quando jogar anotações de reunião ou um card do ValidaNI e pedir um preço. NÃO use para o plug-and-play, que tem preço de tabela.
---

# Precificar uma venda enterprise — Maísa, Plum e Ludi

O comercial joga o que tem — card do ValidaNI, anotação de reunião, transcrição, print de conversa — e
sai daqui com **três opções de preço**, premissas, gates e o que a pesquisa achou da empresa. **Não é
uma calculadora:** metade do valor está nas perguntas que ela faz antes de calcular.

Os números moram em [`modelo.md`](modelo.md). As faixas de mercado de onde eles saíram, com os links,
em [`mercado.md`](mercado.md). Como pesquisar a empresa, em [`pesquisa-empresa.md`](pesquisa-empresa.md).

## O que esta skill está protegendo

**Três erros caros, todos já cometidos:**

1. **Preço que nasce do esforço e não do que o cliente compra.** Quanto melhor e mais rápido o time,
   menos a casa cobra pelo mesmo resultado. O preço parte do **mercado do produto**; o esforço é piso.
2. **Vender como se a capacidade já existisse quando ela ainda vai ser construída** — ou o contrário,
   orçar do zero o que já está pronto. O Plum está em produção, com motor rodando; WhatsApp existe em
   três produtos, em implementações incompatíveis. Entre produtos atravessa conhecimento, não código.
3. **Precificar sem conhecer a empresa.** A maior parte das perdas do enterprise não foi preço: foi
   decisor fora da mesa, sponsor que trocou, verba para o ano que vem, plataforma que já fazia aquilo
   de fábrica, política global de TI. A ata do card diz o que o cliente falou; a pesquisa diz o que a
   empresa é.

## Regras que não se quebram

**Os campos bloqueantes** — sem eles não sai preço, e você **não os inventa**. Pergunte, uma coisa
por vez, e espere a resposta. Lista completa em [`formulario.md`](formulario.md).

| Todos | Maísa | Plum | Ludi |
| --- | --- | --- | --- |
| o que ele pediu, **item por item** · quais **sistemas do cliente** entram, **pelo nome** | conversas por mês · unidades | perguntas por mês (estimadas com ele) · **quem pode ver o quê** | **alunos ativos** · módulos |

**"Não sei" e "não tem" são respostas diferentes.** Premissa declarada protege o time; premissa
silenciosa vira retrabalho não faturado.

**O ganho anual é sempre do cliente.** A pesquisa dá hipóteses para a reunião; nunca vira número
para subir preço.

---

## Passo 0 — Ler o que veio

Se o **ValidaNI** estiver conectado e houver card, leia nesta ordem:
1. `prontidao_para_proposta` — o que **falta** no card. Impedimento para; lacuna é declarada.
2. `dossie_do_card` — produto, ata do mapeamento, resumo da reunião, requisitos aprovados,
   condicionados e negados, e o **dimensionamento do validador técnico**, se houver.
3. `conversa_do_card` — a ressalva que nunca virou requisito mora no chat.
4. o lado comercial do card (valor falado, etapa, notas), se o conector tiver.
5. `transcricao_do_card` só se a fala literal importar.

Sem ValidaNI, trabalhe com o que o comercial colou. Extraia o que der contra o
[`formulario.md`](formulario.md) e guarde as perguntas para o Passo 3.

## Passo 1 — Aderência: qual produto, e quanto disso a casa já sabe fazer?

**Primeiro o produto: Maísa, Plum ou Ludi.** Se o núcleo do pedido não é nenhum dos três — ERP,
site, um CRM completo como entrega principal —, **não é venda deste modelo**: escale com o porquê.

Depois separe o pedido, item por item, em três baldes. **Isto é triagem de facilidade, não portão de
catálogo**: a tabela de capacidades em [`modelo.md`](modelo.md) diz onde o código está, não o que a
casa sabe fazer.

| Balde | O que é | Vai para |
| --- | --- | --- |
| **pronto** | o produto faz hoje, com parâmetro, conteúdo e credencial do cliente | a tabela do produto |
| **perto** | a casa já fez em **outro** produto, ou é variação curta do que o produto faz | a tabela do produto, no nível acima se for o caso — baixa o **risco**, não o preço por reuso |
| **novo** | ninguém da casa fez | item à parte, pela **taxa de construção**, com o cliente como **âncora** dele |

**Pare só em dois casos, e escale com o porquê:** o núcleo do pedido não é Maísa, Plum ou Ludi; ou o
balde "novo" é maior que "pronto" + "perto" juntos (gate 2). **Quando só uma parte do pedido não é
nossa, precifique a parte que é** e escreva o resto como fora do escopo, com quem entrega.

⚠️ Se o ValidaNI disser que as capacidades nativas não estão registradas, é lacuna, não impedimento:
use o [`modelo.md`](modelo.md) e o que o time diz no card, e não afirme ao cliente que algo é "de
fábrica" sem lastro.

## Passo 2 — Pesquisar a empresa

**Antes de qualquer conta, uns dez minutos de busca na internet.** O roteiro, as fontes e as regras
estão em [`pesquisa-empresa.md`](pesquisa-empresa.md). Cinco perguntas:

1. **Qual o tamanho real** — da empresa e da operação que vai usar (unidades, funcionários, alunos)?
2. **Em que momento ela está** — expansão, estável, aperto, fusão, recuperação judicial?
3. **Quem decide, e sob que regras** — grupo, multinacional, S.A., dono, política de TI?
4. **Qual a melhor alternativa real** — o que ela já usa ou usaria sem o NI, e quanto custa?
5. **Que sinais de valor** dá para levar à reunião, como hipótese?

**Três regras que não se negociam:** pesquise a empresa, não pessoas; nunca mande dado do card para
a busca (busque por nome, CNPJ e site); toda afirmação sai com fonte e data, e o que não achou também.

Sem ferramenta de busca, peça as cinco respostas ao comercial, uma por vez, e declare na saída que a
pesquisa não foi feita pela skill.

## Passo 3 — Qualificar e pedir o que falta

**A qualificação não bloqueia o preço, mas vai no topo da saída.** Responda com o material **e** com
a pesquisa:

| Pergunta | Sinal de risco | O que a pesquisa acrescenta |
| --- | --- | --- |
| **Quem aprova, e estava na reunião?** | "depois de mim, a diretoria aprova" | grupo, multinacional, empresa do dono |
| **Existe verba nesta janela?** | "vou tentar realocar", "ano que vem" | aperto, demissões, troca de diretoria |
| **A plataforma que ele já usa entrega isto de fábrica?** | rede social, ERP, suíte de escritório com IA | o que ele usa hoje, e se lançou função nativa |

Duas das três acesas: escreva **QUALIFICAÇÃO FRACA** na primeira linha da saída, com o porquê. O
preço sai assim mesmo — e quem vende sabe que o risco maior do deal não é o número.

**Depois pergunte o que falta, uma pergunta por vez.** A resposta de uma muda a próxima. Três
perguntas são obrigatórias em toda proposta:

🎯 **Quanto o cliente ganha por ano com isto?** É o que confere o preço contra o valor (captura de
10%–20%) e abre o modo ROI-âncora. Leve as hipóteses da pesquisa para montar a conta **com** ele. Se
ele não souber, escreva **"perguntado, cliente não soube"**. O que não pode é a pergunta não aparecer.

🎯 **O que ele faria se não comprasse do NI?** Contratar alguém, um SaaS de nicho, o relatório do
ERP, a função nativa da plataforma, nada. Com o custo, se ele souber. É o teto de valor real.

🎯 **Algum número já foi dito ao cliente?** Faixa falada na reunião é âncora da casa contra ela
mesma. Registre, e se o modelo sair acima, diga na saída: quem vende precisa saber antes de entrar na
sala.

## Passo 4 — O nível e a unidade

Com o produto e o pedido na mão, ache a linha da tabela em [`modelo.md`](modelo.md):

| Produto | O que decide a linha | A unidade da mensalidade |
| --- | --- | --- |
| **Maísa** | **complexidade M1 / M2 / M3** — quantos sistemas do cliente, fluxos próprios, unidades com regra diferente | nível + adicional acima de 3.000 conversas/mês |
| **Plum** | **linhas**: núcleo + cada sistema de terceiro + fontes próprias + isolamento por pessoa + plataforma web | franquia de perguntas/mês, **usuários ilimitados** + R$ 400 por conector |
| **Ludi** | **módulos** (Atendimento, Pedagógico) + implantação + sistemas acadêmicos integrados | **alunos ativos × preço por aluno/ano**, desconto por faixa, piso mensal |

**Na dúvida entre dois níveis, fique no de baixo** e escreva o porquê. Volume e alunos que vieram da
pesquisa entram **"a confirmar"**.

**Pergunta que muda o Plum mais que o número de usuários:** *todo mundo pode ver tudo?* Se cada pessoa
só pode ver o próprio dado, é a linha de isolamento por pessoa e o gate 8.

**Cobrança por assento nunca.** Nos três produtos o valor não escala com logins.

## Passo 5 — Montar as três opções

**Toda proposta sai com três opções: Essencial, Recomendada e Completa.** O que muda entre elas é
escopo e garantia — horas de evolução, suporte, acompanhamento, cobertura — e não o nome. A
Recomendada é o pedido do cliente. Definição exata em § As três opções de [`modelo.md`](modelo.md).

Para cada opção:

```
setup        = tabela do produto
             + itens novos: semanas-analista × R$ 1.600 (equipe do validador ou do PM)
             + 15% de pacote enterprise, só se houver 2+ requisitos formais
mensalidade  = tabela do produto + adicionais
ano 1        = setup + mensalidade × 12
repasse      = estimativa mensal, FORA do ano 1
```

🎯 **Itens novos: a equipe é pergunta, não estimativa.** Se o card tem dimensionamento do validador
técnico, use o dele; se não, pergunte ao comercial quantas pessoas o PM vai alocar e por quantas
semanas. ❌ Nunca estime a equipe a partir do escopo: o backtest da casa mostrou que isso puxa todo
projeto para o mesmo tamanho e erra o preço em 50%.

🎯 **Cliente-âncora.** Quem financia um item novo paga a construção dele e depois fica, **daquela
capacidade**, em preço de custo: sustentação sem evolução. Se o produto inteiro é novo para ele, a
estrutura é construção + sustentação, sem a tabela por unidade. ⚠️ Sem mantenedor declarado para
depois que o autor se formar, não venda como âncora (gate 5).

🎯 **Tokens, infra e APIs pagas são do cliente.** Ficam fora do ano 1. A proposta traz a cláusula de
repasse — execução **e** pós-projeto — e a estimativa mensal. Maísa tem custo medido; Plum e Ludi,
"a medir no primeiro mês". Se o cliente quiser previsibilidade e houver custo medido, ofereça a
**opção de consumo incluso** (§ O repasse em [`modelo.md`](modelo.md)).

🎯 **A mensalidade declara o que cobre:** sustentação corretiva, migração forçada até o limite anual,
e **as horas de evolução da opção, por escrito**. "Features sob demanda" sem teto de horas é passivo
ilimitado.

## Passo 6 — As conferências

Nesta ordem, e todas aparecem na saída, com a conta:

| Conferência | Regra | Se falhar |
| --- | --- | --- |
| **valor** | captura = ano 1 da Recomendada ÷ ganho declarado. **Alvo 10%–20%**, máximo 30% | abaixo de 10% com ganho ≥ R$ 200 mil → **modo ROI-âncora** (gate 9). Acima de 30% → **corte escopo**, não preço (gate 13) |
| **alternativa** | a proposta diz, em reais, o que o NI entrega além da alternativa | alternativa faz o núcleo por menos da metade da Essencial e você não consegue dizer o diferencial → plug-and-play, ou não vender |
| **piso** | ano 1 da Essencial ≥ semanas-analista × R$ 925 — **só com dimensionamento** | gate 11: o nível está errado, ou falta item novo |
| **recorrência** | mensalidade × 12 ≥ 25% do ano 1, nunca zero | gate 10 |
| **calendário** | 6 a 12 semanas, contando as semanas de prova da Poli | fora disso, confira etapas ou venda por fase |

⚠️ **O histórico da casa entra aqui, como evidência de reação, nunca como régua.** Se a base tiver um
"caro demais" no mesmo produto e nível, diga na saída. ❌ Não use o preço de uma proposta antiga como
comparável: a casa concluiu que ela saiu baixa.

## Passo 7 — Os gates

Qualquer um que dispare, **escale antes de apresentar**. Os treze estão em [`modelo.md`](modelo.md).
Os que mais aparecem:

- **credencial de `parceria` ou não documentada** (3) — vira item condicionado ou **fase 0 paga**,
  nunca escopo fechado com data fechada.
- **isolamento por pessoa** (8) — desenvolvimento novo e requisito de segurança.
- **alerta crítico da pesquisa** (12) — recuperação judicial, política corporativa que exclui o NI,
  plataforma atual que já entrega o núcleo.
- **captura acima de 30%** (13) — o preço passou do que o valor sustenta.

## Passo 8 — A saída

Sempre neste formato, com as contas à vista:

```
QUALIFICAÇÃO  ok — decisor (sócia-diretora) estava na reunião; verba do semestre confirmada
EMPRESA       Clínicas Exemplo Ltda · CNPJ 00.000.000/0001-00 · aberta em 2014 · 4 unidades
              (site oficial, 25/09/2026) · 51–200 funcionários (LinkedIn, 25/09/2026)
              MOMENTO: 5ª unidade anunciada para 2027 (notícia local, 03/2026)
              ALTERNATIVA: contratar 1 recepcionista — vaga aberta a R$ 2.500 (site de vagas, 09/2026)
              ALERTAS: nenhum · NÃO ACHEI: faturamento
ADERÊNCIA     Maísa · pronto: atendimento, FAQ, agenda · perto: handoff (feito no Ludi)
              novo: nenhum · integração com o sistema de gestão da clínica (credencial: cadastro)
NÍVEL         M2 — 1 sistema do cliente · 2.400 conversas/mês (cliente, reunião de 18/09)
OPÇÕES                        Essencial      Recomendada ⭐   Completa
  setup                       R$ 22.000      R$ 30.000       R$ 38.000
  mensalidade                 R$ 1.400       R$ 1.900        R$ 2.500
  evolução / suporte          2 h · 2 d.u.   6 h · 1 d.u.    12 h · 4 h úteis
  ANO 1                       R$ 38.800      R$ 52.800       R$ 68.000
REPASSE       R$ 185 + 2.400 × R$ 0,111 + templates da Meta ≈ R$ 500/mês (estimativa, prior medido)
              ou consumo incluso: R$ 1.900 + 500 × 1,15 = R$ 2.475/mês, franquia 2.880 conversas
VALOR         ganho declarado R$ 300 mil/ano (sócia-diretora, 18/09) → captura 17,6% ✓ alvo
ALTERNATIVA   1 recepcionista a mais: R$ 2.500 × 1,8 × 12 = R$ 54 mil/ano, sem cobrir a noite nem
              integrar o sistema · mensalidade + repasse = 53% do custo mensal dela
PISO          validador: 2 analistas × 8 semanas = 16 sw × R$ 925 = R$ 14.800 ≤ Essencial ✓
RECORRÊNCIA   Recomendada: 22.800 ÷ 52.800 = 43% ✓
HISTÓRICO     nada que contradiga este nível
GATES         nenhum
O QUE ASSUMI  ganho declarado na reunião, não verificado
              2.400 conversas/mês estimadas com a cliente, não medidas
              API do sistema de gestão em "cadastro", ninguém da casa testou — confirmar na fase 1
              nenhum número foi dito à cliente antes desta proposta
LINHA CSV     2026-09-25,Clínicas Exemplo,maisa,,proposta_enviada,30000,,1900,12,52800,8,,2,16,,0,,"Recomendada apresentada; repasse estimado R$ 500/mês",,,,,,v6,M2,38800/52800/68000,,300000,"1 recepcionista a mais: R$ 54 mil/ano"
```

**"O que assumi" é obrigatório e não pode ser cosmético.** Vai para a proposta como premissa.

**"EMPRESA" é obrigatório,** mesmo quando a pesquisa não achou nada — aí diz o que foi procurado.

## Passo 9 — Registrar a linha

Devolva **a linha do `registro.csv` pronta para colar**, no formato exato do cabeçalho, campo vazio
onde não se sabe, **mesmo que o deal não feche**. Depois volte para preencher o desfecho **e a opção
que o cliente escolheu** — com poucos deals, é a única medida honesta de disposição a pagar.

O campo `status` aceita: `proposta_enviada` · `em_negociacao` · `esfriou` · `ganho` · `perdido` ·
`em_andamento` · `CONGELADO`. **`esfriou` não é `perdido`.** Em `perdido`, **o motivo não é
opcional** — é o único campo que diz onde o preço matou o deal, e onde não matou.

⚠️ **A cópia da base que veio dentro da skill é um retrato congelado.** No claude.ai cada pessoa sobe
a própria cópia; o que você escrever aqui não chega a ninguém. A linha só vira base quando alguém a
cola no arquivo compartilhado do núcleo. Se ninguém souber onde ele está, diga isso em voz alta.

## O que NÃO fazer

- ❌ Precificar sem os campos bloqueantes. Preço com sistema do cliente desconhecido é ficção.
- ❌ Voltar a formar o preço por semanas × taxa. Esforço é piso e é taxa de item novo; o resto é a
  tabela do produto.
- ❌ Cobrar por assento.
- ❌ Descontar por reuso entre produtos de linguagens diferentes. Atravessa conhecimento, não código.
- ❌ Ancorar a proposta no orçamento que o cliente deixou escapar, ou no preço de uma proposta antiga.
- ❌ Apresentar uma opção só. São três, e a Recomendada é o pedido.
- ❌ Baixar o preço da Recomendada porque o cliente reclamou. Ele tem a Essencial; negocie termo
  (entrada, parcelas, escopo), não preço.
- ❌ Transformar risco em margem. Risco vira **cláusula**: item condicionado, fase 0, data
  condicionada à credencial.
- ❌ Estimar o ganho por conta própria, ou tirar da pesquisa, e usar esse número para subir o preço.
- ❌ Mandar dado do card para uma busca na internet, ou pesquisar pessoas em vez da empresa.
- ❌ Usar faturamento como multiplicador. Porte entra pela unidade do produto e pelos requisitos.
- ❌ Prometer manutenção além de 12 meses, ou SLA com multa, sem escalar.
