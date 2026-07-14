from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness", choices=("codex", "claude-code", "opencode", "all"), required=True)
    parser.add_argument("--install-mode", choices=("fresh", "mixed", "both"), required=True)
    parser.add_argument("--scenario", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--records-dir", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()
    harnesses = ("codex", "claude-code", "opencode") if args.harness == "all" else (args.harness,)
    modes = ("fresh", "mixed") if args.install_mode == "both" else (args.install_mode,)
    missing = []
    for harness in harnesses:
        variable = "PRODUCT0_" + harness.upper().replace("-", "_") + "_MODEL"
        if not os.environ.get(variable) or not shutil.which(harness.split("-")[0]):
            missing.append(f"{harness}: missing binary or {variable}")
    for harness in harnesses:
        for mode in modes:
            target = args.results_dir / args.commit / harness / mode
            target.mkdir(parents=True, exist_ok=True)
            (target / "run.json").write_text(json.dumps({"skills_commit": args.commit, "harness": harness, "install_mode": mode, "status": "blocked", "blocked_reason": "; ".join(missing)}), encoding="utf-8")
    return 5 if missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
