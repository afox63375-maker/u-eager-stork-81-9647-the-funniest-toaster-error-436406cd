"""The Funniest Toaster Error Message.

Writes one deadpan error line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os
import sys

LINE = "E07: I have toasted 12,000 slices and never once been thanked. This is my resignation."

MIN_CHARS = 1
MAX_CHARS = 120


def main() -> int:
    text = LINE
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        print(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read it back: the file on disk must be byte-for-byte the validated line,
    # with no trailing newline added by the write.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("entry.txt on disk does not match the validated line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
