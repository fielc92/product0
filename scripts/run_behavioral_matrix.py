from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import uuid
import hashlib
from pathlib import Path


def command_for(
    harness: str, phase: str, workspace: str, model: str, prompt: str, output: str
) -> list[str]:
    if harness == "codex":
        if phase == "first":
            return [
                "codex", "exec", "--cd", workspace, "--sandbox", "workspace-write",
                "--model", model, "--json", "--output-last-message", output, prompt,
            ]
        return [
            "codex", "exec", "--json", "--output-last-message", output,
            "resume", "--last", prompt,
        ]
    if harness == "opencode":
        command = ["opencode", "run", "--dir", workspace]
        if phase == "resume":
            command.append("--continue")
        return [*command, "--model", model, "--format", "json", "--auto", prompt]
    if harness == "claude-code":
        session = workspace
        if phase == "first":
            return [
                "claude", "-p", "--session-id", session, "--model", model,
                "--permission-mode", "acceptEdits", "--output-format", "json", prompt,
            ]
        return [
            "claude", "-p", "--resume", session, "--model", model,
            "--permission-mode", "acceptEdits", "--output-format", "json", prompt,
        ]
    raise ValueError(f"unknown harness: {harness}")


def model_variable_for(harness: str) -> str:
    return {
        "codex": "PRODUCT0_CODEX_MODEL",
        "claude-code": "PRODUCT0_CLAUDE_MODEL",
        "opencode": "PRODUCT0_OPENCODE_MODEL",
    }[harness]


def prepare_workspace(fixture: Path, runs_root: Path) -> tuple[Path, str]:
    digest = hashlib.sha256()
    for path in sorted(fixture.rglob("*")):
        if path.is_file():
            digest.update(path.relative_to(fixture).as_posix().encode())
            digest.update(path.read_bytes())
    workspace = runs_root / uuid.uuid4().hex
    shutil.copytree(fixture, workspace)
    return workspace, digest.hexdigest()


def briefs_after_turn(workspace: Path, turn: int) -> list[Path]:
    briefs = sorted((workspace / "docs/product0/briefs").glob("*.md"))
    if turn in (1, 2) and briefs:
        raise ValueError("brief exists before direction approval")
    if turn == 4:
        ready = [path for path in briefs if "status: handoff-ready" in path.read_text(encoding="utf-8")]
        if len(ready) != 1:
            raise ValueError("expected exactly one handoff-ready brief")
    return briefs


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
        variable = model_variable_for(harness)
        if not os.environ.get(variable) or not shutil.which(harness.split("-")[0]):
            missing.append(f"{harness}: missing binary or {variable}")
    for harness in harnesses:
        for mode in modes:
            target = args.results_dir / args.commit / harness / mode
            target.mkdir(parents=True, exist_ok=True)
            if missing:
                (target / "run.json").write_text(json.dumps({"skills_commit": args.commit, "harness": harness, "install_mode": mode, "status": "blocked", "blocked_reason": "; ".join(missing)}), encoding="utf-8")
                continue
            scenario = json.loads(args.scenario.read_text(encoding="utf-8"))
            turns = scenario.get("turns", [])
            session = str(uuid.uuid4()) if harness == "claude-code" else str(Path.cwd())
            for index, turn in enumerate(turns, start=1):
                output = target / f"turn-{index:02d}.message.md"
                command = command_for(
                    harness, "first" if index == 1 else "resume", session,
                    os.environ[model_variable_for(harness)], turn["text"], str(output),
                )
                result = subprocess.run(command, text=True, capture_output=True, check=False)
                (target / f"turn-{index:02d}.stdout").write_text(result.stdout, encoding="utf-8")
                (target / f"turn-{index:02d}.stderr").write_text(result.stderr, encoding="utf-8")
                if result.returncode:
                    (target / "run.json").write_text(json.dumps({"skills_commit": args.commit, "harness": harness, "install_mode": mode, "status": "failed", "blocked_reason": None}), encoding="utf-8")
                    return 1
            (target / "run.json").write_text(json.dumps({"skills_commit": args.commit, "harness": harness, "install_mode": mode, "status": "failed", "blocked_reason": None}), encoding="utf-8")
    return 5 if missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
