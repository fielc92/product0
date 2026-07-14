from __future__ import annotations

import subprocess
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("matrix", ROOT / "scripts/run_behavioral_matrix.py")
assert SPEC and SPEC.loader
matrix = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(matrix)


class BehavioralMatrixTest(unittest.TestCase):
    def test_fixture_workspace_is_copied_and_brief_state_is_checked_per_turn(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "fixture"
            fixture.mkdir()
            (fixture / "README.md").write_text("Ikano Pay", encoding="utf-8")
            workspace, fixture_hash = matrix.prepare_workspace(fixture, Path(directory) / "runs")
            self.assertTrue((workspace / "README.md").is_file())
            self.assertEqual(64, len(fixture_hash))
            self.assertEqual([], matrix.briefs_after_turn(workspace, 1))
            (workspace / "docs/product0/briefs").mkdir(parents=True)
            brief = workspace / "docs/product0/briefs/demo.md"
            brief.write_text("---\nstatus: handoff-ready\n---\n", encoding="utf-8")
            self.assertEqual([brief], matrix.briefs_after_turn(workspace, 4))

    def test_codex_adapter_uses_persistent_resume_commands(self) -> None:
        first = matrix.command_for(
            "codex", "first", "/workspace", "gpt-5.6-luna", "prompt", "/tmp/output"
        )
        later = matrix.command_for(
            "codex", "resume", "/workspace", "gpt-5.6-luna", "prompt", "/tmp/output"
        )
        self.assertIn("exec", first)
        self.assertIn("--output-last-message", first)
        self.assertNotIn("--ephemeral", first)
        self.assertIn("resume", later)
        self.assertIn("--last", later)

    def test_opencode_adapter_continues_the_same_workspace_session(self) -> None:
        later = matrix.command_for(
            "opencode", "resume", "/workspace", "opencode/gpt-5.6-luna", "prompt", "/tmp/output"
        )
        self.assertEqual(["opencode", "run"], later[:2])
        self.assertIn("--continue", later)
        self.assertIn("--dir", later)

    def test_harnesses_use_the_specified_model_environment_names(self) -> None:
        text = (ROOT / "scripts/run_behavioral_matrix.py").read_text(encoding="utf-8")
        for variable in ("PRODUCT0_CODEX_MODEL", "PRODUCT0_CLAUDE_MODEL", "PRODUCT0_OPENCODE_MODEL"):
            self.assertIn(variable, text)

    def test_missing_model_is_recorded_as_blocked(self) -> None:
        with self.subTest("runner exits as environment-blocked"):
            result = subprocess.run(["python3", str(ROOT / "scripts/run_behavioral_matrix.py"), "--harness", "codex", "--install-mode", "fresh", "--scenario", str(ROOT / "tests/behavioral/landing-page-session.json"), "--results-dir", "/tmp/product0-results", "--records-dir", "/tmp/product0-records", "--commit", "a" * 40], text=True, capture_output=True, check=False)
            self.assertEqual(5, result.returncode)
