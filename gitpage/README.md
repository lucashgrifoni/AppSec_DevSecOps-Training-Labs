# GitHub Pages — AppSec & DevSecOps Training Labs

Premium static landing page for the [AppSec_DevSecOps-Training-Labs](https://github.com/lucashgrifoni/AppSec_DevSecOps-Training-Labs) repository. Everything in this folder is self-contained and can be published on GitHub Pages independently from the rest of the monorepo.

## Structure

| Path | Description |
|------|-------------|
| `index.html` | Single page with all sections (hero, about, capabilities, architecture, differentiators, showcase, pillars, roadmap, CTA, footer). |
| `css/main.css` | Color tokens, layout, glassmorphism, CSS animations, responsive rules, and `prefers-reduced-motion`. |
| `js/main.js` | Canvas (particles + lines), hero parallax, card tilt, scroll reveal, mobile menu, footer year. |
| `images/favicon.svg` | Favicon aligned with the project palette. |
| `assets/` | Reserved for additional static files (currently only `.gitkeep`). |

## Dependencies

- **No npm packages** — fully static for simple publishing.
- **Google Fonts** (remote): [Outfit](https://fonts.google.com/specimen/Outfit) and [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono), loaded from `fonts.googleapis.com` in `index.html`.

> Without network access, fonts fall back to the system stack (`system-ui`, `ui-monospace`).

## Local preview

1. Open `index.html` directly in the browser, **or**
2. Serve the folder over HTTP (recommended for relative paths and font loading):

```bash
# From the gitpage folder
npx --yes serve .
```

Or with Python:

```bash
cd gitpage
python -m http.server 8080
```

Then open `http://localhost:8080` (or the port shown).

## Publishing on GitHub Pages

### Recommended — GitHub Actions (this repository)

The root workflow `.github/workflows/deploy-github-pages.yml` deploys the **`gitpage/`** directory whenever relevant paths change on `main`. In **Settings → Pages**, set **Source** to **GitHub Actions**.

### Alternative — Deploy from a branch

GitHub’s classic UI usually offers only **`/(root)`** or **`/docs`**, not arbitrary subfolders. If you use this mode, copy the contents of `gitpage/` into `docs/` (or the repo root) and point Pages there.

### Dedicated site repository

Create an empty repo, push only the files from `gitpage/` to the branch root, and enable Pages on **`/(root)`**.

### Final URL

After deploy: `https://<user>.github.io/<repo>/` (or a custom domain if configured).

Relative links (`css/`, `js/`, `images/`) work as long as the published site root is the folder that contains `index.html`.

## Main files to edit

- **Copy and sections:** `index.html`
- **Global look (colors, typography, motion):** `css/main.css`
- **Interaction (canvas performance, parallax, tilt):** `js/main.js`

## Performance and accessibility

- Animations and the canvas are **reduced or disabled** when `prefers-reduced-motion: reduce` is set.
- The canvas caps at **72 nodes** and `devicePixelRatio` at **2** to balance sharpness and cost.
- The mobile menu uses `aria-expanded` and `aria-controls`.

## License

The HTML/CSS/JS here support project promotion; the main repository license applies to the catalog itself (MIT per the root README).
