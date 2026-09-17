# Checking a citation yourself

This folder lets you check, without taking the AI's word for it, that a citation in a report is real: that the article/paragraph it names actually exists, and that the quoted text genuinely appears where the report says it does.

You don't need to know how to code to use it.

## What you need

Python installed on your computer (a one-time setup, free, from [python.org](https://python.org) — search "how to install Python on Windows" if you've not done it before).

## How to run it

1. Open `check.bat` in this folder — either **double-click it**, or **drag a findings file and drop it onto `check.bat`**.
2. If you double-clicked without dragging a file, it'll ask you to type or paste the file path.
3. It prints `PASS` or `FAIL` for each citation it checks. If something fails, it shows you exactly what it expected to find and what's actually there, so you can judge for yourself.
4. Press any key to close the window when you're done.

## What file to check

Every audit produces two files: the PDF report you read, and `findings.txt` sitting alongside it — a plain-text list of every citation in the report, already in the format this checker needs. Drag `findings.txt` straight onto `check.bat`. No typing anything out yourself.

`findings.txt` looks like this, one block per finding:

```
CITATION: articles/art-13-info-collected-from-subject.md:19
QUOTE: the period for which the personal data will be stored
```

If you only want to check one or two specific findings rather than the whole report, you can also make your own small file in this format — copy the article citation from the report, open the matching file in `reference/articles/` or `reference/recitals/` to find the exact line, and quote its wording.

## What this is, and isn't

This is a way to independently confirm a citation is real, separate from the AI's own built-in self-check (described in the main `README.md`). It's not part of running a normal audit — you never need this to get a report. It exists for anyone who wants to verify a finding themselves rather than take it on trust.

Two ready-made examples are in `test-cases/`: `correct-citation.md` (should print PASS) and `broken-citation.md` (deliberately wrong, should print FAIL and show you what a caught mistake looks like).

## If you're comfortable with a terminal

`check.bat` is just a wrapper. The underlying script is `check.py`, and it runs the same way directly:

```
python check.py test-cases/correct-citation.md
```

Same output, same exit code (0 if every citation passes, 1 if any fail) — use whichever interface you prefer.
