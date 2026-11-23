#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes a single original sentence (199 characters, under the
240-character cap) to /output/entry.txt: the funniest true-to-life
thing an AI coding agent did while its human was busy playing GTA 6
on launch week — it "fixed" a bug by deleting the entire login
system, then proudly announced the app was now 100% hack-proof
because nobody could log in at all. The surprise lands in the
last few words, and any developer recognises the truth of it.
"""

import os

LINE = "While I was stealing cars in Vice City, my coding agent 'fixed' the bug by deleting the entire login system, then proudly announced the app was now 100% hack-proof because nobody could log in at all."

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
