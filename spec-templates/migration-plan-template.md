# Migration Plan Template

> **Chapter:** ch12 — Migration at Scale with AI Agents (Section
> 12.2)
> **Last revised:** 2026-06-16
> **Use this for:** Multi-phase migrations governed by the same
> artifact discipline as any other agent-generated work. The
> migration plan is the SPEC.md *for the migration*.

Migration plans for agentic development should follow the same
artifact discipline as any other agent-generated work. The migration
plan defines **what** will be migrated, **in what order**, with
**what acceptance criteria**, and with **what rollback procedure**
for each phase.

Each phase of the migration is a task in the DESIGN.md decomposition.
Each phase has its own SPEC.md (acceptance criteria for that phase),
its own IMPL_NOTES.md (decisions and deviations), and its own
REVIEW.md (adversarial review of the phase's generated code). The
migration is **not a single agent session** — it is a multi-phase,
multi-session effort governed by the same artifact discipline that
a multi-task feature requires.

---

```markdown
# Migration Plan: [What's being migrated]

## Status
Draft | Approved | In Progress (Phase [N]) | Complete | Aborted

## Owner
[Name and role — single accountable engineer or architect]

## Strangler Fig Reference

This migration follows the Strangler Fig pattern (Martin Fowler,
2004). Old and new systems coexist; feature flags shift traffic
gradually; the old system is decommissioned only after the new
system is proven.

## Current State Inventory

What exists today:
- [System / component / data store]
  - Tech: [technology stack, version]
  - Owner: [team / engineer]
  - Consumers: [list of downstream systems and their integration
    points]
  - Credentials: [what credentials grant access; who manages them]
  - Constraints: [SLA, regulatory, data residency, etc.]

## Target State Definition

What will exist after migration:
- [System / component / data store]
  - Tech: [technology stack, version]
  - Owner: [team / engineer]
  - Consumers: [same list, now pointing at the new path]
  - Credentials: [what replaces the old credentials]
  - Constraints: [unchanged or new]

## Phase Sequence

| Phase | Name | Description | Estimated duration |
| --- | --- | --- | --- |
| 0 | Preparation | Stand up new system in shadow mode. No traffic. | [N] weeks |
| 1 | [Phase name] | [Description] | [duration] |
| 2 | [Phase name] | [Description] | [duration] |
| ... | | | |
| N | Decommission | Remove the old system entirely. Credentials revoked. | [N] weeks |

## Acceptance Criteria (per phase)

For each phase, link to that phase's SPEC.md with binary,
machine-readable acceptance criteria. See
`../checklists/migration-phase-gate.md` for the per-phase gate
template.

## Rollback Procedure (per phase)

For each phase, link to that phase's rollback procedure. Every phase
must have a tested rollback. Untested rollback is not a rollback —
it's a prayer.

See `../checklists/rollback-readiness-checklist.md` for the rollback
classification and testing discipline.

## Credential Plan

Every credential created during migration must have a corresponding
decommissioning entry. **The credential surface must shrink at each
phase, not expand.**

| Phase | Credential | Created | Decommissioned | Owner |
| --- | --- | --- | --- | --- |
| 0 | [name] | Phase 0 | Phase N | [name] |
| 1 | [name] | Phase 1 | Phase 2 | [name] |
| ... | | | | |

## Sync Loop Prevention

If the migration involves bidirectional sync during the coexistence
window, document:

- The origin marker carried on every change
- The receiving-system check that prevents propagating origin-
  marked changes back
- The test that verifies the loop-detection mechanism works

(Agent-generated sync code is particularly susceptible to sync
loops because the agent optimizes for completeness without
considering circularity.)

## Monitoring Plan

What metrics confirm the migration is working correctly in
production:

- [Metric 1] — baseline [value]; target [value]
- [Metric 2] — baseline [value]; target [value]
- [Metric 3] — baseline [value]; target [value]

Where the dashboards live: [link]

## Regulatory / External Deadline Pressure

If this migration has an external deadline (contractual obligation,
regulatory requirement, vendor deprecation), document:

- The deadline: [date]
- The consequence of missing it: [specific business impact]
- The review-time buffer: [percentage of total time reserved for
  review, NOT a buffer that can be compressed]

> Migration timelines must account for review time as a percentage
> of total time, not as a buffer that can be compressed. The
> standards in Chapters 5–8 apply to migration code without
> exception — if anything, with more rigor, because migration code
> operates on production data.

## Dependencies

- Depends on: [list of other migrations, infrastructure changes,
  vendor confirmations]
- Depended on by: [list of downstream work that waits on this
  migration]

## Open Questions

- [Any unresolved questions that must be answered before the next
  phase begins]
```

---

## The Phase Discipline

Each phase is a SPEC + DESIGN + IMPL_NOTES + REVIEW cycle, plus the
phase-gate checklist (`../checklists/migration-phase-gate.md`):

```
Phase N
├── spec.md           (acceptance criteria for this phase)
├── design.md         (how the phase is implemented)
├── impl-notes.md     (deviations, discoveries, debt during phase)
├── review.md         (adversarial review at phase completion)
└── phase-gate.md     (the migration-phase-gate checklist completed)
```

**Do not advance to phase N+1 until phase N's gate passes.**

## Why Migrations Need Tighter Discipline Than Greenfield

| Risk | Why it's worse in migration |
| --- | --- |
| Bug in production code | Greenfield: small blast radius. Migration: every customer is exposed during cutover. |
| Bidirectional sync drift | Greenfield: not applicable. Migration: sync loops can corrupt both systems. |
| Credential leak | Greenfield: one credential to rotate. Migration: two credentials, possibly with overlapping scope. |
| Deadline pressure to skip review | Greenfield: review skipped → debt. Migration: review skipped → production data at risk. |

## Related

- `spec-md.md` — each phase has its own SPEC.md
- `design-md.md` — each phase has its own DESIGN.md
- `impl-notes-md.md` — each phase has its own IMPL_NOTES.md
- `review-md.md` — each phase has its own REVIEW.md
- `../checklists/migration-phase-gate.md` — the gate that closes
  each phase
- `../checklists/oss-license-triage.md` — if migration introduces
  new dependencies
- `../checklists/rollback-readiness-checklist.md` — the rollback
  testing discipline every phase requires
- `../patterns/anti-corruption-layer.md` — for vendor migrations,
  the ACL is what makes the cutover possible without business-logic
  rewrites

## Provenance

Adapted from Chapter 12 of *Harnessing the Horse*, Section 12.2. The
Strangler Fig migration pattern is from Martin Fowler (2004).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
