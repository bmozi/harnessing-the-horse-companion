# Impact Boundary Assessment Checklist

> **Chapter:** ch09 — Architectural Stewardship (Section 9.1, "The
> Impact Boundary Assessment")
> **Last revised:** 2026-06-16
> **Run when:** Before any generated code is merged. Determines
> whether the change affects the architecture — not just the code.

Before any generated code is merged, the impact boundary assessment
determines whether the change affects the architecture. If yes, the
change requires architectural review before merge — not just code
review by the PR reviewer, but explicit approval from the owner of
the affected module boundary.

This is the mechanism by which architectural intent survives the
accumulation of individually-correct changes.

---

## The Five Questions

Answer each. If **any answer is yes**, the change requires
architectural review.

### 1. Boundary Crossing

- [ ] Does this change **cross any module boundary** defined in the
      architecture?

### 2. New Inter-Module Dependency

- [ ] Does this change **introduce a new dependency** between
      modules?

### 3. Public API Modification

- [ ] Does this change **modify a public API** that other modules
      depend on?

### 4. New Communication Pattern

- [ ] Does this change **create a new communication pattern**?
  - Synchronous where asynchronous was used?
  - Direct call where event-driven was used?
  - Shared database access where API-mediated access was the norm?

### 5. Architecture Diagram Impact

- [ ] Does this change **require corresponding updates** in the
      architecture diagrams?

---

## Verdict

| Answers | Verdict |
| --- | --- |
| All five **NO** | Code review by PR reviewer is sufficient. |
| **One or more YES** | **Requires architectural review** — explicit approval from the module-boundary owner before merge. Update the diagrams as part of the merge. |

This is not overhead. This is the mechanism by which architectural
intent survives the accumulation of individually-correct changes.

---

## Drift Scan Classification (for findings outside this assessment)

When the answers are uncertain or you're looking at a longer-running
drift, classify each finding into one of three categories:

- **Violation.** Code that clearly violates the documented
  architecture. Module A imports directly from module B's internal
  package. The API layer makes a direct database call that bypasses
  the service layer. A cross-cutting concern is implemented locally
  rather than through the designated shared module. **Violations
  must be resolved** — either fix the code or update the
  architecture to reflect a deliberate decision.

- **Evolution.** Code that suggests the architecture has legitimately
  evolved and the documentation needs updating. A new module has
  been added that does not appear in the architecture diagrams. An
  existing module has taken on new responsibilities not reflected in
  its documented scope. Evolution findings are not defects — they
  are **documentation gaps**. But documentation gaps, left
  unaddressed, become drift, and drift becomes erosion.

- **Ambiguity.** Cases where the architecture documentation is
  unclear about whether a dependency is allowed. The module boundary
  is defined at the package level, but the dependency exists at the
  sub-package level, and the documentation does not specify
  sub-package boundaries. Ambiguity findings indicate that the
  architecture needs **more precision** — more granular boundary
  definitions, more explicit rules.

## Common Failure Modes

- **The Approved Exception That Became the Norm.** An exception is
  approved for one case ("just for this one case, payment can access
  user's internal API"). Six months later, eighteen components do
  the same thing. No single violation was unapproved, but the
  pattern was never evaluated as a whole. **The drift scan catches
  this — if anyone runs it.**
- **The Missing Module Owner.** A module has no designated owner.
  When agent-generated changes modify it, no one feels responsible
  for the architectural implications. Module ownership is not
  optional — it is the human accountability that makes boundary
  enforcement meaningful.
- **The Stale Diagram.** Architecture diagrams last updated eight
  months ago. The system has changed. Reviews that rely on stale
  diagrams cannot catch boundary violations.

## Related

- `../diagrams/baseline-architecture-diagrams.md` — the four
  baseline diagrams these assessments compare against
- `../spec-templates/adr-template.md` — when a YES answer here
  represents a deliberate architectural decision, capture it as an
  ADR
- `integration-verification-checklist.md` — Q1 of the five
  architectural review questions performs this check inline at
  merge time

## Provenance

Adapted from Chapter 9 of *Harnessing the Horse*, Section 9.1. The
five questions are the book's impact boundary assessment. The
three-class drift scan (Violation / Evolution / Ambiguity) is also
from Section 9.1.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
