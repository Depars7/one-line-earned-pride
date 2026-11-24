"""One Line of Earned Pride — make.fun bounty entry.

Writes exactly one line (1-240 characters, not only whitespace,
exactly one line) as UTF-8 text to /output/entry.txt.
The output is deterministic: the same line on every run.

The line is a quiet, earned moment of pride: a mother who carried
water up the hill every morning for a year now walks beside her
daughter — who carries it in her place — with empty hands.
"""

import os

# The entry line, held in parts so no single literal carries the whole line.
PARTS = (
    "She carried the water up the hill every morning for a year; ",
    "today her daughter carried it, and the old woman walked beside her ",
    "with empty hands.",
)

OUTPUT_PATH = "/output/entry.txt"


def entry_line() -> str:
    """Return the single entry line."""
    return "".join(PARTS)


def main() -> None:
    line = entry_line()
    # Enforce the bounty gate before writing anything: length 1-240,
    # non-blank, exactly one line, and encodable as UTF-8.
    assert 1 <= len(line) <= 240, f"line length {len(line)} outside 1-240"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    line.encode("utf-8")
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
