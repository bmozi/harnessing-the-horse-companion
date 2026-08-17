# Equivalence Test Checklist

> **Chapter:** Appendix D — Design Study: Platform Modernization
> (Section D.4, "Testing a Migration Rather Than a System")
> **Last revised:** 2026-06-16
> **Run when:** Multi-system migration where the assertion is "the
> new system produces the same results as the old system."

The testing strategy for a multi-year migration differs from
testing a new system. The primary assertion is not "does it work?"
but **"does it produce the same results as the system it
replaces?"**

This requires three categories of tests that traditional testing
frameworks do not emphasize.

---

## Category 1: Equivalence Tests

For every query that the business runs against the old system
today (customer lookup, appointment scheduling, billing
reconciliation, compliance reporting), an equivalence test runs
the same query against **both** the old and new systems and
asserts the results match.

- [ ] Identify every business-critical query against the old
      system (customer lookup, billing aggregations, etc.)
- [ ] For each query, write an equivalence test that:
  - [ ] Runs the same logical query against both systems
  - [ ] Asserts the results match within an explicit tolerance
  - [ ] Logs discrepancies for investigation
- [ ] Equivalence tests run **continuously in production** — not
      in a test environment
- [ ] Discrepancies generate alerts to the migration team
- [ ] Each discrepancy must be **classified**:
  - [ ] Expected (known data model difference, documented)
  - [ ] Bug in new system (file in migration backlog)
  - [ ] Bug in old system being faithfully reproduced (document
        and decide whether to fix in new)

> **Continuous production execution** is the key discipline.
> Pre-migration tests against a static dataset don't catch the
> events that arrive after the test ran.

---

## Category 2: Temporal Replay Tests

Event sourcing (see [`../patterns/event-sourcing.md`](../patterns/event-sourcing.md))
enables temporal replay: given the events up to time T, does the
projection at time T match the old system's state at time T?

- [ ] Identify sample historical points to validate (e.g., end of
      each month for the last 24 months)
- [ ] For each sample point, build a test that:
  - [ ] Replays new-system events up to time T
  - [ ] Reconstructs the projection state at time T
  - [ ] Compares against the old system's snapshot at time T
  - [ ] Asserts they match within tolerance
- [ ] Document any past-time discrepancies with classification:
  - [ ] Was-bug-then-fixed: the projection is now correct but was
        incorrect at time T due to an event-ordering bug since
        fixed
  - [ ] Was-correct-now-broken: regression in projection logic
  - [ ] Genuine difference: documented data model evolution

> This catches a class of bugs that snapshot comparisons miss:
> a projection that is correct now but was incorrect last Tuesday
> because of an event-ordering bug that was since fixed.

---

## Category 3: Migration Regression Tests

Each domain cutover has a regression suite that exercises the
end-to-end workflow against the new system and verifies the
business outcome matches the old-system workflow.

- [ ] For each bounded context being migrated, define the
      regression suite:
  - [ ] Create the canonical workflow (e.g., for scheduling:
        create an appointment, modify it, cancel it)
  - [ ] Assert each side effect fires correctly (technician
        route updated, customer notification sent, billing
        adjustment made)
- [ ] The same test suite runs:
  - [ ] **Before** cutover (pointed at old system)
  - [ ] **During** parallel-run window (pointed at both,
        comparing outputs)
  - [ ] **After** cutover (pointed at new system)
- [ ] If results diverge between "before" and "after" runs of
      the same test, the migration is **not** producing
      equivalent results — block the cutover until investigated

> The scheduling regression test creates an appointment, modifies
> it, cancels it, and verifies that the technician route,
> customer notification, and billing adjustment all fire
> correctly.

---

## The Tolerance Discipline

Every comparison needs an **explicit tolerance**:

- **Numeric equivalence**: exact match? within 1 cent? within
  1%?
- **Timestamp equivalence**: exact? within 1 second? within 1
  minute?
- **String equivalence**: exact? case-insensitive? whitespace-
  normalized?
- **Set equivalence**: same elements? same order? same count?
- **Approximate-numeric** (for floating-point or rate
  calculations): within an explicit epsilon

A tolerance of "close enough" is not a tolerance. Every
equivalence test must specify exactly what "match" means.

## The Discrepancy Classification

When a discrepancy is detected, it falls into one of three
classes:

- **Migration bug.** The new system has an incorrect
  implementation. Fix in the new system and re-test.
- **Documented divergence.** The two systems are deliberately
  different (e.g., the old system was buggy and the new system
  fixes it). Document the divergence in an ADR and update the
  expected-result baseline.
- **Vendor or data-quality issue.** Neither system is wrong;
  the source data has changed between when each system observed
  it. Investigate the data source.

Every discrepancy must be classified before the migration phase
advances. **Unclassified discrepancies are a blocking finding**
for the phase gate (see
[`migration-phase-gate.md`](migration-phase-gate.md)).

## Why Equivalence Testing Is Not Optional

In a greenfield system, you can be wrong in interesting new ways.
In a migration, **every "interesting" difference is a regression**.

The cost of a missed equivalence failure compounds:

- Day 1: Reports diverge slightly. Nobody notices.
- Day 30: Operations notices that branch revenue reports are off
  by 0.3%. Investigation begins.
- Day 60: Root cause traced to event-ordering bug introduced in
  Phase 2. Three downstream projections affected.
- Day 90: 60 days of incorrect business decisions made on the
  wrong projections.

Continuous equivalence testing catches this on Day 1.

## Worked Example: FieldstoneOS Migration

From the platform modernization design study (Appendix D) — a
documented architecture and migration plan, not yet built. The plan
specifies:

- **Equivalence tests** run continuously in production:
  customer lookup, appointment scheduling, billing
  reconciliation, compliance reporting
- **Temporal replay tests** sample historical points and verify
  FieldstoneOS can reconstruct past states correctly
- **Migration regression tests** for each domain cutover
  (billing, scheduling, etc.) — same test pointed at different
  backends
- Tests generated by AI agents that read FieldRoutes API
  documentation and produce test implementations against both
  systems
- The discipline of test generation is governed by Standard 1's
  constraint discipline (Chapter 7) — each test cites the business
  query it validates and the acceptance criteria that define
  "matching results"

## Related

- [`migration-phase-gate.md`](migration-phase-gate.md) — the gate
  that depends on equivalence tests passing before advancing
- [`../spec-templates/migration-plan-template.md`](../spec-templates/migration-plan-template.md)
  — the migration plan that lists which equivalence tests cover
  which phases
- [`../patterns/event-sourcing.md`](../patterns/event-sourcing.md)
  — the architectural pattern that makes temporal replay possible
- [`../patterns/transactional-outbox.md`](../patterns/transactional-outbox.md)
  — companion pattern that ensures the event stream the temporal
  tests depend on stays consistent

## Provenance

Adapted from Appendix D of *Harnessing the Horse*, Section D.4.
The three test categories (equivalence, temporal replay, migration
regression) are the planned testing strategy for the FieldstoneOS
migration design study.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
