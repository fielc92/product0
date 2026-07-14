#!/usr/bin/env python3
# Validate Product0's portable Agent Skills repository.

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

ACTIVE_SKILLS = {
    "product0",
    "product0-session-memory",
    "product0-using-brief",
}

COMPATIBILITY_SKILLS = {
    "product0-framing-intent",
    "product0-defining-requirements",
    "product0-designing-experience",
    "product0-slicing-scope",
    "product0-preparing-brief",
}

EXPECTED_SKILLS = ACTIVE_SKILLS | COMPATIBILITY_SKILLS
STALE_V02_SIBLING_SKILLS = {
    "product0-orienting-context",
    "product0-shaping-direction",
    "product0-challenging-direction",
    "product0-writing-brief",
    "product0-reviewing-brief",
}

ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
}

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_RE = re.compile(r"(?<![\w/])((?:assets|references)/[A-Za-z0-9._/-]+)")

CORE_WORKFLOW_REFERENCES = (
    "references/orienting-context.md",
    "references/shaping-direction.md",
    "references/challenging-direction.md",
    "references/writing-brief.md",
    "references/reviewing-brief.md",
    "references/version-skew.md",
)


@dataclass(frozen=True)
class SkillDoc:
    directory: Path
    metadata: dict[str, str]
    body: str
    text: str


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_skill(path: Path) -> SkillDoc:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md has no closing YAML frontmatter delimiter")

    raw_frontmatter = text[4:end]
    body = text[end + 5 :]
    metadata: dict[str, str] = {}

    for line in raw_frontmatter.splitlines():
        if not line or line.startswith((" ", "\t", "#")):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not match:
            raise ValueError(f"Unsupported top-level frontmatter line: {line!r}")
        key, raw_value = match.group(1), match.group(2) or ""
        metadata[key] = _unquote(raw_value)

    return SkillDoc(path.parent, metadata, body, text)


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SKILLS_ROOT.is_dir():
        return ([f"Missing skills directory: {SKILLS_ROOT}"], warnings)

    actual_skills = {
        p.name for p in SKILLS_ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    }

    missing = EXPECTED_SKILLS - actual_skills
    unexpected = actual_skills - EXPECTED_SKILLS
    if missing:
        errors.append(f"Missing expected skills: {', '.join(sorted(missing))}")
    if unexpected:
        errors.append(f"Unexpected additional skills: {', '.join(sorted(unexpected))}")

    docs: dict[str, SkillDoc] = {}

    for name in sorted(actual_skills):
        skill_file = SKILLS_ROOT / name / "SKILL.md"
        try:
            doc = parse_skill(skill_file)
        except (OSError, ValueError) as exc:
            errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
            continue

        docs[name] = doc
        meta = doc.metadata
        unknown_fields = set(meta) - ALLOWED_FRONTMATTER
        if unknown_fields:
            errors.append(f"{name}: non-portable frontmatter fields: {', '.join(sorted(unknown_fields))}")

        declared_name = meta.get("name", "")
        description = meta.get("description", "")
        if declared_name != name:
            errors.append(f"{name}: frontmatter name {declared_name!r} must match directory")
        if not NAME_RE.fullmatch(declared_name):
            errors.append(f"{name}: invalid Agent Skills name {declared_name!r}")
        if not 1 <= len(declared_name) <= 64:
            errors.append(f"{name}: name length must be 1-64 characters")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{name}: description length must be 1-1024 characters")
        if not description.startswith("Use when") and not (
            name in COMPATIBILITY_SKILLS
            and description.startswith("Use only when the user explicitly invokes")
        ):
            warnings.append(f"{name}: description should start with 'Use when'")
        if not meta.get("license"):
            errors.append(f"{name}: license is required")
        if not meta.get("compatibility"):
            errors.append(f"{name}: compatibility is required")
        if not doc.body.strip():
            errors.append(f"{name}: empty skill body")

        word_count = len(re.findall(r"\b\w+[\w'-]*\b", doc.body))
        if word_count > 2200:
            warnings.append(f"{name}: long SKILL.md body ({word_count} words)")

        for rel in sorted(set(REFERENCE_RE.findall(doc.body))):
            target = doc.directory / rel
            if not target.is_file():
                errors.append(f"{name}: referenced file does not exist: {rel}")

        eval_path = doc.directory / "evals" / "evals.json"
        if not eval_path.is_file():
            errors.append(f"{name}: missing evals/evals.json")
            continue

        try:
            payload = json.loads(eval_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: invalid eval JSON: {exc}")
            continue

        if payload.get("skill_name") != name:
            errors.append(f"{name}: eval skill_name must match directory")
        cases = payload.get("evals")
        if not isinstance(cases, list) or not cases:
            errors.append(f"{name}: evals must be a non-empty list")
            continue

        ids: set[object] = set()
        for index, case in enumerate(cases, start=1):
            if not isinstance(case, dict):
                errors.append(f"{name}: eval {index} must be an object")
                continue
            case_id = case.get("id")
            if case_id in ids:
                errors.append(f"{name}: duplicate eval id {case_id!r}")
            ids.add(case_id)
            for field in ("prompt", "expected_output"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    errors.append(f"{name}: eval {case_id!r} missing {field}")

    required_fragments = {
        "product0": [
            "PRODUCT0 MUST NOT START TECHNICAL DESIGN OR IMPLEMENTATION",
            "NO BRIEF BEFORE PRODUCT DIRECTION IS APPROVED",
            "NO QUESTION THAT THE REPOSITORY CAN ANSWER",
            "CORE_WORKFLOW_IS_SELF_CONTAINED",
            "references/orienting-context.md",
            "references/shaping-direction.md",
            "references/challenging-direction.md",
            "references/writing-brief.md",
            "references/reviewing-brief.md",
            "handoff-ready",
        ],
        "product0-orienting-context": [
            "ORIENT BEFORE ASKING PRODUCT QUESTIONS",
            "## Lay of the land",
            "DO NOT WRITE A PRODUCT0 BRIEF DURING ORIENTATION",
        ],
        "product0-shaping-direction": [
            "DO NOT WRITE THE BRIEF DURING DISCOVERY",
            "Decision packets",
            "Delegated authority",
        ],
        "product0-challenging-direction": ["DIRECTION_READY", "REVISE"],
        "product0-writing-brief": [
            "ONE APPROVED DIRECTION = ONE COHERENT BRIEF WRITE",
            "docs/product0/briefs/",
        ],
        "product0-reviewing-brief": ["HANDOFF_READY", "NOT_READY"],
        "product0-using-brief": [
            "DO NOT USE A BRIEF UNLESS status: handoff-ready",
            "Product Decision Request",
        ],
        "product0-session-memory": [
            "ONE CONVERSATION SESSION = ONE SESSION FILE",
            "NO MEMORY WRITE WITHOUT AN EXPLICIT WRITE INTENT",
        ],
    }

    for name in COMPATIBILITY_SKILLS:
        required_fragments[name] = ["DEPRECATED COMPATIBILITY ALIAS"]

    for name, fragments in required_fragments.items():
        doc = docs.get(name)
        if not doc:
            continue
        for fragment in fragments:
            if fragment not in doc.text:
                errors.append(f"{name}: missing contract fragment {fragment!r}")

    orchestrator = docs.get("product0")
    if orchestrator and "Ask one blocking question at a time" in orchestrator.text:
        errors.append("product0: v0.1 one-question interview instruction must be removed")
    if orchestrator:
        for rel in CORE_WORKFLOW_REFERENCES:
            if rel not in orchestrator.text:
                errors.append(f"product0: missing core workflow reference {rel!r}")

    template = ROOT / "skills" / "product0" / "references" / "brief-templates" / "marketing-surface.md"
    if template.is_file():
        text = template.read_text(encoding="utf-8")
        for forbidden in ("_Status: pending_", "status: captured", "#### R-01"):
            if forbidden in text:
                errors.append(f"product0-writing-brief: adaptive template contains {forbidden!r}")

    for name in actual_skills:
        scripts_dir = SKILLS_ROOT / name / "scripts"
        if scripts_dir.exists() and any(p.is_file() for p in scripts_dir.rglob("*")):
            errors.append(f"{name}: runtime scripts are not permitted")

    for required_file in (
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "tests" / "baseline-failures.md",
        ROOT / "tests" / "landing-page-regression.md",
    ):
        if not required_file.is_file():
            errors.append(f"Missing repository file: {required_file.relative_to(ROOT)}")

    return errors, warnings


def main() -> int:
    errors, warnings = validate()

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1

    print(
        f"Validated {len(ACTIVE_SKILLS)} active and "
        f"{len(COMPATIBILITY_SKILLS)} compatibility Product0 skills "
        f"with {len(warnings)} warning(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
