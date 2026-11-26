#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt.

The Comment Above the Code (make.fun): one funny, painfully honest line
imagining the comment a developer left above fragile production code.
"""

import os

ENTRY = "// The last person who understood this function left in 2019. It has not been touched since. Neither has the bug."

# The gate allows 1 to 200 characters, a single line, and no trailing
# newline: keep the entry exactly as written, and fail loudly rather
# than silently shipping a line the judge will never see.
MAX_CHARS = 200


def validate(entry: str) -> None:
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} cap")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
