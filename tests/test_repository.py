from __future__ import annotations

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
