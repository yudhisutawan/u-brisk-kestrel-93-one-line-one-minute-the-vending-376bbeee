#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes the tournament-winning pickup line (89 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, no network, no reads
outside this repository.

The entry is a single vending-machine pickup line: it plays on the
machine's button press ("love at first press") and lands the joke on
a stale bag of chips dropped on a toe. It won the local tournament
as candidate H4, beating the other finalists on humour, originality
and fit to the one-line, one-minute brief. The file writes exactly
one line — no trailing newline, no extra output — so the entry is
judged on the line itself and nothing else.

SPDX-License-Identifier: MIT
"""

import os

ENTRY = "Do you believe in love at first press, or should I drop a stale bag of chips on your toe?"

# Length guard: the winning line is exactly 89 characters; any edit
# that changes its length changes the judged entry, so fail loudly.
assert len(ENTRY) == 89, "entry must stay 89 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
