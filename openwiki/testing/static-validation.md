---
type: testing
title: Static validation boundary
description: Understand the source defects checked by CI and the separate browser and deployment evidence.
tags: [ci, static-site, validation]
verified:
  - by: openwiki/0.7.2
    at: 2026-10-14T22:12:01.834Z
sources:
  - id: openwiki-source-f1d0b70c13530a7d6d0551c9
    resource: repo://.github/scripts/validate_site.py
  - id: openwiki-source-164e2da859b5277df81c7d94
    resource: repo://.github/workflows/ci.yml
  - id: openwiki-source-6d8a2d3a27012fbaacf0c3d3
    resource: repo://.github/workflows/deploy-github-pages.yml
generated: { by: "codex", at: "2026-10-14T22:06:38.476Z" }
---

# Static validation boundary

## Pull request checks

The [CI workflow](../../.github/workflows/ci.yml) runs for pull requests and pushes to main. Its two jobs use Ubuntu 24.04 and Windows runners, a read-only repository token and pinned actions. Node checks JavaScript syntax, then the Python validator checks site resources and documentation. These jobs do not publish the site or run the vulnerable applications listed in the catalog.

## Source and resource checks

The [site validator](../../.github/scripts/validate_site.py) requires the landing page, stylesheet, JavaScript file and SVG favicon. It checks the HTML5 doctype, document language, unique IDs and aria-controls references. Literal getElementById bindings must refer to an ID in the page. Local HTML links, CSS resource URLs and links in the repository, site and OpenWiki setup guides must resolve inside the repository. The favicon is parsed as XML. Missing resources or invalid references produce a failing exit code.

The script reads local files and skips external URLs. It does not check upstream availability, execute browser interactions, validate every dynamic selector or provide a full accessibility assessment. A JavaScript syntax check also does not establish runtime behavior.

## Publication is separate

The [Pages workflow](../../.github/workflows/deploy-github-pages.yml) responds to its own main-branch path filters or a manual dispatch. A successful static validation job does not establish that a Pages deployment occurred. Read [Static site and publishing](../architecture/static-site.md) for that publication path and return to [quickstart](../quickstart.md) for catalog usage.
