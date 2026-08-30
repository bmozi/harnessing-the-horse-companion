# REVIEW.md Template

> **Chapter:** ch04 — Foundations (Section 4.6, the four pipeline
> artifacts)
> **Last revised:** 2026-06-16
> **Use this for:** Closing the loop. The reviewer's evidence-backed
> verdict on whether the implementation satisfies the specification.

REVIEW.md is the Prove discipline made tangible. It is the document
that answers: *"How do we know this code is correct?"* Not "we
reviewed it" — that is a process claim. "We verified each functional
requirement, confirmed each MUST-NOT item, conducted a disprove-only
review across eight failure dimensions, and resolved all adversarial
validation findings" — that is an evidence-backed confidence
statement.

**When created:** During review. The reviewer — not the generator —
creates this artifact.
**Who creates it:** The designated reviewer. The implementing
engineer must **not** author their own REVIEW.md (artifact-level
enforcement of the "never merge your own generation" behavioral
hygiene rule).

---

```markdown
# REVIEW: [Feature or Change Name]

## Spec Reference
[Link to SPEC.md]

## Reviewer
[Name and role — must not be the implementing engineer]

## Review Date
[Date]

## Gate Status
- [ ] Compilation: PASS / FAIL
- [ ] Unit tests: PASS / FAIL
- [ ] Security scan: PASS / FAIL (findings: [count by severity])
- [ ] Architecture boundaries: PASS / FAIL
- [ ] Adversarial validation: PASS / FAIL (findings: [count
      by severity])

## Specification Compliance
For each functional requirement in SPEC.md:
- FR-1: [SATISFIED / NOT SATISFIED — with evidence]
- FR-2: [SATISFIED / NOT SATISFIED — with evidence]
- FR-3: [SATISFIED / NOT SATISFIED — with evidence]

## MUST-NOT Compliance
For each item in the MUST-NOT list:
- MN-1: [COMPLIANT / VIOLATED — with evidence]
- MN-2: [COMPLIANT / VIOLATED — with evidence]

## Disprove-Only Findings
[Findings from the three-question disprove-only review]

## Adversarial Validation Findings
[Findings from the adversarial agent, with disposition:
FIXED / ACCEPTED / FALSE POSITIVE / DEFERRED]

## Disposition
- [ ] RECOMMEND_SHIP — requirements and MUST-NOT controls pass for this run
      (final decision remains in `factory-bootstrap/SESSION_DECISION.md`)
- [ ] RECOMMEND_REVISE — [specific revisions required; return to
      generation]
- [ ] RECOMMEND_STOP — [reason; return to design or spec phase]

## Sign-off
[Reviewer name, date]
```

---

## The governance function

In a regulated environment (finance, healthcare, defense), auditors
ask: *"How was this code reviewed before deployment?"* REVIEW.md
provides a complete, structured answer.

In an incident postmortem, the team asks: *"Was this defect reviewable
at the time?"* REVIEW.md provides the evidence: the review checked
dimensions X, Y, and Z, and the defect was in dimension W, which was
not in the review checklist. The postmortem adds dimension W to the
checklist. **The review practice improves.**

## Related

- `../prompts/disprove-only-review.md` — the review prompt this
  document records the output of
- `../prompts/adversarial-validation.md` — produces the Adversarial
  Validation Findings section
- `../checklists/integration-verification-checklist.md` — supplies
  the Gate Status entries

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.6. The
three-question disprove-only review and the adversarial validation
findings it records are the two modes of Standard 7 (Falsification
Review, Chapter 7).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
