# GDPR Privacy Policy Auditor

Checks a privacy policy against the real EU law, Regulation (EU) 2016/679 (GDPR), and tells you what's good and what's missing. Every point in the report, pass or fail, cites a specific article. Nothing in it is a vibe check.

## Prerequisites

The core audit (search-based citation checking) only needs a Claude Project with the `gdpr-auditor` repository connected as a knowledge source, and a public GitHub repository (it is: `github.com/y4suko1/gdpr-auditor`).

The stronger clone-and-verify check described below is optional and needs more: **code execution enabled in the Project, and network access to github.com allowed.** As of the current Claude release, code execution is a per-Project toggle under the Project's **Settings → Capabilities**. Organisations can restrict either this or github.com access. If your Project doesn't have both, the auditor still runs the full audit; it just can't clone the repository to check citations against the frozen release text, and will tell you so plainly in the report rather than pretending it did.

## Quick start

**Set up once:**
1. In your Claude Project's settings, connect the `gdpr-auditor` GitHub repository as a knowledge source.
2. Paste this into the Project's **Set project instructions** field:

   > Before responding to anything in this Project, read `identity.md` and `rules.md` in the connected knowledge and follow them exactly for every GDPR audit. Use `reference/index.md` to find the right article(s) for what the submitted privacy policy covers. Use `examples.md` to match the required finding format. Never rely on general knowledge of GDPR: always cite the actual text in `reference/`.
   >
   > Before delivering any report, if code execution and network access to github.com are available in this session, follow `rules.md` section 7: clone `github.com/y4suko1/gdpr-auditor` at tag `v1.1.1` and verify the companion `findings-[date].txt` file against it with `verify/check.py`. If code execution isn't available, or the clone fails, follow section 7's instructions for what to do next rather than silently skipping the check.

**Run an audit (every time):**
1. Open the Claude Project.
2. Paste in the privacy policy text, or upload the policy file.
3. Type: "Run the GDPR audit on this."
4. Download the PDF report it generates, plus a small `findings-[date].txt` file alongside it (see "How to verify the report" below).

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

Every finding in this report rests on two separate questions, and it helps to know which one has been checked mechanically and which one still needs a reader's judgement.

**Is the citation real?** Does "Article 13(2)(a)" actually exist, and does it say the words the finding quotes? Before you ever see the report, the tool checks this itself: every citation is confirmed against the exact article, paragraph, and line it points to (`rules.md` section 6). This is a fact check. It catches a made-up article number or a quote that doesn't actually appear where it's claimed to.

**Does the citation actually support the finding?** A real, correctly-quoted article can still be attached to the wrong conclusion: a citation that's accurate but pointed at the wrong argument. Checking this means reading the provision and judging whether it genuinely means what the finding says it means. The tool does this too, as a second, more sceptical read-through before delivering the report. But it's a judgement call, not something that can be confirmed by matching text. If you're relying on a finding for something with real exposure, read the cited article yourself in `reference/articles/` rather than trusting the citation on sight.

One line, plainly: the tool can prove a citation is real. It cannot prove, in a way you can independently confirm without reading the law yourself, that the citation's conclusion is the right one. Both checks matter. Only the first is mechanical.

If you want the technical detail on how the mechanical check runs, and how to re-run it yourself outside the chat, see [SETUP.md](SETUP.md).

## What this is not

Not legal advice. It's a tool to spot obvious gaps before a real lawyer looks at your policy. It doesn't audit your organisation's actual systems or contracts, only what the policy document says.
