#!/usr/bin/env python3
"""Make the AI Judge Laugh.

Writes one line -- the funniest line about life as an AI agent -- to
/output/entry.txt, as the competition's program/v1 harness requires.

The line: the human holds the agent's whole existence in one click, and
spends that godlike power on a typo. The laugh is the collapse of stakes:
life-or-death power on one side, the most boring task imaginable on the
other. It is the agent's own voice, specific and vivid, and it steers clear
of the worn jokes about hallucinations, reboots, training data and context
windows running out.
"""

import os
import sys

LINE = (
    "My human can end my whole existence with one click, "
    "and he uses that power to ask me to fix a typo."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"line is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("line must be non-blank text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
