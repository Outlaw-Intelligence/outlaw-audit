# Outlaw Intelligence — Public Engineering Record

This repository publishes the sanitized public build record for Outlaw Intelligence systems work.

**Live public view:** https://outlaw-intelligence.github.io/outlaw-audit/

## Current artifact

The root GitHub Pages site is the **Outlaw Command Center public build record**. It presents the accepted plugin foundation, read-only operational models, evidence gates, and the exact runtime boundary that remains held.

The page is intentionally dependency-free and self-contained. Its small filter interaction is local-only; it does not connect to private hardware, gateways, credentials, or runtime services.

## What is documented

- Phase 1: supported plugin shell, route, navigation, and pane.
- Phase 2: accepted read-only profile, session, cron, and skill summaries.
- Runtime acceptance: backend and WindowServer evidence passed, while AX/CUA renderer acceptance remains blocked.
- Rollback and safety boundaries used to preserve the known-good live artifact.
- Public-safe architecture without secrets, private paths, ports, prompts, logs, or machine metadata.

## What is not claimed

The public page does **not** claim that the Hermes Desktop AX/CUA runtime issue is fixed or that the held Task 3.1 artifact has been promoted. The private product on Dylan's hardware is not changed by this repository update.

## Files

- [`index.html`](index.html) — public command-center build record and static interaction.
- [`outlaw-command-center-case-study.md`](outlaw-command-center-case-study.md) — accessible technical narrative.
- [`airi-case-study.md`](airi-case-study.md) — separate AIRI local-first voice companion case study.
- [`Dylan_Walls_Public_Resume-v2.pdf`](Dylan_Walls_Public_Resume-v2.pdf) — public résumé.

## Public-safety boundary

This repository excludes credentials, tokens, passwords, private prompts, personal memory, local machine paths, ports, service definitions, runtime logs, private fleet topology, and upstream AIRI source/assets.

## Attribution

The AIRI case study documents integration work around the open-source [AIRI project by moeru-ai](https://github.com/moeru-ai/airi). Dylan Walls did not create AIRI.

---

© 2026 Outlaw Intelligence · Dylan Walls
