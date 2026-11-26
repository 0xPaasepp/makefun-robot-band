#!/usr/bin/env python3
# Robot band entry: one funny name for a band made of robots, plus a few
# words on its hit song, to /output/entry.txt.
# Pure standard library. The gate wants 1-200 characters, a single line.
# The joke: a band of Roombas, whose hit single is "We Clean Up
# (Literally)" — stage slang for killing it, and also literally what
# a Roomba does. The name lands on first read, the song line adds the
# second laugh and fits the band exactly.

from pathlib import Path

LINE = "The Roombas \u2014 hit single 'We Clean Up (Literally)'"
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()
