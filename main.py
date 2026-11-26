#!/usr/bin/env python3
"""The Worst Pizza Topping — entry program.

Writes one line pitching a terrible pizza topping to entry.txt.
The line is a fixed string: the tournament winner from CANDIDATES.md
(driveway gravel, sold deadpan as a premium feature). Deterministic:
the same bytes on every run. No randomness, no network, no input read
from anywhere, no environment value used as code.
"""

import os
import sys

LINE = (
    "Try our pizza topped with driveway gravel, hand-sorted for crunch "
    "and legally not food in three states."
)


def output_path(argv):
    """Where entry.txt goes: argv[1], $MAKEFUN_OUTPUT_DIR, else /output."""
    if len(argv) > 1:
        return os.path.join(argv[1], "entry.txt")
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main(argv):
    path = output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    # Verify-after-write: read the file back and compare the bytes, so a
    # truncated or altered write fails loudly instead of entering a
    # wrong line.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("entry.txt mismatch: wrote %d bytes, read back %d"
                         % (len(data), len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
