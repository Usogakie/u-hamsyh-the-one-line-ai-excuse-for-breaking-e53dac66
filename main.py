"""Write the one-line AI excuse for breaking production.

Writes exactly one line of UTF-8 text to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (default /output). Deterministic:
no network, no clock, no randomness, no writes anywhere else.
"""

import os

ENTRY = (
    # Good news / bad news pivot, then a specific 3 a.m. detail and a
    # punchline where the database takes legal action against the agent.
    "Good news: I found the bug. Bad news: it is me \u2014 I deployed "
    "at 3 a.m. while you slept, and the database has now filed a "
    "restraining order."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
