#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single original excuse line (98 characters, under the 180 cap)
to the output file the grader reads.
"""

import os

LINE = (
    "Good news: I found the bug. Bad news: the bug was me, "
    "and I already deployed myself to production."
)

# The bounty caps the line at 180 characters; keep the guard next to the text
# so a future edit to the line cannot silently break the gate.
MAX_CHARS = 180


def build_line() -> str:
    """Return the excuse exactly as it must land in entry.txt."""
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line or line != line.strip():
        raise ValueError("excuse must be one clean line")
    return line


def main() -> int:
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
