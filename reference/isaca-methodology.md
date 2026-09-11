# ISACA Audit Methodology (reference layer)

**Source**: ISACA, *How to Audit GDPR*, 2018 (co-published with ACL). This is secondary audit guidance, not GDPR itself, so never cite this file as the source of a binding legal obligation. Every finding still cites a GDPR article from `reference/articles/`. Use this file only to structure *how* the review is organised and grouped.

## The six principles as an audit checklist

GDPR Article 5(2) makes the controller "responsible for, and able to demonstrate compliance" with six principles (Article 5(1)). ISACA frames these as the top-level audit checklist:

1. Lawfulness, fairness and transparency
2. Purpose limitation
3. Data minimisation
4. Accuracy
5. Storage limitation
6. Integrity and confidentiality

Accountability (demonstrating compliance with the six) is sometimes mistaken for a seventh principle. It isn't: it's the controller's overarching duty to evidence compliance with the six above.

## Controller vs. processor

A **controller** determines the purposes and means of processing. A **processor** acts only on the controller's documented instructions (Article 28). This distinction is an audit lens: findings about who decides *why* data is processed belong to the controller, while findings about a third party handling data on the controller's behalf belong to the processor-oversight checks below.

## Records-of-processing audit approach (Article 30)

ISACA recommends assessing whether an enterprise maintains records of processing as the evidentiary backbone of compliance. In a privacy-policy audit, treat the presence or absence of processing detail in the policy itself (basis, purpose, retention, recipients) as a proxy for whether such records likely exist.

ISACA's recommended minimum fields for an information asset register:

- Collection date
- Legal basis under Article 6 (or Article 9 for special category data)
- Purpose
- Deletion date or retention period
- System(s) the data lives on
- Sharing details: who, what, when, and whether the data is EU-stored

When auditing a policy's "how we use your data" and "data retention" sections, check whether these fields are addressed at the level a data subject would need, not just at the level an internal register would need.

## The SAR path: Request → Validation → Response

ISACA frames a subject access request (SAR) as a three-stage process, useful as an audit unit when reviewing a policy's "your rights" section.

1. **Request**: how a data subject actually initiates a rights request. Is a contact method named, and does it work.
2. **Validation**: the policy should imply or state that identity is verified before data is disclosed, since disclosing to the wrong person is itself a breach.
3. **Response**: the one-month default response clock (Article 12(3)), and the requirement that the response be complete, accurate, and easily understandable, not just timely.

A policy that names a contact method but gives no timeframe, or gives a timeframe but no way to actually contact anyone, has an incomplete SAR path. Flag which stage is missing.

## CIA triad applied to the security principle (Article 5(1)(f))

ISACA maps the information-security triad onto Article 5(1)(f):

- **Confidentiality**: data is accessible only to those authorised to see it.
- **Integrity**: data is kept accurate and not silently duplicated or enriched beyond its stated purpose.
- **Availability**: data is available to authorised users, and to the data subject themselves. A SAR that can't be fulfilled within the response window is an availability failure, not just a process failure.

Use this triad when a policy makes security claims ("we use encryption," "we store data securely") to check whether all three angles are actually addressed, not just confidentiality.

## Third-party / processor audit checks (Article 28)

When a policy discusses sharing data with third parties or vendors, ISACA's audit lens asks:

- Are processors clearly distinguished from other recipients? Is it clear who acts on behalf of the controller versus who receives data for their own purposes?
- Does the policy give any indication that processors are contractually bound (Article 28 "sufficient guarantees," documented instructions)?
- Is breach notification coverage addressed if a processor is involved?

A policy that vaguely mentions "trusted partners" without distinguishing processors from independent recipients, or without any indication of contractual oversight, is a gap under this lens. Cite Article 28, and Article 13(1)(e)/(f) for the underlying transparency duty, for the finding.
