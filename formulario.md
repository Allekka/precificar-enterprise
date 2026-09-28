# Formulário de entrada

O que o comercial joga na skill antes da proposta. **Não é para preencher em ordem nem de uma vez**
— jogue o que tem: card do ValidaNI, texto corrido, transcrição, print de conversa. A skill lê,
pesquisa a empresa na internet, extrai o que consegue e mostra um **painel**: o que já sabe, o que
falta (em ordem do quanto mexe no preço) e a **faixa** em que o preço vai cair. Depois pergunta o que
falta, **uma coisa por vez**, e a faixa estreita a cada resposta.

⚠️ **A faixa do painel é só para você.** Não diga ao cliente: faixa dita antes de fechar o escopo vira
teto na cabeça dele.

## Os campos que mudam o preço

Sem eles não sai preço **fechado** — sai a faixa —, e a skill não deve inventá-los.

| Produto | Campo | Por que bloqueia |
| --- | --- | --- |
| **todos** | **O que o cliente pediu, item por item** | decide o produto, o nível da tabela e o que é item novo |
| **todos** | **Quais sistemas do cliente a solução consulta ou alimenta, pelo nome** | cada sistema é uma linha de preço e uma credencial com prazo próprio, que não é do NI |
| **Maísa** | **Conversas por mês**, **quantas unidades** (regra igual ou diferente) e, **para cada função** (agenda, cadastro, CRM, cobrança, fiscal), **sistema do cliente ou o nosso** | a decisão de sistema define o nível; o volume dá o adicional e o repasse |
| **Plum** | **Perguntas por mês** (estime com ele: quantas pessoas × quantas vezes por semana) e **quem pode ver o quê** | a franquia define a mensalidade; isolamento por pessoa é uma linha inteira e um gate |
| **Ludi** | **Alunos ativos** e **quais módulos** (Atendimento, Pedagógico) | a unidade de preço do Ludi é o aluno |

**Para o nível da Maísa, as quatro perguntas** ([`modelo.md`](modelo.md) § O nível): quantos sistemas
do cliente ela lê ou escreve · as unidades têm regras diferentes · há outro canal além do WhatsApp · ela
faz algo sozinha, com efeito fora da conversa, **sem uma pessoa da empresa aprovar antes** (cobrar,
campanha ativa, orçamento fechado)? Se a última resposta for "não, alguém da empresa recebe e decide",
é M1. A skill mostra o nível e o que o mudaria, e **o comercial confirma**.

### Quanto cada resposta mexe — para saber o que perguntar primeiro

Os números são os de [`modelo.md`](modelo.md), no **ano 1** (setup + 12 mensalidades), sem o repasse.

| Produto | Resposta | Mexe no ano 1 |
| --- | --- | --- |
| **Maísa** | nenhum sistema do cliente, nada sozinha, uma regra, só WhatsApp → **M1** | **R$ 27.200** (R$ 14.000 + R$ 1.100/mês) |
| | 1 ou 2 sistemas do cliente, **ou** 1 processo sozinha, **ou** regras diferentes por unidade → **M2** | **R$ 52.800** (+R$ 25.600) |
| | 3+ sistemas do cliente, **ou** outro canal, **ou** 2+ processos sozinha → **M3** | **R$ 93.400** (+R$ 40.600 sobre o M2) |
| | cada 1.000 conversas/mês acima de 3.000 | +R$ 3.000 |
| **Plum** | núcleo: 1 base própria, até 2.000 perguntas/mês, todo mundo vê tudo | **R$ 41.600** (R$ 20.000 + R$ 1.800/mês) |
| | cada sistema de terceiro (ERP, CRM…) lido por API | +R$ 14.800 (R$ 10.000 + R$ 400/mês) |
| | "cada um só vê o próprio dado" (isolamento) | +R$ 12.000 e o gate 8 |
| | plataforma web própria (SSO, perfis, painel) | +R$ 15.000 |
| | outra base própria do cliente | +R$ 4.000 |
| | de até 2.000 para até 6.000 perguntas/mês · de 6.000 para 15.000 | +R$ 14.400 · +R$ 21.600 |
| **Ludi** | escola até 600 alunos, só Atendimento (o piso manda) | **R$ 19.400** (R$ 5.000 + R$ 1.200/mês) |
| | cada 100 alunos acima de 600, no Atendimento | +R$ 2.400 |
| | módulo Pedagógico | +R$ 45 por aluno por ano |
| | cada sistema acadêmico integrado | +R$ 10.000 |
| **todos** | 2+ requisitos formais (SSO, questionário de LGPD, homologação, jurídico do cliente, cadastro de fornecedor) | +15% no setup |
| | item que ninguém da casa fez | +R$ 1.600 por semana-analista que o PM dimensionar |

Por isso, na Maísa, a primeira pergunta quase sempre é **"agenda, cadastro e CRM ficam no sistema do
cliente ou no da Maísa?"**: é a que separa R$ 27 mil de R$ 53 mil.

Sobre o primeiro campo: **concreto, não adjetivo.** "Quer algo mais personalizado" não é resposta.
"Quer que o lembrete saia 48 h antes em vez de 24 h" é. "Quer consultar quanto sobrou do orçamento
de viagem dele" é.

## As três perguntas que toda proposta faz

| Pergunta | Por quê | Se ele não souber |
| --- | --- | --- |
| **Quanto você ganha por ano com isto?** — horas, pessoas ou dinheiro, **com autor e data** | confere o preço contra o valor (captura de 10–20%) e abre o modo ROI-âncora | monte a conta **com** ele, com as hipóteses da pesquisa. Não soube: escreva "perguntado, cliente não soube" |
| **O que você faria se não contratasse o NI?** — contratar alguém, um SaaS, o relatório do ERP, nada | é o teto de valor real: a proposta tem de dizer em reais o que entrega além disso | a skill procura na pesquisa e escreve "alternativa inferida, a confirmar" |
| **Algum número já foi dito a ele?** — faixa de setup ou de mensalidade falada na reunião | faixa dita antes de dimensionar vira teto na cabeça do cliente | responda "nenhum" só se tiver certeza |

Conta pronta para usar com ele:

```
horas poupadas por mês × custo-hora carregado × 12 = ganho anual
custo-hora carregado = salário mensal × 1,8 ÷ 160
```

**Nunca estime o ganho por conta própria e use o seu número para subir o preço.**

---

## A · Quem é

| Campo | Se não souber |
| --- | --- |
| **Nome da empresa, e site ou CNPJ** | o mínimo para a pesquisa. Com o nome só, a skill tenta; homônimo é comum, então confirme |
| Setor de atuação | a pesquisa responde |
| Área e cargo de quem está pedindo | pergunte na próxima conversa |
| Produto candidato: Maísa · Plum · Ludi · não sei | "não sei" é resposta válida — a skill ajuda a decidir |

## B · O que ele pediu

| Campo | Se não souber |
| --- | --- |
| **Lista item por item** (muda o preço) | volte para o cliente. É o único campo sem substituto |
| Como ele resolve isso hoje — planilha, pessoa, sistema, ninguém | assuma "ninguém" e declare |
| **Sistemas a integrar, um por nome** (muda o preço) | pergunte o nome exato. "O ERP deles" não serve: ERP diferente é preço diferente |
| Ele topa mudar o processo, ou a solução tem que caber no processo atual | assuma que tem que caber, que é o caso caro |

⚠️ **Para cada sistema nomeado, a skill checa a família e o status de credencial** (§ Integrações em
[`modelo.md`](modelo.md)). Provedor-gestor e credencial de `parceria` mudam a proposta antes de
qualquer conta, e costumam pedir uma **fase 0 paga**.

## C · Tamanho

| Campo | Se não souber |
| --- | --- |
| **A unidade do produto** (muda o preço): conversas/mês, perguntas/mês, alunos ativos | estime **com ele** na reunião. A pesquisa ajuda (unidades, matrículas no Censo Escolar), mas entra "a confirmar" |
| Quantas pessoas vão operar a solução | estime pela operação e declare |
| Tamanho da operação atendida, em pessoas | a pesquisa dá o da empresa; a operação atendida costuma ser menor — pergunte |

⚠️ **Porte é da operação que vai usar, não do grupo econômico.** E faturamento não vira
multiplicador: porte entra pela unidade do produto e pelos requisitos enterprise.

## D · Requisitos enterprise

Dois ou mais destes = **pacote enterprise** (+15% no setup). A pesquisa diz quando perguntar: grupo,
S.A., multinacional, setor regulado.

| Requisito | Se não souber |
| --- | --- |
| SSO corporativo | assuma não |
| Questionário de segurança ou de LGPD | pergunte se é empresa grande ou regulada |
| Homologação em ambiente do cliente, ou aprovação em comitê | pergunte |
| Contrato pelo jurídico do cliente, com cláusulas próprias | pergunte |
| Cadastro de fornecedor com exigência documental | pergunte |

## E · Restrições

| Campo | Se não souber |
| --- | --- |
| Prazo pedido, e **por quê** — evento, auditoria, safra, ano letivo | assuma sem prazo apertado |
| Exige SLA com multa? | assuma não; se sim, é gate |
| Exige repositório ou dado segregado? Isolamento por pessoa? | assuma não; se sim, muda o preço |
| Contrato de quanto tempo | assuma 12 meses |
| **Em nome de quem ficam as contas** de LLM, nuvem e WhatsApp | assuma no nome do cliente — é repasse. Se ele preferir consumo incluso, a conta fica com o NI e isso vai escrito |
| Orçamento que ele deixou escapar | deixe em branco — **nunca** ancore a proposta nele |
| **Quem aprova, e se estava na reunião** | pergunte. É a causa de perda mais comum da casa |
| **Se existe verba nesta janela, ou só no próximo ciclo** | pergunte |
| **Equipe e semanas para itens novos** — do validador técnico ou do PM | pergunte ao comercial. Sem isso, o item novo e o piso ficam sem número, declarados |

## F · O que você não sabe

Liste. Sem enfeite.

Esta seção é a mais importante do formulário e a que costuma vir vazia. Lacuna declarada entra na
proposta como premissa e protege o time; lacuna esquecida vira retrabalho não faturado no mês três.

---

## O que a skill devolve

Enquanto falta resposta: o **painel** (o que já sei · o que falta, com quanto mexe · o que impede
apresentar · a faixa agora · a próxima pergunta). Quando tudo o que muda o preço estiver respondido,
ou quando você pedir o número (sai marcado PROVISÓRIO):

0. **Resumo** — o preço em uma linha, se dá para apresentar e o que confirmar antes
1. **Qualificação** — e, se duas das três perguntas acenderem, QUALIFICAÇÃO FRACA no topo
2. **Empresa** — o que a pesquisa achou, com fonte e data, e o que não achou
3. **Aderência** — produto, e o pedido em pronto / perto / novo
4. **Nível** da tabela e a unidade
5. **O preço** — setup, mensalidade e ano 1 —, com cada linha da conta do produto, e a fase 2 se houver
6. **Repasse estimado**, e a opção de consumo incluso quando houver custo medido
7. **Conferências** — valor, alternativa, piso, recorrência — com as contas
8. **Gates disparados** e o que fazer com cada um
9. **O que assumi** — as premissas que entram na proposta
10. **A linha do `registro.csv`** pronta para colar

## O que a skill NÃO faz

- Não escreve a proposta. Devolve os números e as premissas; o texto e o Canva são seus.
- Não decide desconto. Aponta a tabela e a política; a concessão é do comercial.
- Não substitui o mapeamento técnico. Item que ninguém sabe se dá para fazer sai como lacuna
  declarada, não resolvido.
- Não faz due diligence. A pesquisa é de dez minutos, para embasar preço e qualificação.

## Glossário — o que as palavras da saída querem dizer

| Palavra | Quer dizer |
| --- | --- |
| **setup** | o que o cliente paga pela implantação, uma vez |
| **mensalidade** | o que ele paga por mês ao NI: sustentação, 6 h de evolução, suporte, relatório. Não inclui o repasse |
| **ano 1** | setup + 12 mensalidades. É o número que se compara com o ganho do cliente |
| **repasse** | tokens de IA, servidor, WhatsApp da Meta, APIs pagas. O cliente paga direto aos fornecedores, fora do ano 1; a proposta traz uma estimativa |
| **faixa** | o menor e o maior preço possíveis com o que ainda falta responder. Interna |
| **provável** | o preço se o que falta vier como o material sugere, ou o de baixo quando não há pista |
| **M1 · M2 · M3** | os níveis da Maísa: conversa e entrega a uma pessoa · lê ou escreve no sistema do cliente, ou age sozinha · várias integrações, canais ou processos |
| **sistema do cliente** | um sistema que já é dele (ERP, CRM, gestão da clínica) e que a solução lê ou alimenta. Agenda do Google e o cadastro da própria Maísa não contam |
| **semana-analista (sw)** | uma pessoa do time por uma semana de calendário. É como o PM dimensiona item novo |
| **item novo** | algo que ninguém da casa fez. Entra à parte, a R$ 1.600 por semana-analista |
| **item condicionado** | entra na proposta com a condição e o preço ao lado ("se o ERP tiver API: +R$ 14.800") |
| **gate** | alerta que pede alguém do núcleo olhar antes de apresentar. São 13, em [`modelo.md`](modelo.md) |
| **captura** | ano 1 ÷ ganho anual declarado pelo cliente. Alvo de 10% a 20% |
| **fase 2** | o que não coube agora, já com escopo e preço escritos |
| **pacote enterprise** | +15% no setup quando o cliente tem 2+ requisitos formais de empresa grande |
