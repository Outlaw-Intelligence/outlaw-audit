# Olympus adapter contract

The adapter is the security boundary between AIRI and Hermes. It is not a second gateway, scheduler, memory store, approval authority, or general-purpose tool proxy.

## Allowed operations

Each manifest may allow only:

- `health` — dependency and lane readiness without secret values;
- `chat` — bounded text conversation;
- `avatar-state` — listening, thinking, speaking, idle, unavailable;
- `handoff` — structured Zeus/Odin/Thor handoff metadata without private transcripts;
- `status-read` — sanitized status summaries.

Everything else is rejected with a stable 403 response. In particular, reject shell, filesystem, browser, computer-use, arbitrary subprocess, hardware, credentials, raw prompt export, and unbounded tool calls.

## Request controls

The adapter must enforce:

- JSON content type;
- maximum request body from the manifest;
- maximum message count and message length;
- fixed timeout from the manifest;
- avatar ID allowlist;
- profile reference allowlist;
- loopback bind only;
- explicit origin allowlist for the AIRI renderer;
- no redirect following to non-loopback destinations;
- no user-controlled URL or command fields;
- structured error responses without stack traces or secret material.

## Response controls

Return only the fields needed by AIRI:

```text
avatar
text
state
handoff
stream_complete
degraded
error_code
```

Never return:

```text
credentials
provider tokens
filesystem paths
ports
raw logs
private prompts
internal session IDs
model server connection strings
```

## Handoff model

Handoffs are explicit and bounded:

```json
{
  "from": "odin",
  "to": "thor",
  "type": "review-to-build",
  "objective": "short sanitized objective",
  "allowedScope": ["repository-relative/path"],
  "forbidden": ["credentials", "deployment", "hardware"],
  "requiresHumanApproval": true
}
```

The adapter does not execute a handoff. It records or forwards the structured request to the existing Hermes authority lane, which applies its own approval and tool policy.

## Failure behavior

- Backend unavailable → `503` plus `degraded: true`.
- Invalid avatar → `404` or `422`, never fallback to another avatar.
- Oversized request → `413`.
- Disallowed operation → `403`.
- Timeout → `504` with no partial private payload.
- Missing local voice dependency → visible unavailable state; never silent cloud fallback.

## Logging

Log only:

- timestamp;
- request class;
- avatar ID;
- allowlist decision;
- duration bucket;
- success/degraded/error code.

Do not log message content, audio, credentials, session transcripts, prompts, local paths, or model connection strings.
