# precificar-enterprise

Skill de precificação das versões **enterprise** dos produtos do Núcleo de Inovação da Poli Júnior —
as que passam por implementação e adaptação ao que o lead precisa. O plug-and-play tem preço de
tabela e não é orçado aqui.

Este repositório é **público e só de leitura**: qualquer um baixa, só o mantenedor altera. Ele
leva o necessário para usar e mexer na skill — o fluxo, o formulário e o modelo. A base de
propostas e as medições com dados de clientes ficam fora, de propósito.

## Como baixar

Vá em **[Releases](https://github.com/Allekka/precificar-enterprise/releases/latest)** e baixe o **`precificar-enterprise.zip`** da versão
mais nova. Não precisa de conta no GitHub.

## Como instalar no claude.ai

Quem vende usa o **claude.ai**, e é para lá que esta skill vai. São quatro passos, uma vez só:

1. Guarde o arquivo **`precificar-enterprise.zip`**. Não descompacte — o claude.ai quer o `.zip`,
   com a pasta `precificar-enterprise/` dentro dele.
2. Ligue o **code execution** — nas configurações, é a opção de **criar e editar arquivos**
   ("Create and edit files"). Sem ela o claude.ai não consegue abrir os arquivos da skill, e a
   skill não funciona.
3. Abra **Settings → Features → Skills** e clique em **Add / Upload skill**. Em algumas contas o
   caminho aparece como **Customize → Skills**; é a mesma tela.
4. Escolha o `.zip`. Se a skill aparecer na lista como `precificar-enterprise`, acabou.

Depois disso **não precisa chamar a skill pelo nome.** Jogue as anotações da reunião no chat e peça
o preço — a descrição dela já cobre "montar proposta", "orçar cliente" e "quanto custa".

Requer plano **Pro, Max, Team ou Enterprise**.

⚠️ **Cada pessoa sobe a sua própria cópia.** O claude.ai não distribui skill para o time inteiro, e
a cópia de cada um fica congelada na versão que subiu. Quando sair versão nova aqui nas Releases,
baixe e suba de novo — confira a versão no rodapé deste arquivo antes de confiar num número.

<details>
<summary>Se você usa Claude Code em vez do claude.ai</summary>

```bash
git clone https://github.com/Allekka/precificar-enterprise ~/.claude/skills/precificar-enterprise
```

Depois, `/precificar-enterprise`. A skill é a mesma: nada aqui depende de ferramenta que só exista
num dos dois lados.

</details>

## Os arquivos

| Arquivo | O que é | Quem lê |
| --- | --- | --- |
| [`SKILL.md`](SKILL.md) | o fluxo: aderência → rota → âncora → dimensionar → preço → gates → saída | o agente |
| [`formulario.md`](formulario.md) | o que o comercial joga, e o que fazer quando não souber um campo | **o comercial** |
| [`modelo.md`](modelo.md) | fonte da verdade dos números: produtos, ITIP, rateio, multiplicador, camadas do Plum, mensalidade, gates, desconto | o agente, e quem revisa o modelo |
| [`empacotar.py`](empacotar.py) | gera o `.zip` do claude.ai e confere o frontmatter e os links | quem mantém |

**Se você vende:** leia o [`formulario.md`](formulario.md) inteiro uma vez — são os campos que você
vai querer ter na cabeça na próxima reunião.

## Quer propor uma mudança?

O repositório não aceita alteração direta. Fale com o mantenedor, ou faça um *fork*, mude na sua
cópia e mande o que mudou e por quê.

**Para quem mantém:** edite os `.md`, rode `python empacotar.py`, faça commit e push, e publique o
zip como release nova:

```bash
gh release create vN dist/precificar-enterprise.zip --repo Allekka/precificar-enterprise
```

Atualize a versão no rodapé deste arquivo. **Nada com nome de cliente, valor de proposta, motivo de
perda ou dado interno entra aqui** — este repositório é público.

---

**Versão 5 · 25/09/2026.** O Passo 0 é triagem de facilidade (pronto / perto / novo), não portão de
catálogo; integração com API de terceiro custa 4 semanas-analista por sistema (PERT 2/4/6); tokens,
infra e APIs pagas são repasse ao cliente, fora do preço.
