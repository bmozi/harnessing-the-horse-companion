# Pattern Quick Reference

Twelve patterns referenced across the book, each with its
original citation, the problem it solves, and one paragraph
on its application in agentic development. This online reference
replaces the former print appendix. For full reference
cards with implementation guidance, worked examples, and
related patterns, see the `patterns/` directory of the
companion repository.

The patterns are ordered by where they first appear in the
book. Each is referenced from multiple chapters because the
patterns compose — Hexagonal Architecture provides the
boundary that the Anti-Corruption Layer translates across;
the Transactional Outbox makes Event Sourcing tractable;
Scoped Authorization Tokens constrain what every other tool
in the system can do.

---

## 1. Anti-Corruption Layer (ACL)

**Origin.** Eric Evans, *Domain-Driven Design: Tackling
Complexity in the Heart of Software*, Addison-Wesley, 2003,
ISBN 978-0321125217. Full citation discipline and worked
examples appear in Chapter 11 §11.1.

**Intent.** Protect a bounded context from contamination
when integrating with external systems whose models do not
align with the internal domain.

**Application in agentic development.** Each AI agent session
starts fresh — it cannot internalize vendor quirks the way a
human developer eventually does. Without an ACL, every
session must be told about every vendor naming inconsistency,
typo, and semantic mismatch. The ACL eliminates this entire
class of context requirement: the agent generates code
against the domain model, and the ACL handles translation at
the boundary. Vendor specificity is contained in the adapter,
where it cannot leak into business logic. See Chapter 11
§11.1; companion `patterns/anti-corruption-layer.md`.

---

## 2. Hexagonal Architecture (Ports and Adapters)

**Origin.** Alistair Cockburn, "Hexagonal Architecture,"
Portland Pattern Repository wiki, 2005. Book-length
treatment: Cockburn and Juan Manuel Garrido de Paz, 2024.
Full citation discipline appears in Chapter 11 §11.2.

**Intent.** Allow an application to be equally driven by
users, programs, automated tests, or batch scripts, and to
be developed and tested in isolation from its runtime
devices and databases.

**Application in agentic development.** Agent-generated
business logic targets ports, never adapters. The agent
need not know whether the persistence layer is PostgreSQL
or DynamoDB; the database choice is the adapter's concern.
This separation gives agent-generated business logic the
property of *surviving infrastructure changes without
modification*. It also enables the test discipline of
Standard 8 (Chapter 8): the same logic runs against a
real adapter in production and an in-memory adapter in
tests. See Chapter 11 §11.2; companion
`patterns/hexagonal-architecture.md`.

---

## 3. Idempotent Receiver

**Origin.** Gregor Hohpe and Bobby Woolf, *Enterprise
Integration Patterns: Designing, Building, and Deploying
Messaging Solutions*, Addison-Wesley, 2003, ISBN
978-0321200686 (Chapter 10). Full citation discipline
appears in Chapter 11 §11.3.

**Intent.** Ensure that a message can be processed multiple
times without producing duplicate side effects.

**Application in agentic development.** AI agents,
optimizing for the functional specification, consistently
underestimate the importance of idempotency. An agent asked
to "implement a webhook handler" will produce one that
processes the event correctly but breaks on duplicate
delivery. The Idempotent Receiver pattern must be
specified in the acceptance criteria (Standard 1) and
enforced in review (Standard 7). Three implementation
approaches: naturally idempotent operations, deduplication
by message identifier, and version-based application. See
Chapter 11 §11.3; the composite-key idempotency store
implementation appears in Chapter 13 §13.3.

---

## 4. Circuit Breaker

**Origin.** Michael Nygard, *Release It! Design and Deploy
Production-Ready Software*, Pragmatic Bookshelf, 2007,
ISBN 978-0978739218. Full citation discipline appears in
Chapter 11 §11.4.

**Intent.** Prevent cascade failure when an integration
partner becomes unavailable, by failing fast and
periodically probing for recovery.

**Application in agentic development.** Agent-generated
components calling vendor APIs create retry storms: a
generated job retries transient failures in a tight loop
and exhausts the shared rate budget. The breaker at the
vendor boundary trips on a failure threshold and fails
fast with backoff, externalizing the operational
constraint (rate limits, timeouts, vendor outages) from
the generated code into the infrastructure — so the
agent's prompt does not need to encode failure-mode
reasoning. See Chapter 11 §11.4. A secondary use is
infrastructure failover: the Merlin agent gateway
(Chapter 16) applies breakers across five LLM backends,
falling through to the next when one degrades.

**Companion pattern: Centrifuge.** Segment's Centrifuge
(Segment engineering, 2018) extends the breaker where
multiple sources share one rate-limited downstream:
per-source virtual queues with isolated token-bucket rate
budgets, so one source's quota exhaustion affects no one
else. The Fieldstone CRM Hub allocates HubSpot's
per-account API quota this way across its six integration
sources. See Chapter 11 §11.4; Chapters 12 and 14.

---

## 5. Transactional Outbox

**Origin.** Pattern named by Chris Richardson
(microservices.io); concept rooted in Pat Helland, "Life
Beyond Distributed Transactions," CIDR 2007. Detailed
treatment: Chris Richardson, *Microservices Patterns: With
Examples in Java*, Manning, 2018, ISBN 978-1617294549. Full
citation discipline appears in Chapter 11 §11.5.

**Intent.** Atomically update a database and publish a
message without using distributed transactions.

**Application in agentic development.** Agent-generated
code is particularly vulnerable to the dual-write problem
because AI agents do not naturally reason about failure
boundaries. The Transactional Outbox provides a structural
solution that does not depend on the agent's awareness: the
generated code writes its business state and its
notification intent in the same transaction; the outbox
publisher handles delivery. Atomicity becomes
architectural, not cognitive. See Chapter 11 §11.5;
companion `patterns/transactional-outbox.md` and
`code-examples/transactional-outbox/`.

---

## 6. Strangler Fig

**Origin.** Martin Fowler, "StranglerFigApplication,"
martinfowler.com, 2004. Full citation discipline appears in
Chapter 12 §12.1.

**Intent.** Gradually replace a legacy system by building
new components alongside it and incrementally routing
traffic from old to new.

**Application in agentic development.** AI agents make
migration *execution* fast — each replacement component is
a well-scoped, specification-driven task. They do not make
migration *verification* fast: proving that the new
component behaves identically to the legacy in all cases
remains a human judgment task. Teams should plan for
verification time at 2–5× generation time (author's
planning heuristic). See Chapter 12
§12.1; the Fieldstone CRM Hub (Chapter 14) and the FieldstoneOS
platform modernization design study (Appendix D) are worked
examples at 6-month and 5-year scales.

---

## 7. Saga

**Origin.** Hector Garcia-Molina and Kenneth Salem, "Sagas,"
*ACM SIGMOD International Conference on Management of Data*,
1987.

**Intent.** Coordinate a multi-step transaction across
services without distributed two-phase commit, by composing
forward steps with compensating transactions.

**Application in agentic development.** Customer-facing
booking flows, e-commerce checkouts, and multi-service
provisioning all require this pattern. Compensating
transactions are not "undo" — they are forward-moving
operations that neutralize the effect of a completed step
when a later step fails. AI agents generating saga code
must be specified with all failure paths enumerated; the
most common failure mode is omitted compensation. See
Chapter 12 §12.4 (coordinating distributed migration work)
and Chapter 15 (customer-facing transaction safety).

---

## 8. CAS-Guarded Distributed Commit

**Origin.** Maurice Herlihy, "Wait-Free Synchronization,"
*ACM Transactions on Programming Languages and Systems*,
1991 (CAS primitive). Application to distributed workflow
coordination: this book, Chapter 15.

**Intent.** Implement exactly-once semantics for a sequence
of non-idempotent calls across services that do not
cooperate on idempotency, using an atomic compare-and-swap
on entry and per-step checkpoints.

**Application in agentic development.** The state machine
prevents concurrent retries from re-executing. The per-step
checkpoints ensure that a retry after partial completion
skips already-completed steps. The architecture makes the
most dangerous operation (the charge) the one with the
strongest idempotency guarantee — eliminating
double-charges by construction. Agent-generated code does
not need to reason about failure boundaries; the
architecture makes the wrong behavior impossible. See
Chapter 13 §13.3 (multi-step agent workflows) and Chapter
15 (booking-flow case study).

---

## 9. Event Sourcing

**Origin.** Greg Young, "Event Sourcing," 2006. Refined
through community work on CQRS and Domain-Driven Design.

**Intent.** Persist every state change as an immutable
event; current state is a projection.

**Application in agentic development.** Three properties
matter for agents: (1) audit trail by construction — every
change carries actor metadata including agent session ID;
(2) temporal queries for migration validation — replay
events to time T and compare; (3) projection-based read
models that give MCP servers sub-second access to rich
historical context. See Appendix D; the FieldstoneOS
Unified Customer Object is the design-study example.

---

## 10. Scoped Authorization Token

**Origin.** Jerome Saltzer and Michael Schroeder, "The
Protection of Information in Computer Systems,"
*Proceedings of the IEEE*, 1975 (Principle of Least
Privilege). Formalization in session-token form: OAuth 2.0
scope, RFC 6749, 2012. Macaroons: Birgisson et al., 2014.

**Intent.** Constrain a session's authority to the
minimum required for its task.

**Application in agentic development.** Each agent session
receives a token whose scope specifies which tools it can
invoke and with what parameters. Four scope levels:
read-only, domain-scoped mutation, record-scoped mutation,
full access. A compromised session is bounded by the
scope; a misinterpreted task fails at the scope check
rather than succeeding incorrectly. The pattern applies to
both human session tokens (Chapter 15 booking flow) and
agent session tokens (Chapter 13 MCP fleet) — same
principle, two different consumer classes. See Chapter 13
§13.1; companion `patterns/scoped-authorization-token.md`.

---

## 11. Dry-Run-Default on Write Tools

**Origin.** This book, 2026. Named here for the first time
as a design discipline. Applies long-standing CLI dry-run
mode (`rsync --dry-run`, `terraform plan`) as the
*default* for any agent-facing tool that modifies state.

**Intent.** Make the agent's first invocation of any write
tool read-only and reversible; require an explicit
`confirm: true` for actual execution.

**Application in agentic development.** Agents make
mistakes that are difficult to reverse. Dry-run-default
ensures that the agent's first action is always safe. The
destructive action requires a deliberate second step. The
pattern composes with Scoped Authorization Token (Pattern
10) — the scope check runs before the dry-run gate, the
dry-run gate runs before any side effect. See Chapter 13
§13.1; companion `patterns/dry-run-default.md` and
`code-examples/mcp-tool-pattern/`.

---

## 12. Express Arc

**Origin.** This book, 2026. The pattern emerged in the
Merlin Software Factory engagement as a deliberate pivot
away from the original multi-agent specialist pipeline.

**Intent.** A single primary agent owns the entire delivery
sequence — investigate, plan, tests, implement, audit,
ship — without handoffs to specialist agents. Quality gates
fire as inline self-checks.

**Application in agentic development.** Handoffs between
specialist agents consume more tokens (context compaction,
coordination, recovery) than the specialization saves. The
express arc eliminates handoffs. Single-channel reasoning
also eliminates the "auditor tag-text drift" class of bug
where machine-readable verdicts diverge from the prose the
reviewing agent produces. The pattern must pair with
bounded iteration caps (Standard 6) — without them, the
single-agent advantage becomes a single-agent runaway. See
Chapter 16; companion `patterns/express-arc.md`.

---

The catalog above is a quick reference, not a substitute
for the chapter treatment. Each pattern's full discussion —
how it interacts with other patterns, what its failure
modes are, what to specify in SPEC.md to constrain
agent-generated code that uses it — lives in the chapter
that introduces it.

For the patterns named in this book for the first time
(8, 11, 12), the chapter treatment is the canonical
reference — Pattern 8 rests on Herlihy's CAS primitive,
but its application to distributed workflow coordination
is this book's. For the established patterns (1–7 and
9–10), the original sources remain authoritative; this
catalog documents only the *agentic-development
application*.
