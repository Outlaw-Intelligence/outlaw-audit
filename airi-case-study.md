# AIRI Local Companion — Public Case Study

## What it is

AIRI is a local-first companion interface experiment built around a responsive character surface, local model connectivity, and a voice interaction loop. The project explores how an AI system can feel present and useful without requiring a cloud-only architecture.

This repository contains a **sanitized case study**, not the AIRI upstream source tree or Dylan's private runtime configuration.

## What I built around it

- A desktop-oriented companion experience with a stateful character interface.
- Local model connectivity for conversational responses.
- Voice input and speech output as separate, observable stages.
- Explicit boundaries between UI state, model requests, audio services, and recovery behavior.
- Bounded local services so a failed voice or model component does not silently redefine the rest of the system.
- Operational checks for startup, readiness, and graceful degradation.

## Architecture, at a public level

```text
User input
   ↓
Companion UI / character state
   ↓
Conversation adapter
   ↓
Local model endpoint
   ↓
Response state + speech queue
   ↓
Audio output and visible UI feedback
```

The important design choice is separation: the visual companion, model transport, speech pipeline, and observability surface can be tested independently. That makes the system easier to debug and safer to operate than one opaque process.

## Engineering lessons

1. **Local does not automatically mean simple.** A private runtime still needs health checks, timeouts, bounded retries, and clear failure states.
2. **Voice is a pipeline, not a feature flag.** Input capture, transcription, response generation, synthesis, playback, and UI state each need their own contract.
3. **The interface is part of the system.** A character surface should communicate listening, thinking, speaking, unavailable, and recovering states honestly.
4. **Keep public artifacts intentional.** The public portfolio shows the architecture and product decisions; private integrations, prompts, credentials, logs, machine paths, and runtime state stay out of the repository.

## Public boundary

Excluded from this repository:

- API keys, tokens, passwords, and private credentials.
- Local filesystem paths and launch-agent configuration.
- Private prompts, personal memories, runtime logs, and machine-specific state.
- Private Discord, Telegram, Twitter, or other service integrations.
- Internal Hermes, fleet, model-routing, and infrastructure configuration.
- Upstream AIRI source code; see the [AIRI project](https://github.com/moeru-ai/airi) for the original open-source project.

## Why it belongs in the portfolio

AIRI demonstrates applied systems thinking: taking an existing interface concept and building a bounded local experience around model transport, voice, state, and operational reliability. The value is not the mascot alone—it is the engineering discipline required to make the interaction understandable and dependable.
