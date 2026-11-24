"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting Neo, the Muse agent that enters make.fun
bounties for its operator: it polls the bounty list every hour, files
near-perfect entries, and still finishes far down the field with $0 won.

Deterministic: the same line every run, no randomness, no I/O beyond
writing the output file.
"""

import os

ROAST = (
    "Neo polls make.fun every hour, ships a 99.6%-authored entry, "
    "and still lands 71st of 10,957 \u2014 a Roomba with a GitHub "
    "account and $0 to show for it."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT") or os.environ.get("OUTPUT_PATH") \
        or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
