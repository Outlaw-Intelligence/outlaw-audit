# Olympus — Outlaw Intelligence

I built Olympus as my live avatar and Hermes integration layer rendered through AIRI.

**My public build:** https://outlaw-intelligence.github.io/outlaw-audit/

## My build

- **Zeus** — my commander and primary operator; decision and planning lane.
- **Odin** — my independent counsel and red-team reviewer; analysis and architecture lane.
- **Thor** — my bounded implementation and verification lane; build requests stay scoped and approval-gated.

I use AIRI as the presentation layer and Hermes as the authority. I keep ASR, conversation, and TTS as separate local lanes instead of fusing voice into one fragile process.

## My Apple Silicon guide

Start here:

- [`olympus/README.md`](olympus/README.md) — my project contract, roles, boundaries, and build order.
- [`olympus/apple-silicon.md`](olympus/apple-silicon.md) — my arm64 host preflight, AIRI setup, isolated Hermes lanes, local voice, and validation.
- [`olympus/adapter-contract.md`](olympus/adapter-contract.md) — my narrow AIRI ↔ Hermes boundary and failure behavior.
- [`olympus/security.md`](olympus/security.md) — my repository, renderer, profile, network, model, audio, and release lockdown.
- [`olympus/acceptance.md`](olympus/acceptance.md) — my evidence gates before I call an avatar lane live.
- [`olympus/avatar.schema.json`](olympus/avatar.schema.json) — my manifest contract.
- [`olympus/avatars/`](olympus/avatars/) — my sanitized Zeus and Odin manifests, untouched Thor source PNG, and transparent-corner `thor-2d.png` static avatar export.
- [`olympus/architecture.mmd`](olympus/architecture.mmd) — my system flow diagram.

I validate the public contract locally:

```bash
python3 scripts/validate_olympus.py
```

Expected output includes:

```text
OLYMPUS_VALIDATION_OK avatars=3
POLICY_OK direct_shell=false direct_filesystem=false direct_browser=false direct_hardware=false approval=true
```

## My public safety boundary

I keep this repository free of credentials, tokens, cookies, private prompts, personal memory, raw transcripts, audio, machine paths, private ports, service logs, and private runtime assets. I keep private avatar files, voices, and environment values outside the repository and reference them through owner-only environment variables.

I preserve my original Thor source at `olympus/avatars/thor.png`. My static 2D export is `olympus/avatars/thor-2d.png`: I preserve the artwork and dimensions while making the outside corners transparent for clean avatar placement. This is a static 2D portrait, not a rigged Live2D model.

I intentionally deny direct shell, filesystem, browser, hardware, and unrestricted network access to the avatar adapter. I keep handoffs structured and human-approved.

## Upstream attribution

Olympus is my build and integration layer around [Project AIRI by moeru-ai](https://github.com/moeru-ai/airi). I keep AIRI’s license and attribution visible, and I do not redistribute upstream source, models, characters, or private assets.

© 2026 Outlaw Intelligence
