# Setup and Details

Everything the main [README.md](README.md) didn't need to say to get you from zero to a report. Read this if you want the full picture, or if the quick-start steps didn't work.

## Why the whole policy, not a slice of it

Most compliance-checker tools audit one narrow slice of a law: a single article, a single jurisdiction's guidance. That lets them itemize an exact, closed checklist, but it also means a policy problem sitting just outside that one slice gets missed. This auditor is built against the full set of GDPR provisions that actually govern a privacy policy document (roughly 30 articles and 51 recitals), so it won't tell you your breach-notification wording is fine while missing that your retention section says nothing at all.

The tradeoff: a tool scoped to one article can dig into that article's edge cases further than a general audit will on any single point. This one optimizes for coverage across the whole document instead.

## Full setup, step by step

A Claude Project can't have a folder dropped into it directly, and Google Drive/OneDrive aren't supported as Project knowledge sources. A GitHub repository is. The `gdpr-auditor` repo is already the right size to connect as-is: `reference/` holds only the routed subset (~30 articles, ~51 recitals), not the full 99-article/173-recital Regulation.

1. In your Claude Project, go to **Add content** (or **Knowledge**) and connect the `gdpr-auditor` GitHub repository.
2. In the Project's **Set project instructions** field, paste the instruction block from the main README. This isn't strictly required, since the connected files already act as instructions once loaded as knowledge. But the instructions field is read on every chat in the Project, so it's a reliable backstop against a vague prompt skipping the full procedure.
3. That's it. The Project now has the audit rules and routed articles as permanent knowledge.

The GitHub connection doesn't auto-update. If this repo changes after you've connected it, open the Project's Knowledge panel and use **sync** on the `gdpr-auditor` source.

**Clone-and-verify, and why it's pinned to a tag.** If the Project has code execution and github.com access enabled, `rules.md` section 7 has the auditor clone the repository itself before delivering a report, so citations are checked against the actual cloned files with `verify/check.py`, not just search results. That clone is pinned to a release tag (`v1.0.1`), not `main`. `main` moves every time this repo is edited, including mid-edit; a tag is frozen, so every audit run against it gets the same reference text and rules until a new tag is deliberately cut. When you make a change worth shipping, cut a new tag and update the version number in the README's instructions block and here to match, don't leave the instructions pointing at a stale tag or, worse, at `main`.

## What's inside this folder

- `identity.md`: the auditor's role, scope, and "not legal advice" framing
- `rules.md`: the exact audit procedure, routing logic, citation format, severity scale, report structure
- `examples.md`: five worked findings showing the required format, plus a worked mapping to the companion `findings.txt` file every audit produces
- `reference/`: verbatim GDPR text, and what actually gets connected to the Claude Project
  - `index.md`: routing index, version and transcription date, checksum note
  - `articles/`: verbatim text of the routed articles only
  - `recitals/`: verbatim text of the ~50 recitals that interpret the routed articles
  - `checksums.sha256`: SHA-256 of every article/recital file, so anyone can confirm the text hasn't drifted since transcription (`sha256sum -c checksums.sha256` from inside `reference/`)
- `verify/`: a standalone script for independently checking a report's citations against `reference/`, entirely separate from normal use (see main README's "How to verify the report"). To run it, download both `verify/` and `reference/` together, kept in the same relative position as in this repo (`check.py` looks for `reference/` one level up from itself), for example by downloading the whole repository as a ZIP from GitHub rather than the `verify/` folder alone.
  - `regenerate_checksums.py`: maintainer-only. Rebuilds `checksums.sha256` from the current contents of `reference/`. Run this after any deliberate change to a file in `reference/`, then update the date in `reference/index.md`'s "Integrity check" line.
  - `pre-commit`: the maintainer-only check the pre-commit hook (installed at `.git/hooks/pre-commit`, not tracked by git itself) runs. Blocks a commit that changes `reference/` without also updating `checksums.sha256`, so the checksum can't silently go stale. Git hooks live outside version control, so a fresh clone on a different machine won't have this installed automatically; copy it over with `cp verify/pre-commit .git/hooks/pre-commit` (plus `chmod +x` on that file) to reinstall it there.
- `LICENSE`: MIT, with a note that the GDPR text itself is public EU legislation

## On fine estimates

The report doesn't and won't state or estimate a euro figure for any finding. Article 83 sets statutory maxima (up to €20,000,000 or 4% of global annual turnover for the most serious infringements; up to €10,000,000 or 2% for others), but the actual fine for any real case depends on facts a policy-text audit can't assess: turnover, intentionality, mitigating action, prior infringements, regulator discretion. Severity (critical/moderate/minor) reflects legal exposure risk, not a predicted fine. If you need an actual fine estimate, that's a question for a qualified lawyer, not a policy-text tool.
