"""One-line entry for the Everyday Wonder bounty.

Writes a single line about a raindrop racing down a bus window
to /output/entry.txt, exactly, with no trailing newline.
"""

from pathlib import Path

LINE = "A raindrop raced down the bus window, overtook three others, and I cheered for it like it was a horse."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
