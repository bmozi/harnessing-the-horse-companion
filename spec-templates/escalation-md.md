# ESCALATION.md Template

> **Chapter:** ch07 — Generation, Verification, and Review
> **Use when:** A Level 2+ gate override is granted, or an agent session
> has hit the thrashing rule and must hand the work back to a human.

Copy this file into the project root, pull request, or task directory as
`ESCALATION.md`.

```markdown
# Escalation: [short title]

**Date:** [YYYY-MM-DD]
**Task:** [task ID or PR link]
**Authority level:** [1 / 2 / 3 / 4-no-override]
**Decided by:** [name and role]

## What failed

[Specific gate, specific finding, and file:line reference.]

## Classification

- Gate classification: [BLOCKING / ASYNC / ADVISORY / INFORMATIONAL]
- Finding severity: [CRITICAL / HIGH / MEDIUM / LOW]
- Is this a false positive? [yes/no, with evidence]
- Is this a genuine issue? [yes/no, with explanation]

## Thrashing history

- Time spent: [duration]
- Iterations attempted: [count]
- Evidence of convergence: [yes/no]
- Attempts made:
  1. [attempt and result]
  2. [attempt and result]
  3. [attempt and result]

## Why we are overriding or escalating

[The business justification or technical reason. Do not write "timeline"
or "pragmatism" without naming the concrete tradeoff.]

## Risk assessment

- Blast radius: [systems, users, data, dependencies affected]
- Worst credible failure: [what happens if the finding is real]
- Detection mechanism: [how we will know if it occurs]

## Mitigation

[What protects against the risk in the interim.]

## Remediation

- Ticket: [link]
- Owner: [name]
- Deadline: [date]
- Verification required to close: [test/check/review]

## Decision

[Fix / override / escalate / stop shipment]
```

See also:

- [`../prompts/escalation-assessment.md`](../prompts/escalation-assessment.md)
- [`../prompts/escalation-protocol.md`](../prompts/escalation-protocol.md)
- [`review-md.md`](review-md.md)

