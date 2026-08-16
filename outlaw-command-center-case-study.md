# Outlaw Command Center — Public Engineering Case Study

## What this is

This repository is the public, sanitized build record for an Outlaw Intelligence command-center plugin built against the supported Hermes Desktop plugin surface.

The goal was not to create a second control plane. The goal was to add a small operational view inside the existing host: truthful read-only summaries, clear route/navigation behavior, and an acceptance process that could stop safely when the host runtime was not ready.

## Delivered work

### Phase 1 — Native plugin foundation

- Registered a supported plugin route.
- Added native navigation and a command-center pane.
- Kept the surface inside the Hermes host rather than forking or replacing the host.
- Accepted the shell, route, navigation, and pane as separate surfaces.

### Phase 2 — Read-only operational models

Four sanitized read models were accepted:

- profile summary;
- active-profile and recent-session presence;
- cron routine summary;
- canonical per-profile skill counts.

The public artifact does not reproduce private gateway URLs, ports, credentials, prompts, filesystem paths, logs, or machine state.

### Runtime acceptance — deliberately held

Task 3.1 adds a truthful readiness strip, but it was not promoted because the packaged Hermes Desktop runtime failed the native-window acceptance gate.

Observed facts:

- backend readiness passed;
- a real WindowServer surface with nonzero bounds existed;
- macOS Accessibility was trusted;
- CUA exposed `0×0`, no title, and no interactable elements;
- the AX application reported an application-root element instead of an `AXWindow` and exposed no renderer web-content subtree.

That is a host runtime boundary, not evidence that the plugin itself is broken. The known-good prior live artifact remains the rollback point.

## Sanitized architecture

```text
Supported Hermes plugin SDK
          ↓
Existing Hermes Desktop host
          ↓
Gateway-backed read-only models
          ↓
Command-center route / pane / status view
          ↓
This public build record
```

The host remains the authority. The plugin does not publish credentials, create a second approval authority, silently change provider routing, or invent live telemetry when a source is unavailable.

## Acceptance philosophy

A build is not accepted because it compiles or because a backend answers a health request. Acceptance requires the surface that a user or automation layer actually needs:

- static contract checks;
- supported host/API usage;
- route and pane lifecycle;
- real renderer/window observability;
- independent review before promotion;
- a preserved rollback artifact;
- a clear unavailable state when a dependency is not usable.

The runtime repair experiments were reverted when they did not change the AX result. This public page documents the boundary instead of presenting an unverified success state.

## Public-safety boundary

This repository intentionally excludes:

- credentials, tokens, passwords, and provider secrets;
- personal memory, private prompts, transcripts, and conversations;
- local filesystem paths, ports, service names, and launch configuration;
- runtime logs, backups, screenshots containing private state, and machine metadata;
- private fleet topology or internal routing details.

The public artifact is a portfolio and engineering record. It is not a deployment guide and it does not claim that the private Hermes Desktop runtime is currently accepted.

## Related case study

The earlier [AIRI local-first voice companion case study](airi-case-study.md) remains available as a separate portfolio artifact. AIRI is an open-source project created by [moeru-ai](https://github.com/moeru-ai/airi); Dylan Walls did not create AIRI.

## Links

- [Outlaw Command Center public view](https://outlaw-intelligence.github.io/outlaw-audit/)
- [Outlaw Intelligence on GitHub](https://github.com/Outlaw-Intelligence)
- [Dylan Walls — public résumé](Dylan_Walls_Public_Resume-v2.pdf)
- [Dylan Walls on LinkedIn](https://www.linkedin.com/in/dylan-walls-6b634a3b6)
