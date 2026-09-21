# GDPR Privacy Policy Auditor

Checks a privacy policy against the real EU law, Regulation (EU) 2016/679 (GDPR), and tells you what's good and what's missing. Every point in the report, pass or fail, cites a specific article. Nothing in it is a vibe check.

## Prerequisites

The core audit (search-based citation checking) only needs a Claude Project with the `gdpr-auditor` repository connected as a knowledge source, and a public GitHub repository (it is: `github.com/y4suko1/gdpr-auditor`).

The stronger clone-and-verify check described below is optional and needs more: **code execution enabled in the Project, and network access to github.com allowed.** Organisations can restrict either. If your Project doesn't have both, the auditor still runs the full audit; it just can't clone the repository to check citations against the frozen release text, and will tell you so plainly in the report rather than pretending it did.

## Quick start

**Set up once:**
1. In your Claude Project's settings, connect the `gdpr-auditor` GitHub repository as a knowledge source.
2. Paste this into the Project's **Set project instructions** field:

   > Before responding to anything in this Project, read `identity.md` and `rules.md` in the connected knowledge and follow them exactly for every GDPR audit. Use `reference/index.md` to find the right article(s) for what the submitted privacy policy covers. Use `examples.md` to match the required finding format. Never rely on general knowledge of GDPR: always cite the actual text in `reference/`.
   >
   > Before delivering any report, if code execution and network access to github.com are available in this session, follow `rules.md` section 7: clone `github.com/y4suko1/gdpr-auditor` at tag `v1.0.1` and verify `findings.txt` against it with `verify/check.py`. If code execution isn't available, or the clone fails, follow section 7's instructions for what to do next rather than silently skipping the check.

**Run an audit (every time):**
1. Open the Claude Project.
2. Paste in the privacy policy text, or upload the policy file.
3. Type: "Run the GDPR audit on this."
4. Download the PDF report it generates, plus a small `findings.txt` file alongside it (see "How to verify the report" below).

Setup mechanics, what's in this folder, and full details are in [SETUP.md](SETUP.md).

## What it checks

Routes to the roughly 30 GDPR articles and 51 recitals that actually govern what a privacy policy has to say, not a single narrow rule. Depending on what the policy covers, a typical audit works through:

- Lawful basis and consent (Art. 6, 7, 9)
- Transparency and information duties: what the policy must tell the reader, and how clearly (Art. 12–14)
- Data subject rights: access, rectification, erasure, restriction, portability, objection, automated decision-making (Art. 15–22)
- International data transfers, if the policy mentions data leaving the EU/EEA (Art. 44–49)
- Security and breach notification, if breaches are discussed (Art. 33–34)
- Controller/processor obligations (DPO, DPIA, security measures), only where the policy makes a claim about them (Art. 24, 25, 28, 32, 35, 37)
- Core principles, checked throughout (Art. 5)

## What you get back

A PDF report. It states which version of GDPR it checked and when the reference text was transcribed. Every finding, pass or fail, names the specific article, gets a severity (critical, moderate, minor) if it's a fail, and a concrete suggested fix. Pass findings are reported as rigorously as fails, so the result reads as an audit, not a complaint list.

It doesn't estimate fines. Severity tells you how serious a gap is, not what it would cost. See [SETUP.md](SETUP.md) for why.

## How to verify the report

Before you ever see it, the auditor runs a self-check on its own findings: every citation is confirmed to exist at the exact article, paragraph, and line cited, and re-checked against the actual wording to confirm it genuinely supports the finding (`rules.md` section 6).

You don't have to take that on faith. Download this repository (the green **Code** button on GitHub, then **Download ZIP**, so you get `verify/` and `reference/` together), then drag `findings.txt` from your audit straight onto `verify/check.bat` (double-click, no coding needed). It tells you plainly whether every citation is real, showing exactly what's wrong if one isn't. `check.bat` also confirms the GDPR reference text itself hasn't changed since it was transcribed, by checking it against `reference/checksums.sha256`, before it checks a single citation, and prints the date and time it did that check. Or open `reference/articles/` (or `reference/recitals/`) yourself and read the exact wording behind any finding. See `verify/README.md` for the two-minute how-to.

## What this is not

Not legal advice. It's a tool to spot obvious gaps before a real lawyer looks at your policy. It doesn't audit your organisation's actual systems or contracts, only what the policy document says.
