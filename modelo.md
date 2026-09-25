# Modelo de precificação enterprise do NI — v6

Fonte da verdade dos números. O [`SKILL.md`](SKILL.md) descreve o fluxo e aponta para cá; quando os
dois divergirem, **este arquivo está certo**.

**Escopo: a versão enterprise de três produtos — Maísa, Plum e Ludi.** Enterprise é a que passa por
implementação e adaptação ao cliente. O plug-and-play tem preço de tabela (§ Os três produtos) e não
é orçado aqui. Outros produtos da casa ficam fora deste modelo.

## O que mudou na v6, e por quê

Até a v5 o preço nascia do **esforço**: `semanas-analista × ITIP`, calibrado sobre as poucas
propostas que a casa já tinha vendido e herdado da estrutura de consultoria do núcleo de Dados. Três
problemas, todos documentados na pesquisa de 25/09/2026 (a íntegra está em [`mercado.md`](mercado.md)):

1. **Preço por esforço pune o que a casa quer fazer.** Quanto mais reuso, mais IA no
   desenvolvimento e mais rota de configuração, menos semanas, e menos a casa cobra, enquanto o valor
   que o cliente recebe não muda. É a **armadilha da produtividade**.
2. **A literatura põe o valor como âncora e o custo como piso.** O modelo fazia o contrário: custo
   como âncora, valor como ajuste de até 1,70.
3. **Calibrar em cima do próprio histórico reproduz o histórico.** A casa vende pouco; cada deal
   pesava demais, e o que a casa concluía ser preço baixo virava a régua.

**A v6 troca a âncora.** O preço de cada produto parte de uma **tabela ancorada no que o mercado
cobra por aquele tipo de produto**, na unidade que o mercado usa (conversas, perguntas, alunos).
Esforço, valor e histórico continuam no modelo, cada um no seu papel:

| Fonte | Papel na v6 | Onde |
| --- | --- | --- |
| **Mercado** | **âncora**: define a tabela e o formato de cobrança de cada produto | [`mercado.md`](mercado.md), tabelas abaixo |
| **Valor para o cliente** | **teto e alavanca**: captura de 10%–20% do ganho declarado, nunca acima de 30% | § A camada de valor |
| **A empresa** (pesquisa na internet) | **contexto**: porte real, momento, quem decide, alternativa | [`pesquisa-empresa.md`](pesquisa-empresa.md) |
| **Esforço** | **piso** e viabilidade: o preço não pode ficar abaixo do que custa entregar, e o projeto tem de caber na janela | § O piso de esforço |
| **Histórico da casa** | **evidência de reação**: onde um cliente já disse "caro", "gostei" ou "aprovado". Informa, não calibra | § O histórico |

**O que saiu:** o ITIP por rota e por modo de risco, o multiplicador `f_retorno × f_área ×
f_porte`, o teto de payback de 6 meses como teto de preço (capturava até 50% do ganho, muito acima do
que se pratica) e o teto de mensalidade por porte (substituído pelas faixas de cada produto).

**O que ficou igual:** os campos bloqueantes, a triagem de aderência, a qualificação, o repasse de
tokens e infra ao cliente, a meta de recorrência (MRR ≥ 25% do ano 1), a regra do cliente-âncora, a
política de desconto e o princípio de que **risco vira cláusula, não margem**.

---

## Como o preço se forma

```
Toda proposta sai com TRÊS OPÇÕES — Essencial, Recomendada, Completa.

para cada opção:
  setup        = tabela do produto                    ← Maísa por complexidade; Plum por linha;
               + itens novos × taxa de construção        Ludi = implantação + integrações
               (+ 15% se houver pacote enterprise)
  mensalidade  = tabela do produto                    ← a unidade do mercado: conversas,
               (+ adicionais: volume, conectores)        perguntas, alunos
  ano 1        = setup + mensalidade × 12
  repasse      = tokens + infra + APIs pagas, pagos pelo cliente, FORA do ano 1

conferências, nesta ordem:
  valor        captura = ano 1 da Recomendada ÷ ganho anual declarado   alvo 10–20% · máx. 30%
  alternativa  o que o cliente faria sem o NI, e quanto custa
  piso         ano 1 da Essencial ≥ semanas-analista × R$ 925            (se houver dimensionamento)
  recorrência  mensalidade × 12 ≥ 25% do ano 1                           gate 10
```

**O vendedor não escolhe mais um "modo de risco".** As três opções fazem esse trabalho, e melhor: o
cliente se autosseleciona, a opção do meio ganha pelo efeito compromisso, e a de cima serve de
âncora. **Qual opção o cliente escolheu é o dado mais valioso que a casa pode registrar**: é
preferência revelada, e com poucos deals é a única medida honesta de disposição a pagar.

### As três opções

As três têm de ser lucrativas, ou seja, estar acima do piso. **Nenhuma é chamariz.** O que muda entre
elas é **escopo e garantia**, não o nome.

| | **Essencial** | **Recomendada** ⭐ | **Completa** |
| --- | --- | --- | --- |
| Escopo | o núcleo do pedido. O que é "perto" ou "novo" e não é essencial vai para a fase 2, **com preço já escrito** | o pedido inteiro | o pedido + o que reduz o risco do cliente: unidades, canais ou integrações a mais, e cobertura maior de domínio |
| Evolução incluída na mensalidade | 2 h/mês | 6 h/mês | 12 h/mês |
| Suporte | resposta em 2 dias úteis | 1 dia útil | 4 h úteis para incidente crítico, **sem multa** (gate 6) |
| Acompanhamento pós go-live | 2 semanas | 4 semanas | 8 semanas |
| Relatório mensal de resultado | — | ✅ | ✅, com revisão trimestral |

🎯 **A Recomendada é o pedido do cliente.** Não infle a Completa para fazer a Recomendada parecer
barata, nem corte da Recomendada o que ele pediu para ela caber no bolso: se não cabe, a Essencial
existe para isso.

🎯 **O relatório mensal não é enfeite.** Quem vê o ganho todo mês usa mais e renova mais; agente de
IA pouco usado não renova. Ele mostra horas poupadas, conversas resolvidas, perguntas respondidas —
e é o que alimenta a pergunta de valor na renovação.

---

## Os três produtos

Retrato para a triagem de aderência. **A tabela diz onde o código está, não o que a casa pode
vender.**

| Produto | Linguagem | O que é, na versão enterprise |
| --- | --- | --- |
| **Maísa** | TypeScript | Atendente de IA no WhatsApp: atendimento, FAQ, agendamento, qualificação de lead, nota fiscal. **Autopiloto**: faz o trabalho, e compete com o orçamento de pessoas |
| **Plum** | Python | Porteiro entre as bases de dados e quem pergunta: consulta em linguagem natural, read-only, **em produção**. **Copiloto**: ajuda quem decide |
| **Ludi** | Python | Coordenador escolar virtual: FAQ por setor, comunicados, notas, agendamento, e análise de desempenho. **Copiloto** da escola |

**Vender é diferente de reaproveitar.** WhatsApp, agente com tools, agendamento e FAQ vetorial
existem nos três, **em implementações incompatíveis** (linguagens, multi-tenancy e embeddings
diferentes). Entre produtos atravessa **conhecimento**, não código: capacidade que a casa já fez em
outro produto é **"perto"** (baixa o risco, não o preço), nunca "pronta".

**O motor do Plum é o único reuso grande e honesto:** `planner → validação por allowlist → reforços
determinísticos → executor → renderização determinística`. O LLM propõe, o backend valida e executa;
o LLM nunca toca no dado. Herda-se o motor inteiro; **reconstroem-se em todo projeto a fonte, o
domínio e a autorização** — e são essas três camadas que viram as linhas da tabela do Plum.

### Integrações — o status de credencial vem antes do preço

**Escala de credencial:** `aberto` (cria conta sozinho) · `cadastro` (registra aplicação,
self-service) · `parceria` (exige negociação, **prazo desconhecido**) · `temos` · `bloqueado`.
`parceria`, `bloqueado` ou **não documentada** = a data não está nas mãos do NI (gate 3).

**Duas famílias de agenda, e a diferença muda o preço:**
- **Provedor-armazenamento** (Google Calendar, Outlook, CalDAV) guarda o que mandarem. É adapter.
- **Provedor-gestor** (Booksy, Trinks, Fresha, Belle) tem regras próprias de disponibilidade. **Não
  cabe nas portas atuais** — porta nova mais mapa de catálogo (gate 4).

### O plug-and-play, só para saber onde está o degrau

Maísa self-service, sem implantação: **R$ 59 · R$ 97 · R$ 149 por mês**. Entre isso e um setup
enterprise de cinco dígitos não existe SKU. Se o pedido cabe no plug-and-play, **venda o
plug-and-play**: enterprise é para o que a prateleira não faz.

---

## Maísa enterprise

**Formato:** setup por complexidade + mensalidade de sustentação e evolução + repasse de tokens, infra
e Meta a custo. **Referência de mercado:** agente de WhatsApp sob medida, setup de R$ 8–20 mil
(simples), R$ 20–40 mil (médio) e R$ 40–80 mil (complexo) (Forja; Blip); manutenção de R$ 390–800/mês
sem tokens (Zap Trend); plataforma mid-market de R$ 2.500–4.400/mês com IA inclusa (Octadesk).
Detalhe em [`mercado.md`](mercado.md) §1.

### A complexidade

| Nível | O que cabe | Sinal de reconhecimento |
| --- | --- | --- |
| **M1 · padrão** | atendimento, FAQ, agendamento em agenda de armazenamento, lembretes, handoff para humano. Uma regra de negócio para todas as unidades. Nenhum sistema do cliente além da agenda | outro cliente do mesmo segmento usaria igual, trocando o texto |
| **M2 · integrada** | M1 + **1 ou 2 sistemas** do cliente (CRM, ERP, sistema de gestão, emissor fiscal), **ou** um fluxo próprio (qualificação de lead com passagem ao comercial, cobrança, pós-venda), **ou** várias unidades com regras diferentes | "quando o lead responder X, cria no CRM e avisa o vendedor" |
| **M3 · complexa** | **3 ou mais sistemas**, ou mais de um canal, ou vários fluxos próprios ao mesmo tempo | a lista de integrações não cabe numa frase |

Na dúvida entre dois níveis, **fique no de baixo** e escreva o porquê. Item "novo" (ninguém da casa
fez) **não sobe o nível**: entra à parte, pela taxa de construção (§ Itens novos).

### A tabela

| | Essencial | **Recomendada** | Completa |
| --- | --- | --- | --- |
| **Setup M1** | R$ 10.000 | **R$ 14.000** | R$ 18.000 |
| **Setup M2** | R$ 22.000 | **R$ 30.000** | R$ 38.000 |
| **Setup M3** | R$ 42.000 | **R$ 55.000** | R$ 68.000 |
| **Mensalidade M1** | R$ 800 | **R$ 1.100** | R$ 1.500 |
| **Mensalidade M2** | R$ 1.400 | **R$ 1.900** | R$ 2.500 |
| **Mensalidade M3** | R$ 2.400 | **R$ 3.200** | R$ 4.000 |

**Adicional de volume:** acima de **3.000 conversas/mês**, **+R$ 250/mês a cada 1.000 conversas**,
nas três opções. É a curadoria e o monitoramento, que crescem com o volume. *(Conta nossa: na
Octadesk, cada 1.000 contatos a mais custam ~R$ 760 com plataforma e IA; cobramos um terço porque
plataforma e tokens aqui são repasse.)*

**Âncora de valor:** a alternativa da Maísa é gente. Uma recepcionista ou atendente custa
**R$ 3.500–6.000/mês** carregada. Escreva na proposta quanto a mensalidade + repasse representa disso.

⚠️ **Cobrar por resolução ainda não.** O mercado faz (US$ 0,99–2,00 por resolução), mas exige
definição de "resolução" no contrato, exclusão da conversa em que um humano interveio e telemetria
por cliente, que a casa não tem. Quando tiver, o caminho é **um bônus pequeno** sobre a taxa de
resolução medida nos logs do NI, **nunca** sobre as vendas do cliente.

## Plum enterprise

**Formato:** setup **por linha** (núcleo + cada sistema + autorização) + plataforma mensal **fixa,
com usuários ilimitados e franquia de perguntas** + manutenção por conector + repasse. **Nunca por
assento.** **Referência de mercado:** implementação de BI com várias fontes e permissões, R$ 40–120
mil; plataformas de text-to-SQL com usuários ilimitados, US$ 250–720/mês, e US$ 5.000/mês no
enterprise com SLA ([`mercado.md`](mercado.md) §2).

### O setup, por linha

| Linha | Essencial | **Recomendada** | Completa |
| --- | --- | --- | --- |
| **Núcleo** — mobilização, domínio (schema, prompt, planos determinísticos, vocabulário), 1 fonte própria do cliente, autorização binária, go-live | R$ 16.000 | **R$ 20.000** | R$ 25.000 |
| **+ por sistema de terceiro** (leitura via API) | R$ 10.000 | **R$ 10.000** | R$ 10.000 |
| **+ por fonte própria adicional** (outra base do cliente) | R$ 4.000 | **R$ 4.000** | R$ 4.000 |
| **+ isolamento por pessoa** ("cada um só vê o próprio dado") — gate 8 | R$ 12.000 | **R$ 12.000** | R$ 12.000 |
| **+ plataforma web** (SSO, perfis, painel), se pedida | R$ 15.000 | **R$ 15.000** | R$ 15.000 |

**O que muda entre as opções é o núcleo e quantas linhas entram**, não o preço de cada linha. A
Essencial cobre menos do domínio (as perguntas mais frequentes) e pode deixar um sistema para a fase
2; a Completa cobre o domínio inteiro e todos os sistemas. Integração e segurança não têm versão
"barata": ou é feita, ou fica de fora.

### A mensalidade

| Franquia de perguntas/mês, **usuários ilimitados** | Essencial | **Recomendada** | Completa |
| --- | --- | --- | --- |
| até 2.000 | R$ 1.500 | **R$ 1.800** | R$ 2.400 |
| até 6.000 | R$ 2.500 | **R$ 3.000** | R$ 3.900 |
| até 15.000 | R$ 4.000 | **R$ 4.800** | R$ 6.200 |
| acima de 15.000 | sob medida — escale | | |

**+ R$ 400/mês por conector de sistema de terceiro**, nas três opções. É quem paga o conserto quando
a API do outro lado muda, e é o que a casa esquecia de cobrar: um Plum com três sistemas tem três
vezes a superfície de manutenção de um Plum com um.

**Estourou a franquia dois meses seguidos:** sobe de faixa no mês seguinte, avisado por escrito. Não
se cobra por pergunta avulsa: o comprador enterprise paga por previsibilidade.

## Ludi enterprise

**Formato:** **preço por aluno por ano**, cobrado em 12 parcelas mensais, com piso mensal +
implantação. **Referência de mercado:** comunicação escolar, R$ 12–58 por aluno/ano (ClassApp,
Diário Escola); IA pedagógica, R$ 103–110 por aluno/ano (Letrus) ou US$ 15 (Khanmigo)
([`mercado.md`](mercado.md) §3).

### A tabela

| Módulo, por aluno ativo por ano | Essencial | **Recomendada** | Completa |
| --- | --- | --- | --- |
| **Ludi Atendimento** — coordenador virtual no WhatsApp: FAQ por setor, comunicados, notas, agendamento | R$ 15 | **R$ 24** | R$ 34 |
| **Ludi Pedagógico** — análise de desempenho e de simulados com agentes | R$ 30 | **R$ 45** | R$ 65 |
| **Piso mensal do contrato** | R$ 1.000 | **R$ 1.200** | R$ 1.500 |

⚠️ **O Pedagógico fica abaixo do topo do mercado de propósito.** A Letrus cobra R$ 103–110 com
resultado de aprendizagem medido em rede pública; o Ludi ainda não tem esse resultado. Quando tiver
um caso com número, a faixa sobe.

**Desconto por volume, por faixa** (como imposto de renda — cada faixa só vale para os alunos dentro
dela, para não haver degrau):

| Alunos | Preço por aluno |
| --- | --- |
| 1 a 2.000 | cheio |
| 2.001 a 5.000 | −10% |
| 5.001 a 20.000 | −20% |
| acima de 20.000 | −30% |

**Implantação:** **2 mensalidades, mínimo R$ 5.000** (o mercado cobra implantação de 2 a 4
mensalidades) + **R$ 10.000 por sistema acadêmico integrado** via API (mesma linha do Plum).

**Cláusulas que vêm do mercado (o contrato da Letrus é o modelo):** contrato de 12 meses, cobrança
mensal; **preço mantido se o número de alunos variar até ±15%**; recontagem na rematrícula; reajuste
anual por índice (IPCA).

**Escola pequena:** o piso mensal é o que paga a implantação e a sustentação quando o por-aluno não
chega lá. Abaixo de ~500 alunos, o piso quase sempre manda.

---

## Itens novos e o cliente-âncora

**Item "novo"** (ninguém da casa fez) não tem preço de mercado de produto, porque ainda não é
produto. Ele entra no setup pela **taxa de construção**:

```
item novo = semanas-analista da etapa × R$ 1.600
```

A equipe e as semanas vêm do validador técnico ou do PM (Passo 5 do `SKILL.md`), **nunca estimadas
pelo agente a partir do escopo**. R$ 1.600 por semana-analista fica bem abaixo do mercado (squad de
software house: R$ 60–120 mil/mês por 4–5 pessoas, ~R$ 3.000–6.000 por pessoa-semana) — com a
ressalva de que a nossa semana é de dedicação parcial.

**O cliente-âncora** é quem financia uma capacidade que ainda não existe:
- paga a construção e, **daquela capacidade**, fica depois em preço de custo, **sem licença**: paga
  sustentação corretiva, sem evolução;
- o NI mantém o direito de revender, e o âncora sabe disso desde o início;
- ⚠️ se ninguém souber dizer **quem mantém** a capacidade depois que o autor se formar, não venda
  como âncora (gate 5).

⚠️ **Quando o produto inteiro é novo para aquele cliente** (ex.: uma plataforma web de análise que o
Ludi ainda não tem), a estrutura é de âncora: **construção + sustentação** (≈22% da construção por
ano, na mensalidade), sem o por-aluno. Os clientes seguintes pagam a tabela.

## O pacote enterprise

**+15% no setup** quando o cliente tiver **dois ou mais** destes requisitos formais:
- SSO corporativo;
- questionário de segurança ou de LGPD a responder;
- homologação em ambiente de teste do cliente ou aprovação em comitê;
- contrato redigido pelo jurídico do cliente, com cláusulas próprias;
- cadastro de fornecedor com exigência documental.

É trabalho real que a empresa pequena não pede. **Não é "empresa grande paga mais"**: sem os
requisitos, não há pacote, qualquer que seja o faturamento. A pesquisa da empresa diz quando
perguntar (grupo, S.A., setor regulado). ⚠️ Os 15% são decisão, não medição.

---

## A camada de valor

### A pergunta obrigatória: quanto o cliente ganha por ano com isto?

Com o número **do cliente**, com autor e data:

```
captura = ano 1 da Recomendada ÷ ganho anual declarado
```

| Captura | Leitura |
| --- | --- |
| **abaixo de 10%** | há espaço. Se o ganho for ≥ R$ 200 mil, abra o **modo ROI-âncora** (abaixo) |
| **10% a 20%** | **o alvo.** No meio do que se pratica: 5–10% em value pricing de serviços, 20–30% em automação |
| **20% a 30%** | aceitável; mostre a conta na proposta |
| **acima de 30%** | **gate 13.** Não baixe o preço por unidade: **reduza o escopo** (a Essencial vira a recomendada, ou o resto vai para a fase 2) |

**Modo ROI-âncora.** Ganho anual **quantificado e verificável ≥ R$ 200 mil** e captura abaixo de 10%:

```
ano 1 da Recomendada = 15% do ganho anual     (Essencial 10%, Completa 20%)
  a mensalidade fica na tabela; o setup absorve a diferença
  nunca abaixo da tabela do produto — o modo existe para subir, não para descer
```

Dispara o **gate 9**: o preço descolou da tabela, e alguém que responde pela receita olha antes.

Como montar a conta **com** o cliente:

| Forma | Conta |
| --- | --- |
| horas poupadas | horas/mês × custo-hora carregado × 12 |
| custo-hora carregado | salário mensal × 1,8 ÷ 160 |
| pessoas que deixam de ser contratadas | nº de pessoas × salário × 1,8 × 12 |
| receita adicional | receita atribuível × margem de contribuição |

❌ **Nunca estime o ganho por conta própria e use o seu número para subir o preço.** A pesquisa da
empresa dá hipóteses para levar à reunião, não números para precificar. Sem ganho declarado,
escreva "perguntado, cliente não soube" e siga com a tabela.

### A melhor alternativa

O cliente compra se ganhar mais com o NI do que com a alternativa dele. Então **toda proposta
registra a alternativa real e o custo dela**: contratar uma pessoa, um SaaS de nicho, o relatório do
próprio ERP, uma planilha, a função nativa da plataforma que ele já usa.

- **Se a alternativa entrega o núcleo do pedido por menos da metade do ano 1 da Essencial,** a
  proposta tem de dizer **em reais** o que o NI entrega a mais: integração, regras próprias,
  unidades, segurança. Se não conseguir dizer, é caso de plug-and-play, ou de não vender.
- **Se a plataforma que ele já usa entrega o núcleo de fábrica,** nenhum preço ganha o deal (gate 12).
- **Existe diferencial negativo, e ele é nosso:** time que rotaciona, suporte de longo prazo. Garantia
  escrita, documentação e testes automatizados reduzem esse desconto. Diga na proposta como a casa
  cobre isso.

## O piso de esforço

O esforço deixou de formar o preço, mas **o preço não pode ficar abaixo do que custa entregar**.

```
piso = semanas-analista × R$ 925      ← comparado com o ano 1 da ESSENCIAL
```

- **Só calcule se houver dimensionamento** do validador técnico no card ou equipe declarada pelo PM.
  Sem isso, escreva "piso não calculado — sem dimensionamento" e siga. ❌ Não estime a equipe a partir
  do escopo: o backtest da casa mostrou que isso puxa todo projeto para o mesmo tamanho e erra o preço
  em 50%.
- `semanas-analista` = pessoas que **entregam** × semanas de **calendário**, incluindo as semanas de
  prova da Poli. PM, Tech Lead e validador não contam.
- **R$ 925** é a taxa média que a casa praticou nos projetos que vendeu, já com a coordenação. A casa
  concluiu que ela é **baixa**: por isso é piso, e só piso.
- **A Essencial abaixo do piso** (gate 11): o escopo é maior do que o nível da tabela sugere.
  Reclassifique o nível (M1 → M2), ou tire item, ou o que falta é item novo pela taxa de construção.

**Sanidade de calendário.** A casa entrega em **6 a 12 semanas**. Fora disso, confira: abaixo de 6
costuma faltar etapa (mobilização, acessos, go-live, treinamento); acima de 12 sobra escopo para uma
entrega, e é caso de **vender por fase**.

---

## A mensalidade

🎯 **O que o NI cobra por mês é trabalho da casa, não licença e não consumo:**

| Parte | O que é | Na proposta |
| --- | --- | --- |
| **sustentação corretiva** | bug, API de terceiro que mudou, modelo de IA aposentado ou que piorou | incluída, sem limite para corretiva |
| **evolução** | melhorias e funcionalidade nova | **2 / 6 / 12 h por mês** conforme a opção. O que passar é termo aditivo, a R$ 1.600 por semana-analista |
| **migração forçada** | troca de modelo de IA ou de versão de API por decisão do fornecedor | incluída **até 1 semana-analista por ano**; acima disso, orçada à parte |
| ~~operação~~ | tokens, infra, conversas da Meta, APIs pagas | **fora: repasse ao cliente** |

❌ **"Novas features sob demanda" sem teto de horas é passivo ilimitado num valor fixo.** Toda
proposta escreve o número de horas.

**Por que a mensalidade fica acima dos 22% ao ano do mercado de software.** Manter IA custa mais que
manter software comum: modelo aposentado com 60 dias de aviso, drift de qualidade entre versões, API
de terceiro que muda. A mensalidade só se sustenta **se declarar isso**. Proposta que chama de
"manutenção" o que é evolução faz o cliente comparar com contrato de sustentação e achar caro.

### O repasse, e a opção de consumo incluso

**Tokens, infra e APIs pagas são do cliente**, fora do ano 1. A proposta traz a cláusula de repasse,
cobrindo a execução **e** o pós-projeto, e uma **estimativa mensal**, escrita como estimativa:

```
repasse estimado/mês ≈ infra rateada + volume × custo por interação
```

Custo medido: **Maísa**, R$ 0,111 por interação em token + infra de ~R$ 185/mês rateada + mensagens
de template da Meta pela tabela oficial. **Plum e Ludi não medidos**: escreva "a medir no primeiro
mês", não chute.

**Opção de consumo incluso** (para quem quer previsibilidade — e o comprador enterprise costuma
querer):

```
mensalidade com consumo = mensalidade + repasse estimado × 1,15
franquia de consumo     = volume estimado × 1,2
excedente               = custo por interação × 1,15, cobrado no mês seguinte
```

Os 15% são a taxa de gestão de fornecedor que as normas brasileiras de agência admitem. Só ofereça
**com custo medido** (hoje, só a Maísa); no Plum e no Ludi, a partir do quarto mês, com o custo real
em mãos. ⚠️ Com consumo incluso, a conta de LLM, nuvem e WhatsApp fica no nome do NI: repassar vira
cobrança, e o reajuste por câmbio (infra em dólar) tem de estar escrito.

### Recorrência e revisão

- **Nenhuma proposta sai com mensalidade zero**, e **mensalidade × 12 ≥ 25% do ano 1** (gate 10).
  Com as tabelas da v6 isso quase sempre passa; se não passar, alguém cortou a mensalidade.
- **Revisão semestral:** mensalidade contra uso e escopo reais. Sobe ou desce de faixa, por escrito.
- **Cobrança mensal, não anual antecipada.** Quem paga todo mês usa de forma estável e renova mais.

---

## A forma do contrato

**Risco nunca vira margem. Vira cláusula.**

| Risco | Cláusula |
| --- | --- |
| sistema com credencial `parceria`, `bloqueado` ou não documentada | item condicionado, data condicionada à liberação — ou **fase 0** |
| escopo que o cliente ainda não fechou, dado de qualidade desconhecida | **fase 0 paga**: diagnóstico curto, com preço fechado, que entrega a especificação e o dimensionamento |
| pedido novo no meio do projeto | **controle de mudança**: trocar um requisito por outro de mesmo esforço sai sem custo; acréscimo é termo aditivo, pela taxa de construção |
| capacidade do time na virada de safra | janela de entrega declarada, não data cravada |
| término antecipado pelo cliente | taxa de saída escrita |

**Fase 0.** `semanas-analista da fase × R$ 1.600`, tipicamente **R$ 5–8 mil**, **abatida do setup**
se o cliente fechar a implementação em 30 dias. Use quando houver integração com sistema cuja API
ninguém confirmou, ou quando menos da metade do escopo estiver definida: é o formato que a pesquisa
recomenda para fornecedor jovem, que é quem mais absorve estouro em preço fechado.

**Item condicionado entra na proposta com a condição escrita ao lado, ou não entra.**

**Vender fase, não projeto.** Três meses é a janela de uma entrega, não da relação. Desenhe a fase 2
(com escopo e preço) **antes** de fechar a fase 1: é ela que a Essencial empurra para frente.

**Lista do que está fora do escopo**, sempre, na proposta.

---

## O histórico

As propostas que a casa já fez — vendidas e perdidas — são **evidência de como clientes reagiram a
preços**, não régua. Duas regras:

1. **Use a reação, não o preço.** "Um cliente de Maísa M1 recusou por caro um setup acima da
   Completa" é informação útil. "Cobramos X de um cliente parecido, então cobre X" não é: os preços
   da base saíram, na avaliação da própria casa, abaixo do que deviam.
2. **Ausência de objeção não é aprovação.** Muitos deals morreram antes do preço (decisor, timing,
   substituto). Só conta como teto o "caro demais" dito pelo cliente.

A reação observada por produto e por nível da tabela fica na versão interna da skill, com a base de
propostas do núcleo — não neste repositório público.

---

## Os gates

Qualquer um que dispare, **escale antes de apresentar**.

| # | Gate | Por quê |
| --- | --- | --- |
| 1 | **ano 1 da Recomendada > R$ 120.000**, ou prazo > 12 semanas | maior que qualquer projeto que a casa já entregou |
| 2 | **aderência duvidosa** — o balde "novo" é maior que "pronto" + "perto" juntos | é produto novo disfarçado de enterprise |
| 3 | integração com credencial **`parceria`**, **`bloqueado`** ou **não documentada** | a data não está nas mãos do NI |
| 4 | **provedor-gestor** (Booksy, Trinks, Fresha) | não cabe nas portas atuais |
| 5 | âncora **sem mantenedor declarado** | promete manutenção que a casa não tem |
| 6 | compromisso **> 12 meses** ou SLA com multa | o time rotaciona a cada 1–2 anos |
| 7 | contrato exige **repositório ou dado segregado** | muda o custo de versionamento e de operação |
| 8 | **isolamento por pessoa** exigido | desenvolvimento novo e requisito de segurança |
| 9 | **modo ROI-âncora ativo** | o preço descolou da tabela |
| 10 | **mensalidade zero, ou MRR abaixo de 25% do ano 1** | meta de recorrência do núcleo. Diga o motivo: caixa do cliente é informação; desconto ou esquecimento é decisão de quem responde pela receita |
| 11 | **preço fora da tabela** — desconto acima de 15%, Essencial abaixo do piso de esforço, ou preço acima da Completa sem ROI-âncora | a tabela é a âncora; sair dela é decisão, não improviso |
| 12 | **alerta crítico da pesquisa** — recuperação judicial, política corporativa que exclui o NI, plataforma atual que entrega o núcleo de fábrica | preço nenhum resolve; às vezes nem vale apresentar |
| 13 | **captura acima de 30%** do ganho declarado | o preço passou do que o valor sustenta: corte escopo |

Os gates 3 e 4 são de **prazo**, não de preço: a saída é item condicionado ou fase 0, nunca cobrar
mais.

## A política de desconto

**Desconto só existe em troca de contrapartida escrita:** caso público com nome e números,
referência ativa, pagamento antecipado, prazo de decisão curto, escopo reduzido.

| Faixa | Quem aprova |
| --- | --- |
| até 10% | vendedor |
| 10% a 15% | com contrapartida escrita |
| acima de 15% | escala — gate 11 |

**Negocie termo, não preço:** parcelas, entrada, prazo de pagamento e escopo são negociáveis; o preço
por unidade da tabela não. Cliente que acha caro tem a Essencial; baixar a Recomendada ensina o
cliente a pedir desconto.

## Na proposta: o que a pesquisa de comportamento manda

1. **Faça a primeira oferta**, com o número preciso que sai do modelo — R$ 30.000 de tabela, não
   "uns 30 mil". Número preciso com memória de cálculo é menos negociado.
2. **Três opções, lado a lado**, com a Recomendada marcada.
3. **Compare a mensalidade com o custo da alternativa** (uma atendente, um analista), não com preço
   de software.
4. **Nunca diga faixa de preço antes de dimensionar.** Faixa dita na primeira reunião vira teto na
   cabeça do cliente e âncora na cabeça de quem estima.

---

## Limites declarados desta versão

- **As tabelas são decisão ancorada em mercado, não medição.** Os níveis saíram das faixas públicas
  de [`mercado.md`](mercado.md), posicionados no meio delas. Nenhuma proposta foi feita com a v6 ainda:
  a primeira safra é o teste, e **a opção escolhida em cada proposta é o que vai calibrar**.
- **Faixas de mercado brasileiras de agente de IA vêm de poucos fornecedores** que publicam preço, e
  várias de blog. Enterprise quase nunca é público.
- **O Ludi Pedagógico não tem resultado medido**, e por isso fica abaixo do topo do mercado.
- **O adicional de volume da Maísa, os R$ 400 por conector do Plum, o pacote enterprise de 15% e
  as horas de evolução por opção são decisões**, derivadas por conta nossa, não medidas.
- **Custo por consulta do Plum e infra do Ludi não foram medidos**: sem eles não há opção de consumo
  incluso nesses dois.
- **O piso de R$ 925 é da safra que a casa julga barata.** Ele protege contra regressão, não diz
  quanto cobrar.
