# IMPL_NOTES.md Template

> **Chapter:** ch04 — Foundations (Section 4.6, the four pipeline
> artifacts)
> **Last revised:** 2026-06-16
> **Use this for:** The running log of what actually happened during
> implementation. Maintained during generation, not written after the
> fact.

IMPL_NOTES.md is the artifact that distinguishes disciplined agentic
development from undisciplined agentic development. Without it, the
gap between what was designed and what was built is invisible until
someone reads every line of code. With it, the reviewer can
immediately see: where did the implementation deviate from the
design? What new constraints were discovered? What shortcuts were
taken?

**When created:** During generation. Maintained as a running log.
**Who creates it:** The implementing engineer — the person directing
the agent session.

---

```markdown
# IMPL_NOTES: [Feature or Change Name]

## Spec Reference
[Link to SPEC.md]

## Design Reference
[Link to DESIGN.md]

## Implementation Log

### [Date/Time]
- Implemented [component]. Followed the design as specified.
- Deviated from design in [area]: [description of deviation
  and reason].
- Discovered constraint: [something learned during
  implementation that the spec/design did not anticipate].
- Tech debt introduced: [description of shortcut taken and
  why, with ticket reference for remediation].
- Agent uncertainty: [area where the agent was uncertain and
  the implementing engineer made a judgment call].

### [Date/Time]
- [Continue logging as implementation proceeds]

## Deviations from Design
[Summary list of all deviations, with rationale for each]

## Discovered Constraints
[Summary list of constraints discovered during implementation
that were not in the spec or design]

## Tech Debt Register
[List of tech debt items introduced, with remediation tickets]
```

---

## The implementation log is not a journal

It is an **engineering record**. Code can show you *what* was built.
IMPL_NOTES.md shows you *why it was built that way* — including the
places where "that way" differed from the original plan.

For the Communicate discipline of the Harness Framework, IMPL_NOTES.md is
the most valuable artifact because it captures information that no
other artifact contains: the runtime discoveries, the judgment calls,
and the compromises that the implementing engineer made under the
pressure of actual implementation.

## The Tech Debt Register

The debt register inside IMPL_NOTES.md categorizes each item into
three severity levels (per ch09 Standard 10):

- **Must-fix-before-merge** — unacceptable in production. Hardcoded
  credentials, missing error handling on critical paths, placeholder
  implementations that pass tests but don't implement the actual
  business logic, known security vulnerabilities. **BLOCKING**.
- **Should-fix-soon** — acceptable for initial merge but a known risk
  that increases over time. Missing retry logic on network calls,
  incomplete input validation on internal APIs, sub-optimal queries
  that work at current scale but degrade under load, test coverage
  gaps on edge cases. Tracked with specific remediation deadlines.
- **Can-defer** — acknowledged, documented, deprioritized. Style
  inconsistencies, abstraction opportunities that don't affect
  behavior, naming differences that are internally consistent,
  documentation gaps. Tracked for batch resolution during refactoring
  cycles.

Items move between severity levels as circumstances change. The
register's value is not in perfect classification at creation — it
is in maintaining visibility into the debt portfolio so prioritization
decisions are informed rather than reactive.

## Related

- `spec-md.md` — the SPEC this implementation log references
- `design-md.md` — the design this log records deviations from
- `review-md.md` — the review that reads this log to verify discipline

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.6. The
three-severity debt register is from Chapter 9 (Standard 10,
Architectural Stewardship and Debt Governance).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
