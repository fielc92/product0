from __future__ import annotations

import re
import shutil
from pathlib import Path

ALLOWED = {"run.json", "generated-brief.md", "assertion-summary.md"}


def promote(source: Path, destination: Path) -> None:
    staging = destination.with_name(destination.name + ".staging")
    shutil.rmtree(staging, ignore_errors=True)
    staging.mkdir(parents=True)
    for path in source.iterdir():
        if path.name in ALLOWED or re.fullmatch(r"turn-\d+\.message\.md", path.name):
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"(?i)(token|key|secret)=\S+", r"\1=[REDACTED]", text)
            (staging / path.name).write_text(text, encoding="utf-8")
    shutil.rmtree(destination, ignore_errors=True)
    staging.rename(destination)
