#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for missing a deadline
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

The line: the excuse is the excuse-writing itself. The speaker spent so
long crafting the perfect excuse for missing the deadline that the
deadline slipped by while they were at it -- a self-referential loop
with the punch landing on the last word, in the voice of someone
cornered by their boss. Fresh angle, no dog, no dead Wi-Fi, no crashed
laptop: the deadline was missed because of the excuse, not in spite of it.
"""

import os

LINE = "I spent so long writing the perfect excuse for missing the deadline that I missed the deadline."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry line must be a single line"
    assert LINE.strip(), "entry line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
