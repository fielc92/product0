from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from tests.support import POSITIVE_INVOCATION_RE

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_skillset.py"

spec = importlib.util.spec_from_file_location("product0_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class Product0RepositoryTest(unittest.TestCase):
    def test_repository_contract(self) -> None:
        errors, _warnings = validator.validate()
        self.assertEqual([], errors, "\n".join(errors))

    def test_v02_orchestrator_contract(self) -> None:
        text = (ROOT / "skills/product0/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("NO BRIEF BEFORE PRODUCT DIRECTION IS APPROVED", text)
        self.assertIn("NO QUESTION THAT THE REPOSITORY CAN ANSWER", text)
        self.assertIn("CORE_WORKFLOW_IS_SELF_CONTAINED", text)
        self.assertIn("Never invoke a separate Product0 stage skill", text)
        self.assertNotIn("Ask one blocking question at a time", text)

    def test_core_workflow_is_self_contained(self) -> None:
        orchestrator = ROOT / "skills/product0/SKILL.md"
        text = orchestrator.read_text(encoding="utf-8")
        expected_paths = (
            "references/orienting-context.md",
            "references/shaping-direction.md",
            "references/challenging-direction.md",
            "references/writing-brief.md",
            "references/reviewing-brief.md",
        )
        for relative_path in expected_paths:
            self.assertIn(relative_path, text)

        markdown_files = [orchestrator]
        markdown_files.extend(
            sorted((ROOT / "skills/product0/references").rglob("*.md"))
        )
        matches = []
        for path in markdown_files:
            content = path.read_text(encoding="utf-8")
            for match in POSITIVE_INVOCATION_RE.finditer(content):
                line_number = content.count("\n", 0, match.start()) + 1
                line = content.splitlines()[line_number - 1].strip()
                matches.append(
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    f"{match.group('name')}: {line}"
                )
        self.assertEqual([], matches, "\n".join(matches))

    def test_landing_page_regression_is_an_eval(self) -> None:
        payload = json.loads(
            (ROOT / "skills/product0/evals/evals.json").read_text(encoding="utf-8")
        )
        ids = {case["id"] for case in payload["evals"]}
        self.assertIn("landing-page-regression", ids)

    def test_brief_template_is_adaptive(self) -> None:
        text = (
            ROOT / "skills/product0-writing-brief/assets/product-brief-template.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("_Status: pending_", text)
        self.assertNotIn("status: captured", text)
        self.assertIn("Use only sections that add decision value", text)

    def test_old_stages_are_compatibility_aliases(self) -> None:
        for name in validator.COMPATIBILITY_SKILLS:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("DEPRECATED COMPATIBILITY ALIAS", text)


if __name__ == "__main__":
    unittest.main()
