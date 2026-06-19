#!/usr/bin/env python3
"""Lightweight structural validation for civarium-agents."""
from __future__ import annotations

from pathlib import Path
import re
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required for validation: {exc}", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def validate_manifest(agent_dir: Path) -> None:
    manifest = agent_dir / "agent.yaml"
    if not manifest.exists():
        err(f"{agent_dir.relative_to(ROOT)}: missing agent.yaml")
        return
    data = yaml.safe_load(manifest.read_text())
    if not isinstance(data, dict):
        err(f"{manifest.relative_to(ROOT)}: manifest must be a mapping")
        return
    for key in ["schema_version", "slug", "name", "summary", "hermes", "civarium", "safety"]:
        if key not in data:
            err(f"{manifest.relative_to(ROOT)}: missing {key}")
    slug = data.get("slug")
    if slug and slug != agent_dir.name:
        err(f"{manifest.relative_to(ROOT)}: slug {slug!r} must match folder {agent_dir.name!r}")
    if slug and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        err(f"{manifest.relative_to(ROOT)}: slug must be lowercase kebab-case")


def validate_skill(path: Path) -> None:
    text = path.read_text()
    rel = path.relative_to(ROOT)
    if not text.startswith("---"):
        err(f"{rel}: missing opening frontmatter")
        return
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        err(f"{rel}: missing closing frontmatter")
        return
    fm_text = text[3:m.start() + 3]
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as exc:
        err(f"{rel}: invalid YAML frontmatter: {exc}")
        return
    if not isinstance(fm, dict):
        err(f"{rel}: frontmatter must be a mapping")
        return
    for key in ["name", "description"]:
        if not fm.get(key):
            err(f"{rel}: missing {key}")
    if len(str(fm.get("description", ""))) > 1024:
        err(f"{rel}: description too long")
    if not text[m.end() + 3:].strip():
        err(f"{rel}: empty body")


def main() -> int:
    if not AGENTS.exists():
        err("agents/: missing")
    else:
        for agent_dir in sorted(p for p in AGENTS.iterdir() if p.is_dir()):
            if agent_dir.name.startswith("."):
                continue
            validate_manifest(agent_dir)
            if not (agent_dir / "README.md").exists():
                err(f"{agent_dir.relative_to(ROOT)}: missing README.md")
            for required in ["hermes-profile/SOUL.md", "hermes-profile/memories/MEMORY.md", "hermes-profile/memories/USER.md"]:
                if not (agent_dir / required).exists():
                    err(f"{agent_dir.relative_to(ROOT)}: missing {required}")
            for skill in sorted((agent_dir / "skills").glob("*/SKILL.md")):
                validate_skill(skill)

    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1
    print("OK: civarium-agents structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
