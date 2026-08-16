# Olympus — Outlaw Intelligence

Olympus is Outlaw Intelligence's owned live build and integration layer for Hermes avatars rendered through AIRI.

**Public build:** https://outlaw-intelligence.github.io/outlaw-audit/

## The build

- **Zeus** — commander and primary operator; decision and planning lane.
- **Odin** — independent counsel and red-team reviewer; analysis and architecture lane.
- **Thor** — bounded implementation and verification lane; build requests stay scoped and approval-gated.

AIRI is the presentation layer. Hermes remains the authority. Voice is split into local ASR, conversation, and TTS lanes instead of being fused into a fragile all-in-one process.

## Follow the Apple Silicon guide

Start here:

- [`olympus/README.md`](olympus/README.md) — project contract, ownership, roles, and build order.
- [`olympus/apple-silicon.md`](olympus/apple-silicon.md) — arm64 host preflight, AIRI setup, isolated Hermes lanes, local voice, and validation.
- [`olympus/adapter-contract.md`](olympus/adapter-contract.md) — narrow AIRI ↔ Hermes boundary and failure behavior.
- [`olympus/security.md`](olympus/security.md) — repository, renderer, profile, network, model, audio, and release lockdown.
- [`olympus/acceptance.md`](olympus/acceptance.md) — evidence gates before an avatar lane can be called live.
- [`olympus/avatar.schema.json`](olympus/avatar.schema.json) — manifest contract.
- [`olympus/avatars/`](olympus/avatars/) — sanitized Zeus and Odin manifests plus the user-provided Thor PNG preserved byte-for-byte.
- [`olympus/architecture.mmd`](olympus/architecture.mmd) — system flow diagram.

Validate the public contract locally:

```bash
python3 scripts/validate_olympus.py
```

Expected output includes:

```text
OLYMPUS_VALIDATION_OK avatars=3
POLICY_OK direct_shell=false direct_filesystem=false direct_browser=false direct_hardware=false approval=true
```

## Public safety boundary

This repository contains no credentials, tokens, cookies, private prompts, personal memory, raw transcripts, audio, machine paths, private ports, service logs, or private runtime assets. Private avatar files, voices, and environment values belong outside the repository and are referenced through owner-only environment variables.

The manifests intentionally deny direct shell, filesystem, browser, hardware, and unrestricted network access to the avatar adapter. Handoffs remain structured and require human approval.

## Upstream attribution

Olympus is our build and integration layer around [Project AIRI by moeru-ai](https://github.com/moeru-ai/airi). AIRI remains upstream open-source software; respect its license and attribution. This repository does not redistribute AIRI source, models, characters, or private assets.

## Preserved build record

[`command-center.html`](command-center.html) preserves the prior public Command Center build record. [`airi-case-study.md`](airi-case-study.md) remains as historical attribution and integration context; Olympus is the current project and public build.

© 2026 Outlaw Intelligence · Dylan Walls
