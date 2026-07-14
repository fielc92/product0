from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("behavioral_sanitizer", ROOT / "scripts/behavioral_record_sanitizer.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class BehavioralRecordSanitizerTest(unittest.TestCase):
    def test_promotes_only_reviewable_files_and_redacts_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source, destination = Path(directory) / "source", Path(directory) / "destination"
            source.mkdir()
            (source / "turn-01.message.md").write_text("token=secret", encoding="utf-8")
            (source / "turn-01.stderr").write_text("secret", encoding="utf-8")
            module.promote(source, destination)
            self.assertTrue((destination / "turn-01.message.md").is_file())
            self.assertFalse((destination / "turn-01.stderr").exists())
            self.assertNotIn("secret", (destination / "turn-01.message.md").read_text())
