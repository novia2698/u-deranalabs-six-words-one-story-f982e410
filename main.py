#!/usr/bin/env python3
"""Six Words, One Story — entry program.

Writes one complete story, told in exactly six words, to
<output>/entry.txt. The grader reads that file and puts the six
words before the judge.

The story: a person sells the house they lived in for years,
then refuses to let go of the one thing that made it home.
"""

import os
import sys

STORY = "Sold the house. Kept the ghost."


def validate(text: str) -> None:
    """The gate only accepts 1-60 chars; the brief demands six words."""
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story must be 1-60 chars, got {len(text)}")


def main() -> int:
    validate(STORY)
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    print(f"wrote {path} ({len(STORY)} chars, {len(STORY.split())} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
