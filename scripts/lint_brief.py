#!/usr/bin/env python3
"""Deterministic structural authoring checks for Product0 briefs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


TOP_LEVEL_SECTION = re.compile(r"^## (?!#)(.+?)\s*$", re.MULTILINE)
SLICE_HEADING = re.compile(r"^### S-\d{2}: \S.*$", re.MULTILINE)
LEVEL_THREE_HEADING = re.compile(r"^### (?!#).*$", re.MULTILINE)
WORD = re.compile(r"\b[\w'-]+\b")


def finding(code: str, level: str, detail: str | None = None) -> dict[str, str]:
    result = {"code": code, "level": level}
    if detail:
        result["detail"] = detail
    return result


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[index + 1 :])
    raise ValueError("malformed YAML frontmatter")


def strip_non_prose(text: str) -> str:
    text = re.sub(r"\x60\x60\x60.*?\x60\x60\x60", "", text, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("|")
    )


def sections(text: str) -> list[tuple[str, str]]:
    matches = list(TOP_LEVEL_SECTION.finditer(text))
    return [
        (
            match.group(1).strip(),
            text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)],
        )
        for index, match in enumerate(matches)
    ]


def prose_before_heading(body: str) -> str:
    lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("#"):
            break
        if line.strip() and not line.lstrip().startswith("|"):
            lines.append(line.strip())
    return " ".join(lines)


def has_sentence(text: str) -> bool:
    return bool(re.search(r"\S.*[.!?](?:\s|$)", text))


def normalized_sentence_candidates(body: str) -> list[str]:
    prose_lines = [
        line.strip()
        for line in body.splitlines()
        if line.strip() and not line.startswith("#") and not line.lstrip().startswith("|")
    ]
    candidates = re.split(r"(?<=[.!?])\s+|\n{2,}", "\n".join(prose_lines))
    normalized: list[str] = []
    for candidate in candidates:
        tokens = re.findall(r"[\w'-]+", candidate.lower())
        if len(tokens) >= 12:
            normalized.append(" ".join(tokens))
    return normalized


def find_repeated_claims(text: str) -> list[dict[str, str]]:
    claims: dict[frozenset[str], set[str]] = defaultdict(set)
    for heading, body in sections(text):
        if heading == "Developer next step":
            continue
        for sentence in normalized_sentence_candidates(body):
            token_set = frozenset(sentence.split())
            for known_tokens in list(claims):
                union = token_set | known_tokens
                similarity = len(token_set & known_tokens) / len(union) if union else 0
                if similarity >= 0.82:
                    claims[known_tokens].add(heading)
                    break
            else:
                claims[token_set].add(heading)
    return [
        finding(
            "BRIEF_REPEATED_DECISION",
            "ERROR",
            f"Repeated across: {', '.join(sorted(headings))}",
        )
        for headings in claims.values()
        if len(headings) >= 3
    ]


def findings(text: str, kind: str, size: str) -> list[dict[str, str]]:
    body = strip_non_prose(strip_frontmatter(text))
    result: list[dict[str, str]] = []
    section_map = dict(sections(body))

    slice_body = section_map.get("Product slices")
    if slice_body is not None:
        headings = [match.group(0) for match in LEVEL_THREE_HEADING.finditer(slice_body)]
        canonical = [heading for heading in headings if SLICE_HEADING.fullmatch(heading)]
        if any(heading not in canonical for heading in headings):
            result.append(finding("BRIEF_MALFORMED_SLICE_HEADING", "ERROR"))
        if len(canonical) == 0:
            result.append(finding("BRIEF_SLICE_SECTION_EMPTY", "ERROR"))
        elif len(canonical) == 1:
            result.append(finding("BRIEF_ONE_ITEM_SLICE", "ERROR"))
        for match in SLICE_HEADING.finditer(slice_body):
            next_heading = re.search(r"^#{2,3} (?!#)", slice_body[match.end() :], re.MULTILINE)
            content = slice_body[
                match.end() : match.end() + next_heading.start() if next_heading else len(slice_body)
            ]
            if not prose_before_heading(content):
                result.append(finding("BRIEF_SLICE_BODY_EMPTY", "ERROR"))

    requirements_present = "Product requirements" in section_map or bool(
        re.search(r"^### R-\d+\b", body, flags=re.MULTILINE)
    )
    traceability = section_map.get("Traceability rationale")
    traceability_valid = traceability is not None and has_sentence(
        prose_before_heading(traceability)
    )
    if traceability is not None and not traceability_valid:
        result.append(finding("BRIEF_TRACEABILITY_RATIONALE_EMPTY", "ERROR"))
    if kind == "marketing-surface" and size == "small" and requirements_present and not traceability_valid:
        result.append(finding("BRIEF_UNJUSTIFIED_REQUIREMENT_BLOCK", "ERROR"))

    if kind == "marketing-surface" and size == "small":
        word_count = len(WORD.findall(re.sub(r"^#+ .*?$", "", body, flags=re.MULTILINE)))
        proportionality = section_map.get("Proportionality rationale")
        proportionality_words = len(WORD.findall(prose_before_heading(proportionality or "")))
        if proportionality is not None and proportionality_words < 30:
            result.append(finding("BRIEF_PROPORTIONALITY_RATIONALE_EMPTY", "ERROR"))
        if word_count > 1800:
            if proportionality_words >= 30:
                result.append(finding("BRIEF_LENGTH_JUSTIFIED_REVIEW", "WARNING"))
            else:
                result.append(finding("BRIEF_DISPROPORTIONATE_LENGTH", "ERROR"))
        elif word_count > 1500:
            result.append(finding("BRIEF_LENGTH_REVIEW", "WARNING"))

    if re.search(r"_Status:\s*(?:pending|approved)", body) or re.search(
        r"^## Approval record\s*$", body, flags=re.MULTILINE
    ):
        result.append(finding("BRIEF_STAGE_CEREMONY", "ERROR"))
    result.extend(find_repeated_claims(body))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default="general")
    parser.add_argument("--size", default="small")
    parser.add_argument("--format", choices=("human", "json"), default="human")
    parser.add_argument("brief", type=Path)
    args = parser.parse_args()
    try:
        text = args.brief.read_text(encoding="utf-8")
        result = findings(text, args.type, args.size)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3
    if args.format == "json":
        print(json.dumps({"findings": result}, sort_keys=True))
    else:
        for item in result:
            print(f"{item['level']}: {item['code']}")
    return 1 if any(item["level"] == "ERROR" for item in result) else 0


if __name__ == "__main__":
    raise SystemExit(main())
