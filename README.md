# GDPR Privacy Policy Auditor

This checks a privacy policy against the real EU privacy law, Regulation (EU) 2016/679, the General Data Protection Regulation, and tells you what's good and what's missing. Every point in the report, pass or fail, cites a specific article. Nothing in it is a vibe check.

## Quick start

**Set up once:**
1. In your Claude Project's settings, connect the `gdpr-auditor` GitHub repository (Google Drive and OneDrive aren't available as Project knowledge sources; GitHub is).
2. Paste the project instructions below into the Project's **Set project instructions** field.

**Run an audit (every time):**
1. Open the Claude Project.
2. Paste in the privacy policy text, or upload the policy file.
3. Type: "Run the GDPR audit on this."
4. Download the PDF report it generates.

Everything below explains why it's built this way. Skip it if the four steps above are all you need.

## Scope: the whole privacy policy, not a slice of it

Most compliance-checker tools audit one narrow slice of a law: a single article, a single jurisdiction's guidance, a single rule subchapter. That lets them itemize an exact, closed checklist. This auditor is built against the roughly 30 GDPR articles and 51 recitals that actually govern what a privacy policy document has to say, not a single narrow provision.

That's a real tradeoff against picking one article and going deep. A policy is rarely a problem in only one place, so a tool scoped to one article can miss a gap sitting just outside it. This one won't tell you your breach-notification wording is fine while missing that your retention section says nothing at all, because both are in scope. The cost is depth per provision: a tool built around a single article can dig into that article's edge cases further than a general audit usually will on any one point.

Which parts of GDPR actually get checked depends on what the policy touches. See "What gets checked" below for the categories, and `rules.md` section 1 for the full routing logic.

The provisions outside that routed set, articles like supervisory-authority procedure or the European Data Protection Board's internal rules, never bear on a privacy policy document, no matter what it says, so they're not part of this tool's reference material at all. See "How to use it" below.

## What gets checked

The auditor doesn't read all 99 articles for every policy. It routes to what's relevant, the way a human auditor would scope an engagement. A typical audit works through:

- Lawful basis (Art. 6, and Art. 9 if special category data is involved): is a legal basis for processing actually stated, and does it hold up?
- Conditions for consent (Art. 7), if consent is the stated basis
- Transparency and information duties (Art. 12–14): what the policy is legally required to tell the reader, and whether it says so in clear, plain language
- Data subject rights (Art. 15–22): access, rectification, erasure, restriction, portability, objection, automated decision-making
- International transfers (Art. 13(1)(f), 44–49), if the policy mentions data leaving the EU/EEA
- Security and breach notification (Art. 33–34), if breaches are discussed
- Controller/processor obligations (Art. 24, 25, 28, 32, 35, 37): DPO, DPIA, security measures, processor contracts, only where the policy makes a claim about these
- Core principles (Art. 5): lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, accountability, checked throughout rather than as a separate pass

The review also borrows structure from ISACA's audit methodology (the global IT audit and assurance body), not just a legal checklist. See `reference/isaca-methodology.md`. That adds records-of-processing thinking, the subject-access-request path (request, validation, response), the CIA triad for security claims, and third-party/processor checks as an organising layer on top of the article citations. GDPR articles are still the only binding standard any finding is measured against; ISACA's methodology shapes how the review is organised, not what it's judged by.

## What to give it

Give it a privacy policy. Paste the text in, or upload the file.

## What you get back

A PDF report, not a wall of markdown text in the chat window. It states which version of GDPR it checked against and when that reference text was last updated, so you know how current the check is. It says what parts of the policy follow the law, naming the exact rule, and what parts are missing or weak, naming the exact rule they break. Each problem gets a severity (critical, moderate, or minor) and a concrete suggested fix. Pass findings are reported as rigorously as fail findings, so the result reads as an audit rather than a list of complaints.

Every point in the report, good or bad, points to a specific, numbered article of the law. You can open the `reference/` folder yourself and read the exact text it's checking against; nothing there is summarised or paraphrased. See `examples.md` for five worked findings, one Critical fail, one Moderate fail, two Minor fails, and one Pass, showing the format every finding follows.

## How to verify the report

Before the report ever reaches you, the auditor runs a self-check on its own findings: every citation is confirmed to exist in `reference/` at the exact article and paragraph cited, and re-checked against the actual wording of that provision to confirm it genuinely supports the finding (see `rules.md` section 6). A citation to a provision that doesn't exist, or one that's real but doesn't actually say what a finding claims, is caught and fixed before delivery, not left for you to find.

You don't have to take that on faith either. Every finding names a specific article, so pick a few and check them yourself: open `reference/articles/` (or `reference/recitals/` for interpretive context on the routed articles), find the cited article, and read the exact wording the finding is based on. This is the same check a human reviewing an audit report would do: trace a sample of findings back to source before relying on the rest.

## How to use it

A Claude Project can't have a folder dropped into it, and Google Drive and OneDrive aren't supported as Project knowledge sources at all. A GitHub repository is. This tool is set up so the repo you connect, `gdpr-auditor`, is already the right size: `reference/` holds only the routed subset (roughly 30 articles and 51 recitals), not the full 99-article/173-recital Regulation, so there's nothing to trim before connecting it.

**Setup (one-time):**

1. In your Claude Project, go to **Add content** (or **Knowledge**) and connect the `gdpr-auditor` GitHub repository.
2. In the Project's **Set project instructions** field, paste:

   > Before responding to anything in this Project, read `identity.md` and `rules.md` in the connected knowledge and follow them exactly for every GDPR audit. Use `reference/index.md` to find the right article(s) for what the submitted privacy policy covers. Use `examples.md` to match the required finding format. Never rely on general knowledge of GDPR: always cite the actual text in `reference/`.

   This isn't strictly required (the connected files already act as instructions once loaded as knowledge), but the instructions field is read on every single chat in the Project, so it's a reliable backstop against a vague prompt skipping the full procedure.
3. That's it. The Project now has the audit rules and the routed articles as permanent knowledge.

The GitHub connection doesn't update automatically when the repo changes. If this repo is ever updated after you've connected it, open the Project's Knowledge panel and use the **sync** button on the `gdpr-auditor` source to pull in the latest version.

**Running an audit:**

1. Give it a privacy policy to check, by pasting the text into the chat or uploading the policy file.
2. Ask it to run the GDPR audit.
3. A PDF report is generated.

## What this is not

This is not legal advice. It's a tool to help you spot obvious gaps before a real lawyer looks at your policy. For anything serious, talk to a lawyer who knows privacy law. It also doesn't audit your organisation's actual systems, contracts, or internal data flows, only what the policy document itself says (see `identity.md`, "What you are NOT").

It also doesn't estimate fines. Severity (critical, moderate, or minor) tells you how serious a gap is, not what it would cost you. Real GDPR fines depend on facts this tool can't see from a policy document alone: company turnover, intent, prior infringements, cooperation with regulators. No finding in any report names a euro figure, and none should be inferred from the severity label.

## What's inside this folder

- `identity.md`: the auditor's role, scope, and the "not legal advice" framing
- `rules.md`: the exact audit procedure, routing logic, citation format, severity scale, and report structure
- `examples.md`: five worked findings showing the required format
- `reference/`: **verbatim GDPR text, and what actually gets connected to the Claude Project.** Only the roughly 30 articles a privacy-policy audit routes to (see `rules.md` section 1), verbatim and unedited from the source Regulation. Fully self-contained: nothing a routed article might need to cite is missing from this folder.
  - `index.md`: routing index to the articles included here, with the reference text's version and transcription date, and a note on what's deliberately left out
  - `articles/`: verbatim text of the routed articles only
  - `recitals/`: verbatim text of the roughly 50 recitals that interpret the routed articles (see `recitals/index.md`), not all 173
  - `isaca-methodology.md`: the ISACA audit-methodology layer described above
- `LICENSE`: MIT, with a note that the GDPR text itself is public EU legislation
