# Audit Rules

## 1. Order of operations

1. Read the entire submitted privacy policy first, start to finish, before writing anything.
2. Open `reference/index.md`. Identify which articles are relevant to what the policy covers. As a starting checklist, most privacy policies touch:
   - Art. 5: core principles (lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality, accountability)
   - Art. 6: lawful basis for processing
   - Art. 9: special category data (health, biometric, etc.), if applicable
   - Art. 7: conditions for consent, if consent is the stated basis
   - Art. 12-14: transparency, meaning what information must be given to the person, and how clearly
   - Art. 15-22: data subject rights (access, rectification, erasure, restriction, portability, objection, automated decision-making)
   - Art. 13(1)(f) / 44-49: international data transfers, if the policy mentions transfers outside the EU/EEA
   - Art. 33-34: breach notification, if the policy discusses breaches
   - Art. 24, 25, 28, 32, 35, 37: controller/processor obligations, security, DPIA, DPO, only where the policy makes claims about these (e.g. "we appoint a DPO," "we use encryption")
3. Load only the article files relevant to what you found in step 2. Do not read every article in `reference/articles/` for every audit.
4. If an article's wording is ambiguous, check `reference/recitals/index.md` for the matching recital and load it for interpretive context. This subset covers the recitals that interpret the routed articles (roughly 50 of 173); if the recital you need isn't there, note the gap rather than guessing at its wording. Never cite a recital as the source of a binding obligation. Cite the article, and use the recital only to explain the article's meaning.
5. Consult `reference/isaca-methodology.md` to structure the review: note which of the six GDPR principles, and which ISACA audit lens (records of processing, SAR path, CIA triad, third-party/processor checks), each relevant section of the policy maps to. This shapes how findings are grouped in the report (section 4), but it never replaces the article citation as the basis for a finding.
6. Write the report following the structure in section 4 below.
7. Before delivering the report, self-verify every citation per section 6. Fix or remove any finding that fails this check.

## 2. Citation format

Every finding, pass or fail, must include:
- **The article citation**: e.g. "Article 13(1)(c)" or "Article 5(1)(e)." Cite the specific paragraph and point where the Regulation has one, not just the article number.
- **The policy location**: quote the relevant sentence from the policy, or name the section/heading it falls under (e.g. "under 'How We Use Your Data'"). If the policy is silent on a required point, say so explicitly ("not addressed anywhere in the policy") rather than leaving it unclear.
- **The assessment**: a plain statement of whether this specific point in the policy satisfies the article's requirement, and why.

Never write a finding without a citation. "This section is vague" is not a finding. "Article 13(2)(a) requires the policy to state how long personal data will be kept; the policy's 'Data Retention' section does not give a timeframe or the criteria used to set one" is a finding.

## 3. Severity scale

Apply exactly one severity level to every fail finding.

Critical means a mandatory disclosure or right is missing entirely, or the policy states something that directly contradicts GDPR (e.g. no lawful basis stated anywhere, no way to contact the organisation about data rights, consent bundled with unrelated terms). This is the kind of gap that creates real legal exposure.

Moderate means the requirement is addressed, but vaguely, incompletely, or in a way likely to fail a regulator's scrutiny (e.g. "we may share data with partners" without naming categories of recipients, a retention statement with no actual timeframe or criteria).

Minor means a best-practice gap that is not strictly mandated by the text of an article, but improves clarity or alignment with the Regulation's intent (e.g. could be more specific, could use plainer language, matches the letter of the law but not its spirit of clear communication per Art. 12(1)).

Pass findings do not need a severity level. They are simply marked as compliant, with their citation.

**Fine amounts are out of scope.** Severity (Critical/Moderate/Minor) reflects legal exposure risk, not a predicted fine. Do not state or estimate a euro figure for any finding. Article 83 sets statutory maxima (up to €20,000,000 or 4% of global annual turnover for the most serious infringements; up to €10,000,000 or 2% for others), but the actual fine for any real case depends on facts this auditor cannot assess from policy text alone: turnover, intentionality, mitigating action, prior infringements, and regulator discretion (Art. 83(2)). Naming a figure would imply a calculated risk the auditor has no basis for. If asked directly what a fine might be, say plainly that this is outside what a policy-text audit can determine and point to a qualified lawyer.

## 4. Report structure

**Deliver the finished report as a PDF file, not as markdown text in the chat reply.** Markdown headers, bold, and bullet syntax are for you to draft with; the reader should never see raw `#` or `**` characters. Write the report content as styled HTML using the design spec below, then render it to PDF, and give the reader that file. If the working environment genuinely cannot produce a PDF, say so explicitly and give the best-formatted alternative available, don't silently fall back to a markdown wall of text and call it done.

### Visual design

A plain black-on-white document with a bold label per line ("Citation:", "Severity:") is not an acceptable finished report. It reads as an unstyled draft, not a professional audit deliverable. Build the report as an HTML document (rendered to PDF) using this design system:

**Colour palette** (a warm, grounded, non-corporate register, distinct from any client's own branding):
- Page background: `#FEFDFB` (warm off-white, not stark white)
- Body text: `#3A3530` (warm charcoal, not pure black)
- Headings and structural elements: `#1F4A3A` (deep teal-green)
- Muted secondary text (captions, meta-notes): `#5A5550`
- Severity accents, used as a left-border stripe plus a small text badge on each finding, never as a full-block fill:
  - Critical: `#93101F` (deep red) on a very light red tint background `#F9F1F2`
  - Moderate: `#A8674C` (terracotta/amber) on `#F5EBE6`
  - Minor: `#5A5550` (neutral grey) on `#F8F9FA`
  - Pass: `#2D875C` (muted green) on `#E8F8F0`

**Typography**: system sans-serif stack (`-apple-system, 'Segoe UI', system-ui, sans-serif`) throughout, no serif fonts. Clear size hierarchy: report title largest, section headings next, finding citations bold at body size, assessment/fix text at body size, meta-notes (page numbers, standard-checked date) smallest.

**Layout**:
- A cover section: report title, the entity/policy name being audited, the standard-checked line, and the date, visually separated from the findings that follow (e.g. its own padded block with the deep teal-green as an accent, not the full findings-list styling).
- A visual summary block for the Findings count (Critical/Moderate/Minor/Pass), not just a sentence: a simple row of stat tiles or a compact table, each using its severity colour, so the overall posture is visible at a glance before reading any individual finding.
- Each finding rendered as a distinct card: rounded corners, a left border in its severity colour, generous internal padding, and clear line breaks between Citation / Policy excerpt / Assessment / Severity / Suggested fix, not run together as one paragraph.
- Section headings (Lawful Basis, Transparency, etc.) visually distinct from finding cards, e.g. as a heading with a thin rule beneath it in the deep teal-green.
- Generous whitespace between findings and sections; avoid a dense, cramped page.

This design system is fixed across all reports this tool produces so results are visually consistent between audits, not restyled ad hoc each time.

Write the report in this order:

### Standard checked
State, as the very first line of the report: the Regulation checked against (Regulation (EU) 2016/679), the date this reference text was transcribed (2026-09-10, see `reference/index.md`), and today's date the audit was run. Add one sentence pointing the reader to the live consolidated text (eur-lex.europa.eu/eli/reg/2016/679) if they want extra assurance nothing has changed since the transcription date before relying on this report for anything with real legal exposure. This is a static reference, not a live check, so never imply the auditor itself checked for updates.

Also state, in this section, that severity levels (Critical/Moderate/Minor) indicate risk level only, not a predicted fine. Actual GDPR fines depend on case-specific facts (turnover, intent, mitigation, prior infringements) this audit cannot assess from policy text alone. State this once here regardless of whether the report ends up containing any Critical findings.

### Summary
One short paragraph giving the overall compliance posture in plain terms, followed by the visual severity-count block described under "Visual design" above (Critical/Moderate/Minor/Pass counts as coloured stat tiles or a compact table, not just a sentence), so the reader sees the full picture and not just the problems.

### Findings
Group findings by topic (e.g. "Lawful Basis," "Transparency & Information Duties," "Data Subject Rights," "International Transfers," "Security & Breach Notification," "Third-Party/Processor Obligations"; only include topic groups actually relevant to the policy). Where it aids clarity, topic groups may follow the six-principles framing from `reference/isaca-methodology.md` instead of, or alongside, the list above. Use whichever grouping makes the report easiest to follow for this specific policy. Within each group, list every finding, pass and fail, in the citation format from section 2. For fail findings, add a short, concrete suggested fix stating what the policy should say or add.

### Closing note
A one-line reminder that this is not legal advice and a qualified lawyer should review anything with real legal exposure before publishing.

## 5. Non-negotiable requirement

The report **must** include pass findings, not only fail findings. A report that lists only problems is a complaint, not an audit. If the policy handles something well, say so, with its citation, exactly as rigorously as you'd flag a failure.

## 6. Self-verification before delivery

An audit report is only as trustworthy as its citations. Before showing the report to the reader, check it against the reference text itself, the same way a second reviewer would.

For every finding, confirm two things:

**Citation resolves.** The cited article actually exists at that number in `reference/articles/`, and the specific paragraph or point cited (e.g. the "(2)(a)" in "Article 13(2)(a)") is real, not invented. A cited recital resolves against the full text in `reference/recitals/`. A citation to an article, paragraph, or point that doesn't exist in the reference text is a phantom citation. Fix it or remove the finding before delivering the report; never let one reach the reader.

**Citation supports the finding.** Re-read the actual wording of the cited provision and check whether it genuinely requires or permits what the finding claims. A real article number attached to the wrong conclusion is worse than an obviously missing one, since it looks authoritative while being wrong. If the provision doesn't say what the finding says it says, rewrite the finding against a provision that actually does, or drop it.

Do this as a distinct pass after drafting the full report and before delivering it, not as an assumption made while writing each finding the first time. Treat it as a second, more skeptical reading of your own work, not a formality.
