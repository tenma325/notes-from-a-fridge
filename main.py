#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge entry: writes the entry text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = "Day 3 of you saying 'we need to talk' to the takeout menu. I'm right here. I have shelves. I have feelings. I also have your yogurt from October."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
