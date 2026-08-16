# Olympus

I built Olympus as my avatar and Hermes integration build. I use AIRI as the presentation layer, while Hermes remains my authority for conversation, planning, counsel, and implementation handoffs.

This is my live build guide and implementation contract. I wrote it so another Apple Silicon operator can reproduce the architecture without receiving private credentials, machine paths, ports, prompts, or fleet state.

## The three avatars

| Avatar | Authority | Public role | Direct avatar capabilities |
|---|---|---|---|
| **Zeus** | Decision | Commander, primary operator, user-facing coordination | Conversation, planning, status read |
| **Odin** | Counsel | Independent architecture counsel and red-team review | Analysis, red-team, architecture review, status read |
| **Thor** | Implementation | Bounded build and verification lane | Implementation planning, code review, bounded build request, status read |

The manifests in [`avatars/`](avatars/) are the contract. They deliberately do not grant any avatar direct shell, filesystem, browser, hardware, or unrestricted network access.

## System boundary

```text
Apple Silicon microphone / text input
                ↓
        Local ASR adapter
                ↓
     Olympus conversation adapter
                ↓
  Hermes named profile / bounded authority lane
                ↓
        Local TTS adapter
                ↓
          AIRI avatar renderer
```

AIRI renders the avatar. It does not become the approval authority, scheduler, memory store, or tool router. Olympus adapters translate only the smallest required request and response fields.

## Repository contract

- [`avatar.schema.json`](avatar.schema.json) defines the public manifest shape.
- [`avatars/zeus.json`](avatars/zeus.json), [`avatars/odin.json`](avatars/odin.json), and [`avatars/thor.json`](avatars/thor.json) define the three lanes.
- [`apple-silicon.md`](apple-silicon.md) is the host setup and implementation sequence.
- [`adapter-contract.md`](adapter-contract.md) defines the narrow AIRI ↔ Hermes boundary.
- [`security.md`](security.md) is the lockdown checklist.
- [`acceptance.md`](acceptance.md) defines the gates for calling an avatar live.
- [`../scripts/validate_olympus.py`](../scripts/validate_olympus.py) validates manifests and scans the public tree.
- [`../command-center.html`](../command-center.html) preserves the prior public Command Center build record.

## Build order

1. Prepare an Apple Silicon workspace and verify native arm64 tooling.
2. Run AIRI independently before integrating Hermes.
3. Create three isolated Hermes authority lanes without cloning secrets or channels.
4. Add the loopback-only Olympus adapter with request allowlists and hard limits.
5. Add local ASR and TTS as separate services.
6. Bind each AIRI avatar to one manifest, one voice reference, and one Hermes profile reference.
7. Validate direct model lanes, then the adapter, then the AIRI renderer.
8. Run the security and acceptance checklists.
9. Publish only sanitized manifests and documentation.

## Ownership and attribution

Olympus is Outlaw Intelligence's build and integration layer. AIRI remains an upstream open-source project by [moeru-ai](https://github.com/moeru-ai/airi); respect its license and attribution when using the upstream code. This repository does not redistribute AIRI source, models, characters, or private runtime assets.

## Current status vocabulary

- **accepted** — the contract and required evidence passed.
- **live** — the accepted surface is running and the required end-to-end behavior was observed.
- **held** — intentionally not promoted because a dependency or acceptance gate is incomplete.
- **blocked** — a reproducible failure prevents the next gate.
- **unverified** — no claim is made because evidence has not been collected.

Never replace `held`, `blocked`, or `unverified` with `live` to make a dashboard look complete.
