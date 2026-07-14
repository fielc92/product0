from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("release_gate", ROOT / "scripts/check_behavioral_release_gate.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class BehavioralReleaseGateTest(unittest.TestCase):
    def test_missing_records_fail_the_gate(self) -> None:
        self.assertFalse(module.check_records(ROOT / "tests/behavioral-records", "a" * 40))
