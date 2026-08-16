# Olympus on Apple Silicon

This is the reproducible implementation sequence for an Apple Silicon Mac. It is intentionally provider-neutral: use a local runtime that supports arm64/Metal, and keep the exact model identifiers in an owner-only environment file rather than publishing them here.

## 0. Host preflight

Use a native arm64 terminal. Rosetta is a compatibility fallback, not the target runtime.

```bash
uname -m
node -p "process.arch"
pnpm --version
xcode-select -p
```

Expected architecture:

```text
arm64
arm64
pnpm 10.x
/Library/Developer/CommandLineTools or an Xcode developer path
```

Install only the public prerequisites through a reviewed package manager path:

```bash
xcode-select --install
brew install git node pnpm
corepack enable
```

Do not paste credentials into shell history. Keep private values in an owner-only environment file that is excluded by the repository `.gitignore`.

## 1. Prepare the upstream AIRI workspace

Olympus is our integration layer. Keep the upstream AIRI checkout separate so updates and attribution remain clear.

```bash
git clone https://github.com/moeru-ai/airi.git olympus-airi
cd olympus-airi
pnpm install --frozen-lockfile
pnpm build
```

The upstream repository currently declares pnpm `10.33.0` in its package metadata. Confirm the exact version in the checkout before installing dependencies; do not silently substitute an incompatible package manager.

Start the web stage only after the build passes:

```bash
pnpm dev:web
```

First acceptance gate: AIRI must render its own UI before any Hermes or Olympus adapter is introduced.

## 2. Create isolated Hermes authority lanes

Create three named Hermes profiles using the supported Hermes profile workflow. Do not clone the default profile's credentials, messaging channels, browser state, private memory, or broad tool permissions.

Use private profile-local values for:

```text
OLYMPUS_ZEUS_PROFILE
OLYMPUS_ODIN_PROFILE
OLYMPUS_THOR_PROFILE
OLYMPUS_ZEUS_AVATAR_ASSET
OLYMPUS_ODIN_AVATAR_ASSET
OLYMPUS_THOR_AVATAR_ASSET
OLYMPUS_ZEUS_VOICE
OLYMPUS_ODIN_VOICE
OLYMPUS_THOR_VOICE
```

The public manifests use these environment references instead of real values. Keep the default Hermes routing unchanged unless a separate owner-approved migration exists.

### Zeus lane

- user-facing conversation and planning;
- status reads only by default;
- no direct shell, filesystem, browser, hardware, or arbitrary subprocess access through AIRI;
- decision authority remains with me and the Hermes host;

### Odin lane

- independent counsel and red-team analysis;
- architecture and risk review;
- no implementation ownership and no direct mutation authority;
- receives a bounded brief and returns a structured verdict packet.

### Thor lane

- implementation planning, code review, and bounded build requests;
- repository/worktree scope is enforced by the Hermes implementation lane, not by the avatar renderer;
- no direct hardware control and no unrestricted avatar-side tool access;
- local model residency and Apple Silicon memory safety are checked before loading.

## 3. Add the adapter boundary

AIRI should call one Olympus adapter contract, not three arbitrary Hermes endpoints. The adapter selects the manifest by an allowlisted avatar ID and forwards only:

```json
{
  "avatar": "zeus",
  "conversation": {
    "messages": [{"role": "user", "content": "..."}],
    "conversationId": "opaque-session-reference"
  },
  "request": {"type": "chat"}
}
```

The adapter returns only:

```json
{
  "avatar": "zeus",
  "text": "...",
  "state": "speaking",
  "handoff": null,
  "degraded": false
}
```

Do not forward Hermes tool schemas, shell commands, filesystem paths, credentials, private prompts, raw transcripts, or internal routing metadata to AIRI.

## 4. Add local voice services as separate lanes

Keep voice modular:

```text
ASR → text adapter → Hermes profile → text response → TTS → AIRI playback/lip-sync
```

Each service must have:

- native arm64/Metal-compatible runtime where supported;
- loopback-only binding;
- explicit health endpoint;
- bounded request size and timeout;
- valid audio/container validation;
- visible failure state;
- no automatic cloud fallback.

Do not load ASR, conversation, and TTS models in one unbounded process. Apple Silicon unified memory is shared by CPU, GPU, model weights, caches, and the desktop UI. Measure warm and cold paths separately and keep concurrency at one until real capacity is proven.

## 5. Bind the AIRI renderer

For each avatar:

1. select the matching manifest;
2. provide the private avatar asset reference;
3. provide the private local voice reference;
4. set the adapter's allowlisted avatar ID;
5. verify typed text first;
6. verify local TTS playback;
7. verify visible avatar state transitions;
8. only then verify microphone → ASR → Hermes → TTS → lip-sync.

A successful backend request does not prove that AIRI rendered the correct avatar, played audio, or transitioned through listening/thinking/speaking states.

## 6. Apple Silicon operational rules

- Prefer arm64-native Node, Python, model runtimes, and audio dependencies.
- Use Metal/MPS where the selected runtime supports it; record whether a component falls back to CPU.
- Keep heavy local roles serialized until unified-memory pressure is measured.
- Do not load Leo and Kronos together.
- Do not unload Thor or another protected local role as an incidental cleanup step.
- Keep the AIRI conversation lane separate from the coding lane.
- Use launchd only after the manual command path passes.
- Verify process identity, bound address, health response, and one real request after every restart.

## 7. Reproducible validation

From this repository:

```bash
python3 scripts/validate_olympus.py
```

Then run the acceptance sequence in [`acceptance.md`](acceptance.md). A guide implementation is complete only when the direct runtime, adapter, AIRI renderer, audio playback, and avatar state gates are all independently recorded.
