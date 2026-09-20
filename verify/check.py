#!/usr/bin/env python3
"""
Independent citation checker for GDPR Auditor.

Not part of the audit workflow. A real audit runs entirely inside a Claude
Project chat and never calls this script. This exists so a skeptical reader
(a competition judge, or Yasuko spot-checking a report) can verify, by
running actual code rather than trusting the AI's own self-report, that
every citation in a findings file resolves to a real line in reference/ and
that the quoted text genuinely appears there.

Every audit produces findings.txt alongside the PDF report, already in the
format below -- that's the normal input to this script. It's never shown
in the report itself (rules.md section 2); it exists purely so this script
can check it.

Usage:
    python check.py <findings-file.md>

A findings file is a plain-text/markdown file containing one or more
citation blocks in this form:

    CITATION: articles/art-13-info-collected-from-subject.md:19
    QUOTE: the period for which the personal data will be stored

Before checking any citation, the script also verifies every file listed in
reference/checksums.sha256 still matches its recorded SHA-256 hash. This
confirms the reference text itself has not drifted since it was transcribed,
independent of whether any individual citation is correct. A citation can
only be trusted if the file it points at is provably the same file that was
checksummed.

The script checks, for each block:
  1. reference/ passes the checksum verification above.
  2. The file exists under reference/.
  3. The line number exists in that file.
  4. The quoted text appears at that line, or within a small window around
     it (provisions often wrap across lines when transcribed as prose).

On any failure it prints the citation, the line actually found there, and
exits non-zero. It never modifies reference/ or the findings file.
"""

import hashlib
import re
import sys
from pathlib import Path

REFERENCE_ROOT = Path(__file__).resolve().parent.parent / "reference"
CHECKSUM_FILE = REFERENCE_ROOT / "checksums.sha256"
LINE_WINDOW = 2  # lines above/below the cited line also checked, since a
                  # quote can span a wrapped sentence rather than sit on
                  # the exact cited line alone.


def verify_checksums():
    if not CHECKSUM_FILE.exists():
        return False, [f"checksum file not found: {CHECKSUM_FILE}"]

    problems = []
    checked = 0
    for line in CHECKSUM_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        expected_hash, _, rel_path = line.partition(" *")
        if not rel_path:
            expected_hash, _, rel_path = line.partition("  ")
        rel_path = rel_path.strip()
        target = REFERENCE_ROOT / rel_path
        checked += 1
        if not target.exists():
            problems.append(f"missing file listed in checksums.sha256: reference/{rel_path}")
            continue
        actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual_hash != expected_hash.strip():
            problems.append(
                f"checksum mismatch: reference/{rel_path}\n"
                f"    expected: {expected_hash.strip()}\n"
                f"    actual:   {actual_hash}"
            )

    if problems:
        return False, problems
    return True, [f"{checked} file(s) match their recorded checksum."]

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

    print("Checking reference/ against checksums.sha256...")
    checksums_ok, checksum_messages = verify_checksums()
    for message in checksum_messages:
        print(("PASS  " if checksums_ok else "FAIL  ") + message)
    print()
    if not checksums_ok:
        print("reference/ does not match its recorded checksums. Citations cannot be trusted until this is resolved.")
        sys.exit(1)

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
