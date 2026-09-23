# Escalation Protocol Prompt

> **Chapter:** ch07 — Generation, Verification, and Review (Standard
> 6 governed-exception practice)
> **Last revised:** 2026-06-16
> **Use this for:** When a quality gate fails. Channels pressure into
> documented, traceable decisions instead of silent gate bypasses.

In the absence of an escalation protocol, a quality gate failure
triggers one of two responses: the engineer fixes the issue (good), or
the engineer works around the issue by lowering the gate (catastrophic).

The second response is never phrased as "I lowered the gate." It is
phrased as "I made a pragmatic decision given the timeline" or "this
is a known false positive" or "we'll address this in the next sprint."
**These phrases are the sound of standards evaporating under pressure.**

An escalation protocol does not prevent pressure. It channels pressure
into documented, traceable decisions that can be reviewed after the
fact.

The critical insight: **escalation is not failure**. A
well-documented escalation is a *contribution*. It surfaces a tension
between the standard and the reality of the codebase, the timeline, or
the tooling.

---

## The Thrashing Prevention Rule

The most expensive failure mode in agentic development is not a bug
that ships to production. It is **thrashing**: the cycle where the
engineer asks the agent to fix an issue, the agent's fix introduces a
new issue, the engineer asks the agent to fix the new issue, and the
cycle repeats until the engineer has spent more time on the fix loop
than the original generation saved.

Thrashing occurs when the agent encounters a problem outside its
capability envelope. The agent will not say "I cannot solve this." It
will produce a plausible-looking fix that addresses the symptom while
missing the root cause.

> **The rule:** if an agent has not resolved an issue within 30
> minutes or three iterations (whichever comes first), the issue is
> escalated to a human.

This is the single most counterintuitive standard in the book.
Engineers who have invested 25 minutes in a fix loop are
psychologically committed to seeing it through. Stopping feels like
giving up. **It is not.** It is the highest-leverage decision
available: spend 5 minutes documenting the problem clearly (which the
next person can use immediately) instead of spending 45 more minutes
generating code that will be thrown away.

---

## The Four Authority Levels

**Level 1: Implementing Engineer.** May override ADVISORY findings
with a documented rationale. The rationale must explain why the
finding does not apply to *this specific change*, not why the finding
is inconvenient. Recorded in the PR, visible to the reviewer.

**Level 2: Designated Reviewer.** A reviewer other than the
generating engineer may override a BLOCKING finding that is a
confirmed false positive. Requires a written explanation including
evidence (a test demonstrating the flagged condition does not
actually occur, vendor documentation contradicting the scanner's
assumption, etc.). Recorded in ESCALATION.md and tracked as a
gate-quality issue for the tool team.

**Level 3: Technical Lead / Architect.** May override a BLOCKING
finding that is a genuine issue. A conscious decision to accept a
known risk. Requires:
- Written risk assessment (severity, blast radius, mitigation plan).
- Remediation ticket with owner and deadline.
- Explicit sign-off documented in ESCALATION.md.
- Review of the remediation ticket's completion at the deadline.

**Level 4: No Override Available.** Certain blocking gates cannot be
overridden at any level:
- Security findings at CRITICAL severity involving production data
  exposure, authentication bypass, or injection vulnerabilities.
- Other categories defined per-project as "no business justification
  outweighs the risk."

The code does not ship until the finding is resolved. This absolute
floor exists because some classes of failure are catastrophic enough
that no business justification outweighs the risk.

---

## The Prompt

```markdown
## Escalation Assessment

A quality gate has failed. Complete this assessment before any
override is considered.

### Gate Failure Details
- Gate name: [which gate failed]
- Classification: [BLOCKING / ADVISORY]
- Finding: [specific finding with file:line reference]
- Severity: [CRITICAL / HIGH / MEDIUM / LOW]

### Root Cause
- Is this a false positive? [yes/no, with evidence]
- Is this a genuine issue? [yes/no, with description]
- Is this a tooling limitation? [yes/no, with explanation]

### Thrashing Check
- How long has the engineer been working on this issue? [duration]
- How many fix iterations have been attempted? [count]
- Is the issue converging toward resolution? [yes/no, with evidence]
- If duration >= 30 minutes OR iterations >= 3:
  STOP. Document and escalate to human. Do not iterate further.

### Override Assessment (if override is requested)
- Authority level required: [1 / 2 / 3 / 4-no-override]
- Business justification: [specific, not general]
- Risk assessment: [severity if the finding is real and ships to
  production]
- Mitigation: [what controls reduce the risk until remediation]
- Remediation plan: [ticket number, owner, deadline]
- Blast radius if the finding is real: [reference Standard 3
  analysis]

### Decision
- [ ] Fix the issue (no override needed)
- [ ] Override with documentation (Level 1-3, with all required
      artifacts)
- [ ] Escalate to human (issue exceeds agent capability)
```

---

## ESCALATION.md Format

When a Level 2+ override is granted, or when thrashing is detected and
a task is handed back to a human, document the escalation in
`ESCALATION.md` at the project root (or task directory):

```markdown
# Escalation: [short title]

**Date:** [YYYY-MM-DD]
**Task:** [task ID or PR link]
**Authority level:** [1 / 2 / 3]
**Decided by:** [name]

## What failed
[Specific gate, specific finding, specific file:line]

## Why we are overriding (or escalating)
[The business justification, NOT "we are tired of this finding"]

## Mitigation
[What protects against the risk in the interim]

## Remediation
[Ticket, owner, deadline]

## What we attempted (for thrashing escalations)
[List of fix attempts and why each failed]
```

## Related

- `quality-gate-config-review.md` — the gate classification this
  protocol operates on
- `disprove-only-review.md` and `adversarial-validation.md` — review
  prompts that generate the findings escalation handles
- `blast-radius-analysis.md` — the override assessment's "blast
  radius" line references the Standard 3 analysis

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 6. The
thrashing prevention rule (30 min / 3 iterations) and the four-tier
authority model were refined through Merlin Software Factory
operations.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
