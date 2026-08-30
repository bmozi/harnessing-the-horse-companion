# Pattern Catalog

Named architectural patterns referenced across *Harnessing the
Horse*, with their original citations and their application to
agentic development.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and
> case-study context that make these patterns concrete in practice.
> Pattern reference cards in this directory are licensed under
> CC BY-NC-SA 4.0 ([see `../LICENSE-CONTENT`](../LICENSE-CONTENT)).

## What's here

Each pattern reference card follows the same structure:

- **Origin** — author, year, venue (the canonical citation)
- **Intent** — what the pattern solves
- **Application in Agentic Development** — what it specifically
  prevents in AI-generated code
- **Implementation** — pointer to `../code-examples/` when one exists
- **Pitfalls** — common failure modes
- **Related** — companion templates and other patterns

## Patterns with Reference Cards

### Integration patterns (Chapter 11)

| Pattern | Origin | Card |
| --- | --- | --- |
| Anti-Corruption Layer | Evans (2003) | [`anti-corruption-layer.md`](anti-corruption-layer.md) |
| Hexagonal Architecture | Cockburn (2005) | [`hexagonal-architecture.md`](hexagonal-architecture.md) |
| Transactional Outbox | Richardson / Helland (2007) | [`transactional-outbox.md`](transactional-outbox.md) |

### Agent infrastructure patterns (Chapter 13)

| Pattern | Origin | Card |
| --- | --- | --- |
| Dry-Run-Default on Write Tools | This book (2026) | [`dry-run-default.md`](dry-run-default.md) |
| Scoped Authorization Token | Saltzer & Schroeder (1975) / OAuth 2.0 RFC 6749 (2012) | [`scoped-authorization-token.md`](scoped-authorization-token.md) |

### Case-study-grounded patterns (Part IV and Appendix B)

| Pattern | Origin | Card |
| --- | --- | --- |
| CAS-Guarded Distributed Commit | Herlihy (1991) — applied to distributed commit in Ch15 | [`cas-guarded-distributed-commit.md`](cas-guarded-distributed-commit.md) |
| Event Sourcing | Greg Young (2006) — design study in Appendix B | [`event-sourcing.md`](event-sourcing.md) |
| Express Arc | This book (2026) — emerged in Ch16 Merlin Software Factory | [`express-arc.md`](express-arc.md) |

## Patterns Referenced in the Book (Prose Coverage)

These patterns are intentionally covered in the book rather than duplicated as
standalone companion cards. Each cites the original work and is treated in
prose in the relevant chapter section.

### Enterprise Integration Patterns (Hohpe & Woolf, 2003)

Referenced throughout Chapter 11 §11.3.

- **Message Bus** — decouples agent-generated components through
  shared messaging infrastructure
- **Idempotent Receiver** — handles at-least-once delivery; three
  implementation approaches (naturally idempotent, deduplication,
  versioning) are discussed
- **Dead Letter Channel** — destination for messages that cannot be
  processed; captures failure modes the generating session did not
  anticipate
- **Content-Based Router** — maps directly to multi-agent
  orchestration

### Resilience patterns (Chapter 11 §11.4)

- **Circuit Breaker** — Michael Nygard, *Release It!* (Pragmatic
  Bookshelf, 2007). Prevents cascade failure at vendor boundaries.
- **Centrifuge Pattern** — Twilio Segment (2018). Virtual queues with
  isolated rate budgets.

### Agent-API patterns (Chapter 13)

- **Composite-Key Idempotency Store** — Hohpe & Woolf + Stripe-style
  cached responses (Brandur Leach, "Implementing Stripe-like
  idempotency keys in Postgres," 2017)
- **CAS-Guarded Distributed Commit** — Maurice Herlihy, "Wait-Free
  Synchronization," *ACM Transactions on Programming Languages and
  Systems*, 1991, applied to distributed workflows
- **Backend for Frontend (BFF)** — Sam Newman, *Building
  Microservices* (O'Reilly, 2015). Adapted as "BFF for Agents."

### Strangler Fig Migration (Chapter 12 §12.1)

- **Strangler Fig** — Martin Fowler (2004). Six-phase migration
  approach with feature flags. Worked example from the Fieldstone CRM
  Hub engagement is in the chapter.

### Domain-Driven Design (Chapter 12 §12.4)

- **Event Sourcing** — Greg Young (2006)
- **CQRS** — Greg Young (2010)
- **Bounded Contexts** — Eric Evans, DDD

## Why the catalog matters for agentic development

Every named pattern in this catalog has decades of production
validation. What is new is their application to agentic development,
where they serve a **dual purpose**:

1. They protect the system from the specific failure modes of
   AI-generated code (vendor coupling, hallucinated interfaces,
   missed failure boundaries, scope expansion).
2. They simplify the context that AI agents need to generate
   correct code. Patterns are vocabulary the agent can rely on.

When the architecture provides the pattern, the agent does not need
to reason about the underlying complexity. The pattern is the
guardrail that makes the correct behavior the easy behavior — which
is precisely the relationship between architecture and agent-
generated code that this book is about.

## Related

- `../spec-templates/adr-template.md` — capture the architectural
  decision to adopt a specific pattern with explicit Agent
  Implications
- `../code-examples/` — runnable code for patterns where a code
  example exists
