# STRATEGIC_PIVOT.md Template

> **Chapter:** ch16 — Case Study: The Merlin Software Factory
> (Section 16.1)
> **Last revised:** 2026-06-16
> **Use this for:** Documenting a significant architectural course
> correction so future contributors (human and AI) understand *why*
> the original design was abandoned, not just *that* it was.

A strategic pivot is **an ADR at the architectural-direction level**
— larger in scope than a single ADR, smaller than the full project
SPEC. It records the rationale for a significant change in
direction.

The original design is preserved as historical context. New work
references this document to understand the constraints the pivot
established.

**When to write one:**

- You are abandoning an architectural pattern that was previously
  central to the system
- The change affects how multiple agents (human or AI) approach the
  codebase
- The original design has measurable evidence of failure that
  justifies a public retrospective
- Future contributors will encounter the historical code and need
  to understand why it should not be extended

---

```markdown
# STRATEGIC_PIVOT: [Short title of the pivot]

## Status
Proposed | Adopted (date) | Reverted (date, reason)

## Decision Owner
[Name and role of the person accountable for this pivot]

## Date
[YYYY-MM-DD of adoption]

## Summary
[One paragraph: what changed, and what the new direction is.]

## The Original Design
[1-2 paragraphs: what the system was designed to do before the
pivot. Be concrete — name the architectural pattern, the modules
involved, the original rationale. This section is historical
record; it should remain accurate even after the pivot is fully
implemented.]

## Why the Original Design Failed (Measured, Not Felt)
[Evidence-based account of what went wrong. Include:
  - Specific metrics that degraded (throughput, cost, latency,
    coherence)
  - Specific failure modes that recurred (with frequency)
  - Specific operational pain points (with examples)
This section must cite measurements, not opinions. "It felt slow"
is not evidence. "Mean time from Work Order intake to merged PR
was 4.2 hours, of which 3.1 hours was inter-agent coordination
overhead" is evidence.]

## The New Direction
[Detailed description of the new design. Include:
  - What modules are central
  - What patterns are adopted
  - What patterns are deliberately rejected
  - What the system looks like for a new contributor]

## What This Means for New Work
[Specific, actionable guidance:
  - New code should [pattern].
  - New code MUST NOT extend [legacy module/pattern].
  - When in doubt, [decision heuristic].
  - The legacy code in [path] is preserved but slated for removal;
    do not add to it.]

## What This Means for Agent Sessions
[Specific guidance for AI agent sessions that will be working in
this codebase:
  - The CLAUDE.md / AGENTS.md context file has been updated to
    reflect the new direction.
  - Agents must use [new pattern] when implementing [scenario].
  - Agents must NOT extend [legacy pattern].
  - The historical code in [path] is preserved for reference but
    is on the forbidden-paths list for new generation.]

## What This Means for Operations
[Specific operational implications:
  - Deployment changes (if any)
  - Monitoring or alerting changes
  - Rollback strategy if the pivot needs to be reversed
  - Decommissioning timeline for legacy code]

## What We're Giving Up
[Honest accounting of what the new direction loses compared to the
original. Pivots are tradeoffs; the costs should be documented.
This protects future contributors from re-litigating decisions when
they encounter the cost without the context.]

## Validation Criteria
[How will we know the pivot was the right call? List specific
measurable outcomes:
  - [Metric 1] should improve by [X]% within [timeframe]
  - [Failure mode 1] should drop to zero
  - [Operational pain point 1] should be eliminated
If these criteria are not met within [review timeframe], the pivot
is reviewed and potentially reverted.]

## Historical Code Status
[Catalog of legacy code paths affected by the pivot:
  - `[path]` — original [purpose], deprecated [date], removal
    target [date]
  - `[path]` — original [purpose], deprecated [date], removal
    target [date]
These paths should be flagged in the CI as "do not extend" zones.]

## Related Decisions
- Original design: [link to original SPEC.md or design doc]
- Companion ADRs: [list]
- Subsequent ADRs that build on this pivot: [list, populated as
  they are written]

## Review Cadence
[When this document is reviewed:
  - First review: [date, typically 30 days after adoption]
  - Subsequent reviews: [cadence]
  - Trigger for ad-hoc review: [conditions]]
```

---

## Why a Separate Document

A pivot is **bigger than an ADR but smaller than a full project
SPEC**. It deserves its own canonical location for three reasons:

1. **Discoverability** — A new contributor (human or AI) should be
   able to find the pivot rationale in a single, well-known
   location, not buried in commit history or scattered across ADRs.
2. **Persistence** — Pivots affect the codebase for years. ADRs are
   incremental decisions; pivots are architectural-direction
   changes. They warrant a different document class.
3. **Communication** — The document signals to every future agent
   session that the codebase carries historical complexity for a
   documented reason, not by accident.

## Worked Example: Merlin Express Arc Pivot

In the Merlin Software Factory case (ch16), the
`STRATEGIC_PIVOT.md` documented the pivot from multi-agent pipeline
to express arc:

- **Original design**: Multi-agent pipeline with specialist agents
  (architect, builder, tester, reviewer) coordinating through a
  central pipeline
- **Why failed**: Handoff overhead consumed more tokens than
  specialization saved. Context compaction, coordination, and
  recovery dominated cycle time.
- **New direction**: Single primary agent owns
  investigate → plan → tests → implement → audit → ship. Quality
  gates fire inline.
- **What new work means**: All new agent infrastructure targets
  the express arc. The blueprint engine code is preserved but
  slated for removal.

See [`../patterns/express-arc.md`](../patterns/express-arc.md) for
the resulting architectural pattern.

## Pitfalls

- **The pivot without evidence.** "We're switching to X because Y
  feels more elegant" is not a pivot — it's a preference. Pivots
  require measured failure of the original.
- **The pivot without a deprecation plan.** If legacy code remains
  alive indefinitely, the pivot is half-done. Every pivot should
  include a decommissioning timeline.
- **The pivot that the CLAUDE.md doesn't reflect.** If the context
  file still describes the old direction, agent sessions will
  reproduce the old patterns. The pivot must update the context
  file in the same commit.
- **The forgotten pivot.** Pivots get adopted then forgotten. Six
  months later, a new contributor extends the legacy code because
  nobody pointed them to the document. Discoverability is the most
  critical property.

## Related

- `spec-md.md` — the project SPEC the pivot operates inside
- `adr-template.md` — for smaller architectural decisions that fall
  short of a full pivot
- `claude-md-template.md` — must be updated whenever a pivot is
  adopted
- [`../patterns/express-arc.md`](../patterns/express-arc.md) — the
  worked example of a pattern adopted via strategic pivot

## Provenance

Adapted from Chapter 16 of *Harnessing the Horse*, Section 16.1,
where the Merlin Software Factory's `STRATEGIC_PIVOT.md` is
described as the canonical record of the multi-agent → express-arc
decision.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
