from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

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
        self.assertIn("product0-orienting-context", text)
        self.assertIn("product0-shaping-direction", text)
        self.assertIn("product0-challenging-direction", text)
        self.assertIn("product0-writing-brief", text)
        self.assertNotIn("Ask one blocking question at a time", text)

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
