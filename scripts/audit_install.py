from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from skill_metadata import EXPECTED_VERSION, parse_skill
except ModuleNotFoundError:
    from scripts.skill_metadata import EXPECTED_VERSION, parse_skill

ACTIVE_SKILLS = {"product0", "product0-session-memory", "product0-using-brief"}
COMPATIBILITY_SKILLS = {
    "product0-framing-intent", "product0-defining-requirements",
    "product0-designing-experience", "product0-slicing-scope", "product0-preparing-brief",
}
STALE_V02_SIBLING_SKILLS = {
    "product0-orienting-context", "product0-shaping-direction",
    "product0-challenging-direction", "product0-writing-brief", "product0-reviewing-brief",
}
EXPECTED_SKILLS = ACTIVE_SKILLS | COMPATIBILITY_SKILLS
EXPECTED_ROLES = {
    "product0": "orchestrator", "product0-session-memory": "cross-cutting",
    "product0-using-brief": "bridge",
    **{name: "compatibility" for name in COMPATIBILITY_SKILLS},
}


def audit_root(root: Path) -> dict[str, object]:
    report: dict[str, object] = {
        "path": str(root.absolute()), "status": "malformed", "active_present": [],
        "aliases_present": [], "stale_v02_siblings": [], "stale_alias_bodies": [],
        "missing_expected": [], "unknown_product0_directories": [],
        "metadata_versions": {}, "issues": [], "recommended_removals": [],
    }
    issues: list[dict[str, str]] = report["issues"]  # type: ignore[assignment]
    if not root.is_dir():
        issues.append({"code": "ROOT_NOT_FOUND", "detail": "root is not a directory"})
        return report
    for child in root.iterdir():
        if not child.name.startswith("product0"):
            continue
        if child.name in STALE_V02_SIBLING_SKILLS:
            report["stale_v02_siblings"].append(child.name)  # type: ignore[index]
            report["recommended_removals"].append(str(child.absolute()))  # type: ignore[index]
            continue
        if child.name not in EXPECTED_SKILLS:
            report["unknown_product0_directories"].append(child.name)  # type: ignore[index]
            issues.append({"code": "UNKNOWN_PRODUCT0_DIRECTORY", "detail": child.name})
            continue
        try:
            doc = parse_skill(child / "SKILL.md", child.name)
        except (OSError, ValueError) as exc:
            issues.append({"code": "MALFORMED_SKILL", "detail": f"{child.name}: {exc}"})
            continue
        version = doc.metadata.get("version", "")
        report["metadata_versions"][child.name] = version  # type: ignore[index]
        if version != EXPECTED_VERSION:
            if child.name in COMPATIBILITY_SKILLS:
                report["stale_alias_bodies"].append(child.name)  # type: ignore[index]
                report["recommended_removals"].append(str(child.absolute()))  # type: ignore[index]
            else:
                issues.append({"code": "VERSION_MISMATCH", "detail": child.name})
            continue
        if child.name in ACTIVE_SKILLS and doc.metadata.get("role") == EXPECTED_ROLES[child.name]:
            report["active_present"].append(child.name)  # type: ignore[index]
        elif child.name in COMPATIBILITY_SKILLS and doc.metadata.get("role") == "compatibility" and "EXPLICIT INVOCATION ONLY" in doc.body and "Load product0" in doc.body:
            report["aliases_present"].append(child.name)  # type: ignore[index]
        else:
            report["stale_alias_bodies"].append(child.name)  # type: ignore[index]
            report["recommended_removals"].append(str(child.absolute()))  # type: ignore[index]
    present = set(report["active_present"]) | set(report["aliases_present"])  # type: ignore[arg-type]
    report["missing_expected"] = sorted(EXPECTED_SKILLS - present)
    stale = bool(report["stale_v02_siblings"] or report["stale_alias_bodies"])  # type: ignore[index]
    has_current = bool(report["active_present"] or report["aliases_present"])  # type: ignore[index]
    if report["unknown_product0_directories"] or issues or (report["missing_expected"] and not stale):  # type: ignore[index]
        report["status"] = "mixed" if has_current and stale else "malformed"
    elif stale:
        report["status"] = "mixed" if has_current else "stale"
    else:
        report["status"] = "clean"
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("human", "json"), default="human")
    parser.add_argument("roots", nargs="+", type=Path)
    args = parser.parse_args()
    reports = [audit_root(root) for root in args.roots]
    precedence = {"clean": 0, "stale": 1, "malformed": 2, "mixed": 3}
    overall = max((report["status"] for report in reports), key=precedence.get)
    if args.format == "json":
        print(json.dumps({"schema_version": 1, "expected_version": EXPECTED_VERSION, "overall_status": overall, "roots": reports}))
    else:
        for report in reports:
            print(f"Product0 install audit\nroot: {report['path']}\nstatus: {report['status']}")
        print(f"overall_status: {overall}")
    return {"clean": 0, "stale": 2, "malformed": 3, "mixed": 4}[overall]


if __name__ == "__main__":
    raise SystemExit(main())
