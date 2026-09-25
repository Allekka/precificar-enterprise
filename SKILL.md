---
name: precificar-enterprise
description: Chegar a um preço defensável para a versão enterprise de um produto do NI — a que passa por implementação e adaptação ao que o lead precisa. Use quando o comercial disser que precisa montar proposta, orçar um cliente, responder "quanto custa", ou quando jogar anotações de reunião e pedir um preço. NÃO use para o plug-and-play, que tem preço de tabela.
---

# Precificar uma venda enterprise

O comercial joga o que tem — anotação de reunião, transcrição, print de conversa — e sai daqui com
preço, premissas e gates. **Não é uma calculadora:** metade do valor está nas perguntas que ela faz
antes de calcular.

Escopo: **só as versões enterprise**, as que passam por implementação e adaptação. O plug-and-play
tem preço de tabela e não entra aqui — a tabela está em § Os produtos de [`modelo.md`](modelo.md)
só para você saber onde está o degrau.

## O que esta skill está protegendo

**O erro caro não é errar o preço para cima ou para baixo. É vender como se a capacidade já
existisse quando ela ainda vai ser construída** — ou o contrário, orçar do zero o que já está
pronto e perder o deal por preço inventado.

Os dois acontecem:

Quem lê só a documentação técnica pode concluir que o produto de consulta a dados não existe em
código. **O Plum real está em produção**, com motor de consulta rodando. Quem orça como produto
novo chuta para cima.

Na direção oposta: WhatsApp existe **3×** na casa. Maísa é TypeScript, Smiller e Ludi são Python.
Entre produtos o que atravessa é **conhecimento e contrato de porta**, não arquivo. Descontar 80%
por reuso entre linguagens é promessa falsa com número em cima.

## Regra que não se quebra

**Quatro campos são bloqueantes** — o que ele pediu item por item, quais sistemas do cliente entram,
quantas pessoas operam e quantas são atendidas, e o volume mensal. Sem eles não sai preço, e você
**não os inventa**. Pergunte, uma coisa por vez, e espere a resposta. Lista completa em
[`formulario.md`](formulario.md).

E: **"não sei" e "não tem" são respostas diferentes.** Premissa declarada protege o time; premissa
silenciosa vira retrabalho não faturado.

---

## Passo 0 — Aderência: quanto disso a casa já sabe fazer?

Antes de qualquer conta. **Isto não é um portão de catálogo, é uma triagem de facilidade.** A
pergunta não é "está escrito na tabela de capacidades?" — tabela é retrato, e retrato fica velho.
A pergunta é: **o que disso a gente já faz fácil, o que está perto, e o que seria construção de
verdade?** A resposta decide a rota e o risco, não se a proposta sai.

Separe o pedido, item por item, em três baldes:

| Balde | O que é | Vai para |
| --- | --- | --- |
| **pronto** | o produto faz hoje, com parâmetro, conteúdo e credencial do cliente | rota configuração |
| **perto** | a casa já fez em **outro** produto (handoff no Smiller, leads no Ludi) ou é variação curta do que o produto faz | rota extensão — o conhecimento atravessa e baixa o **risco**, não o preço por reuso de código |
| **novo** | ninguém da casa fez | etapa própria no dimensionamento, e o cliente é **âncora** dela (Passo 3) |

**Uma capacidade que não aparece na tabela não é, sozinha, motivo para parar.** Se o núcleo do
pedido é o **tipo de coisa** que o produto faz — atender, qualificar e encaminhar gente no
WhatsApp é Maísa, mesmo que a Maísa hoje seja vendida como agendamento —, siga. O que faltar vai
para "perto" ou "novo" e aparece no dimensionamento, com o custo dele.

**Pare só em dois casos, e mesmo assim não recuse sozinho — escale com o porquê:**
1. **O núcleo do pedido não é produto de IA do NI** — ERP, site, um CRM completo como entrega
   principal. Aí não é venda enterprise deste modelo.
2. **O balde "novo" é maior que "pronto" + "perto" juntos.** Aí é produto novo disfarçado de
   enterprise, e a decisão é do núcleo, não do vendedor.

**Quando só uma parte do pedido não é nossa, precifique a parte que é** e escreva o resto como
fora do escopo, com quem entrega (o cliente, outro núcleo, um parceiro). Exemplo: pedido de
chatbot de qualificação mais um CRM básico — o chatbot é Maísa, o CRM é de outro núcleo. Sai a
proposta da Maísa, com a integração condicionada ao CRM existir.

⚠️ Se o ValidaNI disser que as **capacidades nativas do produto não estão registradas**, isso é
lacuna, não impedimento: use § Os produtos de [`modelo.md`](modelo.md) e o que o time diz no card,
e não afirme ao cliente que algo é "de fábrica" sem lastro.

### E a qualificação — não bloqueia o preço, mas vai no topo da saída

**Boa parte das perdas do enterprise morre antes do preço**: decisor fora da mesa, sponsor que
trocou, orçamento para "o ano que vem". Nenhum ajuste de preço recupera esses deals. Então, antes
de calcular, responda três coisas a partir do material:

| Pergunta | Sinal de risco | Categoria de perda que ela previne |
| --- | --- | --- |
| **Quem aprova, e estava na reunião?** | "depois de mim, a diretoria aprova" | autoridade |
| **Existe verba nesta janela?** | "não tenho orçamento para este ano, vou tentar realocar" | timing |
| **A plataforma que ele já usa entrega isto de fábrica?** | Meta, Google, o próprio ERP | substituto nativo |

Se duas das três acenderem, escreva **QUALIFICAÇÃO FRACA** na primeira linha da saída, com o
porquê. O preço sai assim mesmo — mas quem vende fica sabendo que o risco maior do deal não é o
número, e que o modo 🔥 agressivo está fora (ele exige decisor acessível).

## Passo 1 — Ler o que veio e pedir o que falta

Extraia do material o que der, contra o [`formulario.md`](formulario.md). Depois **pergunte o que
falta, uma pergunta por vez** — a resposta de uma muda a próxima.

Não despeje o formulário inteiro na cara do comercial. Ele já está com o cliente na cabeça; o que
ele precisa é da próxima pergunta certa.

🎯 **Uma pergunta é obrigatória: quanto o cliente ganha por ano com isto.** Não é opcional e não
depende do caso. Ela abre o modo ROI-âncora, que é **a única rota de preço que não depende de
horas** — e o NI entrega em no máximo ~3 meses, então o preço por esforço tem teto de construção
(§ A janela de três meses em [`modelo.md`](modelo.md)). O cliente nunca declara o ganho se
ninguém perguntar, e perguntar não custa deal nenhum.

🎯 **Pergunte também: algum número já foi dito ao cliente?** Faixa falada na reunião ("de 20 a
40 mil") é âncora — **da casa contra ela mesma**, e pior que o orçamento que o cliente deixa
escapar, porque foi dita antes de qualquer dimensionamento. Registre a faixa em "O que assumi", e
se o modelo sair acima dela, diga isso na saída: quem vende vai ter de explicar a diferença, e
precisa saber antes de entrar na sala. É o caso comum, não a exceção — a faixa dita na primeira
conversa costuma ficar abaixo do que o modelo dá.

Se ele não souber dizer o ganho, **escreva "perguntado, cliente não soube"** na saída do Passo 7 e
siga com `f_retorno = 1,00`. O que não pode é a pergunta não aparecer. ❌ E nunca estime o ganho
por conta própria para subir o preço — o número tem de ser do cliente.

## Passo 2 — A rota

Três, e só três. A rota decide a tabela inteira.

| Rota | Quando | Sinal de reconhecimento |
| --- | --- | --- |
| **configuração** | tudo o que ele pediu cabe em parâmetro, conteúdo e credencial dele | o produto atenderia hoje com um botão ligado e o texto trocado |
| **extensão** | há comportamento que só esse cliente tem | precisa de código novo, mas dentro do produto |
| **motor + domínio** | é o Plum: reaproveita o esqueleto e reconstrói fonte, domínio e autorização | o pedido é "consultar nossos dados", e os dados são de cada cliente |

**Como distinguir configuração de extensão:** pergunte se outro cliente do mesmo segmento usaria a
mesma coisa sem mudar nada. Se sim, é configuração. Se só esse cliente quer, é extensão — e ele é
o âncora dela.

**A rota motor + domínio é a mais aberta e a mais mal orçada.** O esqueleto reaproveitado é real, o
que se joga fora por projeto também. As camadas que se reconstroem e o quanto cada uma custa estão
em [`modelo.md`](modelo.md).

## Passo 3 — Âncora ou seguidor

A pergunta que muda o contrato, não só o número.

**Âncora** financia capacidade que ainda não existe: paga a implementação e depois fica em **preço
de custo, sem licença**. O NI mantém o direito de revender, e o âncora sabe disso desde o início.
⚠️ **Preço de custo não é mensalidade zero.** A mensalidade do NI nunca foi licença — é manutenção
corretiva —, então o âncora paga essa parte e fica **sem a parte de evolução**. O piso de
recorrência (MRR ≥ 25% do ano 1, gate 10) vale para ele igual.

**Seguidor** compra capacidade que já está pronta: **setup reduzido mais mensalidade** com as duas
partes (manutenção corretiva, evolução com limite de horas).

Nos dois casos, **tokens, infra e APIs pagas são repassados ao cliente**, fora da mensalidade.

⚠️ Se ninguém souber dizer **quem mantém** a capacidade depois que o autor se formar, não venda
como âncora. Você acabou de prometer manutenção que a casa não tem, num time que rotaciona a cada
1–2 anos.

## Passo 4 — Dimensionar

Por etapa, em PERT: semanas otimista (O), mais provável (M), pessimista (P), e quantos analistas.

```
semanas_PERT     = (O + 4M + P) / 6
semanas-analista = Σ_etapas (semanas_PERT × analistas)   ← pessoas alocadas × semanas de
                                                           calendário. NÃO converta para FTE
rateio           = semanas-analista × fator_coordenação  ← PM e Tech Lead, por fora da equipe
```

🎯 **A equipe é pergunta, não estimativa.** Quantas pessoas vão entregar é decisão do PM, e o
mesmo escopo sai com 2 ou 3 pessoas conforme quem está livre. Estimar a equipe a partir do escopo
puxa todo projeto para ~30 sw: os pequenos saem até 80% maiores e o preço erra em torno de 50%.
Então: se o card no ValidaNI tem dimensionamento do validador técnico, **use o dele**; se não tem,
**pergunte ao comercial quantas pessoas o PM vai alocar**. Só na falta das duas coisas use a tabela
de camadas — e escreva em "O que assumi" que a equipe foi estimada.

⚠️ **`semanas-analista` é alocação, não esforço.** Conte **pessoas declaradas × semanas de
calendário da etapa** — é a unidade sobre a qual as taxas foram calibradas, e converter para FTE
derruba o preço pela metade. Trainee que entrega **conta**; Tech Lead, PM e validador **não**
(entram no rateio).

**Não esqueça o rateio.** O PM e o Tech Lead pegam vários projetos; são trabalho real. O fator
depende de quantos projetos rodam em paralelo: **+31% com 2 projetos, +15% com 4, +10% com 6**. Na
dúvida, +15%.

Para a rota **motor + domínio**, use a tabela de camadas de [`modelo.md`](modelo.md) — ela já
separa o que herda do que se reconstrói, e é mais confiável que estimar do zero.

🎯 **Sanidade de calendário.** Propostas da casa ficam entre **6 e 12 semanas**, mediana 8. Se o
seu dimensionamento sair **fora de 6–12 semanas**, pare e confira: abaixo de 6 costuma faltar etapa
(mobilização, acessos, go-live, treinamento); acima de 12 sobra escopo, e estoura a janela de
entrega do núcleo. O que varia entre projetos é o **número de pessoas**, não o calendário.

🎯 **Conte as semanas de prova da Poli.** As semanas do modelo são de **calendário**, e o time não
trabalha durante as provas da Escola Politécnica — o que acrescenta pelo menos uma semana ao
projeto que atravessar uma. Elas entram no prazo da proposta **e** em `semanas-analista`.

## Passo 5 — As três pernas

```
base        = semanas-analista + rateio
referência  = base × ITIP_alvo             ← O PREÇO COMEÇA AQUI. depende da rota E do modo ↓
PREÇO ANO 1 = referência × multiplicador   ← f_retorno × f_área × f_porte, teto 1,70
teto        = payback do cliente ≤ 6 meses ← o freio
piso        = base × R$ 805                ← alarme de regressão. Nunca abaixo, nunca o começo

  só depois:  preço ano 1 = setup + (mensalidade × meses)
              PISO DE RECORRÊNCIA: mensalidade nunca zero, e MRR ≥ 25% do ano 1
```

🎯 **Pergunte o modo de risco antes de calcular, e diga estes números:**

| Rota | 🛡️ Conservador | ⚖️ Padrão | 🔥 Agressivo |
| --- | --- | --- | --- |
| configuração | 1.100 | **1.400** | 1.700 ⚠️ |
| extensão | 1.200 | **1.600** | 2.000 |
| motor + domínio | 1.300 | **1.800** | 2.400 |

O padrão é o default e não precisa de justificativa. **Conservador exige motivo escrito.**
**Agressivo exige duas coisas:** a pergunta de ROI respondida pelo cliente **e** decisor
identificado e acessível — se faltar uma, caia para o padrão. ⚠️ Agressivo em **configuração** é o
território onde a casa já ouviu "caro demais". O modo mexe **só no ITIP alvo**: piso, teto de
payback, multiplicador e os limites de mensalidade valem igual nos três. Detalhe em § O modo de
risco de [`modelo.md`](modelo.md).

🎯 **`f_porte` conta quem VAI USAR, não quem assina.** Empresa de 1.500 funcionários comprando para
um setor de 70 pessoas é `f_porte = 1,10`, não 1,50. Escreva a contagem na proposta. Faturamento
não define o degrau — sobe no máximo um, e só com operação atendida ≥ 250.

🎯 **Nenhuma proposta sai com mensalidade zero.** O mínimo é 25% do contrato do ano 1; com 12
meses, `mensalidade ≥ contrato do ano 1 ÷ 48`. Abaixo disso, **gate 10**.

🎯 **Tokens, infra e APIs pagas são do cliente.** Ficam **fora** do contrato do ano 1 e da
mensalidade, e a proposta traz a cláusula de repasse — cobrindo a execução **e** o pós-projeto —
mais uma **estimativa mensal do repasse** (`infra + V × custo por interação`), escrita como
estimativa. Se o produto não tem custo medido (Plum, Ludi, Smiller), escreva "a medir no primeiro
mês" em vez de chutar. Se mensalidade + repasse estimado passar do teto de porte, avise. Detalhe em
§ O custo de operação é do cliente, em [`modelo.md`](modelo.md).

🎯 **A mensalidade é manutenção do produto — correção de bugs e sustentação —, não licença.**
Isso muda o direcionador: o custo de manter escala com **superfície** (nº de integrações de
terceiros e código sob medida), não com volume de uso — o volume vai para o repasse. E muda o
comparável que o cliente tem na cabeça: contrato de manutenção de mercado custa **15% a 25% do
valor da implantação por ano**. Acima disso, a mensalidade só se sustenta se **declarar** o que
entrega além de bug: manutenção corretiva e **evolução com limite de horas escrito**. ❌ "Novas
features sob demanda" sem teto de horas é passivo ilimitado.

⚠️ **Mas a mensalidade tem teto, pelo tamanho da operação atendida** — R$ 1.500 até 50 pessoas ·
R$ 3.000 de 50 a 250 · R$ 5.000 de 250 a 1.000 · R$ 8.000 acima disso. **O teto ganha dos pisos:**
mensalidade que não cabe no caixa do cliente derruba o deal por caixa, não por valor. Quando ele
morde, **o contrato do ano 1 não muda** — a mensalidade para no teto e o setup absorve a diferença.
O gate 10 dispara assim mesmo, e você escreve que foi **limite de porte**, não desconto.

⚠️ **Comece pela referência, nunca pelo piso.** Os R$ 805 são a taxa praticada numa safra que a
casa **já concluiu que saiu barata demais**. O piso existe para acender uma luz — "você
regrediu" —, não para dizer quanto cobrar.

**O modelo dá um número: o contrato do ano 1.** O corte entre setup e mensalidade vem depois e é
decisão de caixa — a regra de qual formato usar está em [`modelo.md`](modelo.md).

**Não existe banda de preço por porte.** Banda indexada ao porte ignora o tamanho do projeto e erra
feio. O que manda é `semanas-analista × ITIP`; porte pesa no máximo 50% (`f_porte` até 1,50),
**multiplicando** dentro do multiplicador — nunca substituindo o tamanho do projeto.

**Se o preço estourar o teto, o problema não é o preço — é o escopo.** Corte etapa, não margem.

**Qual postura usar.** O padrão é a **postura 2, ancorada em mercado** (ITIP alvo × multiplicador),
e ela não precisa de justificativa. Na rota **configuração** o alvo está acima de um preço que já
foi recusado por caro — foi mantido de propósito, porque o objetivo é um preço que faça sentido,
não o que maximiza fechamento; **conte com perder alguns deals nessa rota e registre o motivo**.
Use a **3, ancorada em valor**, sempre que o cliente quantificar o ganho. A **1, ancorada em custo**
(base × R$ 1.300) é **exceção**: só depois de o cliente recusar um número concreto, ou com escopo
tão incerto que nem o diagnóstico fechou. ⚠️ **"O cliente é sensível a preço", dito por quem vende
e não pelo cliente, não é critério** — se fosse, valeria sempre, e a postura 1 viraria o padrão
pela porta dos fundos. As três, com o risco de cada uma, estão em [`modelo.md`](modelo.md).

⚠️ **Registre a perda, e sobretudo o motivo.** Perda total e perda **por preço** são números
diferentes, e confundir os dois leva a cortar preço para resolver um problema de qualificação —
decisor fora da mesa, timing, substituto nativo. Motivo auto-reportado subestima preço ("timing" é
mais confortável de escrever que "estava caro"), então pergunte de novo antes de fechar a linha.

## Passo 6 — Os gates

Qualquer um que dispare, **escale antes de apresentar**. Os dez estão em
[`modelo.md`](modelo.md). Os três que mais aparecem:

- **credencial de `parceria` ou não documentada** — a data não está nas mãos do NI. Nunca entra em
  escopo fechado com data fechada; vira etapa condicionada, com a condição escrita ao lado do item.
- **provedor-gestor** (Booksy, Trinks, Fresha) — não cabe nas portas atuais.
- **isolamento por pessoa** ("cada um só vê o próprio dado") — é desenvolvimento novo, não
  configuração, e é requisito de segurança, não conveniência.

## Passo 7 — A saída

Sempre neste formato, com as contas à vista:

```
ADERÊNCIA     ok — atendimento por WhatsApp é o núcleo da Maísa
ROTA          extensão · cliente-âncora de "lembrete configurável"
DIMENSION.    3 etapas · PERT 7,3 semanas · 2 analistas = 14,6 sw-analista
              + rateio de coordenação 15% (4 projetos em paralelo) = 16,8 sw
MODO          ⚖️ padrão
REFERÊNCIA    16,8 × R$ 1.600 = R$ 26.880
MULTIPLICADOR 1,10 (ROI estimável) × 1,00 (core) × 1,10 (120 pessoas atendidas) = 1,21 → R$ 32.500
TETO          ganho declarado R$ 480k/ano → payback de R$ 32,5k = 0,8 mês ✓
PISO          16,8 × R$ 805   = R$ 13.524   ← alarme: o preço está 2,4× acima ✓
PREÇO ANO 1   R$ 32.500 = setup R$ 24.100 + R$ 700 × 12
              mensalidade = manutenção corretiva, sem evolução (âncora)
              MRR 26% ≥ 25% ✓ · teto de porte (50–250 pessoas) R$ 3.000 ✓
REPASSE       tokens + infra + WhatsApp pagos pelo cliente, fora do ano 1
              estimativa: R$ 185 + 2.400 × R$ 0,111 ≈ R$ 450/mês (prior da Maísa)
              mensalidade + repasse ≈ R$ 1.150 ≤ teto R$ 3.000 ✓
GATES         nenhum
O QUE ASSUMI  ganho declarado pelo cliente na reunião de 12/09, não verificado
              volume mensal estimado junto com o cliente, não medido
              4 projetos simultâneos na janela — confirmar com o PM
              120 pessoas atendidas, contadas pelo cliente — escrever na proposta
LINHA CSV     (uma linha só) 2026-09-12,Cliente Exemplo,maisa,extensao,proposta_enviada,24100,,700,12,32500,7.3,,2,14.6,2226,0,,"âncora de lembrete configurável; rateio 15%; MRR 26%",,,,,
```

**"O que assumi" é obrigatório e não pode ser cosmético.** Vai para a proposta como premissa.

## Passo 8 — Registrar a linha

Devolva **a linha da base de propostas pronta para colar**, **mesmo que o deal não feche**, neste
cabeçalho exato — campo vazio onde não se sabe:

```
data_proposta,cliente,produto,rota,status,setup_proposto,setup_contratado,mrr,meses_mrr,valor_contrato_total,semanas_proposta,semanas_reais,analistas_declarados,sw_analista,itip_contrato_ano1,desconto_pct,contrapartida,observacao,trainees,sw_analista_hi,itip_lo,categoria_perda,motivo_perda
```

Depois volte para preencher o desfecho.

O campo `status` aceita: `proposta_enviada` · `em_negociacao` · `esfriou` · `ganho` · `perdido` ·
`em_andamento` · `CONGELADO`. **`esfriou` não é `perdido`** — só vira derrota quando o cliente
decide, e dar lost cedo demais inventa uma perda que a base não teve.
Em `perdido`, **o motivo vai em `motivo_perda` e a categoria em `categoria_perda`** (`PRECO` ·
`autoridade` · `timing` · `substituto_nativo` · `budget` · `viabilidade` · `desconhecido`) — é o
único campo da base que diz onde o preço matou o deal.

⚠️ **A base de propostas do núcleo é interna e não vem com esta skill.** A linha só vira dado
quando alguém a cola no arquivo compartilhado do núcleo. Se ninguém souber onde esse arquivo está,
diga isso em voz alta — linha que fica no chat é dado que nunca existiu.

## O que NÃO fazer

- ❌ Precificar sem os quatro campos bloqueantes. Preço com sistema do cliente desconhecido é
  ficção.
- ❌ Descontar por reuso entre produtos de linguagens diferentes. Atravessa conhecimento, não
  código.
- ❌ Ancorar a proposta no orçamento que o cliente deixou escapar.
- ❌ Usar o preço de uma proposta antiga, ou "o que cobramos do cliente X", como comparável de
  **preço**. Propostas antigas servem de referência de **tamanho e equipe**; os preços delas estão
  abaixo do alvo, e citá-los é ancorar contra a própria casa.
- ❌ Baixar preço porque o cliente reclamou. Precificar abaixo da taxa-base não compra o sim.
- ❌ Transformar risco em margem. Risco vira **cláusula**: escopo condicionado, etapa separada, data
  condicionada à credencial.
- ❌ Estimar o ROI por conta própria e usar o seu número para subir o preço.
- ❌ Prometer manutenção além de 12 meses, ou SLA com multa, sem escalar.
