# Olympus lockdown checklist

Olympus is accepted only when the renderer, adapters, Hermes lanes, and Apple Silicon host all pass this checklist.

## Repository

- [ ] No credentials, tokens, cookies, private prompts, personal memory, raw transcripts, audio, logs, machine paths, or private ports are committed.
- [ ] `.gitignore` excludes private Olympus assets and environment files.
- [ ] Avatar manifests validate against [`avatar.schema.json`](avatar.schema.json).
- [ ] Public examples use environment references, not real values.
- [ ] Upstream AIRI attribution and license remain visible.

## AIRI renderer

- [ ] AIRI runs independently before Olympus integration.
- [ ] Renderer origin is explicitly allowlisted.
- [ ] Avatar IDs are allowlisted; user input cannot select arbitrary files or endpoints.
- [ ] Renderer receives only the narrow adapter response contract.
- [ ] Microphone and screen permissions remain user-controlled.

## Hermes lanes

- [ ] Zeus, Odin, and Thor use isolated named authority lanes.
- [ ] Default Hermes routing is unchanged unless separately approved.
- [ ] AIRI cannot invoke arbitrary Hermes tools.
- [ ] Odin has counsel/review authority, not mutation authority.
- [ ] Thor build requests are repository/worktree scoped and approval-gated.
- [ ] No avatar lane inherits private messaging channels, browser state, secrets, or broad filesystem access.

## Network and process

- [ ] Every local adapter binds to `127.0.0.1`.
- [ ] No public listener or tunnel is enabled by default.
- [ ] Request body, message count, output length, and timeout limits are enforced.
- [ ] Health checks identify dependency state without exposing secrets.
- [ ] launchd supervision is added only after manual startup passes.
- [ ] Process identity, listener address, health, and one real request are verified after restart.

## Local model and audio safety

- [ ] Model task is classified as ASR, conversation, or TTS before download.
- [ ] License and total installed footprint are recorded.
- [ ] Apple Silicon architecture and Metal/CPU behavior are recorded.
- [ ] Heavy local roles are serialized until unified-memory capacity is proven.
- [ ] No automatic model download occurs during a user request.
- [ ] Audio output is validated before AIRI receives it.
- [ ] Missing local dependencies fail visibly; no silent cloud fallback.

## Release gates

- [ ] `python3 scripts/validate_olympus.py` passes.
- [ ] Direct runtime smoke passes.
- [ ] Adapter health and allowlist tests pass.
- [ ] AIRI typed-text flow passes.
- [ ] TTS playback and visible lip-sync pass.
- [ ] Real microphone flow passes, or is explicitly marked unverified.
- [ ] Public documentation uses `accepted`, `live`, `held`, `blocked`, and `unverified` truthfully.
