---
type: "architecture"
title: "Static site and publishing"
description: "Trace the static assets, motion preferences and path-filtered GitHub Pages deployment."
tags: ["static-site","pages","accessibility"]
verified:
  - by: openwiki/0.7.2
    at: 2026-10-14T18:50:09.040Z
sources:
  - id: openwiki-source-6d8a2d3a27012fbaacf0c3d3
    resource: repo://.github/workflows/deploy-github-pages.yml
  - id: openwiki-source-869e380690467c4d9dec853b
    resource: repo://gitpage/index.html
  - id: openwiki-source-66815d2ee39c30230823e5ae
    resource: repo://gitpage/js/main.js
generated: { by: "codex", at: "2026-10-14T18:50:09.040Z" }
---

# Static site and publishing

## Asset flow

`gitpage/index.html` loads `css/main.css`, remote font CSS and `js/main.js`. Links route visitors back to the GitHub catalog ([document](../../gitpage/index.html#L10-L13), [script inclusion](../../gitpage/index.html#L449-L459)). This is a static landing page; the training applications live in their own upstream repositories.

The JavaScript reads `prefers-reduced-motion`, fills in the footer year, and provides mobile navigation, scroll reveal, parallax, tilt and canvas behavior. The canvas caps device-pixel ratio at 2 and uses zero nodes under reduced motion versus 72 otherwise ([motion preference](../../gitpage/js/main.js#L8-L16), [canvas limits](../../gitpage/js/main.js#L150-L157)). These implementation choices do not establish a full accessibility audit.

## Publication ownership

The versioned Pages workflow triggers on relevant `gitpage/**` or workflow-path changes pushed to `main`, or a manual dispatch. It uploads the `gitpage` directory and deploys that artifact to the GitHub Pages environment. Its token permissions include contents read, Pages write and ID-token write ([workflow](../../.github/workflows/deploy-github-pages.yml)). A configured workflow is separate from a completed deployment and from the account's Pages settings.

An OpenWiki-only change does not match the existing push path filter. Read the [site guide](../../gitpage/README.md) before changing publication settings. Return to [quickstart](../quickstart.md) for catalog usage.
