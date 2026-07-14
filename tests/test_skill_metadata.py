from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_metadata", ROOT / "scripts/skill_metadata.py")
assert SPEC and SPEC.loader
metadata = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = metadata
SPEC.loader.exec_module(metadata)


class SkillMetadataTest(unittest.TestCase):
    def test_parses_nested_string_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "SKILL.md"
            path.write_text("---\nname: demo\ndescription: Use when demo\nlicense: MIT\ncompatibility: portable\nmetadata:\n  author: product0\n  version: \"0.2.1\"\n  role: bridge\n---\nbody\n", encoding="utf-8")
            parsed = metadata.parse_skill(path, expected_name="demo")
        self.assertEqual("0.2.1", parsed.metadata["version"])
        self.assertEqual("bridge", parsed.metadata["role"])
        self.assertEqual("0.2.1", metadata.EXPECTED_VERSION)

    def test_rejects_duplicate_and_non_string_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "SKILL.md"
            path.write_text("---\nname: demo\nname: other\ndescription: Use when demo\nlicense: MIT\ncompatibility: portable\n---\nbody\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                metadata.parse_skill(path)
            path.write_text("---\nname: demo\ndescription: Use when demo\nlicense: MIT\ncompatibility: portable\nmetadata:\n  version: [0.2.1]\n---\nbody\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                metadata.parse_skill(path)
