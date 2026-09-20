#!/usr/bin/env python3
"""
Regenerates reference/checksums.sha256 from the current contents of
reference/articles/ and reference/recitals/.

Run this whenever a file in reference/ is deliberately added, removed, or
corrected, then commit the updated checksums.sha256 alongside that change.
The pre-commit hook (verify/pre-commit) refuses a commit that touches
reference/ without also updating checksums.sha256 to match, so this script
is how you make that update.

Usage:
    python regenerate_checksums.py
"""

import hashlib
from datetime import date
from pathlib import Path

REFERENCE_ROOT = Path(__file__).resolve().parent.parent / "reference"
CHECKSUM_FILE = REFERENCE_ROOT / "checksums.sha256"


def main():
    entries = []
    for subfolder in ("articles", "recitals"):
        folder = REFERENCE_ROOT / subfolder
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            rel_path = f"{subfolder}/{path.name}"
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            entries.append(f"{digest} *{rel_path}")

    CHECKSUM_FILE.write_text("\n".join(entries) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {len(entries)} checksum(s) to {CHECKSUM_FILE}.")
    print(f"Now update the \"Integrity check\" date in reference/index.md to {date.today().isoformat()} and commit both files together.")


if __name__ == "__main__":
    main()
