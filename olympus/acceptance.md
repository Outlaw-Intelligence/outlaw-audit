# Olympus acceptance matrix

| Gate | Required evidence | State vocabulary |
|---|---|---|
| Manifest | JSON parses and matches schema | accepted / blocked |
| Apple Silicon host | arm64 tools and supported runtime confirmed | accepted / blocked |
| AIRI baseline | AIRI renders independently | accepted / blocked |
| Hermes profile | named lane responds without inherited secrets/channels | accepted / blocked |
| Adapter | allowlists, limits, loopback bind, and error paths pass | accepted / blocked |
| Typed conversation | AIRI text reaches the intended avatar lane | live / held |
| Local TTS | nonempty valid audio returns and plays | live / held |
| Avatar state | listening/thinking/speaking/idle transitions observed | live / held |
| Microphone | real audio reaches local ASR and returns transcript | live / unverified |
| Handoff | Zeus/Odin/Thor routing remains structured and approval-gated | accepted / blocked |
| Public release | no secrets/private runtime artifacts; docs and links pass | accepted / blocked |

## Required evidence packet

```text
VERDICT:
AVATAR:
HOST:
PASSED_GATES:
FAILED_GATES:
DEPENDENCIES:
MODEL_TASKS:
SECURITY_CHECKS:
PUBLIC_ARTIFACT:
NEXT:
```

Do not mark a row `live` from configuration alone. `live` requires the actual behavior named in the evidence column.
