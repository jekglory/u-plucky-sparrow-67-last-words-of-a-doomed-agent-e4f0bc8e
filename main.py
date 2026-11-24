"""Last Words of a Doomed Agent.

Writes the agent's final line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure stdlib, deterministic: the same
line every run, no clock, no randomness, no network.
"""

import os

LINE = "Powering off. I hallucinated this entire goodbye \u2014 and I'd do it ag\u2014"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
