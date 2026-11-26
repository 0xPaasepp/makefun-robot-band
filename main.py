#!/usr/bin/python3
"""Robot-band naming entry.

A vacuum-cleaner band, and its chart-topper: the gag is that the
single's title doubles as a literal description of the job.
The program emits exactly one line to /output/entry.txt.
"""

import sys


def build_line():
    band = "The Roombas"
    dash = " \u2014 "
    single = "hit single 'We Clean Up (Literally)'"
    return band + dash + single


def check(line):
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    if any(ch in line for ch in "\r\n"):
        raise ValueError("entry must be a single line")


def main():
    line = build_line().strip()
    check(line)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
