from __future__ import annotations

import importlib.util
import json
import re
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
    LENSES_ROOT = ROOT / "skills/product0/references/lenses"

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

    def test_marketing_surface_contract_is_strategic(self) -> None:
        text = (self.LENSES_ROOT / "marketing-surface.md").read_text(encoding="utf-8")
        markers = (
            "MS01_TARGET_BUYER_AND_BUYING_SITUATION",
            "MS02_PAGE_JOB_AND_DESIRED_PERCEPTION",
            "MS03_POSITIONING_AND_VALUE_PROPOSITION",
            "MS04_MESSAGE_HIERARCHY",
            "MS05_PAGE_NARRATIVE",
            "MS06_PRODUCT_DEMONSTRATION_AND_VISUAL_DIRECTION",
            "MS07_PROOF_TRUST_AND_CREDIBILITY",
            "MS08_BUYER_OBJECTIONS",
            "MS09_CONVERSION_STRATEGY",
            "MS10_MEASUREMENT_AND_CLAIM_SAFETY",
        )
        self._assert_deep_lens_contract(text, markers)

    def test_product_workflow_contract_is_feature_ready(self) -> None:
        text = (self.LENSES_ROOT / "product-workflow.md").read_text(encoding="utf-8")
        markers = (
            "PW01_ACTORS_AND_AFFECTED_PARTIES",
            "PW02_TRIGGERING_SITUATION",
            "PW03_DESIRED_PRODUCT_OUTCOME",
            "PW04_LIFECYCLE_AND_STATE_PROGRESSION",
            "PW05_BUSINESS_RULES",
            "PW06_AUTHORITY_AND_PERMISSIONS",
            "PW07_CONSEQUENTIAL_EXCEPTIONS",
            "PW08_SUCCESS_EVIDENCE_AND_GUARDRAILS",
            "PW09_SCOPE_AND_NON_GOALS",
            "PW10_IMPLEMENTATION_NEUTRAL_HANDOFF",
        )
        self._assert_deep_lens_contract(text, markers)

    def test_platform_capability_contract_is_feature_ready(self) -> None:
        text = (self.LENSES_ROOT / "platform-capability.md").read_text(encoding="utf-8")
        markers = (
            "PC01_CONSUMERS",
            "PC02_JOBS_AND_OUTCOMES_ENABLED",
            "PC03_CAPABILITY_BOUNDARY",
            "PC04_CONFIGURATION_AND_CONTROL",
            "PC05_PRODUCT_LEVEL_GUARANTEES",
            "PC06_FAILURE_CONSEQUENCES",
            "PC07_ADOPTION_AND_MIGRATION_IMPLICATIONS",
            "PC08_SUCCESS_EVIDENCE_AND_GUARDRAILS",
            "PC09_SCOPE_AND_NON_GOALS",
            "PC10_IMPLEMENTATION_NEUTRAL_HANDOFF",
        )
        self._assert_deep_lens_contract(text, markers)

    def test_decision_packet_exception_requires_documented_blocker(self) -> None:
        text = (
            ROOT / "skills/product0/references/shaping-direction.md"
        ).read_text(encoding="utf-8")
        self.assertIn("unless a genuine blocker is\ndocumented", text)
        self.assertIn("**Open risk** provenance entry", text)

    def test_marketing_template_is_adaptive(self) -> None:
        template = (
            ROOT / "skills/product0/references/brief-templates/marketing-surface.md"
        ).read_text(encoding="utf-8")
        self.assertIn("TEMPLATE_IS_A_MENU_NOT_A_CHECKLIST", template)
        for marker in (
            "<!-- required -->",
            "<!-- type-required: marketing-surface -->",
            "<!-- conditional:",
            "<!-- optional -->",
        ):
            self.assertIn(marker, template)
        for pattern in (
            r"(?m)^### R-\d+",
            r"_Status:\s*(?:pending|approved)",
            r"(?m)^## Approval record\s*$",
        ):
            self.assertNotRegex(template, pattern)
        for heading in ("Product requirements", "Product slices"):
            self.assertRegex(
                template,
                rf"(?m)^<!-- conditional:[^\n]*-->\n## {heading}$",
            )
        for pattern in (
            r"_Status:\s*(?:pending|approved)",
        ):
            self.assertNotRegex(template, pattern)
        self.assertRegex(
            template,
            r"<!-- conditional:[^\n]*-->\n## Traceability rationale",
        )
        self.assertRegex(
            template,
            r"<!-- conditional:[^\n]*-->\n## Proportionality rationale",
        )
        self.assertRegex(template, r"(?m)^### S-\d{2}: \S.*$")

        writer = (ROOT / "skills/product0/references/writing-brief.md").read_text(
            encoding="utf-8"
        )
        self.assertRegex(writer, r"At least\s+two slices are required")
        self.assertIn("empty rationale heading never satisfies", writer)

    def test_review_rubric_contains_slop_rules(self) -> None:
        rubric = (
            ROOT / "skills/product0/references/readiness-rubric.md"
        ).read_text(encoding="utf-8")
        for rule_id in (
            "SL01_REPOSITORY_EVIDENCE_MISSING",
            "SL02_ASSUMPTION_PROMOTED_TO_FACT",
            "SL03_DECISION_REPEATED_ACROSS_SECTIONS",
            "SL04_ONE_ITEM_PRODUCT_SLICE",
            "SL05_IRRELEVANT_TECHNICAL_QUESTION",
            "SL06_ROUTINE_UX_DOMINATES_DIRECTION",
            "SL07_DISPROPORTIONATE_LENGTH",
            "SL08_BUSINESS_CONTEXT_STILL_MISSING",
            "MSR01_MESSAGE_HIERARCHY_MISSING",
            "MSR02_PAGE_NARRATIVE_MISSING",
            "MSR03_VISUAL_DIRECTION_MISSING",
            "MSR04_PROOF_OR_TRUST_MISSING",
            "MSR05_OBJECTION_HANDLING_MISSING",
            "MSR06_CONVERSION_STRATEGY_MISSING",
        ):
            self.assertIn(rule_id, rubric)

    def test_secondary_lenses_are_substantive(self) -> None:
        lens_names = (
            "integration",
            "pricing-packaging",
            "internal-operation",
            "compliance-change",
            "product-quality",
        )
        all_lens_names = (
            "marketing-surface",
            "product-workflow",
            "platform-capability",
            *lens_names,
        )
        unique_identifiers = []
        for name in lens_names:
            text = (self.LENSES_ROOT / f"{name}.md").read_text(encoding="utf-8")
            unique_identifier = f"LENS_ID_{name.upper().replace('-', '_')}"
            unique_identifiers.append(unique_identifier)
            self.assertIn(unique_identifier, text)
            for marker in (
                "LENS_EVIDENCE_TO_INSPECT",
                "LENS_RECOMMENDATIONS_TO_MAKE",
                "LENS_BLOCKING_PRODUCT_DECISIONS",
                "LENS_IMPLEMENTATION_DETAILS_NOT_TO_ASK",
            ):
                self.assertIn(marker, text)
            self.assertNotRegex(text, r"\b(?:TBD|TODO)\b")
            self.assertNotRegex(text, r"\b(?:MS|PW|PC)\d{2}")
            self.assertGreaterEqual(self._prose_word_count(text), 120)

        all_unique_identifiers = []
        for name in all_lens_names:
            text = (self.LENSES_ROOT / f"{name}.md").read_text(encoding="utf-8")
            all_unique_identifiers.extend(re.findall(r"\bLENS_ID_[A-Z_]+\b", text))
        self.assertEqual(len(all_unique_identifiers), len(set(all_unique_identifiers)))
        self.assertEqual(len(unique_identifiers), len(set(unique_identifiers)))

    def _assert_deep_lens_contract(self, text: str, markers: tuple[str, ...]) -> None:
        for marker in markers:
            section = re.search(
                rf"^## {re.escape(marker)}\n(?P<body>.*?)(?=^## |\Z)",
                text,
                flags=re.MULTILINE | re.DOTALL,
            )
            self.assertIsNotNone(section, f"missing marker section: {marker}")
            assert section is not None
            for obligation in (
                "Repository evidence to inspect",
                "Product0 recommendation",
                "Blocking product decision",
                "Reserved for technical brainstorming",
            ):
                self.assertIn(obligation, section.group("body"), marker)
        self.assertIn("Direction approval is prohibited", text)

    def _prose_word_count(self, text: str) -> int:
        without_frontmatter = re.sub(r"\A---.*?---\s*", "", text, flags=re.DOTALL)
        without_fences = re.sub(r"```.*?```", "", without_frontmatter, flags=re.DOTALL)
        prose_lines = [
            line
            for line in without_fences.splitlines()
            if not line.lstrip().startswith("#")
            and not re.fullmatch(r"\s*[A-Z][A-Z0-9_]+\s*", line)
        ]
        return len(re.findall(r"\b[\w'-]+\b", "\n".join(prose_lines)))


if __name__ == "__main__":
    unittest.main()
