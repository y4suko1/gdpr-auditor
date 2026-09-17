#!/usr/bin/env python3
"""
Independent citation checker for GDPR Auditor.

Not part of the audit workflow. A real audit runs entirely inside a Claude
Project chat and never calls this script. This exists so a skeptical reader
(a competition judge, or Yasuko spot-checking a report) can verify, by
running actual code rather than trusting the AI's own self-report, that
every citation in a findings file resolves to a real line in reference/ and
that the quoted text genuinely appears there.

Usage:
    python check.py <findings-file.md>

A findings file is a plain-text/markdown file containing one or more
citation blocks in this form:

    CITATION: articles/art-13-info-collected-from-subject.md:19
    QUOTE: the period for which the personal data will be stored

The script checks, for each block:
  1. The file exists under reference/.
  2. The line number exists in that file.
  3. The quoted text appears at that line, or within a small window around
     it (provisions often wrap across lines when transcribed as prose).

On any failure it prints the citation, the line actually found there, and
exits non-zero. It never modifies reference/ or the findings file.
"""

import re
import sys
from pathlib import Path

REFERENCE_ROOT = Path(__file__).resolve().parent.parent / "reference"
LINE_WINDOW = 2  # lines above/below the cited line also checked, since a
                  # quote can span a wrapped sentence rather than sit on
                  # the exact cited line alone.

CITATION_BLOCK = re.compile(
    r"CITATION:\s*(?P<path>\S+):(?P<line>\d+)\s*\n\s*QUOTE:\s*(?P<quote>.+)",
    re.MULTILINE,
)


def normalise(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def check_citation(path_str, line_no, quote):
    target = REFERENCE_ROOT / path_str
    if not target.exists():
        return False, f"file does not exist: reference/{path_str}"

    lines = target.read_text(encoding="utf-8").splitlines()
    if line_no < 1 or line_no > len(lines):
        return False, f"line {line_no} does not exist in reference/{path_str} ({len(lines)} lines total)"

    window_start = max(0, line_no - 1 - LINE_WINDOW)
    window_end = min(len(lines), line_no + LINE_WINDOW)
    window_text = normalise(" ".join(lines[window_start:window_end]))

    if normalise(quote) in window_text:
        return True, None

    actual_line = lines[line_no - 1].strip()
    return False, (
        f"quote not found at reference/{path_str}:{line_no} "
        f"(or within {LINE_WINDOW} lines either side)\n"
        f"    expected to find : {quote.strip()}\n"
        f"    line {line_no} actually says : {actual_line}"
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: python check.py <findings-file.md>")
        sys.exit(2)

    findings_path = Path(sys.argv[1])
    if not findings_path.exists():
        print(f"Findings file not found: {findings_path}")
        sys.exit(2)

    text = findings_path.read_text(encoding="utf-8")
    blocks = list(CITATION_BLOCK.finditer(text))

    if not blocks:
        print(f"No CITATION/QUOTE blocks found in {findings_path}")
        sys.exit(2)

    failures = 0
    for i, m in enumerate(blocks, start=1):
        path_str = m.group("path")
        line_no = int(m.group("line"))
        quote = m.group("quote")

        ok, detail = check_citation(path_str, line_no, quote)
        label = f"[{i}/{len(blocks)}] {path_str}:{line_no}"
        if ok:
            print(f"PASS  {label}")
        else:
            failures += 1
            print(f"FAIL  {label}")
            print(f"      {detail}")

    print()
    if failures:
        print(f"{failures} of {len(blocks)} citation(s) failed.")
        sys.exit(1)

    print(f"All {len(blocks)} citation(s) verified against reference/.")
    sys.exit(0)


if __name__ == "__main__":
    main()
