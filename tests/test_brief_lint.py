from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "scripts/lint_brief.py"
FIXTURES = ROOT / "tests/fixtures/briefs"


class BriefLintTest(unittest.TestCase):
    def run_linter(
        self, fixture: str, output_format: str = "json"
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "python3",
                str(LINTER),
                "--type",
                "marketing-surface",
                "--size",
                "small",
                "--format",
                output_format,
                str(FIXTURES / fixture),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def finding_codes(self, result: subprocess.CompletedProcess[str]) -> set[str]:
        payload = json.loads(result.stdout)
        return {finding["code"] for finding in payload["findings"]}

    def test_good_small_marketing_brief_exits_zero(self) -> None:
        result = self.run_linter("good-small-marketing.md")

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(set(), self.finding_codes(result))

    def test_one_item_slice_is_an_error(self) -> None:
        result = self.run_linter("bad-one-item-slice.md")

        self.assertEqual(1, result.returncode)
        self.assertIn("BRIEF_ONE_ITEM_SLICE", self.finding_codes(result))

    def test_malformed_slice_heading_is_an_error(self) -> None:
        result = self.run_linter("bad-malformed-slice-heading.md")

        self.assertEqual(1, result.returncode)
        self.assertIn("BRIEF_MALFORMED_SLICE_HEADING", self.finding_codes(result))

    def test_empty_traceability_rationale_does_not_permit_requirements(self) -> None:
        result = self.run_linter("bad-empty-traceability-rationale.md")

        self.assertEqual(1, result.returncode)
        self.assertTrue(
            {
                "BRIEF_TRACEABILITY_RATIONALE_EMPTY",
                "BRIEF_UNJUSTIFIED_REQUIREMENT_BLOCK",
            }.issubset(self.finding_codes(result))
        )

    def test_empty_proportionality_rationale_is_an_error_for_an_overlong_brief(self) -> None:
        result = self.run_linter("bad-empty-proportionality-rationale.md")

        self.assertEqual(1, result.returncode)
        self.assertTrue(
            {
                "BRIEF_PROPORTIONALITY_RATIONALE_EMPTY",
                "BRIEF_DISPROPORTIONATE_LENGTH",
            }.issubset(self.finding_codes(result))
        )

    def test_repeated_decision_across_three_sections_is_an_error(self) -> None:
        result = self.run_linter("bad-repeated-decisions.md")

        self.assertEqual(1, result.returncode)
        self.assertIn("BRIEF_REPEATED_DECISION", self.finding_codes(result))

    def test_overlong_small_marketing_brief_is_an_error(self) -> None:
        result = self.run_linter("bad-overlong-small-marketing.md")

        self.assertEqual(1, result.returncode)
        self.assertIn("BRIEF_DISPROPORTIONATE_LENGTH", self.finding_codes(result))

    def test_traceability_rationale_permits_requirements(self) -> None:
        result = self.run_linter("good-small-marketing.md")

        self.assertNotIn("BRIEF_UNJUSTIFIED_REQUIREMENT_BLOCK", self.finding_codes(result))

    def test_human_and_json_output_have_the_same_codes(self) -> None:
        json_result = self.run_linter("bad-empty-traceability-rationale.md")
        human_result = self.run_linter(
            "bad-empty-traceability-rationale.md", output_format="human"
        )

        self.assertEqual(
            self.finding_codes(json_result),
            {
                line.split(": ", 1)[1]
                for line in human_result.stdout.splitlines()
                if line
            },
        )

    def test_missing_input_exits_three(self) -> None:
        result = subprocess.run(
            ["python3", str(LINTER), str(FIXTURES / "missing.md")],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(3, result.returncode)


if __name__ == "__main__":
    unittest.main()
