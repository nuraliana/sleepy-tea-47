"""One Letter: Coffee or Tea — entry program (original CST work).

Writes exactly one letter, "B" (tea), and nothing else to
$MAKEFUN_OUTPUT_DIR/entry.txt: 1 byte, no trailing newline,
no word, no explanation, no punctuation. Python stdlib only.
"""

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(b"B")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
