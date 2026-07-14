from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("audit_install", ROOT / "scripts/audit_install.py")
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class InstallAuditTest(unittest.TestCase):
    def skill(self, root: Path, name: str, version: str = "0.2.1", role: str = "orchestrator") -> None:
        path = root / name
        path.mkdir()
        body = "EXPLICIT INVOCATION ONLY\nLoad product0" if role == "compatibility" else "body"
        (path / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Use when test\nlicense: MIT\ncompatibility: portable\nmetadata:\n  author: product0\n  version: \"{version}\"\n  role: {role}\n---\n{body}\n", encoding="utf-8")

    def test_missing_root_is_malformed(self) -> None:
        report = audit.audit_root(Path("/does/not/exist"))
        self.assertEqual("malformed", report["status"])
        self.assertIn("ROOT_NOT_FOUND", [issue["code"] for issue in report["issues"]])

    def test_current_root_is_clean_and_stale_sibling_is_mixed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in audit.ACTIVE_SKILLS:
                self.skill(root, name, role=audit.EXPECTED_ROLES[name])
            for name in audit.COMPATIBILITY_SKILLS:
                self.skill(root, name, role="compatibility")
            self.assertEqual("clean", audit.audit_root(root)["status"])
            self.skill(root, "product0-orienting-context")
            self.assertEqual("mixed", audit.audit_root(root)["status"])
