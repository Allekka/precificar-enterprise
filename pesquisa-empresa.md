# Pesquisar a empresa antes de precificar

A ata do card diz o que o cliente **falou**. A pesquisa diz o que a empresa **é**: tamanho real,
momento, quem decide, o que ela já usa. As duas juntas embasam o preço. Nenhuma sozinha basta.

**Por que isto existe.** A maior parte das perdas do enterprise não é de preço: é decisor que não
estava na mesa, sponsor que trocou, verba "para o ano que vem", plataforma que já entregava de
fábrica, política global de TI que exigia outro fornecedor. **Várias delas dão sinal numa busca de
dez minutos**, e as outras viram pergunta certa para a próxima reunião.

## Quando e quanto

- **Sempre, antes do Passo 4** (a tabela do produto) do [`SKILL.md`](SKILL.md). É a primeira coisa
  depois de ler o material.
- **Uns dez minutos, oito a doze buscas.** Não é due diligence. Se a empresa não aparece em lugar
  nenhum, isso também é informação: escreva.
- **Sem ferramenta de busca na web?** Peça ao comercial as cinco respostas do § O que responder,
  uma por vez, e declare na saída que a pesquisa não foi feita pela skill.

## As regras

1. **Pesquise a empresa, não pessoas.** Nome e cargo público de quem decide (site, página da empresa
   no LinkedIn, notícia) pode. Vida pessoal, contato particular e perfis pessoais não.
2. **Não mande dado do card para a busca.** Busque por nome, CNPJ, site e setor. Nunca por valor de
   proposta, requisito ou qualquer coisa que o cliente contou em reunião.
3. **Toda afirmação sai com fonte e data.** Separe **fato de fonte primária** (site oficial, Receita,
   comunicado, balanço) de **estimativa de fonte secundária** (blog, agregador, notícia de terceiro).
4. **A pesquisa não substitui número do cliente.** Volume, porte da operação e ganho que vierem da
   internet entram como **"a confirmar com o cliente"**. ❌ E o ganho anual **nunca** sai da pesquisa
   para subir o preço: vira **pergunta para a próxima reunião**, com a sua hipótese ao lado.
5. **Ata e pesquisa em conflito: vale a ata para o que o cliente disse, e a divergência vira
   pergunta.** A ata diz 50 atendentes e o LinkedIn diz 2.000 funcionários? Provavelmente as duas
   estão certas: a operação atendida é um setor. Pergunte, não escolha.
6. **Faturamento não vira multiplicador.** Porte entra no preço pela **unidade do produto**
   (conversas, perguntas, alunos) e pelos requisitos enterprise que o cliente tiver, nunca por
   "empresa grande paga mais". Faixa de preço por porte já foi testada e reprovada (erro de 164%).

## O que responder

Cinco perguntas, e a saída traz as cinco com fonte.

### 1. Qual o tamanho real — da empresa e da operação que vai usar?

| Onde olhar | O que tirar |
| --- | --- |
| Consulta pública de CNPJ (Receita Federal e sites de consulta) | razão social, data de abertura, porte na Receita, CNAE, capital social, matriz e filiais |
| Site oficial | número de unidades, lojas, clínicas ou escolas; cidades; serviços |
| Página da empresa no LinkedIn | faixa de funcionários; crescimento |
| Rankings (Valor 1000, Exame Melhores e Maiores) e balanço, se for S.A. | faturamento, só para empresa grande |
| **Escola:** QEdu e Censo Escolar (INEP) | **matrículas por escola e por etapa** — é a unidade de preço do Ludi |

### 2. Em que momento a empresa está?

| Sinal | Onde | O que muda |
| --- | --- | --- |
| Expansão, novas unidades, captação, aquisição feita | notícias dos últimos 12 meses, site, LinkedIn | ✅ vale desenhar a fase 2 já na proposta |
| Vagas abertas para atendimento, recepção, dados | páginas de vagas, LinkedIn | ✅ dor real e âncora de valor: o salário da vaga é o custo da alternativa |
| Demissões, fechamento de unidades, queda de receita | notícias | ⚠️ verba apertada: escopo menor agora (o resto na fase 2), entrada menor, parcelas curtas |
| Fusão ou aquisição em andamento, troca de diretoria | notícias, comunicado | ⚠️ sponsor pode trocar no meio do ciclo: confirme quem aprova |
| Recuperação judicial, falência, protestos relevantes | notícias, consulta de processos | 🔴 **gate 12** |

### 3. Quem decide, e sob que regras?

| Sinal | O que muda |
| --- | --- |
| Faz parte de grupo ou multinacional | a decisão pode subir para o grupo, e o grupo pode ter **política de IA ou de fornecedor** (ex.: só Copilot). 🔴 Se houver política que exclua o NI, é **gate 12** |
| Capital aberto, setor regulado (saúde, financeiro, educação pública) | ciclo de compra longo, revisão de segurança e LGPD, cadastro de fornecedor: pergunte os requisitos. Se existirem, entra o **pacote enterprise** do [`modelo.md`](modelo.md) |
| Empresa do dono (fundador, familiar) | o dono decide. Se ele não estava na reunião, o risco é de autoridade |

### 4. Qual é a melhor alternativa real do cliente?

É o que define o teto de valor ([`modelo.md`](modelo.md) § A camada de valor). Procure o que ele
**já usa** e o que ele **usaria** se não comprasse do NI.

| Produto | Onde olhar | Alternativas típicas |
| --- | --- | --- |
| **Maísa** | abra o site e o WhatsApp do cliente: já tem chatbot? Qual (Blip, Zenvia, Octadesk)? O sistema de gestão dele (de clínica, de salão, ERP) já tem IA nativa? A plataforma de rede social dele entrega o caso de uso de fábrica? | contratar atendente (R$ 3.500–6.000/mês carregado), SaaS de nicho (R$ 150–1.000/mês), plataforma mid-market (R$ 2.500–4.400/mês) |
| **Plum** | vagas que citam o stack ("experiência com TOTVS/Sankhya/SAP", "Power BI"); site do fornecedor do ERP (tem módulo de IA?); a empresa é Microsoft 365 (Copilot)? | analista de dados, relatório do próprio ERP, implementação de Power BI (R$ 8–120 mil), Copilot |
| **Ludi** | site da escola (app de comunicação que já usa: ClassApp, Agenda Edu, Sponte, Layers), sistema acadêmico | secretaria e coordenação respondendo à mão, app de comunicação por aluno (R$ 12–58/ano) |

🔴 **Se a plataforma que o cliente já usa entrega o núcleo do pedido de fábrica, é gate 12.**
Nesse caso o preço não resolve; a decisão é de produto.

### 5. Que sinais de valor dá para levar à reunião?

Hipóteses para **construir a conta de ganho com o cliente**, nunca para precificar sozinho:

| Produto | Sinais |
| --- | --- |
| **Maísa** | número de unidades × atendentes por unidade; salário de recepcionista ou atendente na região (vagas, pesquisas salariais); horário de atendimento (fora do horário = demanda perdida); volume de avaliações e reclamações públicas (Google, Reclame Aqui) como proxy de volume e de dor |
| **Plum** | número de colaboradores que dependem de relatório; salário de analista de dados ou de BI na região; quantos sistemas aparecem nas vagas |
| **Ludi** | matrículas (QEdu/INEP); mensalidade da escola (site, notícias), para dizer quanto o Ludi pesa por aluno; número de unidades e segmentos |

## O que a pesquisa muda no preço

| Achado | Efeito |
| --- | --- |
| porte ou volume confirmados | escolhe a faixa da tabela do produto (conversas, perguntas, alunos), **a confirmar com o cliente** |
| requisitos enterprise prováveis (grupo, S.A., regulado) | vira pergunta; se confirmados, **pacote enterprise** |
| empresa em expansão | desenhar a fase 2 (novas unidades, novos módulos) antes de fechar a fase 1 |
| verba apertada ou momento ruim | escopo menor agora, o resto na fase 2; negociar termo (entrada, parcelas), não preço |
| alternativa barata que resolve | a proposta tem de mostrar o diferencial em reais, ou é caso de plug-and-play ou de não vender |
| alerta crítico (🔴 acima) | **gate 12**: escale antes de apresentar |

## Como sai na resposta

```
EMPRESA       <razão social> · CNPJ <nº> · aberta em <ano> · <porte na Receita>
              <n> unidades em <cidades> (site oficial, 25/09/2026)
              <faixa> funcionários (LinkedIn, 25/09/2026) · operação atendida: <n> — A CONFIRMAR
MOMENTO       <expansão / estável / aperto>: <fato> (<fonte>, <data>)
DECISÃO       <grupo? multinacional? dono?> · política de TI conhecida: <sim/não/não achei>
ALTERNATIVA   <o que já usa ou usaria> · custo de referência <R$> (<fonte>)
SINAIS        <hipóteses de valor para validar na reunião>
ALERTAS       <nenhum | 🔴 o quê, fonte> 
NÃO ACHEI     <o que procurei e não encontrei>
```

**"Não achei" é obrigatório** quando for o caso. Pesquisa sem lacuna declarada parece mais sólida
do que é.
