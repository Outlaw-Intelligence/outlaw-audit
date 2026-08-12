# AIRI: Engineering a Local-First Voice Companion

## Project attribution

[AIRI](https://github.com/moeru-ai/airi) is an open-source AI companion project created by **moeru-ai**. Dylan Walls did not create AIRI. He used the upstream project as the interface foundation, then engineered and verified a private local integration around its desktop avatar experience.

This repository is a sanitized case study. It contains no AIRI source code or assets and no private runtime configuration.

## The engineering problem

A convincing companion is not a single model behind a character. It is a latency-sensitive system in which speech recognition, response generation, synthesis, playback, avatar state, and recovery must remain synchronized and understandable.

The target experience had four requirements:

1. Keep the core conversation path local.
2. Make the avatar visibly reflect listening, processing, speaking, and recovery states.
3. Reduce avoidable startup and per-turn latency.
4. Fail visibly and recover by component rather than silently switching authority.

## What Dylan engineered

### Desktop build recovery

Dylan recovered the application workspace, verified the relevant packages, rebuilt the desktop experience, and validated the installed application rather than treating a successful compile as acceptance.

### Onboarding hardening

The setup experience could reopen even when an appropriate local provider was already configured. Provider detection and persisted-state behavior were hardened so a valid local setup remained usable without an unnecessary onboarding loop.

### Fast local conversation

The conversation lane was connected to a local model endpoint with streamed output and bounded replies suitable for spoken interaction. The interface could begin presenting useful text before the complete response had finished generating.

### Persistent local speech recognition

Speech recognition was kept resident rather than paying model startup cost on every turn. That changed transcription from an isolated command into a responsive service stage with its own readiness boundary.

### Local speech synthesis and avatar behavior

Local speech synthesis was connected to playback and the avatar's speaking behavior. Acceptance included observing a real transition into visible speech/lip-sync motion and a return toward idle—not merely receiving a successful audio response.

### Reliability boundaries

Each stage was treated as independently observable: startup, health, request, timeout, response, playback, and recovery. A voice-component problem should not silently redefine the conversation provider or turn a local system into an unapproved cloud path.

## Sanitized architecture

```text
Voice input
   ↓
Local speech recognition
   ↓
Streamed local conversation
   ↓
Local speech synthesis
   ↓
Audio playback + avatar lip-sync

Each arrow crosses an explicit readiness and failure boundary.
```

The production implementation uses private loopback-only services. Their ports, paths, service definitions, credentials, prompts, and routing details are intentionally excluded.

## Observed development results

| Stage | Local observation |
|---|---:|
| Short transcription | approximately 0.25 seconds |
| First visible streamed chat content | approximately 0.27 seconds |
| Short synthesized audio response | approximately 0.40 seconds |

These are bounded observations from specific local smoke tests, not product guarantees or universal benchmarks. Model selection, hardware, input length, cache state, and runtime load affect performance.

## Verification philosophy

The work was accepted through real behavior rather than configuration claims:

- The relevant application packages typechecked and built.
- The desktop application launched into its intended avatar surface.
- A real typed conversation produced assistant text.
- Local speech synthesis returned playable audio.
- The avatar visibly changed mouth, face, and body state during speech.
- Onboarding remained suppressed when a valid local provider was already present.
- Temporary diagnostic access was removed after verification.

Exact private commands and machine artifacts are omitted from this public version.

## Privacy and safety boundary

This public repository excludes:

- API keys, tokens, passwords, and provider credentials
- Personal memory, prompts, transcripts, or private conversation data
- Local filesystem paths, ports, service labels, and launch configuration
- Internal orchestration details and operational control surfaces
- Runtime logs, backups, screenshots containing private state, and machine metadata
- Upstream AIRI code, models, characters, artwork, or other project assets

The public claim is deliberately narrow: the tested core conversation loop was configured to run locally. Optional AIRI capabilities and unrelated tooling are outside this case study.

## Engineering lessons

1. **Local does not mean simple.** Private systems still need timeouts, readiness checks, bounded retries, and truthful degraded states.
2. **Voice is a pipeline.** Recognition, generation, synthesis, playback, and animation need separate contracts.
3. **The interface is operational feedback.** Listening, thinking, speaking, unavailable, and recovering states should tell the truth.
4. **Latency is cumulative.** Persistent services and streaming improve the experience more than optimizing a single benchmark in isolation.
5. **A green build is not acceptance.** Real audio, visible state transitions, and recovery behavior must be exercised.
6. **Public documentation needs its own threat model.** Architecture can be demonstrated without publishing credentials, private endpoints, or machine-specific internals.

## Links

- [AIRI by moeru-ai](https://github.com/moeru-ai/airi)
- [Dylan Walls — public résumé](Dylan_Walls_Public_Resume-v2.pdf)
- [Dylan Walls on LinkedIn](https://www.linkedin.com/in/dylan-walls-6b634a3b6)
- [Outlaw Intelligence on GitHub](https://github.com/Outlaw-Intelligence)
