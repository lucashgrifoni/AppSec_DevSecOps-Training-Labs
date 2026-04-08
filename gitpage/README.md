# GitHub Pages — AppSec & DevSecOps Training Labs

Landing page premium (estática) dedicada ao repositório [AppSec_DevSecOps-Training-Labs](https://github.com/lucashgrifoni/AppSec_DevSecOps-Training-Labs). Todo o conteúdo desta pasta é independente do restante do monorepo e pode ser publicado isoladamente no GitHub Pages.

## Estrutura

| Caminho | Descrição |
|--------|-----------|
| `index.html` | Página única com todas as seções (hero, sobre, capacidades, arquitetura, diferenciais, showcase, pilares, roadmap, CTA, footer). |
| `css/main.css` | Tokens de cor, layout, glassmorphism, animações CSS, responsividade e `prefers-reduced-motion`. |
| `js/main.js` | Canvas (partículas + linhas), parallax no hero, tilt em cards, scroll reveal, menu mobile, ano no footer. |
| `images/favicon.svg` | Favicon inline-friendly (paleta do projeto). |
| `assets/` | Pasta reservada para futuros arquivos estáticos adicionais (vazia, com `.gitkeep`). |

## Dependências

- **Nenhum pacote npm** — site 100% estático para publicação trivial.
- **Google Fonts** (remoto): [Outfit](https://fonts.google.com/specimen/Outfit) e [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono), carregados via `fonts.googleapis.com` em `index.html`.

> Em ambientes sem internet, as fontes caem no stack do sistema (`system-ui`, `ui-monospace`).

## Como abrir localmente

1. Abra o arquivo `index.html` diretamente no navegador **ou**
2. Sirva a pasta com um servidor HTTP simples (recomendado para testar caminhos relativos e CORS de fontes):

```bash
# Na pasta gitpage
npx --yes serve .
```

Ou com Python:

```bash
cd gitpage
python -m http.server 8080
```

Acesse `http://localhost:8080` (ou a porta indicada).

## Como publicar no GitHub Pages

### Opção A — Publicar só a pasta `/gitpage` (recomendado para manter o repo principal intacto)

1. No GitHub: **Settings → Pages**.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Selecione a branch (ex.: `main`) e a pasta raiz do site:
   - **Folder:** `/gitpage` (GitHub usa o nome exato da pasta no dropdown “/ (root)” vs “/docs” vs subpasta — se a UI só oferecer `/` ou `/docs`, vá para a Opção B).

> Se a interface do repositório **não** listar subpastas arbitrárias como fonte (apenas `/` ou `/docs`), use a Opção B ou um workflow de deploy.

### Opção B — Copiar conteúdo de `gitpage/` para `docs/` na branch `main`

1. Copie todo o conteúdo **de dentro** de `gitpage/` para uma pasta `docs/` na raiz do repositório (sem alterar este tutorial fora do fluxo que você preferir no Git).
2. Em **Settings → Pages**, defina **Source** como branch `main` e folder **`/docs`**.

### Opção C — Repositório dedicado só para o site

1. Crie um repositório vazio (ex.: `AppSec-Training-Labs-site`).
2. Envie apenas os arquivos desta pasta `gitpage` para a raiz desse repositório.
3. Ative GitHub Pages com branch `main` e folder **`/ (root)`**.

### URL final

Após o deploy: `https://<user>.github.io/<repo>/` (ou domínio customizado, se configurado).

Se a página estiver numa subpasta (`/gitpage`), os links relativos (`css/`, `js/`, `images/`) continuam corretos desde que a URL base seja a pasta publicada.

## Arquivos principais para edição

- **Conteúdo e seções:** `index.html`
- **Visual global (cores, tipografia, animações):** `css/main.css`
- **Interação (performance do canvas, parallax, tilt):** `js/main.js`

## Observações de performance e acessibilidade

- Animações e canvas são **reduzidos ou desligados** quando `prefers-reduced-motion: reduce` está ativo.
- O canvas usa no máximo **72 nós** e `devicePixelRatio` capado em **2** para equilibrar nitidez e custo.
- Menu mobile usa `aria-expanded` e `aria-controls`.

## Licença do site

O HTML/CSS/JS desta pasta segue o propósito de divulgação do projeto; o repositório principal permanece sob a licença indicada no root (MIT, conforme README do catálogo).
