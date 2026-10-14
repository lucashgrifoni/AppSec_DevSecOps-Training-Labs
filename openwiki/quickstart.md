---
type: "quickstart"
title: "Training labs catalog"
description: "Choose a training topic and understand the boundary between this catalog and upstream vulnerable applications."
tags: ["training","catalog","static-site"]
verified:
  - by: openwiki/0.7.2
    at: 2026-10-14T18:50:09.040Z
sources:
  - id: openwiki-source-3535f3a252249f9a8668b40b
    resource: repo://gitpage/README.md
  - id: openwiki-source-23775c3de52f3ab95a13cb8b
    resource: repo://README.md
generated: { by: "codex", at: "2026-10-14T18:50:09.040Z" }
---

# Training labs catalog

## Catalog boundary

This repository indexes deliberately vulnerable applications and security-training resources. The catalog routes readers by category and training-focus tags, then directs them to each upstream project for installation and usage. It requires isolated, controlled environments rather than production deployment ([catalog instructions](../README.md)). The index does not install those applications or grant permission to test a third-party target.

## Choose a route

Use the README's category and training-path sections to select material, then follow the selected project's own documentation. Avoid treating catalog descriptions as current upstream compatibility or vulnerability receipts.

For the landing page's implementation and publication path, read [Static site and publishing](architecture/static-site.md). For source-linked documentation maintenance, read [OpenWiki setup](../docs/openwiki.md).

## Local preview

The `gitpage` guide describes opening its HTML file or serving that folder locally. HTML, CSS and JavaScript are self-contained files; Google Fonts is a separate network dependency with a system-font fallback ([site guide](../gitpage/README.md)). No application scanner is run by previewing the catalog.
