# O que o mercado cobra — referência por produto

Levantado em **2026-09-25**, com links testados nesse dia. É a **âncora** do preço na v6 do modelo
([`modelo.md`](modelo.md)): as tabelas de preço de cada produto saíram destas faixas, e é daqui que
sai o argumento na negociação.

> **Como ler.**
> - Preço marcado *(secundária)* veio de blog ou comparador, não da página do fornecedor.
> - Valores em dólar ficaram em dólar. Quando uma conta converte, está marcada **(conta nossa)**.
> - Página de preço muda. Antes de citar um número ao cliente, abra o link.
> - Se tiver busca na web, **confira a faixa do produto antes de cada proposta grande** (acima de
>   R$ 60 mil no ano 1) e registre a data. Faixa velha também é âncora errada.

---

## 1 · Maísa — agente de atendimento no WhatsApp

| Oferta | Modelo | Valores | Fonte |
| --- | --- | --- | --- |
| Forja (sob medida) | setup + operação | agente de WhatsApp: setup R$ 8–25 mil + R$ 800–2.500/mês | [forjadesistemas.com.br](https://forjadesistemas.com.br/blog/quanto-custa-ia-agentica-empresa/) |
| Forja (agente de IA, por complexidade) | setup + operação | simples R$ 8–20 mil + R$ 200–800/mês · médio R$ 20–40 mil + R$ 500–1.500 · complexo R$ 40–80 mil + R$ 800–3.000. Payback típico: 4–8 meses | idem |
| Blip | franquia de conversas; WhatsApp à parte | não público. Estimativa: setup R$ 8–25 mil + R$ 1.500–5.000/mês *(secundária)* | [blip.ai](https://www.blip.ai/en/pricing/) |
| Octadesk | mensalidade por contato ativo; IA inclusa; onboarding obrigatório | R$ 2.499/mês (3.000 contatos) e R$ 4.399/mês (5.500) | [octadesk.com](https://www.octadesk.com/precos) |
| Zenvia | usuários + interações + setup | US$ 130–845/mês; setup US$ 137–842; interação extra US$ 0,19–1,00 | [zenvia.com](https://zenvia.com/en/prices/) |
| Zap Trend (decomposição da mensalidade) | — | R$ 500–1.400/mês = tokens (R$ 30–250) + Meta (R$ 0–100) + infra (R$ 80–250) + **manutenção (R$ 390–800)** | [zaptrend.com.br](https://zaptrend.com.br/blog/quanto-custa-agente-ia-atendimento-whatsapp/) |
| SaaS de clínica (Secretária Odonto, Clinicorp IA, Sou Vitória, Densya) | mensalidade, em geral sem setup | R$ 120–1.000/mês | [secretariaodonto.com.br](https://secretariaodonto.com.br/) · [clinicorp.com](https://www.clinicorp.com/clinicorp-ia) · [souvitoria.com.br](https://souvitoria.com.br/ia-para-clinicas/) |
| Intercom Fin | por resultado, sem setup | US$ 0,99 por resolução (mínimo 50/mês) | [fin.ai/pricing](https://fin.ai/pricing) |
| Zendesk AI agents | por resolução, franquia por plano | US$ 1,50–2,00 por resolução *(secundária)* | [zendesk.com.br](https://www.zendesk.com.br/pricing/) |
| Salesforce Agentforce | conversa, crédito ou usuário | US$ 2/conversa; US$ 0,10/ação; a partir de US$ 125 por usuário/mês | [salesforce.com](https://www.salesforce.com/agentforce/pricing/) |

**API do WhatsApp (Meta).** Cobrança por mensagem de template desde 01/07/2025, faturada em reais
desde 01/07/2026. Marketing ~R$ 0,32 e utilidade ~R$ 0,035 por mensagem *(secundária)*. ⚠️ Blogs
anunciam cobrança de mensagens de **serviço** a partir de 01/10/2026; a documentação oficial não
dizia isso em 25/09/2026. Confira antes de montar a estimativa de repasse:
[documentação oficial](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).

**O que isto diz.**
- **O mercado tem três camadas:** SaaS de clínica (R$ 150–1.000/mês, sem setup), plataforma
  mid-market (R$ 2.500–4.400/mês, com onboarding pago) e sob medida (setup de R$ 8–80 mil). **A Maísa
  enterprise está na terceira**, e só se justifica pelo que o SaaS não entrega: integração com o
  sistema do cliente, fluxo próprio, várias unidades com regras diferentes.
- **Âncora de valor:** uma recepcionista ou atendente custa **R$ 3.500–6.000/mês** carregada (Forja).
  Compare a mensalidade com isso, não com o preço de outro software.
- **A mensalidade de manutenção do mercado é R$ 390–800**, sem tokens nem Meta. A nossa, que inclui
  horas de evolução, fica acima disso de propósito, e a proposta tem de dizer por quê.

## 2 · Plum — consulta a dados em linguagem natural

| Oferta | Modelo | Valores | Fonte |
| --- | --- | --- | --- |
| Implementação de Power BI no Brasil | projeto | básica R$ 8–20 mil; **avançada, com várias fontes e permissões, R$ 40–120 mil** | [beanalytic.com.br](https://beanalytic.com.br/blog/preco-implementacao-power-bi/) |
| Vanna.ai | assinatura com limite de perguntas | Team: US$ 500/mês, 300 perguntas/dia, apoio no setup | [vanna.ai](https://vanna.ai/pricing) |
| Dot | assinatura + créditos, usuários ilimitados | Team: US$ 720/mês, SSO e permissão por linha | [getdot.ai](https://www.getdot.ai/pricing) |
| Wren AI | assinatura + créditos | Enterprise Cloud: US$ 559/mês, permissão por linha e coluna | [getwren.ai](https://www.getwren.ai/pricing) |
| TextQL | consumo + assinatura | Team: US$ 250/mês, assentos ilimitados | [textql.com](https://www.textql.com/pricing) |
| Defog | fixo por volume | Enterprise Cloud: US$ 5.000/mês, 20 mil+ consultas, onboarding e SLA | [defog.ai](https://defog.ai/pricing) |
| Amazon QuickSight Q | usuário + pergunta + taxa fixa | 500 perguntas por US$ 250/mês; extra a US$ 0,50 | [aws.amazon.com](https://aws.amazon.com/quicksight/pricing/) |
| Snowflake Cortex Analyst | por mensagem + compute | ≈ US$ 0,13–0,20 por mensagem *(secundária)* | [docs.snowflake.com](https://docs.snowflake.com/en/user-guide/snowflake-cortex/pricing) |
| ThoughtSpot | por usuário, com cota de IA | Pro: US$ 50 por usuário/mês, 25 consultas por usuário | [thoughtspot.com](https://www.thoughtspot.com/pricing) |
| Power BI | por usuário | Pro: US$ 14 (~R$ 80 no Brasil); Copilot exige capacidade Fabric | [microsoft.com](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) |
| Metabase | base + usuário + tokens | Pro: US$ 575/mês; Enterprise a partir de US$ 20 mil/ano | [metabase.com](https://www.metabase.com/pricing/) |

**O que isto diz.**
- **Por assento não escala.** 542 usuários custariam ~US$ 27 mil/mês no ThoughtSpot Pro ou
  ~R$ 43 mil/mês no Power BI Pro **(conta nossa)**. O formato defensável é **plataforma fixa,
  usuários ilimitados, franquia de perguntas** — o que as ferramentas nativas de text-to-SQL fazem.
- **O preço por pergunta vai de ~US$ 0,05 a ~US$ 0,50.** Serve para desenhar franquia e excedente.
- **Integração e permissão são os maiores direcionadores de preço** de BI no Brasil, e o mercado
  cobra integração à parte: setup **por sistema integrado** e manutenção **por conector**.
- **"Enterprise" é sempre "sob consulta"**, e o que o justifica é o que o Plum já entrega:
  permissão por pessoa, SSO, auditoria, SLA.
- ⚠️ Os ROIs mais citados (Forrester TEI: 289% ThoughtSpot, 379% Fabric) são **encomendados pelos
  fornecedores**. Ordem de grandeza, não prova.

## 3 · Ludi — assistente escolar

| Oferta | Modelo | Valores | Fonte |
| --- | --- | --- | --- |
| ClassApp (comunicação) | adesão + por aluno | em 2019: R$ 900 de adesão + R$ 1 por aluno/mês. Hoje não é público | [techtudo (2019)](https://www.techtudo.com.br/noticias/2019/04/conheca-o-classapp-aplicativo-que-cria-comunicacao-entre-pais-e-escola.ghtml) |
| Diário Escola (gestão + IA) | por aluno | R$ 0,16 por aluno/dia ≈ R$ 58 por aluno/ano **(conta nossa)** | [diarioescola.com.br](https://diarioescola.com.br/o-que-voce-faz-com-16-centavos-por-dia/) |
| Letrus (IA de redação, rede pública) | por aluno/ano, reajuste por IGP-M, preço mantido se o volume variar ±15% | R$ 103–110 por aluno/ano em redes de 63 a 128 mil alunos | [proposta à SEDUC-GO (PDF)](https://www.educacao.go.gov.br/documentos/pregao2023/PROPOSTA%20COMERCIAL.pdf) |
| Khanmigo (distritos dos EUA) | por aluno/ano | US$ 15 por aluno | [blog da Khan Academy](https://blog.khanacademy.org/becoming-a-khan-academy-districts-partner/) |
| MagicSchool | por professor; Enterprise sob consulta | Plus: US$ 8,33 por usuário/mês no anual | [magicschool.ai](https://www.magicschool.ai/pricing) |
| Toolzz (agentes de WhatsApp para escolas) | por agente | R$ 399–3.900+/mês | [toolzz.com.br](https://www.toolzz.com.br/lp/agentes-ia-whatsapp-escolas-tecnicas-8b8f1d) |

**O que isto diz.**
- **O padrão é preço por aluno por ano**, em duas faixas: **comunicação escolar, R$ 12–58**; **IA
  pedagógica, R$ 103–110** (Letrus) ou US$ 15 (Khanmigo).
- **Escola compra com orçamento anual fixo**, e o contrato da Letrus é um modelo pronto: preço por
  aluno, faixa de ±15% sem reajuste, reajuste por índice.
- **Um piso mensal fixo cobre a escola pequena**, onde o por-aluno não paga a implantação.

## 4 · Implementação sob medida e hora de mercado, no Brasil

| Referência | Valores | Fonte |
| --- | --- | --- |
| Software house | hora de R$ 150 (freelancer) a R$ 600 (sênior); squad de 4–5 pessoas por R$ 60–120 mil/mês | [forjadesistemas.com.br](https://forjadesistemas.com.br/blog/quanto-custa-desenvolver-software-brasil-2025/) |
| Especialista em agente de IA | hora de R$ 180–400 | [forjadesistemas.com.br](https://forjadesistemas.com.br/blog/quanto-custa-ia-agentica-empresa/) |
| Consultoria de BI | hora de R$ 50 (júnior) a R$ 100–150 (especialista) | [beanalytic.com.br](https://beanalytic.com.br/blog/quanto-custa-consultoria-power-bi/) |
| Consultoria de IA | primeiro caso de uso R$ 30–120 mil; operação e evolução R$ 5–20 mil/mês | [waxi.com.br](https://www.waxi.com.br/blog/quanto-custa-consultoria-de-ia) |
| Salário de desenvolvedor | júnior R$ 4,2 mil · pleno R$ 7,8 mil · sênior R$ 15,6 mil por mês | [pesquisa Código Fonte 2025](https://pesquisa.codigofonte.com.br/2025) |

⚠️ **Semana-analista não é semana de 40 horas.** A nossa unidade é pessoa alocada × semana de
calendário, com dedicação parcial. "Somos N vezes mais baratos que uma software house" precisa
dessa ressalva.

## 5 · Quanto do valor o fornecedor captura

| Referência | Captura | Fonte |
| --- | --- | --- |
| Value pricing em serviços (Weiss) | 5% a 10% do valor anualizado (ROI de 10:1 a 20:1) | [a fórmula do autor](https://alanweiss.com/formula-for-value-based-fees/) |
| Três opções de Stark | 4%, 9% e 18% do valor | [Breaking Free From Hourly Billing (PDF)](https://www.bqe.com/hubfs/EBooks%20and%20WhitePapers%20and%20Reports/Ebook%20-%20Breaking%20Free%20From%20Hourly%20Billing%20-%20Jonathan%20Stark%20-%20BQE%20CORE.pdf) |
| Fornecedores de automação | 20% a 30% da economia | [BillingPlatform](https://billingplatform.com/blog/how-to-calculate-value-based-pricing) |
| Payback de 6 meses | equivale a capturar 50% do ganho do ano 1 — **frouxo demais como alvo** | conta nossa |

Daqui sai a faixa do modelo: **mirar 10%–20% do ganho anual declarado, nunca passar de 30%**.

## 6 · Manutenção e sustentação

| Referência | Valor | Fonte |
| --- | --- | --- |
| SAP e Oracle | 22% da licença por ano | páginas oficiais |
| Agências de IA (retainer, com operação e evolução) | 5% a 15% do setup **por mês** · EUA: US$ 3–20 mil/mês | [layer3labs.io](https://www.layer3labs.io/roi/ai-automation-agency-cost) |
| Aposentadoria de modelo | OpenAI avisa com ≥ 6 meses; Anthropic, com ≥ 60 dias | [OpenAI](https://developers.openai.com/api/docs/deprecations) · [Anthropic](https://platform.claude.com/docs/en/docs/about-claude/model-deprecations) |
| Drift de LLM | GPT-4 caiu de 84% para 51% de acerto numa tarefa entre duas versões | [Chen, Zaharia & Zou (2023)](https://arxiv.org/abs/2307.09009) |
| Taxa sobre custo de terceiros (CENP) | 15% quando quem vende gerencia o fornecedor; 5%–10% quando só contrata | [Normas-Padrão (PDF)](https://www.sinaprosp.org.br/wp-content/uploads/2020/04/Normas_Padrao_2011_Portugues.pdf) |

**Manter IA custa mais que manter software comum** (Sculley et al., *Hidden Technical Debt in
Machine Learning Systems*): modelo aposentado, API que muda, drift. É o que sustenta a mensalidade
acima dos 22% ao ano, desde que a proposta **declare** o que ela cobre.
