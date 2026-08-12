# AIRI — Local-First Voice Companion Case Study

A public, sanitized engineering case study documenting how **Dylan Walls** integrated, customized, and hardened the open-source [AIRI](https://github.com/moeru-ai/airi) project into a responsive local voice-and-avatar experience.

**Live site:** [outlaw-intelligence.github.io/outlaw-audit](https://outlaw-intelligence.github.io/outlaw-audit/)

## Attribution

AIRI is an open-source project created by **moeru-ai**. Dylan did not create AIRI. This repository documents his surrounding integration and reliability work; it does not redistribute AIRI source code or assets.

## Engineering scope

- Recovered and verified the desktop workspace and application build.
- Hardened onboarding and provider-detection behavior.
- Connected streamed local conversation through LM Studio.
- Kept speech recognition, conversation, speech synthesis, and avatar playback as observable stages.
- Integrated persistent local Whisper transcription and local Qwen speech synthesis.
- Verified visible avatar speech and lip-sync state transitions.
- Added health, readiness, timeout, recovery, and graceful-degradation boundaries.

## Local development evidence

| Stage | Observed result |
|---|---:|
| Short transcription | ~0.25 s |
| First visible streamed chat content | ~0.27 s |
| Short synthesized audio response | ~0.40 s |

These are bounded observations from local development tests—not universal benchmarks. Results vary with hardware, model, input length, runtime state, and configuration.

## Public-safety boundary

This repository intentionally excludes credentials, private prompts, personal memory, machine paths, ports, service definitions, logs, provider secrets, internal routing, runtime state, and upstream AIRI source/assets.

## Contents

- [`index.html`](index.html) — self-contained GitHub Pages case study
- [`airi-case-study.md`](airi-case-study.md) — accessible technical narrative
- [`Dylan_Walls_Public_Resume-v2.pdf`](Dylan_Walls_Public_Resume-v2.pdf) — public résumé

## Public links

- [AIRI upstream project](https://github.com/moeru-ai/airi)
- [Dylan Walls on LinkedIn](https://www.linkedin.com/in/dylan-walls-6b634a3b6)
- [Outlaw Intelligence on GitHub](https://github.com/Outlaw-Intelligence)

---

This is a portfolio artifact, not a deployment guide. No private runtime configuration is published here.
