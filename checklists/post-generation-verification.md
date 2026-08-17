# Post-Generation Verification Checklist

> **Chapter:** ch05 — Discovery and Planning (Standard 1, the
> post-generation gate)
> **Last revised:** 2026-06-16
> **Run when:** After the agent finishes generating code, before the
> output is presented for human review.

After generation, before the output is presented for human review,
this second gate verifies that the generation stayed within the
boundaries established by the pre-generation gate.

The post-generation gate transforms the code review from *"read
everything and hope you catch the problems"* to *"verify the agent's
claims against the specification."* The reviewer's job becomes
**falsification, not comprehension** — which is the foundation of the
disprove-only review in Chapter 7.

---

## Check 1: File Inventory

- [ ] List every file created or modified during generation.
- [ ] Confirm none are outside the scope defined in the pre-generation
      gate.
- [ ] Any unexpected file — a file not listed in the scope but created
      or modified during generation — requires explanation.

> Unexpected files are the signature of scope drift, and scope drift
> is the mechanism that produces unreviewable output.

## Check 2: Interface Integrity

- [ ] Confirm **no existing function signatures, API endpoints, or
      data schemas were modified** unless explicitly specified in the
      task scope.
- [ ] List every interface present in the generated code.
- [ ] Compare against the interfaces declared in
      `../spec-templates/interface-spec.md` and `task-spec.md`.

## Check 3: Dependency Delta

- [ ] List any new imports or dependencies added during generation.
- [ ] Each must have been approved in the pre-generation gate **or**
      flagged here as a deviation requiring review.

## Check 4: Test Coverage

- [ ] Confirm tests exist for every public function or endpoint
      created.
- [ ] List the test files and what they cover.
- [ ] Every public interface must have:
  - At least one test exercising its **primary behavior**
  - At least one test exercising an **edge case**

> Test coverage is not a percentage target — it is a completeness
> check.

## Check 5: MUST-NOT Verification

- [ ] Re-check every MUST-NOT constraint from the SPEC.md.
- [ ] Confirm none were violated during generation.
- [ ] Cite each MN-N by ID with explicit COMPLIANT / VIOLATED status.

---

## What Passing This Gate Looks Like

The agent outputs a structured post-generation report alongside the
generated code:

```markdown
## Post-Generation Verification

### File Inventory
Files modified:
- src/users/handler.go (added SearchUsers function, 78 lines)
- src/users/handler_test.go (added TestSearchUsers, 124 lines)
Comparison to pre-gen plan: MATCH. No deviations.

### Interface Integrity
Interfaces in this change:
- New: handler.SearchUsers(ctx, req) → (resp, error)
- Used (unchanged): repository.UserRepository.FindByEmail
- Used (unchanged): middleware.Authenticated
No existing interfaces modified. COMPLIANT.

### Dependency Delta
Imports added: none.
Imports removed: none.
Dependency manifest unchanged. COMPLIANT.

### Test Coverage
TestSearchUsers covers:
- Primary behavior: returns users matching the query (2 cases)
- Edge cases: empty query → 400, query too short → 400, no
  results → 200 with empty array, malformed cursor → 400
All public interfaces covered. COMPLIANT.

### MUST-NOT Verification
- MN-1 (MUST-NOT modify users table schema) — no schema changes.
  COMPLIANT.
- MN-2 (MUST-NOT bypass auth middleware) — handler wrapped in
  middleware.Authenticated. COMPLIANT.

All checks PASS. Generation complete; presenting for review.
```

## What Failing Looks Like

If any check fails, the agent does not present the output for review
— it stops and reports the deviation. Common failure patterns:

- **Unexpected file** in Check 1 → the agent expanded scope mid-session.
  Discard the session, refine the prompt, regenerate.
- **Modified interface** in Check 2 → the agent "helpfully" refactored.
  Every other consumer of the interface is now broken. Revert and
  regenerate.
- **Unauthorized dependency** in Check 3 → the agent added a package
  that was not in the manifest. Either authorize it (and document
  in IMPL_NOTES.md) or regenerate without it.
- **Missing edge-case test** in Check 4 → not done.
- **MUST-NOT violation** in Check 5 → not even close to done.

## Areas of Critique

- Does the post-generation file inventory **match** the pre-generation
  plan? Any unexpected files require explanation.
- Are the interface contracts the agent claims to have verified
  actually real? Spot-check three of them against the codebase.
- Does the test coverage section list both primary behavior and edge
  cases, or just a single happy-path test?
- Does the MUST-NOT verification cite each item by ID, or just
  assert "all MUST-NOTs compliant" without evidence?

## Related

- `pre-generation-verification.md` — the first gate that establishes
  the baseline this gate checks
- `../prompts/disprove-only-review.md` — the human review that runs
  after this gate passes
- `../spec-templates/spec-md.md` — the source of the MUST-NOT list

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Section 5.1. The
five checks (File Inventory, Interface Integrity, Dependency Delta,
Test Coverage, MUST-NOT Verification) are the book's post-generation
gate.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
