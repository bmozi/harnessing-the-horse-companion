# Integration Verification Checklist

> **Chapter:** ch08 — Execution Discipline (Standard 8: Integration
> Verification)
> **Last revised:** 2026-06-16
> **Run when:** Before merge, after the generated component has passed
> its own unit tests and the disprove-only review.

AI agents optimize locally. Each session sees its task spec, the
relevant context files, and whatever portions of the codebase were
included in its context window. It does not see — and cannot reason
about — the full dependency graph of the system it is modifying.

Integration verification closes that gap. **It is the practice of
running the system, not just the component.**

---

## Level 1: Contract Verification (static)

Before running any code, verify interfaces between the generated
component and its dependencies are consistent.

- [ ] Function signatures match callers' expectations
- [ ] API contracts match consumer expectations (OpenAPI spec
      compared)
- [ ] Event payload schemas match consumer expectations
- [ ] Data types are compatible across the boundary
- [ ] No interfaces were silently modified (compare against
      `../spec-templates/interface-spec.md`)

> In the Merlin Software Factory, contract verification caught
> approximately **30% of integration issues** before a single test
> ran.

## Level 2: Cross-Component Testing

Run integration tests that exercise the boundaries — not the unit
tests the generating session produced, which use mocks.

- [ ] Real (or realistic) database connection
- [ ] Real HTTP calls between services
- [ ] Real event bus message passing
- [ ] All boundary tests pass

## Level 3: System-Level Smoke Testing

Fast critical-path check (under five minutes) that confirms major
user journeys are intact.

- [ ] Login / authentication flow
- [ ] Primary read flow for the affected domain
- [ ] Primary write flow for the affected domain
- [ ] No new error types appearing in baseline observability

---

## The Refactoring Pass (six dimensions)

AI-generated code optimizes for the task at hand, not the codebase as
a whole. Before integration, every generated component goes through
this pass. The goal is not "cleaner code in some abstract sense" — the
goal is to **ensure the code, once merged, does not make the next
change harder**.

- [ ] **Duplication.** No retry-with-backoff utility (or equivalent)
      duplicated because two sessions could not see each other's
      output.
- [ ] **Pattern consistency.** Async/await vs. callbacks, class vs.
      functional components, etc. — matches the surrounding codebase.
- [ ] **Abstraction opportunities.** No repeated try/catch/retry/log
      structure across recently-generated components that should be a
      shared utility.
- [ ] **Coupling.** Module boundaries from the architecture diagrams
      are respected; no reaching into another module's internal
      directory.
- [ ] **Naming.** Consistent with codebase conventions (no
      `getUserById` / `fetchUser` / `loadUserRecord` mix).
- [ ] **Dead code.** No unreachable helper functions, unused utility
      classes, or intermediate-purpose code that was not removed.

---

## The Five Architectural Review Questions

Before merge, questions 1, 4 and 5 require yes; questions 2 and 3 require no or reviewer-approved justification.
Adapted from Cloudflare deployment review practices and refined
through the Merlin Software Factory.

- [ ] **1. Does this change respect module boundaries?**
      Check the architecture diagrams. If it crosses a boundary that
      should be respected, it needs architectural review before
      merge.
- [ ] **2. Does this change introduce a new dependency?**
      Every new dependency is a liability: supply chain risk, version
      management, license compliance. If new — was it justified in
      IMPL_NOTES.md and approved?
- [ ] **3. Does this change make the next change harder?**
      Look for tight coupling, missing abstractions, and hardcoded
      values that should be configuration. Think one step beyond the
      current change.
- [ ] **4. Does this change have a rollback plan?**
      If this causes a 2 AM incident, can it be reverted with a
      single command? If migration / schema / data transformation is
      involved, see `rollback-readiness-checklist.md`.
- [ ] **5. Does this change have observability?**
      Can you tell if this code is working correctly in production
      without reading the source? Logging, metrics, health checks,
      alerts — not nice-to-haves, requirements.

**Every answer needs evidence and the expected disposition above before merge.**

---

## Common Failure Modes

- **The Assumed Interface.** Two sessions interpret an ambiguous
  spec differently. Session A returns a list. Session B expects a
  paginated response with a cursor. Both are reasonable readings of
  a vague spec. Fix: tighter interface spec
  (`../spec-templates/interface-spec.md`).
- **The Phantom Dependency.** Agent imports a package that exists in
  package.json but is not installed, or imports a version with a
  different API than the lockfile specifies. Code compiles in the
  agent's context because it does not execute the code — it generates
  it. Caught at the contract level before runtime.
- **The Silent Regression.** Generated component passes all its own
  tests but degrades performance of an existing component by adding
  queries to a shared table without an index. No test fails. No
  contract is violated. System is slower. Caught only by system-level
  smoke tests that include performance baselines or by observability
  infrastructure.

## Related

- `../spec-templates/interface-spec.md` — Level 1 contract
  verification compares against these contracts
- `../prompts/disprove-only-review.md` — the review pass that runs
  before this checklist
- `deployment-safety-checklist.md` — what runs *after* integration
  verification passes
- `rollback-readiness-checklist.md` — Q4 of the five questions
  references this

## Provenance

Adapted from Chapter 8 of *Harnessing the Horse*, Standard 8. The
five architectural review questions are adapted from Cloudflare
deployment review practices and refined through Merlin Software
Factory operations.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
