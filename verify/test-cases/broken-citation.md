# Test case: broken citation (deliberate neighbour swap)

This finding uses the real quote from Article 13(2)(a) (retention period)
but points it at Article 13(1)(e) (categories of recipients) instead —
a real quote attached to the wrong provision, the exact fault this round's
competition judging tested for. Running this through check.py should FAIL,
and the failure should print what line 13 actually says.

CITATION: articles/art-13-info-collected-from-subject.md:13
QUOTE: the period for which the personal data will be stored
