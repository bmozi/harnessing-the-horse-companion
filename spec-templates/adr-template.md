# ADR Template (with Agent Implications)

> **Chapter:** ch09 — Architectural Stewardship (Section 9.3,
> "Architecture Decision Records in the Agentic Era")
> **Last revised:** 2026-06-16
> **Use this for:** Capturing architectural decisions so future agent
> sessions inherit the constraints — not just future humans.

Architecture Decision Records (Michael Nygard, "Documenting
Architecture Decisions," 2011) are short documents that capture the
context, decision, and consequences of significant architectural
choices.

In the agentic era, ADRs serve a **dual audience**:
- **Humans** who need to understand why a previous decision was made.
- **AI agents** that need to understand the constraints their
  generated code must respect.

This template adds the **Agent Implications** section that the
traditional ADR format does not include — the section that transforms
the ADR from a historical document humans might consult into a
machine-readable guardrail that agents receive automatically.

---

## Tier 1: Full ADR (multi-module, new pattern, long-term consequences)

```markdown
# ADR-[NNN]: [Short title of the decision]

## Status
Proposed | Accepted | Superseded by ADR-[NNN] | Deprecated

## Date
[YYYY-MM-DD]

## Context
[The forces at play. What is the problem we are trying to solve? What
constraints exist? What changed that requires a decision now?]

## Decision
[The choice we are making. State it as a positive declarative
sentence: "We will use X."]

## Alternatives Considered
- **[Alternative A]** — [Why considered. Why rejected.]
- **[Alternative B]** — [Why considered. Why rejected.]
- **[Alternative C]** — [Why considered. Why rejected.]

## Consequences

### Positive
- [What we gain]
- [What problems are solved]

### Negative
- [What we lose]
- [What problems are introduced or remain]

### Neutral
- [Tradeoffs accepted]

## Agent Implications

[This is the section that distinguishes an agentic-era ADR from a
traditional ADR. State explicitly how this decision constrains
future agent-generated code.]

- Any agent-generated code that [specific scenario] must use [specific
  pattern], not [the rejected alternative].
- The [pattern] is defined in [file:line or module path].
- Agents must [import / call / extend] [specific named API or class]
  rather than implementing their own [equivalent mechanism].
- If a task specification requires [scenario] and does not reference
  [the required API], the specification is incomplete — flag this as
  a scope expansion request in IMPL_NOTES.md.
- [Any test that should run to verify the decision is being followed]

## References
- [Link to related ADRs]
- [Link to relevant SPEC.md / DESIGN.md]
- [External references — papers, books, RFCs]
```

---

## Tier 2: Lightweight ADR (single module, establishes precedent)

For decisions affecting a single module but establishing a precedent.
Captured as a structured entry inside `IMPL_NOTES.md`:

```markdown
## Decision: [Short title]

**Date:** [YYYY-MM-DD]
**Decision:** [What we are doing]
**Reason:** [Why — the 1-paragraph rationale]
**Agent Implications:** [How this constrains future agent sessions in
this module]
```

Promote to Tier 1 if the pattern is adopted by other modules.

---

## Tier 3: Implicit ADR (captured in code conventions)

For decisions captured in the code itself — naming conventions, error
handling patterns, retry strategies. These are not separate documents.
They live as module conventions in `AGENTS.md` / `CLAUDE.md`. Same
purpose as a formal ADR (providing context for future agent sessions)
without the overhead of a separate document.

---

## Worked Example: Agent Implications in Practice

For a decision to use PostgreSQL advisory locks for idempotency
instead of a unique constraint approach (because advisory locks allow
detection of "in-progress" events, not just the case where a previous
processing attempt completed):

> **Agent Implications.** Any agent-generated code that implements
> idempotency in this service must use PostgreSQL advisory locks, not
> unique constraints. The advisory lock pattern is defined in
> `/services/common/idempotency.py`. Agents must import and use the
> existing `IdempotencyGuard` class rather than implementing their own
> idempotency mechanism. If a task specification requires idempotency
> and does not reference `IdempotencyGuard`, the specification is
> incomplete — flag this as a scope expansion request in
> IMPL_NOTES.md.

This explicit constraint is specific (use this class), actionable
(import from this path), and testable (the integration tests verify
the correct pattern is used).

## The ADR-to-Prompt Pipeline

The most effective use of ADRs in agentic development is systematic:

1. ADRs are referenced in `AGENTS.md` / `CLAUDE.md` (the context file
   template includes this in its Architecture Boundaries section).
2. When a session is initiated, the task specification identifies the
   modules that will be modified.
3. Relevant ADRs (mapped to the affected modules) are surfaced in the
   agent's context — directly for short ADRs, as summaries with
   references for long ones.
4. The agent receives not just the task spec but the architectural
   decisions that constrain how the task should be implemented.

An ADR that is not in the agent's context is, for the purposes of
agentic development, an ADR that does not exist.

## Common Failure Modes

- **The Decision Without a Record.** Team discusses an approach in a
  meeting, reaches a decision, implements it — but no ADR is written.
  Three months later, an agent session encounters the same problem
  and proposes a different approach. The team re-debates a settled
  decision.
- **The ADR That Lives Alone.** Written and stored in `/docs/adr/`
  but never referenced in `AGENTS.md` or included in any agent
  session's context. The ADR exists. It informs no one.
- **The ADR With No Agent Implications.** Written in the traditional
  format. Humans understand it. Agents do not. The dual-audience
  function is lost.

## Related

- `claude-md-template.md` — the context file references ADRs by index
- `../checklists/impact-boundary-assessment.md` — used to decide when
  a change requires a new ADR
- `impl-notes-md.md` — Tier 2 lightweight ADRs live here

## Provenance

Adapted from Chapter 9 of *Harnessing the Horse*, Section 9.3. The
underlying ADR format is from Michael Nygard, "Documenting
Architecture Decisions," 2011. The Agent Implications section and
the three-tier approach are the book's adaptation for agentic
development.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
