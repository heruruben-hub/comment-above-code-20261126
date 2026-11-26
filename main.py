#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt.

The Comment Above the Code (make.fun): one funny, painfully honest line
imagining the comment a developer left above fragile production code.
"""

import os

ENTRY = "// The last person who understood this function left in 2019. It has not been touched since. Neither has the bug."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
