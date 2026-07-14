from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = {(harness, mode) for harness in ("codex", "claude-code", "opencode") for mode in ("fresh", "mixed")}


def check_records(records: Path, commit: str) -> bool:
    found = set()
    for path in records.rglob("run.json") if records.exists() else ():
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return False
        if record.get("skills_commit") == commit and record.get("status") == "passed":
            found.add((record.get("harness"), record.get("install_mode")))
    return found == REQUIRED


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", required=True)
    parser.add_argument("--records-dir", type=Path, required=True)
    args = parser.parse_args()
    return 0 if check_records(args.records_dir, args.commit) else 1


if __name__ == "__main__":
    raise SystemExit(main())
