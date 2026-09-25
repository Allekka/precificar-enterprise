# Modelo de precificação enterprise do NI

Fonte da verdade dos números. O [`SKILL.md`](SKILL.md) descreve o fluxo e aponta para cá; quando os
dois divergirem, **este arquivo está certo**.

**Escopo:** só a versão enterprise dos produtos — a que passa por implementação e adaptação. O
plug-and-play tem preço de tabela (§ Os produtos) e não é orçado por este modelo.

## Por que o preço não é só horas × taxa

O NI vende **software que continua rodando depois da entrega**, não projeto de consultoria. Três
consequências:

**O desconto de empresa júnior está na taxa, não no preço final.** Um time júnior cobra menos por
semana-analista que o mercado sênior, mas gasta mais semanas para a mesma entrega. Precificar por
custo produz preço próximo do de mercado sem a marca de mercado para sustentá-lo.

**O que a casa entrega tem custo recorrente.** Infra, tokens e conversas do WhatsApp existem depois
da última semana faturada — e são **repassados ao cliente**, que paga direto (§ O custo de operação
é do cliente). O que fica com a casa é a **manutenção**: bug, API de terceiro que muda, sustentação.
Preço fechado sem mensalidade é esse trabalho de graça, com atraso.

**A margem vem de reuso, não de multiplicador.** O motor do Plum é o exemplo: cada projeto que
reaproveita o esqueleto derruba o piso do seguinte.

---

## Os produtos

Retrato para o Passo 0. **A tabela diz onde o código está, não o que a casa pode vender** — ver a
nota abaixo dela.

| Produto | Linguagem | O que é |
| --- | --- | --- |
| **Maísa** | TypeScript | Atendente de IA no WhatsApp. Vendida hoje como secretária (agendamento, nota fiscal); atendimento e qualificação de lead por WhatsApp é o mesmo produto |
| **Smiller** | Python | A Maísa para clínica odontológica — um **fork**: correção numa não chega na outra |
| **Ludi / LUT** | Python | Coordenador escolar virtual: FAQ por setor, notas, comunicados |
| **Plum** | Python | Porteiro entre as bases de dados e quem pergunta: consulta em linguagem natural, read-only. **Em produção** |
| **Maestro** | — | Kits de campanha (social, conteúdo, mídia) gerados com IA a partir de dados via API. Em produção num cliente só: um segundo pedido é **extensão** |

**Vender é diferente de reaproveitar.** Uma capacidade que existe **3×** só é barata se a venda for
no **mesmo produto**; entre produtos, o que atravessa é conhecimento, não código.

| Capacidade | Onde existe | Vezes |
| --- | --- | --- |
| WhatsApp via Evolution API | Maísa (TS) · Smiller (Py) · Ludi (Py) | 3× |
| Agente LLM com tools | Maísa · Smiller · Ludi | 3× |
| Multi-tenancy | Maísa · Smiller · Ludi — **três mecanismos incompatíveis** | 3× |
| Agendamento | Maísa · Smiller · Ludi | 3× |
| FAQ com busca vetorial | Maísa · Smiller · Ludi — **dois modelos de embedding incompatíveis** | 3× |
| Google Calendar / OAuth | Maísa · Ludi | 2× |
| Handoff humano | Smiller · Ludi | 2× |
| Memória de conversa | Maísa · Smiller | 2× |
| Auth / sessão | Maísa · Ludi | 2× |
| Leads / outreach | Smiller · Ludi | 2× |
| Nota fiscal (Focus NFe) | Maísa | 1× |
| Comunicados · etiquetas com IA · notas escolares · e-mail transacional | Ludi | 1× |
| Debounce de mensagens | Smiller | 1× |
| CRM de leads por WhatsApp | protótipo arquivado, nunca foi para produção — **não é feature entregue** | 0× |

⚠️ **Capacidade que não está na Maísa mas que a casa já fez em outro produto** (handoff, leads) é
**"perto"** no Passo 0 — rota extensão, com a etapa no dimensionamento —, e **não fora de escopo**.
Só não desconte como se o código viesse junto.

### Integrações — o status de credencial vem antes do preço

| Provedor | Família | Credencial | Já implementado em |
| --- | --- | --- | --- |
| Evolution API (WhatsApp) | armazenamento | ✅ `temos` | Maísa, Smiller, Ludi |
| WhatsApp Cloud API (Meta) | armazenamento | ✅ em uso | Plum |
| Google Calendar | armazenamento | ✅ `temos` | Maísa, Ludi |
| Gemini · Anthropic · Supabase · Redis · Resend | — | ✅ em uso | vários |
| Focus NFe | — | ✅ em uso | Maísa |
| HubSpot · Meta Ads · Google Ads | — | ✅ em uso | Maestro |
| **Booksy** | 🔴 **gestor** | ⚠️ `parceria` | nenhum |
| ERP do cliente (ex.: Sankhya) | — | ❓ **não documentada** até alguém confirmar API de leitura | nenhum |

**Escala de credencial:** `aberto` (cria conta sozinho) · `cadastro` (registra aplicação,
self-service) · `parceria` (exige negociação, **prazo desconhecido**) · `temos` · `bloqueado`.
**Nunca prometa integração sem ler este campo.** `parceria` significa que a data de entrega não
está nas mãos do NI.

**Duas famílias, e a diferença muda o preço:**

- **Provedor-armazenamento** (Google Calendar, Outlook, CalDAV) guarda o que mandarem. O produto é
  dono da disponibilidade. É adapter — trabalho conhecido.
- **Provedor-gestor** (Booksy, Trinks, Fresha, Belle) tem modelo próprio de agenda e regras
  próprias de disponibilidade. Calcular o vago por fora produz horário que o próprio provedor
  recusa na hora de marcar. **Não cabe nas portas atuais** — é porta nova mais mapa de catálogo.

### Preços plug-and-play em vigor

**Preço de tabela, self-service, sem implantação** — fora do escopo deste modelo.

| | Essencial | Profissional ⭐ | Clínica |
| --- | --- | --- | --- |
| Mensal | R$ 59 | **R$ 97** | R$ 149 |
| Anual (11×) | R$ 649 | **R$ 1.067** | R$ 1.639 |
| Notas incluídas/mês | 60 | 200 | 500 |

⚠️ **O degrau é enorme.** Entre R$ 149/mês self-service e um setup enterprise de cinco dígitos não
existe SKU. Cliente de porte médio cai nesse vão.

### Duas regras da casa que aparecem na proposta

**Contrato de cliente-âncora.** Quem financia uma capacidade que ainda não existe paga o
desenvolvimento e depois fica em **preço de custo, sem licença** — paga manutenção corretiva, sem
evolução. O NI mantém o direito de revender, e o âncora sabe disso desde o início.

**Feature só vira produto com dois clientes pedindo e alguém que a mantenha.** Se ninguém sabe
dizer quem mantém depois que o autor se formar, a capacidade fica como extensão paga por quem a
quer.

---

## Como o preço se forma

```
semanas-analista = Σ_etapas (semanas_PERT × quem ENTREGA)   ← pessoas alocadas × semanas de
                                                              CALENDÁRIO, incluindo as de prova
                                                              da Poli. NÃO é esforço em FTE.
                                                              Trainee conta; TL, PM e validador não
rateio           = semanas-analista × fator_coordenação      ← PM + Tech Lead, por fora da equipe
base             = semanas-analista + rateio                 ← base = sw × 1,15 no padrão

referência  = base × ITIP_alvo          ← O PREÇO COMEÇA AQUI. Depende da rota E do modo de risco
PREÇO ANO 1 = referência × multiplicador de valor (1,00 a 1,70)
teto        = payback do cliente ≤ 6 meses
piso        = base × R$ 805             ← alarme de regressão. Nunca venda abaixo, e nunca
                                          comece por aqui

  depois, e só depois:  preço ano 1 = setup + (mensalidade × meses)
                        PISO de recorrência: nunca zero, MRR ≥ 25% do ano 1
                        TETO de mensalidade por operação atendida — o teto GANHA do piso
```

⚠️ **O modelo precifica o contrato do ano 1 inteiro. O corte entre setup e mensalidade é decisão de
caixa, não de preço.**

⚠️ **O ITIP praticado (R$ 805) não é referência de preço: é o diagnóstico.** Serve para duas
coisas e nenhuma outra: **acender o alarme de regressão** e **medir o que ficou na mesa**. Como
ponto de partida do cálculo, ou como comparável numa negociação, ele só reproduz o problema que
este modelo existe para corrigir.

**Fator de coordenação**, função de quantos projetos rodam em paralelo:

| Projetos simultâneos | 2 | 3 | 4 | 6+ |
| --- | --- | --- | --- | --- |
| Acréscimo sobre as semanas-analista | **+31%** | +21% | **+15%** | +10% |

Na dúvida, use **+15%**. O custo de coordenação é quase fixo: fica caro por projeto justamente
quando o portfólio esvazia.

**Por que não bandas de preço por porte.** Banda absoluta por rota × porte é indexada ao tamanho do
cliente e **ignora o tamanho do projeto** — erra por mais de 100% contra propostas reais.
`semanas-analista × ITIP`, olhando o contrato do ano 1, reproduz a prática da casa com erro de
~15%.

## As três rotas

| Rota | O que se faz | ITIP praticado (piso) | **ITIP alvo (padrão)** |
| --- | --- | --- | --- |
| **configuração** | parâmetro, conteúdo, credencial do cliente, treinamento | R$ 805 | **R$ 1.400** |
| **extensão** | código novo para um cliente, dentro do produto | R$ 805 | **R$ 1.600** |
| **motor + domínio** | reaproveita o esqueleto do Plum e reconstrói fonte, domínio e autorização | R$ 805 | **R$ 1.800** |

**O praticado é um número só.** A casa não diferencia rota no preço que pratica; a diferença de
ITIP alvo por rota é decisão de custo de senioridade.

⚠️ **Na configuração, o alvo de 1.400 está acima de um preço que um cliente já recusou por caro.**
Foi mantido de propósito: o objetivo é um preço que **faça sentido**, não o que maximiza
fechamento, e a ~R$ 950 a rota ficaria sem margem sobre o piso. Precificar no alvo ali é
território onde **se espera perder alguns deals** — aceitável enquanto a perda **por preço** ficar
em 20%–40%.

**Use o praticado para calcular o piso e o alvo para propor.** O piso responde "abaixo de quanto
estamos regredindo?"; o alvo responde "para onde a taxa deveria ir na próxima proposta".

Contra o mercado: R$ 805 por unidade de base equivale a **~R$ 20/hora**. Software house no Brasil
cobra R$ 250 a R$ 600/hora; freelancer sênior, R$ 90 a R$ 220. É esse múltiplo, não o preço
nominal, o argumento numa negociação.

⚠️ **Três avisos que deixam todo piso deste modelo otimista:**

- **Coordenador, Tech Lead e validador de CS** só entram pelo rateio — o validador, em conta
  nenhuma.
- **`semanas` são de CALENDÁRIO, incluindo as semanas de prova da Escola Politécnica**, em que o
  time não trabalha. O prazo da proposta tem de incluí-las, e elas contam em `semanas-analista`.
- **`semanas-analista` é pessoas declaradas × semanas de calendário.** Não converta para FTE: hoje
  o analista pega 1 projeto no geral e as duas medidas quase coincidem, mas no dia em que alguém
  pegar dois a conta muda de significado sem mudar de fórmula.

---

## A rota motor + domínio, por camada

É a rota mais aberta e a mais mal orçada, porque o que se herda e o que se joga fora não são óbvios.
Esta tabela existe para não estimar do zero — mas **a equipe declarada pelo PM ganha da soma
dela** (Passo 4).

**O que se herda é o motor:** `planner → validação por allowlist → reforços determinísticos →
executor → renderização determinística`, com a filosofia "o LLM propõe, o backend valida e executa".
O LLM nunca toca no dado; o contrato entre os dois é uma consulta read-only descrita em JSON. **É o
único lugar deste modelo onde o desconto de reuso é grande e honesto**, porque é a mesma linguagem
e a mesma base.

| Camada | Herda? | Semanas-analista |
| --- | --- | --- |
| Motor: planner, validação, executor, renderizadores | ✅ inteiro | 0 |
| Safeguards já pagos: fronteira de palavra na detecção de entidade, limpeza de histórico entre turnos, saneamento de alucinação do plano, timeout e retry do LLM, dedup de mensagem, junção de fragmentos | ✅ | 0 |
| Testes de padrão: validação, herança de contexto, reforço de filtro | ✅ | 0 |
| **Mobilização**: discovery, PRD e liberação de acessos | ❌ sempre | **2 semanas × a equipe inteira** (≈6) |
| **Executor — fonte própria** (base do cliente em Postgres, consulta em memória) | ✅ | 0,5 |
| **Executor — por API de terceiro** | ❌ reescreve | **4 por sistema** (PERT 2 / 4 / 6) |
| **Domínio**: schema, prompt, planos determinísticos, matcher de entidade, renderizadores de domínio | ❌ reescreve | 4 a 6 |
| **Autorização — porta binária** (autenticado vê tudo) | ✅ | 0,5 |
| **Autorização — isolamento por pessoa, obrigatório e não-removível** | ❌ novo | **2 a 3**, mais o teste que prova a impossibilidade de acesso a terceiro |
| **Persistência de estado** (tirar da memória do processo) | ❌ | 1 |
| **Go-live, treinamento e acompanhamento** | ❌ sempre | 3 a 4 |
| **PM e Tech Lead** | ❌ sempre | não são semanas cheias: entram pelo **fator de coordenação** (+10% a +31%) |
| **Plataforma web**: SSO, RBAC, shell, onboarding self-service | ❌ novo | ~3 semanas × 5 pessoas |

O "4 por sistema" vem de quem integrou: três APIs de terceiro feitas por um analista em menos de
10 semanas, com margem para credencial que atrasa, API mal documentada e reconciliação entre
fontes. Credencial de `parceria` ou não documentada continua sendo **cláusula** (gate 3), não
semana a mais.

**A lição vale além desta rota:** dimensionar por camada técnica e somar erra. Dimensione em **dois
blocos** — mobilização, que é quase fixa, e execução, que escala com o número de sistemas — e conte
o Tech Lead pelo rateio.

### As três perguntas que dimensionam esta rota

**1. De onde vêm os dados?** Base própria do cliente é o caso barato: o executor herdado consulta em
memória e pronto. **API de terceiro muda a natureza do executor** — deixa de ser consulta sobre uma
tabela cheia e vira chamada escopada por pessoa. Conte **por sistema**, e cheque o status de
credencial de cada um.

**2. Quão grande é o vocabulário do domínio?** O schema, o prompt, os planos determinísticos e o
matcher de entidade são 100% do cliente. Herda-se a *estrutura*, nunca o *conteúdo*.

**3. Quem pode ver o quê?** Esta é a pergunta que o comercial não faz e que mais muda o preço. Se
"todo mundo autenticado vê tudo", herda de graça. Se **cada pessoa só pode ver o próprio dado**, é
desenvolvimento novo: a identidade tem de ser resolvida antes da consulta, o filtro tem de ser
injetado pelo backend de forma não-removível, e o LLM nunca pode construí-lo. É requisito de
segurança, não conveniência, e dispara gate.

---

## Porte do cliente

Duas medidas, porque os produtos da casa têm dois tipos de usuário e confundi-los erra o preço nos
dois sentidos.

**U — quem opera.** Atendentes, secretárias, coordenadores, ou quem faz as perguntas ao Plum. Dirige
treinamento, perfis de permissão e complexidade de autorização.

**V — volume mensal.** Atendimentos, conversas ou consultas processadas. Define a banda da
mensalidade e a **estimativa do repasse** de tokens e conversas, que o cliente paga direto.

| Porte | Operação atendida | Referência |
| --- | --- | --- |
| **P0** micro | < 10 pessoas | consultório individual — enterprise raramente cabe aqui |
| **P1** pequeno | 10 – 50 | clínica com várias unidades, escola pequena |
| **P2** médio | 50 – 250 | rede, escola grande, operação regional |
| **P3** grande | > 250, ou faturamento > R$ 300M | quase sempre dispara gate |

⚠️ **Porte é da operação que vai usar a solução, não do grupo econômico.** Subsidiária brasileira
prevalece sobre receita global.

**Cobrança por assento é o padrão errado aqui**: o valor de produto agêntico não escala com o
número de logins. Porte entra só no `f_porte`. ⚠️ **V define a parte de operação — que é repasse —,
não a mensalidade inteira**: o que a casa vende no mensal é manutenção, e manutenção escala com
**superfície** (integrações, código sob medida). Ver § Mensalidade.

## Multiplicador de valor

Aplica sobre a referência. É a peça que captura valor além do custo.

```
multiplicador = f_retorno × f_área × f_porte      (teto 1,70)
```

| Fator | Valor | Critério |
| --- | --- | --- |
| **f_retorno** | 1,00 | o cliente não sabe quantificar o ganho |
| | 1,10 | ganho estimável em termos qualitativos ("some meia pessoa desse processo") |
| | *gate* | ganho **alto e quantificado** → vai para o modo ROI-âncora, abaixo |
| **f_área** | 1,00 | **core** — o cliente fala de receita, produto, cliente final |
| | 0,92 | **função-meio** — o cliente fala de processo, operação, back-office |
| **f_porte** | 1,00 | **operação atendida** até 50 pessoas |
| | 1,10 | 50 a 250 |
| | 1,25 | 250 a 1.000 |
| | 1,50 | acima de 1.000 |

⚠️ **O `f_porte` até 1,50 é decisão do núcleo, não medição**: empresa grande provavelmente aceita
gastar mais, mas a base ainda não tem como provar que a disposição a pagar acompanha o porte.

🎯 **`operação atendida` é quem VAI USAR, não quem assina o contrato.** É a diferença que decide o
fator, e errar aqui é o jeito mais fácil de inflar uma proposta indevidamente:

> Uma empresa de 1.500 funcionários comprando para **um setor de 70 pessoas** é `f_porte = 1,10`,
> não 1,50. O que se atende são 70.

Conte o que o produto de fato cobre: usuários do Plum, atendentes ou pacientes que a Maísa
responde, alunos que o Ludi acompanha. Na dúvida entre dois degraus, **fique no de baixo** e
escreva a contagem na proposta.

⚠️ **Faturamento não define o degrau — no máximo sobe um.** Um cliente com faturamento acima de
R$ 1B pode subir **um único degrau**, e **só se a operação atendida já estiver em 250 ou mais**.
Sem essa trava, o fator vira banda por porte.

**Área core vs função-meio é o fator mais subjetivo do modelo.** Regra prática: cliente de área
core fala de receita; cliente de função-meio fala de processo. Consulta de escala, férias e
reembolso pelos colaboradores é função-meio; um agente que atende o paciente e marca a consulta é
core.

⚠️ **Porte entra aqui, e só aqui.** Porte modula o preço em até 50%; **o tamanho do projeto
continua sendo o que o define**. Um projeto de 6 semanas-analista numa empresa de 5.000 pessoas
segue sendo um projeto de 6 semanas-analista: o `f_porte` multiplica, não substitui.

## Modo ROI-âncora

Ativa quando o cliente declara ganho anual **quantificado e verificável ≥ R$ 200k**.

⚠️ **Só vale quando dá um preço maior que `referência × multiplicador`.** O modo existe para
capturar valor acima do custo, não para justificar preço abaixo dele. Se a conta do ROI der menos,
descarte o modo — ganho declarado pequeno é motivo para rever o escopo, nunca para dar desconto.

```
setup = 10% a 20% do ganho anual líquido do primeiro ano
        piso: nunca abaixo de referência × multiplicador
        teto: preço total do ano 1 ≤ ganho anual ÷ 2   (payback ≤ 6 meses)
```

Fornecedores de automação enterprise capturam tipicamente 20% a 30% dos savings. O NI fica em 10% a
20% — abaixo, porque a marca não sustenta o topo da faixa.

**Como calcular o ganho, sempre com número do cliente:**

| Forma | Conta |
| --- | --- |
| horas poupadas | horas/mês × custo-hora carregado × 12 |
| custo-hora carregado | salário mensal × 1,8 ÷ 160 |
| headcount evitado | nº de pessoas × custo anual carregado |
| receita adicional | receita atribuível × margem de contribuição |

## Como partir o preço entre setup e mensalidade

O modelo produz **um número: o contrato do ano 1**. Partir esse número é decisão de caixa e de
risco, não de preço.

**A pergunta que decide:** a solução fica rodando e a casa mantém?

| Situação | Formato | Por quê |
| --- | --- | --- |
| A solução fica rodando e a casa mantém | **híbrido** — setup menor + mensalidade | sem mensalidade, a manutenção sai da margem do ano seguinte |
| Entrega fechada, o cliente opera sozinho, sem compromisso de manutenção | **tudo no setup** | não há manutenção a cobrir — e o piso de 25% (gate 10) diz que isso não é opção hoje |
| Cliente resiste ao valor cheio de uma vez | **híbrido** | mesmo preço no ano 1, entrada menor |
| Cliente-âncora | **híbrido, sem a parte de evolução** | o âncora fica em preço de custo — custo é a manutenção corretiva (a operação já é repassada), e o piso de 25% (gate 10) vale igual |

Em todos os formatos, **tokens, infra e APIs pagas são repassados ao cliente** e ficam fora do
contrato do ano 1 (§ O custo de operação é do cliente).

⚠️ **Mensalidade zero com "2 a 3 meses de acompanhamento inclusos" não é formato fechado** — é
híbrido com a mensalidade zerada. Depois do terceiro mês, ou existe contrato novo, ou existe
trabalho de graça.

## Mensalidade

🎯 **O que o NI vende na mensalidade é manutenção do produto dentro da empresa: correção de bugs e
sustentação. Não é licença de software.** A distinção troca o direcionador de preço e o comparável
de mercado:

| | Licença / SaaS | **Manutenção (o caso do NI)** |
| --- | --- | --- |
| direcionador | volume de uso | **superfície a manter**: integrações de terceiros e código sob medida |
| comparável | R$ 400 – 1.500/mês para PME | **15% a 25% do custo de implantação por ano** |
| o que quebra o contrato | pico de uso | terceiro mudar a API |

⚠️ **Mensalidade acima de 25% do setup por ano não é caro por si — é mensalidade que entrega mais
que manutenção sem dizer.** Prometer *"novas features sob demanda"* dentro do valor fixo é preço
de evolução com nome de manutenção: o cliente compara com um contrato de sustentação e acha caro, e
a casa fica devendo feature sem limite.

🎯 **Declare as partes na proposta, separadas** — duas na mensalidade, e a operação como repasse:

| Parte | Direcionador | Referência |
| --- | --- | --- |
| **manutenção corretiva** — bugs, quebra de API de terceiro | nº de integrações e código sob medida | 15% a 25% do setup por ano |
| **evolução** — horas de feature por mês | **tem de ter limite declarado** | é o que justifica passar dos 25% |
| ~~operação~~ — infra, tokens, APIs pagas | volume mensal V | **fora da mensalidade: repassada ao cliente**, com a estimativa escrita na proposta (abaixo) |

⚠️ **"Features sob demanda" sem teto de horas é passivo ilimitado num valor fixo.** Se a evolução
entra na mensalidade, **escreva quantas horas por mês** e o que acontece quando estoura — termo
aditivo.

**Âncora e seguidor pagam mensalidade.** O âncora paga **manutenção corretiva**, sem a parte de
evolução. O seguidor paga as duas. Os dois pagam a operação direto, pelo repasse.

| Volume mensal (V) | **Banda** |
| --- | --- |
| < 500 | R$ 500 – 900 |
| 500 – 2.000 | R$ 900 – 1.800 |
| 2.000 – 10.000 | R$ 1.800 – 4.000 |
| > 10.000 | a partir de R$ 4.000, com componente variável |

**Três integrações de terceiro custam três vezes para manter.** Quando qualquer uma mudar a API, o
conserto sai da mensalidade — por isso o direcionador é superfície, não volume.

Mercado: custo mensal total de agente de IA para PME brasileira fica entre R$ 400 e R$ 1.500,
somando plataforma, conversas da API do WhatsApp e tokens; em WhatsApp Business API com volume alto,
de R$ 800 a R$ 8.000. **Modelo híbrido — setup mais mensalidade — é o padrão de 2026.**

### 🎯 O custo de operação é do cliente

Decidido pelo núcleo: **tokens, infra e APIs pagas (conversas da API do WhatsApp, emissor fiscal,
APIs de Ads) são repassados ao cliente**, e a proposta diz isso por escrito. A mensalidade do NI é
**só trabalho da casa**: manutenção corretiva e evolução com limite de horas.

- **Não existe piso de mensalidade por custo.** A regra `mensalidade ≥ 3 × custo recorrente` só
  volta se a proposta **incluir** a operação no valor — exceção, e com o custo medido.
- **O cliente vai perguntar quanto custa o token.** Então a proposta leva uma **estimativa do
  repasse**, declarada como estimativa, não como preço:

  ```
  repasse estimado/mês ≈ infra rateada + V × custo por interação
  ```

  Prior da Maísa: infra ~R$ 185/mês e ~R$ 0,111 por interação em token. Conversas de WhatsApp pela
  tabela da Meta. Plum, Ludi e Smiller **não têm custo medido** — escreva "a medir no primeiro mês"
  em vez de chutar.
- **Volume alto não quebra o corte**: o custo da Meta vai no repasse, não na mensalidade.
- **O caixa do cliente é mensalidade + repasse.** O teto de mensalidade por porte vale só para a
  mensalidade do NI, mas se a soma com o repasse estimado passar do teto, **avise na saída** — o
  deal pode morrer por caixa do mesmo jeito.
- **Defina de quem é a conta.** O ideal é a conta de LLM, nuvem e WhatsApp no nome do cliente. Se
  ficar no nome do NI, repassar vira cobrança — com serviço cotado em dólar, sujeito a câmbio —, e
  isso tem de estar escrito.
- ⚠️ **Cubra o período de projeto também.** Escreva que o repasse vale "ao longo da execução e do
  período pós-projeto", ou declare que o consumo durante o projeto está no setup.

### 🎯 Piso de recorrência — a meta declarada do núcleo

O núcleo quer migrar para receita recorrente. Em vez de meta por produto, **um piso duro para
todas as rotas**:

> **Nenhuma proposta sai com mensalidade zero.**
> **A mensalidade × meses vale no mínimo 25% do contrato do ano 1.**

Quem dispara isso é o **gate 10**. O "2 a 3 meses de acompanhamento incluso" **deixa de ser uma
opção**.

**Como chegar nos 25%:** `mensalidade ≥ (0,25 × contrato do ano 1) ÷ meses`. Com 12 meses, a
mensalidade mínima é `contrato do ano 1 ÷ 48`. (Só se a operação estiver incluída, exceção,
compare com `3 × custo recorrente` e **vale o maior dos dois**.)

#### ⚠️ E um teto, porque mensalidade alta demais não cabe no caixa do cliente

**A mensalidade tem teto, pela mesma escada de `operação atendida` do `f_porte`:**

| Operação atendida | **Teto de mensalidade** | De onde vem a âncora |
| --- | --- | --- |
| até 50 | **R$ 1.500** | topo da faixa de mercado para PME brasileira (R$ 400 – 1.500) |
| 50 a 250 | **R$ 3.000** | 2× a faixa PME |
| 250 a 1.000 | **R$ 5.000** | acima de toda mensalidade que a casa já propôs |
| acima de 1.000 | **R$ 8.000** | topo da faixa de WhatsApp Business API com volume alto |

**A ordem de cálculo, com as regras que podem colidir:**

```
mensalidade = banda por volume V            ← V é o que DEFINE
  piso:    ≥ 25% do contrato do ano 1 ÷ meses
  (piso por custo, ≥ 3 × custo recorrente, só se a operação for incluída — exceção)
  TETO:    teto por operação atendida       ← o teto GANHA de todos os pisos
```

⚠️ **Quando o teto morde, o contrato do ano 1 NÃO muda — muda só o corte.** A mensalidade para no
teto e **o setup absorve a diferença**. O **gate 10** dispara para que alguém registre que a meta
de recorrência não coube naquele cliente — é informação, não erro.

**Exemplo do conflito.** Setup de R$ 80.000 numa operação de 40 pessoas: o piso de 25% pediria
R$ 2.222/mês, mas o teto do porte é R$ 1.500. Vale R$ 1.500 — ano 1 de R$ 98.000, MRR de 18%,
gate 10 disparado **por limite de porte, não por desconto**.

| Operação atendida | Teto de mensalidade | Acima deste setup, nem os 25% cabem |
| --- | --- | --- |
| até 50 | R$ 1.500 | R$ 54.000 |
| 50 a 250 | R$ 3.000 | R$ 108.000 |
| 250 a 1.000 | R$ 5.000 | R$ 180.000 |
| acima de 1.000 | R$ 8.000 | R$ 288.000 |

#### A escada de transição

Os 25% são ponto de partida deliberado, não destino. **Suba 10 pontos por safra, e só quando as
duas condições valerem:**

| Condição para subir o piso | Por quê |
| --- | --- |
| **nenhum deal perdido por causa da mensalidade** na safra anterior, com motivo escrito | a perda é o instrumento, não o palpite |
| **superfície a manter declarada** (nº de integrações e código sob medida por contrato) | com a operação repassada, a mensalidade é só manutenção e evolução — subir a fatia exige mostrar o que se mantém |

**Teto da escada: 65%.** ⚠️ **A escada sobe por porte, não para a casa inteira:** numa operação de
até 50 pessoas, 65% exigiria setup abaixo de ~R$ 9.700, ou seja, **65% só é realista em operação
grande**. O teto de mensalidade manda sempre.

---

## Quanto arriscar no preço

**Suba, e acompanhe a taxa de perda POR PREÇO — não a taxa de perda, e não o preço.** A maior
parte das perdas do enterprise acontece por autoridade (decisor fora da mesa), timing ou substituto
nativo — e nenhum ajuste de preço recupera essas. Tratar os dois números como o mesmo levaria a
cortar preço para resolver um problema de qualificação.

| Taxa de perda **por preço** | Leitura |
| --- | --- |
| 0% | o preço ainda está baixo. Suba de novo |
| **20% a 40%** | **faixa saudável — o preço está encostando no teto** |
| acima de 50% | passou. Volte um degrau, ou o problema é escopo, não preço |

⚠️ **Motivo de perda auto-reportado subestima preço** — "timing" é mais confortável de escrever que
"estava caro". Antes de creditar uma perda ao preço, elimine: decisor não acessível, sponsor que
trocou no meio do ciclo, timing de fim de ano, proposta sem equipe declarada.

⚠️ **A perda também não é monotônica no preço.** Onde a plataforma que o cliente já usa entrega o
caso de uso (a IA nativa da Meta, do Google, do ERP), **nenhuma postura de preço ganha o deal** —
nem abaixo do piso. É decisão de produto.

### As três posturas

| | **1 · Ancorada em custo** | **2 · Ancorada em mercado** | **3 · Ancorada em valor** |
| --- | --- | --- | --- |
| Fórmula | base × R$ 1.300 | base × ITIP alvo × multiplicador | 10% a 20% do ganho anual declarado |
| Argumento ao cliente | transparência: nosso esforço × nossa taxa | somos várias vezes mais baratos que software house | você ganha X, pagamo-nos com Y meses |
| Risco de perder o deal | baixo | médio | alto |
| Exige do NI | nada — só decidir | defender o múltiplo numa conversa | o cliente quantificar o ganho |
| Quando usar | **exceção** — o cliente já recusou um número, ou nem o diagnóstico do escopo fechou | **padrão** | ganho declarado ≥ R$ 200k e área core |

⚠️ **A postura 1 é exceção e precisa de fato, não de impressão.** "Relação nova" e "cliente
sensível a preço" descrevem praticamente todo lead da casa. Usada assim, a postura 1 vira o padrão
pela porta dos fundos. Ela só se justifica quando **o cliente recusou um número concreto**, e a
exceção vai registrada com o motivo.

### Alavancas que sobem o preço médio sem subir o risco de perder

**Menu de duas opções.** Proposta com escopo enxuto e escopo completo, lado a lado, muda a pergunta
do cliente de "aceito ou não" para "qual dos dois".

**Mensalidade obrigatória quando a solução fica rodando.** Zero com meses de acompanhamento
inclusos é receita recorrente dada de graça.

**Desconto amarrado a prazo de decisão.** É a contrapartida mais barata que existe.

**Piloto pago antes do projeto cheio.** Reduz o risco percebido pelo cliente e permite preço maior
no contrato principal.

**A pergunta de ROI.** Abre a postura 3, a mais cara de todas, e não custa deal nenhum.

❌ **O que NÃO fazer ainda: cobrança por resultado ou gainshare.** Exige medir o resultado, e a casa
não tem telemetria por cliente. Cobrar por variável que não se mede é transferir risco para quem
não pode absorvê-lo.

## O modo de risco — escolhido no início, aplicado até o fim

O vendedor escolhe **um dos três modos** no começo do cálculo, e ele vale para a proposta inteira.
É o mesmo `ITIP alvo` da tabela de rotas, em três níveis:

| Rota | 🛡️ Conservador | ⚖️ **Padrão** | 🔥 Agressivo |
| --- | --- | --- | --- |
| **configuração** | R$ 1.100 | **R$ 1.400** | R$ 1.700 |
| **extensão** | R$ 1.200 | **R$ 1.600** | R$ 2.000 |
| **motor + domínio** | R$ 1.300 | **R$ 1.800** | R$ 2.400 |

Num projeto típico de 8 semanas × 3 analistas (24 sw, base 27,6), isso dá:

| Rota | 🛡️ Conservador | ⚖️ Padrão | 🔥 Agressivo |
| --- | --- | --- | --- |
| configuração | R$ 30.400 | R$ 38.600 | R$ 46.900 |
| extensão | R$ 33.100 | R$ 44.200 | R$ 55.200 |
| motor + domínio | R$ 35.900 | R$ 49.700 | R$ 66.200 |

*Para comparar: o piso nesse tamanho é R$ 22.200.*

**🛡️ Conservador** — ponto médio entre o praticado (R$ 805) e o alvo da rota. Não é "voltar ao
preço antigo", é o degrau mais baixo que este modelo aceita. Use quando: **o deal precisa fechar**
(meta de safra, primeira venda num setor, case que vocês querem), concorrente conhecido na mesa, ou
cliente que já disse que orçamento é problema. **Escreva por que escolheu** — conservador sem motivo
escrito vira o padrão pela porta dos fundos.

**⚖️ Padrão** — o alvo da rota. É o default e **não precisa de justificativa**.

**🔥 Agressivo** — o nível que a casa já viu passar em motor + domínio sem recusa por preço.
Em extensão, não testado. ⚠️ **Em configuração, fica acima de um preço já recusado por caro** — é
o território com um "não" conhecido.

**Exigências do modo agressivo**, as duas obrigatórias:
1. **a pergunta de ROI respondida pelo cliente** — sem ganho declarado, não há argumento para o
   número, e o vendedor vai defender o preço com a própria opinião;
2. **decisor identificado e acessível** — preço alto com decisor ausente é a pior combinação.

Se qualquer uma faltar, caia para o padrão.

| Situação | Modo |
| --- | --- |
| motor + domínio, decisor acessível, ganho declarado | 🔥 agressivo |
| caso normal, sem sinal forte nos dois sentidos | ⚖️ padrão |
| rota configuração acima de R$ 1.400 | ⚖️ padrão — ali existe um "não" medido |
| deal que precisa fechar, ou concorrente na mesa | 🛡️ conservador, **com motivo escrito** |
| cliente sem orçamento declarado, ou produto com substituto nativo | nenhum: **não é deal de preço** |

⚠️ **O modo mexe só no `ITIP alvo`.** Piso, teto de payback, multiplicador, piso de recorrência e
teto de mensalidade por porte **valem igual nos três** — são limites, não preferências.

## A janela de três meses, e por que o ITIP sozinho não basta

O NI entrega em **no máximo ~3 meses** (propostas de 6 a 12 semanas, mediana 8). Preço por esforço
multiplica semanas por taxa — então **a janela curta põe teto de construção no preço**: o maior
projeto que a casa já fez (40 sw) dá R$ 82.800 de referência na rota motor + domínio. **E cobrar
por esforço pune o reuso**: quanto melhor fica o motor do Plum, menos semanas o projeto leva — e
menos a casa cobra.

**Três saídas, em ordem de impacto:**

**1. Recorrência — e a janela curta é uma vantagem aqui.** O projeto acaba em 10 semanas; a receita
não precisa acabar junto. Um setup de R$ 45.000:

| Fatia de MRR | Mensalidade | Ano 1 | Acumulado em 3 anos |
| --- | --- | --- | --- |
| 25% (piso de hoje) | R$ 1.250 | R$ 60.000 | R$ 90.000 |
| 45% (um degrau) | R$ 3.068 | R$ 81.818 | R$ 155.455 |
| **65% (teto da escada)** | **R$ 6.964** | **R$ 128.571** | **R$ 295.714** |

⚠️ **Mas os 65% exigem porte**: a mensalidade de R$ 6.964 só cabe em operação acima de 1.000
pessoas atendidas. Em operação pequena, a saída é a pergunta de ROI e a venda por fase.

**2. A pergunta de ROI, obrigatória.** É a única rota que quebra o teto do esforço, porque não
depende de horas: um projeto de 8 semanas que economiza R$ 600k/ano vale R$ 60–120k no modo
ROI-âncora, contra os ~R$ 30k que o esforço daria. **O cliente precisa declarar o número.**

**3. Vender fase, não projeto.** Três meses é a janela de **uma entrega**, não da relação. Desenhe a
fase 2 **antes** de fechar a fase 1, para que ela exista como escopo e preço e não como intenção.

❌ **O que NÃO resolve:** subir o ITIP para compensar a janela. A saída é mudar **o que** se cobra
(recorrência, valor, fase), não inflar a taxa.

---

## Os dez gates

Qualquer um que dispare, escale antes de apresentar.

| # | Gate | Por quê |
| --- | --- | --- |
| 1 | **semanas-analista > 40**, ou contrato do ano 1 > **R$ 90.000** | maior que qualquer projeto que a casa já entregou |
| 2 | **aderência duvidosa** — no Passo 0, o balde "novo" é maior que "pronto" + "perto" juntos | é produto novo disfarçado de enterprise. Capacidade que a casa já fez em outro produto conta como "perto", não como faltante |
| 3 | integração com credencial **`parceria`**, **`bloqueado`** ou **não documentada** | a data não está nas mãos do NI |
| 4 | **provedor-gestor** (Booksy, Trinks, Fresha) | não cabe nas portas atuais: porta nova + mapa de catálogo |
| 5 | âncora **sem mantenedor declarado** | promete manutenção que a casa não tem |
| 6 | compromisso **> 12 meses** ou SLA com multa | o time rotaciona a cada 1–2 anos |
| 7 | contrato exige **repositório ou dado segregado** | muda o custo de versionamento e de operação |
| 8 | **isolamento por pessoa** exigido | autorização por linha é desenvolvimento novo e é requisito de segurança |
| 9 | **modo ROI-âncora ativo** | o preço descolou do piso |
| 10 | **mensalidade zero, ou MRR abaixo de 25% do contrato do ano 1** | é a meta de recorrência do núcleo (§ Piso de recorrência). ⚠️ Ao escalar, **diga qual dos dois motivos**: se foi o **teto por porte** é informação, não erro; se foi **desconto ou esquecimento**, é decisão de quem responde pela receita, não do vendedor |

Os gates 3 e 4 são de **prazo**, não de preço, e a saída deles não é cobrar mais: é tirar o item do
escopo fechado e transformá-lo em etapa condicionada.

## Política de desconto

**Desconto só existe em troca de contrapartida**, e a contrapartida vai escrita na proposta: caso
público com nome e números, referência ativa, pagamento antecipado, escopo reduzido, ou prazo
folgado.

| Faixa | Quem aprova |
| --- | --- |
| até 10% | vendedor |
| 10% a 15% | com contrapartida escrita |
| acima de 15% | escala — é gate |

**Baixar preço não compra o sim.** Perder por preço é quase sempre orçamento ou relacionamento, não
o número.

## Risco nunca vira margem

Risco não é multiplicador — é cláusula.

| Risco | Cláusula, não preço |
| --- | --- |
| credencial de terceiro pendente | etapa separada, data condicionada à liberação |
| dado do cliente em qualidade desconhecida | etapa de diagnóstico com saída antecipada |
| escopo que o cliente ainda não fechou | item condicionado, com a condição escrita ao lado |
| capacidade do NI na virada de safra | janela de entrega declarada, não data cravada |

Item condicionado **entra na proposta com a condição escrita ao lado, ou não entra**.

## Limites declarados desta versão

- **A forma foi validada, os níveis não.** `semanas-analista × ITIP` reproduz a prática da casa,
  mas foi ajustado sobre poucos pontos. Os ITIP alvo, o rateio e o `f_porte` até 1,50 são
  **decisão do núcleo**, não medição.
- **O elo fraco é quem decide a equipe.** Com a equipe declarada pelo PM, o piso erra ~15%; com a
  equipe estimada a partir do escopo, ~50%. Por isso o Passo 4 trata a equipe como pergunta.
- **O fator de coordenação vem de um projeto só**, e o validador de CS não está em conta nenhuma.
- **Custo de operação do Plum, do Ludi e do Smiller não foi medido.**
- **Nenhuma implementação foi medida ponta a ponta** — sabe-se preço, prazo e equipe declarada, não
  o esforço real gasto.
