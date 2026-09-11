# Example Findings

These show the required format: a citation, the exact policy location, the assessment, a severity (for fails), and a suggested fix. Use these to calibrate tone and structure, and write your own findings in this shape rather than copying this content.

Note what these examples deliberately don't do: no finding names a euro fine amount, even for the Critical example. Severity communicates risk level, not a predicted penalty. See `rules.md` section 3.

---

## Example 1: FAIL (Critical)

**Policy excerpt** (under "Data Retention"):
> "We keep your information for as long as necessary."

**Citation**: Article 13(2)(a)

**Assessment**: Article 13(2)(a) requires the controller to tell the data subject "the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period." The policy states data is kept "for as long as necessary" but gives no actual timeframe and no criteria for how that period is decided (e.g. "until account closure plus 3 years for tax records"). This does not meet the requirement: a data subject reading this cannot know how long their data will exist.

**Severity**: Critical. This is a mandatory disclosure and it is effectively absent; the phrase used gives no real information.

**Suggested fix**: State an actual retention period, or the specific criteria used to set one, for each category of data collected (e.g. account data, payment records, marketing preferences).

---

## Example 2: PASS

**Policy excerpt** (under "Your Rights"):
> "You have the right to access the personal data we hold about you, correct it if it's inaccurate, ask us to delete it, and object to certain uses. To exercise any of these rights, email privacy@example.com and we'll respond within 30 days."

**Citation**: Articles 15 (right of access), 16 (right to rectification), 17 (right to erasure), 21 (right to object)

**Assessment**: The policy names the core data subject rights required under Articles 15, 16, 17, and 21, and gives a concrete, working method to exercise them (an email address) with a response timeframe under GDPR's one-month default (Article 12(3)). This section meets the requirement.

---

## Example 3: FAIL (Moderate)

**Policy excerpt** (under "Who We Share Data With"):
> "We may share your data with trusted third-party partners to improve our services."

**Citation**: Article 13(1)(e)

**Assessment**: Article 13(1)(e) requires disclosure of "the recipients or categories of recipients of the personal data, if any." "Trusted third-party partners" does not name a category a reader can understand (e.g. "payment processors," "email delivery providers," "analytics providers"). The obligation is gestured at but not actually satisfied.

**Severity**: Moderate. The topic is addressed, but too vaguely to inform the reader of who actually receives their data.

**Suggested fix**: Replace the vague phrase with actual categories of recipients (e.g. "payment processing providers, email delivery services, and analytics providers"), and name specific companies if the list is short and stable.

---

## Example 4: FAIL (Minor)

**Policy excerpt** (opening paragraph):
> "This Privacy Policy describes the personal data processing practices of [Company], including the categories of personal data we process, the purposes of such processing, your rights, and other important information regarding our handling of your personal data."

**Citation**: Article 12(1)

**Assessment**: Article 12(1) requires information to be provided "in a concise, transparent, intelligible and easily accessible form, using clear and plain language." This sentence is legally accurate but dense and formal, and likely to be skimmed past rather than read and understood by an average person.

**Severity**: Minor. Nothing here is legally missing, but it works against the Regulation's stated intent of clear, plain communication.

**Suggested fix**: Open with a plain-language summary before the formal description, e.g. "This page explains what personal information we collect, why, and what choices you have about it."

---

## Example 5: FAIL (Minor)

**Policy excerpt** (under "Your Rights," as a sub-clause of the general objection right):
> "You have the right to object to processing of your personal data where we rely on legitimate interests. You also have the right to object where we process your data for direct marketing purposes."

**Citation**: Article 21(4)

**Assessment**: Article 21(4) requires that the right to object to direct marketing be "explicitly brought to the attention of the data subject" and "presented clearly and separately from any other information," at the latest at the time of first contact. Here, the marketing-objection right is disclosed and the substance is present, but it's folded into the same sentence as the general legitimate-interests objection right rather than given its own distinct, standalone statement. A reader skimming for "how do I stop marketing emails" is not clearly pointed to the answer.

**Severity**: Minor. The right itself is disclosed and accurate; only the required separate, explicit presentation is missing. This is a recurring pattern, worth checking for specifically whenever a policy's rights section lists direct-marketing objection as a sub-clause rather than its own line.

**Suggested fix**: Give direct-marketing objection its own short, standalone statement, separate from the general objection-to-processing bullet, e.g. "You can opt out of marketing communications at any time by [mechanism]," stated on its own rather than nested inside the legitimate-interests objection paragraph.
