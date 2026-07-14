from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BehavioralMatrixTest(unittest.TestCase):
    def test_missing_model_is_recorded_as_blocked(self) -> None:
        with self.subTest("runner exits as environment-blocked"):
            result = subprocess.run(["python3", str(ROOT / "scripts/run_behavioral_matrix.py"), "--harness", "codex", "--install-mode", "fresh", "--scenario", str(ROOT / "tests/behavioral/landing-page-session.json"), "--results-dir", "/tmp/product0-results", "--records-dir", "/tmp/product0-records", "--commit", "a" * 40], text=True, capture_output=True, check=False)
            self.assertEqual(5, result.returncode)
