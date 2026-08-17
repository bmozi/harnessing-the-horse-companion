# Express Arc: Single Agent, End-to-End Delivery

> **Chapter:** ch16 — Case Study: The Merlin Software Factory (Section 16.1)
> **Last revised:** 2026-06-16

## Origin

Named in this book (2026). The pattern emerged in the Merlin
Software Factory engagement as a deliberate pivot away from the
original multi-agent specialist pipeline.

## Intent

**A single primary agent owns the entire delivery sequence — from
investigation through plan, tests, implementation, self-audit, and
ship — without handoffs to specialist agents.**

Quality gates fire as **inline checks** during execution rather than
as separate pipeline stages with handoffs between them.

## The Pivot

The original Merlin design was a multi-agent pipeline with
specialist agents (architect, builder, tester, reviewer)
coordinating through a central pipeline. It failed for a predictable
reason: **handoff overhead**.

Each handoff requires:

- **Context compaction** — summarizing the previous agent's output
  to fit the next agent's context window
- **Coordination** — ensuring the next agent has the right tools,
  permissions, and scope
- **Recovery** — handling the case where the next agent's output
  contradicts the previous agent's decisions

The handoff overhead **consumed more time and tokens than the
specialization saved**.

The express arc eliminated handoffs. One agent, with access to all
tools, owns the entire delivery. The result:

- **Higher throughput** (merged PRs per week)
- **Lower cost** (fewer tokens consumed on compaction and
  coordination)
- **More coherent output** (no semantic drift between agents with
  different context windows)

## The Single-Channel Property

The express arc has a structural property the multi-agent pipeline
cannot match: **a single reasoning channel**.

In multi-agent systems, separate channels can drift. Auditor agents
produce verdicts as **both** machine-readable severity tags *and*
natural-language prose; the aggregator dispatches off the tags, the
developer agent reads the prose. When the tags and the prose
disagree (because they were produced by different reasoning paths),
the system makes incorrect decisions.

> The system diagnosed its own bug, identified the architectural
> reason the bug existed, and observed that its own strategic
> evolution would render the fix unnecessary. The separate tag and
> text channels cannot drift if there is only one channel.

The express arc eliminates this entire class of bug.

## When to Use This

Strong indicators:

- The work fits within a single agent's context window across the
  full delivery arc
- Quality gates can be expressed as inline checks (linters, test
  runners, security scanners) rather than requiring a specialist
  agent
- Coordination overhead between specialists exceeds the
  specialization benefit (often true with current frontier models)
- Throughput and coherence matter more than maximum specialization

Weak indicators (consider multi-agent specialization instead):

- Different parts of the delivery genuinely require different
  models with different capabilities
- The arc legitimately requires more context than any single agent
  can hold
- Specialist agents already exist as services consumed by other
  systems (the specialization has compounding value outside this
  arc)

## Structure

```
Single Agent Session
┌────────────────────────────────────────────────────────┐
│  Investigate  →  Plan  →  Tests  →  Implement  →       │
│       ▼            ▼         ▼          ▼              │
│   [gate G1]    [gate G2]  [gate G3]  [gate G4...G6]    │
│                                                         │
│       Audit  →  Ship                                    │
│         ▼         ▼                                     │
│     [gate G7]  [gate G8, G9]                            │
└────────────────────────────────────────────────────────┘
```

Quality gates classify as **BLOCKING / ADVISORY / INFORMATIONAL /
ASYNC** (see Chapter 8 Standard 9). A BLOCKING gate failure halts the agent
mid-arc; the agent surfaces to human review or attempts a bounded
rework iteration.

## Bounded Iteration as Companion Discipline

The express arc must be paired with **bounded iteration caps** (see
[`../checklists/iteration-caps.md`](../checklists/iteration-caps.md)).
Without iteration bounds, a single agent owning the entire arc can
enter a rework loop that consumes thousands of dollars in API costs
producing increasingly divergent output.

Typical bounds from Merlin:

- Max 2 CI fix iterations per gate failure
- Max 25 tool-use iterations per agent loop
- Daily token budget enforced at the session level

The bounds ensure that **failure is cheap and visible** — a session
that exhausts its iteration count surfaces the failure to the
operator rather than continuing to thrash.

## Pitfalls

- **The unbounded express arc.** Without iteration caps, the
  single-agent advantage becomes a single-agent runaway.
- **The over-stuffed context.** A single agent owning the entire
  arc holds more context than necessary at any given moment.
  Architecture-as-code and explicit non-goals (negative space
  documentation) become essential.
- **The implicit handoff.** If the agent calls subagents or
  delegates to specialist tools that themselves run multi-step
  reasoning, you've reintroduced the handoff overhead. Inline
  checks should be deterministic computations, not specialist
  agents.
- **The premature multi-agent reach.** Reaching for specialist
  agents because "this task is complex" before measuring whether
  the express arc handles it. Default to express; introduce
  specialists only when measurement proves the specialization
  benefit exceeds the coordination cost.

## Worked Example: Merlin Software Factory

- Single primary agent owns investigate → plan → tests →
  implementation → self-audit → ship
- G1–G9 quality gates fire inline (no separate stages)
- CI fix iterations capped at 2
- Tool-use loops capped at 25 iterations
- Daily token budgets enforced
- Strategic decision recorded in `STRATEGIC_PIVOT.md` (see
  [`../spec-templates/strategic-pivot-template.md`](../spec-templates/strategic-pivot-template.md))
- Five backend options (Codex, Codex CLI, Claude CLI, nimue,
  Anthropic API) selected by preference with circuit-breaker
  fallthrough

## Related

- [`../spec-templates/strategic-pivot-template.md`](../spec-templates/strategic-pivot-template.md)
  — template for recording the decision to adopt the express arc
- [`../checklists/iteration-caps.md`](../checklists/iteration-caps.md)
  — the companion bounded-iteration discipline
- [`../checklists/self-improvement-safety-rails.md`](../checklists/self-improvement-safety-rails.md)
  — when the express arc agent also has self-improvement
  capabilities
- **Single-responsibility sessions** (ch05 Std 2, Scope Definition
  and Session Boundaries) — the express arc is the same
  single-responsibility principle applied at the delivery-arc
  level, not just the task level

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
