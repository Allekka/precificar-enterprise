# Ligar o ValidaNI no claude.ai

Com o ValidaNI ligado, a skill lê o card sozinha: o que falta para a proposta, os requisitos
aprovados, a ata, o chat do time e o dimensionamento. Sem ele a skill funciona igual, mas você cola o
material.

## Está ligado?

Numa conversa, clique em **+** → **Conectores**: o ValidaNI aparece na lista, ligado? A skill também
avisa na primeira resposta — `ValidaNI: ✅ conectado` ou `⚠️ não conectado nesta conversa`.

## Por que no Claude Code funciona e no claude.ai não

O claude.ai só aceita conector que faz **login** (OAuth) ou que não pede nada. O ValidaNI pede um
**token fixo** — o `vni_…` que vai no Claude Code —, e a tela de conector do claude.ai, na maioria
das contas, não tem onde pôr token. Por isso adicionar o endereço do ValidaNI como conector
personalizado dá erro de autorização.

## Os caminhos, do que funciona hoje ao definitivo

| Caminho | Onde funciona | De quem é o token | Quem faz |
| --- | --- | --- | --- |
| **1. App do Claude no computador + extensão do ValidaNI** | Claude Desktop, com a mesma conta e as mesmas skills do claude.ai | o seu | você, em 2 minutos |
| **2. Conector da organização com o token no cabeçalho** | web, desktop e celular | um só para a organização inteira | o Owner da organização no claude.ai, se a organização tiver o recurso |
| **3. Login do ValidaNI pelo claude.ai** | web, desktop e celular | o seu, pelo login | quem mantém o ValidaNI (muda o servidor) |
| **4. Colar o material** | qualquer lugar | — | você |

### 1 · App do Claude + extensão do ValidaNI — funciona hoje

1. Instale o app do Claude no computador (<https://claude.ai/download>) e entre com a **mesma conta**
   do claude.ai. A skill que você já subiu aparece lá.
2. Peça ao núcleo o arquivo **`validani.mcpb`** e o seu token do ValidaNI, se ainda não tiver.
3. No app: **Settings → Extensions**, arraste o `validani.mcpb` para a janela e clique em **Install**.
4. Cole o token quando o app pedir. Ele fica guardado no app, mascarado; não precisa colar de novo.
5. Numa conversa nova: **+ → Conectores**, ValidaNI ligado. Teste com *"liste os cards do ValidaNI"*.

⚠️ A extensão roda no seu computador: no navegador ela não aparece. Se o ValidaNI demorar a
responder na primeira chamada do dia, é o servidor acordando — a extensão espera até dois minutos.

### 2 · Conector da organização com o token no cabeçalho — só para o Owner

Em **Organization settings → Connectors → Add → Custom → Web**: o endereço do ValidaNI (peça a quem o
mantém), **Authentication: No sign-in** e, em **Request headers**, `authorization` com o valor
`Bearer vni_…` (com a palavra `Bearer` e o espaço). Depois cada pessoa liga o conector em
**Customize → Connectors**.

⚠️ **Se a seção Request headers não aparecer, a organização não tem o recurso** (está em beta, para
poucas organizações). E **todo mundo usa o mesmo token**: para o ValidaNI, tudo o que alguém fizer pelo
claude.ai parece feito pelo dono do token, inclusive as escritas (publicar próximos passos, criar
tarefas). Use um token criado só para isso.

### 3 · Login pelo claude.ai — o definitivo

Quando o ValidaNI aceitar login pelo claude.ai, basta **Customize → Connectors → Add custom connector**
com o endereço, clicar em **Connect** e entrar com a sua conta do ValidaNI. Funciona na web, no app e
no celular, cada um com o próprio acesso. Depende de uma mudança no servidor do ValidaNI; quem o mantém
sabe o que falta.

### 4 · Colar o material — sempre funciona

Abra o card no ValidaNI e cole na conversa, nesta ordem de importância:

1. os **requisitos**, separados em aprovados, condicionados, negados e em validação;
2. a **ata do mapeamento** e o **resumo da reunião**;
3. o **chat do card** — a ressalva que nunca virou requisito mora ali;
4. o **dimensionamento** do validador técnico, se houver;
5. o valor já falado ao cliente e a etapa do negócio, se souber.

A skill diz na saída que leu o que você colou, e não o card.

## No Claude Code

```bash
claude mcp add --transport http validani <endereço do ValidaNI> --header "Authorization: Bearer vni_…"
```
