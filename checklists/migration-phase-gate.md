# Migration Phase Gate Checklist

> **Chapter:** ch12 — Migration at Scale with AI Agents (Section
> 12.2)
> **Last revised:** 2026-06-16
> **Run when:** Before transitioning between migration phases.
> Reusable across migration tracks (data, API, UI).

The checklist is the **Enforce** discipline of the Harness Framework
applied to migration: it makes the quality gate explicit, binary, and
auditable.

An agent generating migration code can reference this checklist to
understand what "done" means for each phase.

---

```markdown
# Phase Gate Checklist: [Phase Name] → [Next Phase]

## Pre-Conditions (all must be TRUE to proceed)
- [ ] Parallel-run window completed: [N] days with zero divergence alerts
- [ ] Data reconciliation: old-system and new-system record counts match within [tolerance]%
- [ ] Feature flag: new path is serving [X]% of traffic via gradual rollout
- [ ] Rollback tested: feature flag revert confirmed in staging within [N] seconds
- [ ] Performance baseline: p99 latency within [N]ms of old path

## Acceptance Criteria
- [ ] All SPEC.md acceptance criteria for this phase are met
- [ ] Adversarial review (REVIEW.md) completed with zero critical findings
- [ ] Integration tests passing against new path (not just old path)
- [ ] Monitoring dashboards show no error rate increase above baseline

## Rollback Triggers (any one = revert immediately)
- [ ] Error rate exceeds [X]% for [N] minutes
- [ ] Data divergence detected between old and new systems
- [ ] Customer-reported issue attributable to migration
- [ ] Performance degradation exceeding [N]ms p99

## Sign-Off
- [ ] Engineer: _____________ Date: _______
- [ ] Architect review (for cross-boundary migrations): _____________ Date: _______
```

---

## The Three Migration-Specific Risks This Checklist Addresses

### 1. Credential surface expansion during migration

During the migration window, both the legacy system and the new
system need access to the vendor's API. This means **two sets of
credentials** (or shared credentials with a wider scope), **two sets
of rate allocations**, and **two potential points of
misconfiguration**.

An agent generating migration code may create new API keys, new
service accounts, or new OAuth clients without considering that the
legacy system's credentials are still active.

**The governance requirement:** every credential created during
migration must have a corresponding decommissioning entry in the
migration plan. **The credential surface must shrink at each phase,
not expand.**

### 2. Bidirectional sync loop prevention

During the coexistence window (when both legacy and new systems are
active), data can flow from legacy → new and from new → legacy —
creating the possibility of **sync loops** where a change in one
system triggers a change in the other, which triggers a change in
the first, infinitely.

Agent-generated sync code is particularly susceptible because the
agent optimizes for completeness — "sync all changes in both
directions" — without considering the circularity.

**The governance requirement:** every sync adapter must include a
**loop-detection mechanism** (typically an origin marker on each
change that the receiving system checks before propagating).

### 3. Regulatory deadline pressure and the temptation to skip review

Migrations often have external deadlines — contractual obligations,
regulatory requirements, vendor deprecation timelines — that create
pressure to ship migration code without full review. The pressure is
amplified by agentic development because the code can be generated
quickly, creating the illusion that the work is "almost done" when
in fact the review, integration testing, and rollback verification
are the majority of the remaining effort.

**The governance requirement:** migration timelines must account for
review time as a **percentage of total time**, not as a buffer that
can be compressed. The standards in Chapters 5 through 8 apply to
migration code **without exception** — if anything, with more rigor,
because migration code operates on production data.

## Related

- `../spec-templates/migration-plan-template.md` — the migration plan
  this phase belongs to (the SPEC.md equivalent for a multi-phase
  migration)
- `oss-license-triage.md` — when migration involves swapping
  dependencies, evaluate license class before adopting
- `deployment-safety-checklist.md` — the standard pre-deploy gate
  this phase gate complements
- `rollback-readiness-checklist.md` — the standard rollback gate
  this phase gate complements

## Provenance

Adapted from Chapter 12 of *Harnessing the Horse*, Section 12.2.
Strangler Fig migration approach: Martin Fowler (2004).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
