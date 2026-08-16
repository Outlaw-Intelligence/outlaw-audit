#!/usr/bin/env python3
"""Validate the public Olympus contract without third-party dependencies."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
AVATAR_DIR = ROOT / "olympus" / "avatars"
EXPECTED = {"zeus", "odin", "thor"}
CAPABILITIES = {
    "conversation", "planning", "analysis", "red-team", "architecture-review",
    "status-read", "implementation-planning", "code-review", "bounded-build-request",
}
FORBIDDEN_PATTERNS = {
    "credential-key": re.compile(r"(?i)(api[_ -]?key|access[_ -]?token|client[_ -]?secret)\s*[:=]\s*[A-Za-z0-9_./+\-]{12,}"),
    "bearer-token": re.compile(r"(?i)bearer\s+[A-Za-z0-9_./+\-]{20,}"),
    "private-home-path": re.compile(r"/(Users|home)/[A-Za-z0-9_.-]+/"),
    "private-ip-port": re.compile(r"(?:127\.0\.0\.1|localhost|0\.0\.0\.0):\d{2,5}"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?" + "PRIVATE " + "KEY-----"),
}


def fail(message: str) -> NoReturn:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    schema_path = ROOT / "olympus" / "avatar.schema.json"
    schema: dict = {}
    try:
        schema = json.loads(schema_path.read_text())
    except Exception as exc:
        fail(f"schema unreadable: {exc}")
    if schema.get("title") != "Olympus Avatar Manifest":
        fail("unexpected schema title")

    files = sorted(AVATAR_DIR.glob("*.json"))
    if {p.stem for p in files} != EXPECTED:
        fail(f"avatar set mismatch: {[p.stem for p in files]}")

    manifests: dict[str, dict] = {}
    for path in files:
        data: dict = {}
        try:
            data = json.loads(path.read_text())
        except Exception as exc:
            fail(f"{path.name} is not valid JSON: {exc}")
        if data.get("id") != path.stem:
            fail(f"{path.name}: id does not match filename")
        required = {"id", "displayName", "role", "authority", "avatar", "voice", "capabilities", "adapter", "security"}
        missing = required - data.keys()
        if missing:
            fail(f"{path.name}: missing {sorted(missing)}")
        if data["avatar"].get("renderer") != "airi":
            fail(f"{path.name}: renderer must be airi")
        if data["adapter"].get("transport") != "loopback-http" or data["adapter"].get("bind") != "127.0.0.1":
            fail(f"{path.name}: adapter must be loopback-http on 127.0.0.1")
        if not set(data["capabilities"]).issubset(CAPABILITIES):
            fail(f"{path.name}: unknown capability")
        security = data["security"]
        for key in ("allowShell", "allowFilesystem", "allowBrowser", "allowHardware"):
            if security.get(key) is not False:
                fail(f"{path.name}: {key} must be false")
        if security.get("requiresHumanApproval") is not True:
            fail(f"{path.name}: human approval must be required")
        if not 1024 <= security.get("maxRequestBytes", 0) <= 1048576:
            fail(f"{path.name}: request limit out of range")
        if not 1000 <= security.get("timeoutMs", 0) <= 120000:
            fail(f"{path.name}: timeout out of range")
        manifests[data["id"]] = data

    if not {"planning", "status-read"}.issubset(manifests["zeus"]["capabilities"]):
        fail("Zeus capability contract incomplete")
    if not {"red-team", "architecture-review"}.issubset(manifests["odin"]["capabilities"]):
        fail("Odin counsel contract incomplete")
    if not {"implementation-planning", "bounded-build-request"}.issubset(manifests["thor"]["capabilities"]):
        fail("Thor implementation contract incomplete")

    scanned = 0
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name in {"validate_olympus.py"}:
            continue
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        scanned += 1
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                violations.append(f"{label}: {path.relative_to(ROOT)}")
    if violations:
        fail("public-safety scan found " + ", ".join(violations))

    print(f"OLYMPUS_VALIDATION_OK avatars={len(manifests)} files_scanned={scanned}")
    print("POLICY_OK direct_shell=false direct_filesystem=false direct_browser=false direct_hardware=false approval=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
