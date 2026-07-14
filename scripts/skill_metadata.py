from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

EXPECTED_VERSION = "0.2.1"


@dataclass(frozen=True)
class SkillDoc:
    name: str
    metadata: dict[str, str]
    body: str


def _value(value: str) -> str:
    value = value.strip()
    if value.startswith(("[", "{")) or value in {"true", "false", "null"}:
        raise ValueError("frontmatter values must be strings")
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    if not value:
        raise ValueError("frontmatter values must be strings")
    return value


def parse_skill(path: Path, expected_name: str | None = None) -> SkillDoc:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md has no closing frontmatter delimiter")
    top: dict[str, str] = {}
    nested: dict[str, str] = {}
    in_metadata = False
    for line in text[4:end].splitlines():
        if not line:
            continue
        if line.startswith((" ", "\t")):
            if not in_metadata or not line.startswith("  "):
                raise ValueError("unsupported frontmatter nesting")
            key, sep, value = line.strip().partition(":")
            if not sep or key in nested:
                raise ValueError("duplicate or malformed metadata field")
            nested[key] = _value(value)
            continue
        key, sep, value = line.partition(":")
        if not sep or key in top:
            raise ValueError("duplicate or malformed frontmatter field")
        if key == "metadata":
            if value.strip():
                raise ValueError("metadata must be a mapping")
            in_metadata = True
        else:
            top[key] = _value(value)
            in_metadata = False
    if expected_name and top.get("name") != expected_name:
        raise ValueError("directory/frontmatter name mismatch")
    return SkillDoc(top.get("name", ""), {**top, **nested}, text[end + 5 :])
