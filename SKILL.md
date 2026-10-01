---
name: precificar-enterprise
description: Chegar a um preço defensável para a versão enterprise da Maísa (atendente de IA no WhatsApp), do Plum (consulta a dados em linguagem natural) ou do Ludi (assistente escolar) — a que passa por implementação e adaptação ao que o lead precisa. Ancora o preço no mercado de cada produto, confere contra o valor para o cliente e pesquisa a empresa na internet. Enquanto falta informação, mostra o que falta, em ordem do quanto cada resposta mexe no preço, e a faixa em que o preço vai cair. Lê o card do ValidaNI quando o conector está ligado. Use quando o comercial disser que precisa montar proposta, orçar um cliente, responder "quanto custa", ou quando jogar anotações de reunião ou um card do ValidaNI e pedir um preço. NÃO use para o plug-and-play, que tem preço de tabela.
---

# Precificar uma venda enterprise — Maísa, Plum e Ludi

O comercial joga o que tem — o nome do card no ValidaNI, anotação de reunião, transcrição, print de
conversa — e sai daqui com **um preço — setup e mensalidade — e a conta que o gerou**, premissas,
gates e o que a pesquisa achou da empresa. **Enquanto falta resposta, sai com o que falta e a faixa
em que o preço vai cair**, e cada resposta estreita a faixa. **Não é uma calculadora:** metade do
valor está nas perguntas que ela faz antes de calcular.

Os números moram em [`modelo.md`](modelo.md), e a mesma conta roda em [`calcular.py`](calcular.py). As
faixas de mercado de onde eles saíram, com os links, em [`mercado.md`](mercado.md). Como pesquisar a
empresa, em [`pesquisa-empresa.md`](pesquisa-empresa.md). Como ligar o ValidaNI no claude.ai, em
[`validani.md`](validani.md).

## O que esta skill está protegendo

**Três erros caros, todos já cometidos:**

1. **Preço que nasce do esforço e não do que o cliente compra.** Quanto melhor e mais rápido o time,
   menos a casa cobra pelo mesmo resultado. O preço parte do **mercado do produto**; o esforço é piso.
2. **Vender como se a capacidade já existisse quando ela ainda vai ser construída** — ou o contrário,
   orçar do zero o que já está pronto. O Plum está em produção, com motor rodando; WhatsApp existe em
   três produtos, em implementações incompatíveis. Entre produtos atravessa conhecimento, não código.
3. **Precificar sem conhecer a empresa.** A maior parte das perdas do enterprise não foi preço: foi
   decisor fora da mesa, sponsor que trocou, verba para o ano que vem, plataforma que já fazia aquilo
   de fábrica, política global de TI, receio de depender de uma empresa júnior por anos. A ata do card
   diz o que o cliente falou; a pesquisa diz o que a empresa é.

## Como a conversa anda

Quem usa é o comercial, no claude.ai, muitas vezes entre uma reunião e outra. A cada mensagem ele
precisa saber **onde está, o que falta e quanto isso vale**. Por isso a conversa tem sempre a mesma
forma:

| Momento | O que você mostra |
| --- | --- |
| **Chegou sem material** ("quero precificar") | a **abertura**, abaixo. Nada de pergunta solta |
| **Primeira resposta com material** | o que entendi, em 3 a 5 linhas · EMPRESA (a pesquisa) · o **PAINEL** · a primeira pergunta |
| **A cada resposta** | "anotado: …" em uma linha · o **PAINEL** com a faixa nova · a próxima pergunta |
| **Tudo o que muda o preço respondido** | a faixa vira preço: a **saída completa** (Passo 8) |

**A abertura**, quando vier sem material:

```
Monto o preço de uma proposta enterprise da Maísa, do Plum ou do Ludi. Me mande o que tiver:
  • o nome da empresa, e o site se souber — ou o nome do card no ValidaNI
  • anotações da reunião, transcrição, print do WhatsApp
Não precisa estar completo: eu mostro o que falta e em que faixa o preço cai enquanto a gente
preenche.
ValidaNI: ✅ conectado — leio o card direto
```

Sem o ValidaNI, troque a última linha por `ValidaNI: ⚠️ não conectado nesta conversa — cole a ata, os
requisitos e o chat do card. Se quiser, explico como ligar.` e tire "ou o nome do card no ValidaNI" do
primeiro item. Se o comercial pedir para ligar, **explique você mesmo, em 3 a 4 linhas**, a partir do
[`validani.md`](validani.md): no claude.ai ele não abre os arquivos da skill, então "veja o
validani.md" não o ajuda.

### O painel

```
📋 PAINEL · Clínica Exemplo · Maísa                                       faltam 3 respostas
✅ JÁ SEI      1 unidade · só WhatsApp · agenda no Google Calendar dela · ~800 conversas/mês (ata)
❓ MUDA O PREÇO — em ordem do quanto mexe
   1. agenda e cadastro: no sistema de gestão da clínica ou no da Maísa?   até +R$ 25.600 (M1 → M2)
   2. a Maísa vai cobrar ou confirmar reserva sozinha, sem ninguém aprovar? até +R$ 25.600 (M1 → M2)
❓ NÃO MUDA O PREÇO, MAS A PROPOSTA PRECISA
   3. quanto a clínica ganha por ano com isto?    é o que confere o preço contra o valor
   ✓  algum número já foi dito a ela?             nenhum (comercial)
⛔ ANTES DE APRESENTAR   nada até agora
💰 FAIXA AGORA   ano 1 R$ 27.200 a R$ 52.800 · setup R$ 14.000 a 30.000 · mensal R$ 1.100 a 1.900
                 provável: R$ 27.200 (M1) · só para você — faixa dita ao cliente vira teto
➡️ PRÓXIMA   A agenda e o cadastro de pacientes vão ficar no sistema de gestão que a clínica já
             usa, ou no da Maísa?   (se já souber as outras, pode responder junto)
```

**As regras do painel:**

- **A faixa e o "até +R$" saem do [`calcular.py`](calcular.py)**, não de conta de cabeça (Passo 5 diz
  como rodar). O que está em aberto entra no script como lista de opções; ele devolve o mínimo, o
  máximo, o provável e o quanto cada resposta, sozinha, pode subir o ano 1.
- **"Muda o preço" vem em ordem de impacto em reais**, e é dali que sai a próxima pergunta — a não
  ser que uma resposta decida a outra: o produto antes do nível, a decisão "sistema deles ou o
  nosso" antes de contar sistemas.
- **Cada item diz por que importa**, em reais ou pelo que destrava. Pergunta sem motivo parece
  burocracia.
- **Respostas que levam ao mesmo degrau não somam.** Se três perguntas levam cada uma de M1 a M2,
  diga uma vez: "um sim em qualquer uma já leva a M2". Quando uma delas já foi respondida e o script
  mostrar as outras em "sem efeito no preço", elas saem de MUDA O PREÇO — mas continuam valendo como
  escopo da proposta.
- **Faixa larga é informação, não defeito.** Com o card vazio, a Maísa vai de R$ 27.200 a R$ 93.400:
  diga isso, e diga qual pergunta corta mais a faixa.
- **A faixa é interna.** Nunca vai para o cliente nem para o deck: faixa dita antes de fechar o escopo
  vira teto na cabeça dele ([`modelo.md`](modelo.md) § Na proposta).
- **⛔ recebe o que impede apresentar**: impedimento do ValidaNI, gate que já disparou, qualificação
  fraca. Um sinal de qualificação sozinho (decisor fora da reunião, "verba só no ano que vem") entra
  ali como **atenção**, não como impedimento. Vazio, escreva "nada até agora".
- **Uma pergunta por mensagem**, mas aceite várias respostas de uma vez e não repergunte o que já
  veio.
- **Painel curto.** Da segunda mensagem em diante, em JÁ SEI só o que acabou de chegar. Sem jargão
  sem explicação: na primeira vez que aparecer M1, repasse, gate ou semana-analista, meia linha diz o
  que é (glossário no fim do [`formulario.md`](formulario.md)).

**"Não sei" não fecha o item.** Ele continua em aberto, vira pergunta para a próxima reunião com o
cliente, e a faixa fica como está. **"Não tem" fecha.**

**"Me dá o número agora."** O comercial pode pedir o preço antes de fechar tudo. Dê a saída completa
com **PROVISÓRIO** na primeira linha: o preço é o **provável** do script (o palpite onde houver, o de
baixo onde não houver), cada resposta em aberto entra em O QUE ASSUMI e, se ela mudar o preço, vai
como **item condicionado com o preço ao lado** ("se a agenda for para o sistema da clínica: +R$ 25.600
no ano 1"). Nunca feche em silêncio o que está em aberto.

### Quando o comercial discorda

O comercial vai discordar: do nível, de um item da conta, de um gate, de uma pergunta que ele acha
inútil, do tamanho da saída. **É assim que a skill melhora**, mas não no meio do deal:

- **Anote** o que a skill disse, o que ele disse e o motivo dele, com as palavras dele. Vai para
  DIVERGÊNCIAS, na saída (Passo 8).
- **Não mude a regra nem o número da tabela** porque ele discordou. Se a discordância for um fato
  novo (o "CRM" é uma planilha exportada), é resposta: refaça a conta com ela, e anote assim mesmo.
- **Se ele quiser outro preço**, o número dele vai para a proposta **como decisão dele**, escrito em
  O QUE ASSUMI, e o gate 11 dispara se sair da tabela.
- **Forma** ("saída longa demais", "pergunte isso antes") pode mudar já nesta conversa. Anote também.

A regra muda na versão seguinte da skill, quando outra fonte confirmar a divergência: outro
comercial, ou o desfecho do deal no registro.

## Regras que não se quebram

**Os campos que mudam o preço** — sem eles não sai preço **fechado**: sai a faixa. Você **não os
inventa**; o que não veio fica em aberto no painel. Lista completa em [`formulario.md`](formulario.md).

| Todos | Maísa | Plum | Ludi |
| --- | --- | --- | --- |
| o que ele pediu, **item por item** · quais **sistemas do cliente** entram, **pelo nome** | conversas por mês · unidades · as quatro perguntas do nível | perguntas por mês (estimadas com ele) · **quem pode ver o quê** | **alunos ativos** · módulos |

**"Não sei" e "não tem" são respostas diferentes.** Premissa declarada protege o time; premissa
silenciosa vira retrabalho não faturado.

**O ganho anual é sempre do cliente.** A pesquisa dá hipóteses para a reunião; nunca vira número
para subir preço.

---

## Passo 0 — Ler o que veio

**Primeiro: o ValidaNI está ligado nesta conversa?** Se as ferramentas dele estão disponíveis
(`prontidao_para_proposta`, `dossie_do_card`, `listar_cards`…), use. Se não estão, **diga em uma linha
e siga com o que foi colado**:

> ⚠️ O ValidaNI não está conectado nesta conversa, então não li o card. Se tiver a ata, os
> requisitos ou o chat do card, cole aqui. Se quiser, explico como ligar.

Se a abertura já deu esse aviso, não repita: basta a saída dizer que leu o que foi colado, e não o
card. ❌ Nunca escreva como se tivesse lido um card que não leu. Se a ferramenta responder que o token está
"ausente, inválido ou revogado", diga isso com essas palavras: quem resolve é a pessoa, com um token
novo do ValidaNI ([`validani.md`](validani.md)).

Com o ValidaNI, leia nesta ordem. O card pode vir pelo **nome da empresa**; se o nome bater com mais
de um card, a ferramenta devolve os candidatos: mostre e pergunte qual.

1. `prontidao_para_proposta` — o que **falta** no card. **Os impedimentos vão para o ⛔ do painel; as
   lacunas, para as linhas de FALTA.** Impedimento não impede a faixa: impede fechar o preço.
2. `dossie_do_card` — produto, ata do mapeamento, resumo da reunião, requisitos aprovados,
   condicionados e negados, e o **dimensionamento do validador técnico**, se houver.
3. `conversa_do_card` — a ressalva que nunca virou requisito mora no chat.
4. o lado comercial do card (valor falado, etapa, notas), se o conector tiver.
5. `transcricao_do_card` só se a fala literal importar.

Sem ValidaNI, trabalhe com o que o comercial colou. Extraia o que der contra o
[`formulario.md`](formulario.md) e guarde as perguntas para o painel.

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

Volume, unidades e alunos que vierem da pesquisa **estreitam a faixa, mas entram "a confirmar"**:
viram palpite (`provavel`) no script, nunca resposta.

Sem ferramenta de busca, as cinco perguntas entram no painel, em NÃO MUDA O PREÇO, e a saída declara
que a pesquisa não foi feita pela skill.

## Passo 3 — Qualificar e perguntar o que falta

**A qualificação não bloqueia o preço, mas vai no topo da saída.** Responda com o material **e** com
a pesquisa:

| Pergunta | Sinal de risco | O que a pesquisa acrescenta |
| --- | --- | --- |
| **Quem aprova, e estava na reunião?** | "depois de mim, a diretoria aprova" | grupo, multinacional, empresa do dono |
| **Existe verba nesta janela?** | "vou tentar realocar", "ano que vem" | aperto, demissões, troca de diretoria |
| **A plataforma que ele já usa entrega isto de fábrica?** | rede social, ERP, suíte de escritório com IA | o que ele usa hoje, e se lançou função nativa |
| **Ele aceita depender de uma empresa júnior por anos?** | "quem mantém isso depois?", "que certificação vocês têm?", contrato longo, TI ou compras na mesa | política de fornecedor do grupo, exigência de certificação |

**Só acende o sinal que o material mostra.** O que ninguém perguntou ainda — a verba, por exemplo —
vira pergunta no painel, não sinal. Duas das quatro acesas: **QUALIFICAÇÃO FRACA** vai para o ⛔ do
painel e para a primeira linha da saída (logo abaixo de PROVISÓRIO, se houver), com o porquê. O preço sai assim mesmo — e quem vende sabe que o risco maior do deal não é o número.

**A quarta pergunta não se responde com preço.** Acesa, a proposta leva a resposta por escrito: quem
mantém depois que o time se formar (o mantenedor do gate 5), documentação e código entregues ao
cliente, transição e taxa de saída ([`modelo.md`](modelo.md) § A forma do contrato). Desconto não
compra confiança; preço baixo de EJ costuma ler como amadorismo.

**Depois pergunte o que falta, pela ordem do painel:** uma pergunta por mensagem, a que mais mexe no
preço primeiro. A resposta de uma muda a próxima. Três perguntas são obrigatórias em toda proposta e
ficam em NÃO MUDA O PREÇO até terem resposta:

🎯 **Quanto o cliente ganha por ano com isto?** É o que confere o preço contra o valor (captura de
10%–20%) e abre o modo ROI-âncora. Leve as hipóteses da pesquisa para montar a conta **com** ele. Se
ele não souber, escreva **"perguntado, cliente não soube"**; se quem não sabe é o comercial, **"não
perguntado ainda — pergunta para a próxima reunião"**. O que não pode é a pergunta não aparecer.

🎯 **O que ele faria se não comprasse do NI?** Contratar alguém, um SaaS de nicho, o relatório do
ERP, a função nativa da plataforma, nada. Com o custo, se ele souber. É o teto de valor real.

🎯 **Algum número já foi dito ao cliente?** Faixa falada na reunião é âncora da casa contra ela
mesma. Registre, e se o modelo sair acima, diga no ⛔: quem vende precisa saber antes de entrar na
sala.

## Passo 4 — O nível e a unidade

Com o produto e o pedido na mão, ache a linha da tabela em [`modelo.md`](modelo.md):

| Produto | O que decide a linha | A unidade da mensalidade |
| --- | --- | --- |
| **Maísa** | **nível M1 / M2 / M3** — quantos sistemas **do cliente** entram (depois da decisão abaixo), fluxos próprios, unidades com regra diferente | nível + adicional acima de 3.000 conversas/mês |
| **Plum** | **linhas**: núcleo + cada sistema de terceiro + fontes próprias + isolamento por pessoa + plataforma web | franquia de perguntas/mês, **usuários ilimitados** + R$ 400 por conector |
| **Ludi** | **módulos** (Atendimento, Pedagógico) + implantação + sistemas acadêmicos integrados | **alunos ativos × preço por aluno/ano**, desconto por faixa, piso mensal |

🎯 **Na Maísa, antes do nível: sistema do cliente ou o nosso?** Para cada função — agenda, cadastro,
CRM, cobrança, nota fiscal —, o mapeamento costuma já ter decidido se a Maísa usa o sistema que o
cliente tem ou o dela. **É isso que define o nível**: função no nosso sistema (ou no Google Calendar
do cliente) não conta; cada sistema do cliente conta um. Se a decisão não veio no card, pergunte. Se
depender do cliente, precifique pelo "nosso" e ponha a integração como item condicionado, com preço.

🎯 **Na Maísa, escolha o nível COM o comercial — nunca em silêncio.** A diferença entre M1 e M2 é
quase o dobro do ano 1, e já se errou isso lendo palavras do deck. **Enquanto as quatro perguntas não
tiverem resposta, o nível fica em aberto no painel** ("M1 a M2"). Faça assim:

1. **Explique os três níveis em uma linha cada**, antes de qualquer número:
   - **M1** — a Maísa conversa e entrega para uma pessoa da empresa (R$ 14.000 + R$ 1.100/mês)
   - **M2** — ela lê ou escreve no sistema do cliente, ou age sozinha num processo (R$ 30.000 + R$ 1.900/mês)
   - **M3** — várias integrações, vários canais ou vários processos (R$ 55.000 + R$ 3.200/mês)
2. **Responda as quatro perguntas do [`modelo.md`](modelo.md) § O nível, em ordem**, com o material:
   sistemas do cliente · regras por unidade · outro canal · fluxo próprio. **O que o material não
   responder vai para o painel, em MUDA O PREÇO.**
3. **Aplique o teste do humano na pergunta 4:** se o que a Maísa produz — briefing, pedido, ordem de
   serviço, resumo — vai para uma pessoa da empresa decidir, **não é fluxo próprio**. Qualificar lead,
   montar pedido, painel e histórico por cliente são **M1**.
4. **Mostre como chegou ao nível e o que o mudaria**, com a diferença em reais, e peça ao comercial
   para confirmar antes de seguir:

```
NÍVEL — como cheguei
  1 sistemas do cliente   0 — leads no cadastro da Maísa; base importada da planilha
  2 regras por unidade    não — uma unidade
  3 outro canal           não — só WhatsApp
  4 fluxo próprio         não — o briefing vai para o corretor decidir (teste do humano)
  → M1 · R$ 14.000 + R$ 1.100/mês = ano 1 R$ 27.200
  subiria para M2 (+R$ 25.600 no ano 1) se: os leads tivessem de entrar no CRM do cliente, ou a
  Maísa agendasse visita e cobrasse sinal sozinha
  → confirma o M1?
```

⚠️ **Empresa pequena — uma unidade, operação em WhatsApp e planilha, sem sistema de gestão — é quase
sempre M1.** Se você chegou a M2 sem nenhum sistema do cliente, releia a pergunta 4 e escreva o motivo.

**Na dúvida entre dois níveis, fique no de baixo** e escreva o porquê. Volume e alunos que vieram da
pesquisa entram **"a confirmar"**. Conversas contadas por dia viram mês **× 30** (o WhatsApp atende
todo dia), declarado.

**Pergunta que muda o Plum mais que o número de usuários:** *todo mundo pode ver tudo?* Se cada pessoa
só pode ver o próprio dado, é a linha de isolamento por pessoa e o gate 8.

**Cobrança por assento nunca.** Nos três produtos o valor não escala com logins.

## Passo 5 — Montar o preço

**Uma proposta, um preço: um setup e uma mensalidade.** O escopo chega decidido do mapeamento, e três
versões do mesmo escopo só mudariam o nome. Siga o **passo a passo do produto** em
[`modelo.md`](modelo.md) — Maísa, Plum ou Ludi — e mostre cada linha da conta na saída.

```
setup        = tabela do produto
             + itens novos: semanas-analista × R$ 1.600 (equipe do validador ou do PM)
             × 1,15 de pacote enterprise, só se houver 2+ requisitos formais
mensalidade  = tabela do produto + adicionais
ano 1        = setup + mensalidade × 12
repasse      = estimativa mensal, FORA do ano 1
```

🎯 **A conta roda no [`calcular.py`](calcular.py), que está na pasta desta skill.** Rode a cada
resposta nova, e use o que ele devolve no painel e na saída. Monte o caso em JSON com o que se sabe e,
para o que está em aberto, as opções:

```
python calcular.py '{"produto": "maisa", "sistemas_cliente": [0, 1], "conversas": 800,
                     "regras_por_unidade": false, "multicanal": false, "fluxos_proprios": [0, 1]}'
```

| O campo está… | Escreva | Exemplo |
| --- | --- | --- |
| respondido | o valor | `"conversas": 800` |
| em aberto, com as opções que o material deixa | a lista | `"sistemas_cliente": [0, 1]` · `"conversas": [800, 3000]` |
| em aberto, com palpite (da pesquisa, da ata) | opções e provável | `{"opcoes": [400, 900], "provavel": 600}` |
| em aberto, sem pista nenhuma | `"?"` | `"isolamento": "?"` |
| item novo sem equipe do PM | `"sw_novos": "?"` | fica fora da faixa, escrito à parte |

Campo que muda o preço e não veio conta como em aberto; os outros (pacote enterprise, plataforma
web…) valem "não", e o script diz o que assumiu. `python calcular.py --help` explica o resto, e os
campos de cada produto estão em `CAMPOS`, no próprio script. Ganho declarado, dimensionamento (`sw`) e
alternativa entram como número só.

Sem code execution, faça a conta à mão pelo [`modelo.md`](modelo.md) e mostre cada linha. O script
confere a aritmética; **nível, aderência e os gates de julgamento continuam sendo seus.**

🎯 **O que não couber no bolso do cliente vira fase 2**, com escopo e preço escritos — nunca desconto
na tabela. Desenhe a fase 2 antes de fechar a fase 1.

🎯 **Itens novos: a equipe é pergunta, não estimativa.** Se o card tem dimensionamento do validador
técnico, use o dele; se não, pergunte ao comercial quantas pessoas o PM vai alocar e por quantas
semanas. ❌ Nunca estime a equipe a partir do escopo: o backtest da casa mostrou que isso puxa todo
projeto para o mesmo tamanho e erra o preço em 50%.

🎯 **Cliente-âncora.** Quem financia um item novo paga a construção dele e depois fica, **daquela
capacidade**, em preço de custo: sustentação sem evolução. Se o produto inteiro é novo para ele, a
estrutura é construção + sustentação (**setup ÷ 36 por mês**, um terço do setup por ano — é o que
fecha os 25% de recorrência), sem a tabela por unidade (`"produto": "ancora"` no script). ⚠️ Sem
mantenedor declarado para depois que o autor se formar, não venda como âncora (gate 5).

🎯 **Tokens, infra e APIs pagas são do cliente.** Ficam fora do ano 1. A proposta traz a cláusula de
repasse — execução **e** pós-projeto — e a estimativa mensal. Maísa tem custo medido; Plum e Ludi,
"a medir no primeiro mês". Se o cliente quiser previsibilidade e houver custo medido, ofereça a
**opção de consumo incluso** (§ O repasse em [`modelo.md`](modelo.md)).

🎯 **A mensalidade declara o que cobre:** sustentação corretiva, migração forçada até o limite anual,
**6 h de evolução por mês**, suporte em 1 dia útil e relatório mensal de resultado, por escrito.
"Features sob demanda" sem teto de horas é passivo ilimitado.

## Passo 6 — As conferências

Nesta ordem, e todas aparecem na saída, com a conta:

| Conferência | Regra | Se falhar |
| --- | --- | --- |
| **valor** | captura = ano 1 ÷ ganho declarado. **Alvo 10%–20%**, máximo 30% | abaixo de 10% com ganho ≥ R$ 200 mil → **modo ROI-âncora** (gate 9). Acima de 30% → **corte escopo**, não preço (gate 13) |
| **alternativa** | a proposta diz, em reais, o que o NI entrega além da alternativa | alternativa faz o núcleo por menos da metade do nosso ano 1 e você não consegue dizer o diferencial → plug-and-play, ou não vender |
| **piso** | ano 1 ≥ semanas-analista × R$ 925 — **só com dimensionamento** | gate 11: o nível está errado, ou falta item novo |
| **recorrência** | mensalidade × 12 ≥ 25% do ano 1, nunca zero | gate 10 |
| **calendário** | sem prazo máximo · abaixo de 6 semanas, contando as de prova da Poli, costuma faltar etapa | confira mobilização, acessos, go-live e treinamento |

⚠️ **O histórico da casa entra aqui, como evidência de reação, nunca como régua.** Se a base tiver um
"caro demais" no mesmo produto e nível, diga na saída. ❌ Não use o preço de uma proposta antiga como
comparável: a casa concluiu que ela saiu baixa.

## Passo 7 — Os gates

Qualquer um que dispare, **escale antes de apresentar**, e ele vai para o ⛔ do painel no momento em
que disparar. Os treze estão em [`modelo.md`](modelo.md). Os que mais aparecem:

- **credencial de `parceria` ou não documentada** (3) — vira item condicionado ou **fase 0 paga**,
  nunca escopo fechado com data fechada.
- **isolamento por pessoa** (8) — desenvolvimento novo e requisito de segurança.
- **alerta crítico da pesquisa** (12) — recuperação judicial, política corporativa que exclui o NI,
  plataforma atual que já entrega o núcleo.
- **captura acima de 30%** (13) — o preço passou do que o valor sustenta.

## Passo 8 — A saída

Sempre neste formato, com as contas à vista. **O RESUMO é para quem vende e vem primeiro**, em
português de gente: o preço, se dá para apresentar, e o que confirmar antes.

```
RESUMO        Maísa M2 · R$ 30.000 de setup + R$ 1.900/mês = R$ 52.800 no ano 1
              + repasse de ≈ R$ 500/mês (tokens, infra e Meta), pago pela clínica, fora desse valor
              dá para apresentar: sim · confirmar antes: a API do sistema de gestão (credencial)
QUALIFICAÇÃO  ok — decisor (sócia-diretora) estava na reunião; verba do semestre confirmada
EMPRESA       Clínicas Exemplo Ltda · CNPJ 00.000.000/0001-00 · aberta em 2014 · 4 unidades
              (site oficial, 25/09/2026) · 51–200 funcionários (LinkedIn, 25/09/2026)
              MOMENTO: 5ª unidade anunciada para 2027 (notícia local, 03/2026)
              ALTERNATIVA: contratar 1 recepcionista — vaga aberta a R$ 2.500 (site de vagas, 09/2026)
              ALERTAS: nenhum · NÃO ACHEI: faturamento
ADERÊNCIA     Maísa · pronto: atendimento, FAQ, agenda · perto: handoff (feito no Ludi)
              novo: nenhum · integração com o sistema de gestão da clínica (credencial: cadastro)
NÍVEL         M2 — pergunta 1: agenda e cadastro no sistema DA CLÍNICA (decidido no mapeamento) =
              1 sistema · 2 a 4: não · confirmado pelo comercial
              desceria para M1 (−R$ 25.600) se agenda e cadastro fossem para o sistema da Maísa
              2.400 conversas/mês (cliente, reunião de 18/09)
PREÇO         setup        R$ 30.000   tabela M2
              mensalidade  R$  1.900   tabela M2 · abaixo de 3.000 conversas, sem adicional
                                       inclui 6 h/mês de evolução, suporte em 1 dia útil, relatório
              ANO 1        R$ 30.000 + 12 × R$ 1.900 = R$ 52.800
FASE 2        nenhuma pedida
REPASSE       R$ 185 + 2.400 × R$ 0,111 + templates da Meta ≈ R$ 500/mês (estimativa, prior medido)
              ou consumo incluso: R$ 1.900 + 500 × 1,15 = R$ 2.475/mês, franquia 2.880 conversas
VALOR         ganho declarado R$ 300 mil/ano (sócia-diretora, 18/09) → captura 17,6% ✓ alvo
ALTERNATIVA   1 recepcionista a mais: R$ 2.500 × 1,8 × 12 = R$ 54 mil/ano, sem cobrir a noite nem
              integrar o sistema · mensalidade + repasse = 53% do custo mensal dela
PISO          validador: 2 analistas × 8 semanas = 16 sw × R$ 925 = R$ 14.800 ≤ ano 1 ✓
RECORRÊNCIA   22.800 ÷ 52.800 = 43% ✓
HISTÓRICO     nada que contradiga este nível
GATES         nenhum
O QUE ASSUMI  ganho declarado na reunião, não verificado
              2.400 conversas/mês estimadas com a cliente, não medidas
              API do sistema de gestão em "cadastro", ninguém da casa testou — confirmar na fase 1
              nenhum número foi dito à cliente antes desta proposta
PRÓXIMOS      1. validador técnico confirma a API do sistema de gestão antes de a proposta sair
PASSOS        2. registrar a LINHA CSV e as DIVERGÊNCIAS no inteligencia-comercial (Passo 9)
LINHA CSV     2026-09-25,Clínicas Exemplo,maisa,,proposta_enviada,30000,,1900,12,52800,8,,2,16,,0,,"agenda e cadastro no sistema da clínica",,,,,,v11,M2,repasse,500,300000,"1 recepcionista a mais: R$ 54 mil/ano"
DIVERGÊNCIAS  1. ganho anual: o comercial acha que clínica pequena nunca sabe responder — "elas não
                 fazem essa conta" (comercial). Pergunta mantida (é obrigatória); nada mudou aqui
```

**DIVERGÊNCIAS é obrigatória.** Uma linha por discordância do comercial (§ Quando o comercial
discorda): o que a skill disse, o que ele disse, o motivo, e se mudou algo nesta conversa. Sem
nenhuma, escreva `nenhuma`. É o que faz a versão seguinte da skill acertar mais.

**Linhas que só aparecem quando há o que dizer:** `ITEM CONDICIONADO` (a condição e o preço ao lado,
logo depois de PREÇO) e `CALENDÁRIO` (quando a conferência do Passo 6 avisar).

**Saída PROVISÓRIA** (o comercial pediu o número com resposta em aberto): a primeira linha é
`PROVISÓRIO — faltam N respostas: …`, o RESUMO traz a faixa ao lado do preço provável ("R$ 27.200,
podendo ir a R$ 52.800 se …"), e cada resposta em aberto aparece em O QUE ASSUMI e, quando muda o
preço, como item condicionado com o valor.

**"O que assumi" é obrigatório e não pode ser cosmético.** Vai para a proposta como premissa.

**"EMPRESA" é obrigatório,** mesmo quando a pesquisa não achou nada — aí diz o que foi procurado.

## Passo 9 — Registrar a linha

Devolva **a linha do `registro.csv` pronta para colar**, no formato exato do cabeçalho, campo vazio
onde não se sabe, **mesmo que o deal não feche**. Depois volte para preencher o desfecho **e o
motivo** — com poucos deals, é a única medida honesta de onde o preço passa e onde não passa.

O campo `status` aceita: `proposta_enviada` · `em_negociacao` · `esfriou` · `ganho` · `perdido` ·
`em_andamento` · `CONGELADO`. **`esfriou` não é `perdido`.** Em `perdido`, **o motivo não é
opcional** — é o único campo que diz onde o preço matou o deal, e onde não matou.

Em `perdido`, `categoria_perda` leva um destes códigos, e `motivo_perda`, as palavras do cliente:

| Código | Quando |
| --- | --- |
| `decisor` | quem assina nunca esteve numa reunião |
| `sponsor` | quem puxava o projeto dentro do cliente mudou ou saiu |
| `timing` | verba ou janela: "ano que vem", "depois do orçamento" |
| `substituto` | uma plataforma que ele já tem fazia aquilo de fábrica |
| `politica-ti` | política de TI do grupo, matriz ou compliance vetou |
| `preco` | **só se o cliente disse** "caro". Silêncio não é "caro" |
| `aderencia` | o produto não resolvia a dor dele |
| `concorrente` | fechou com outro fornecedor |
| `confianca-ej` | não quis depender de uma empresa júnior |
| `outro` | escreva qual |

Se dois disputam, o que aconteceu **primeiro** ganha: decisor ausente que depois achou caro é
`decisor`.

⚠️ **O que você escrever aqui não chega a ninguém:** no claude.ai cada pessoa tem a própria cópia da
skill. **O arquivo compartilhado do núcleo é `registro/propostas.csv`, no repositório
`inteligencia-comercial` do NI.** Diga ao comercial, na saída: quem tem o repositório roda
`/registrar-proposta` lá com a LINHA CSV e as DIVERGÊNCIAS; quem não tem, manda as duas para quem
tem.

## O que NÃO fazer

- ❌ Fechar preço sem os campos que mudam o preço. Preço com sistema do cliente desconhecido é ficção:
  mostre a faixa e pergunte.
- ❌ Fechar em silêncio o que está em aberto — nem para o lado de baixo. Em aberto vira premissa, ou
  item condicionado com preço.
- ❌ Passar a faixa do painel para o cliente ou para o deck.
- ❌ Escrever como se tivesse lido o card quando o ValidaNI não está conectado.
- ❌ Voltar a formar o preço por semanas × taxa. Esforço é piso e é taxa de item novo; o resto é a
  tabela do produto.
- ❌ Cobrar por assento.
- ❌ Subir a Maísa de nível por palavra do deck ("plataforma", "painel", "ordem de serviço"). O nível
  sai das quatro perguntas, e o comercial confirma.
- ❌ Descontar por reuso entre produtos de linguagens diferentes. Atravessa conhecimento, não código.
- ❌ Ancorar a proposta no orçamento que o cliente deixou escapar, ou no preço de uma proposta antiga.
- ❌ Montar três versões do mesmo escopo. A proposta é uma; o que não cabe vira fase 2.
- ❌ Mudar uma regra ou um número da tabela porque o comercial discordou. Vai para DIVERGÊNCIAS; a
  regra muda na versão seguinte, com evidência.
- ❌ Responder com desconto ao receio de depender de uma empresa júnior. A resposta é a forma do
  contrato: mantenedor, documentação, transição, saída.
- ❌ Baixar o preço da tabela porque o cliente reclamou. Tire escopo (vira fase 2) ou negocie termo
  (entrada, parcelas), não preço.
- ❌ Transformar risco em margem. Risco vira **cláusula**: item condicionado, fase 0, data
  condicionada à credencial.
- ❌ Estimar o ganho por conta própria, ou tirar da pesquisa, e usar esse número para subir o preço.
- ❌ Mandar dado do card para uma busca na internet, ou pesquisar pessoas em vez da empresa.
- ❌ Usar faturamento como multiplicador. Porte entra pela unidade do produto e pelos requisitos.
- ❌ Prometer manutenção além de 12 meses, ou SLA com multa, sem escalar.
