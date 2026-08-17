# Pre-Generation Verification Checklist

> **Chapter:** ch05 — Discovery and Planning (Standard 1, the
> pre-generation gate)
> **Last revised:** 2026-06-16
> **Run when:** After SPEC.md and DESIGN.md are approved, before any
> code is generated.

This gate validates that the specification is ready for generation —
not that it is complete in some abstract sense, but that it is
**executable**. The agent (or the engineer) runs through four checks
before any code is generated.

It takes the agent approximately 30 seconds to perform. It saves
hours of rework when it catches a scope violation, a hallucinated
API, an unauthorized dependency, or a MUST-NOT violation **before a
single line of code is generated**.

> Only proceed with generation after all four checks pass. Output the
> confirmation as a checklist before generating any code.

---

## Check 1: Scope Boundary

- [ ] List every file the agent plans to create or modify.
- [ ] Compare against the Scope Boundary section in SPEC.md and the
      Files list in `../spec-templates/task-spec.md`.
- [ ] If any file is **outside the specified scope** — stop and
      report the deviation.

## Check 2: Interface Contracts

- [ ] List every function signature, API endpoint, or data schema the
      agent plans to use from other modules.
- [ ] Confirm **each one exists in the current codebase** — verify
      against the actual code, not against training data.
- [ ] Hallucinated interface references are one of the most common
      and most expensive failure modes; this check is the defense.

## Check 3: Dependency Check

- [ ] List every import or dependency the agent plans to use.
- [ ] Confirm each one is in the project's dependency manifest
      (`package.json`, `requirements.txt`, `go.mod`, `pubspec.yaml`,
      etc.).
- [ ] If a new dependency is needed → stop and document the
      justification in `IMPL_NOTES.md`.

## Check 4: Constraint Check

- [ ] Review the MUST-NOT list in SPEC.md.
- [ ] Confirm the plan does not violate any constraint.
- [ ] If any MUST-NOT item is at risk → revise the plan before
      generating.

---

## What Passing This Gate Looks Like

The agent outputs a structured pre-generation checklist as its first
action, before any code generation:

```markdown
## Pre-Generation Verification

### Scope Boundary
Files I plan to modify:
- src/users/handler.go (create new function)
- src/users/handler_test.go (add tests)
Comparison to task-spec Files list: MATCH.

### Interface Contracts
External interfaces I plan to use:
- repository.UserRepository.FindByEmail — verified at
  src/repositories/user.go:42
- middleware.Authenticated — verified at
  src/middleware/auth.go:18
All interfaces verified against the actual codebase.

### Dependency Check
Imports I plan to use:
- "github.com/go-chi/chi/v5" — present in go.mod
- "github.com/stretchr/testify/assert" — present in go.mod
- "encoding/json" — stdlib
No new dependencies required.

### Constraint Check
MUST-NOT list reviewed:
- MN-1: MUST-NOT modify the users table schema — my plan does
  not include schema changes. COMPLIANT.
- MN-2: MUST-NOT bypass the auth middleware — my plan uses the
  Authenticated middleware. COMPLIANT.

All checks PASS. Proceeding to generation.
```

If the agent omits this output and begins generating immediately, the
generation did **not** follow the standard. The reviewer should
reject the output and require the gate to be re-run.

## Areas of Critique

- Did the agent actually perform the gate before generating, or did
  it skip straight to code? Most common compliance failure.
- Are the listed interface contracts real, or hallucinated? Spot-check
  3 — if any is hallucinated, the gate failed.
- Is the dependency list complete? Or did the agent skip implicit
  dependencies (environment variables, database tables, external
  APIs)?
- Does the MUST-NOT compliance section cite each item by ID, or just
  give a blanket assertion?

## Related

- `../spec-templates/spec-md.md` — the SPEC the Scope Boundary,
  Interface Contracts, and MUST-NOT items come from
- `../spec-templates/task-spec.md` — provides the Files list
- `post-generation-verification.md` — the second gate that runs
  after generation completes

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Section 5.1. The
four checks (Scope Boundary, Interface Contracts, Dependency Check,
Constraint Check) are the book's pre-generation gate.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
