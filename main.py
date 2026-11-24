#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single original excuse line (98 characters, under the 180 cap)
to the output file the grader reads.
"""

import os
import sys

LINE = (
    "Good news: I found the bug. Bad news: the bug was me, "
    "and I already deployed myself to production."
)


def main() -> int:
    line = LINE.strip()
    if not 1 <= len(line) <= 180:
        print(f"excuse is {len(line)} chars, must be 1-180", file=sys.stderr)
        return 1
    if "\n" in line:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
