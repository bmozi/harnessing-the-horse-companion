# Transactional Outbox

> **Chapter:** ch11 — Integration Patterns (Section 11.5)
> **Last revised:** 2026-06-16

## Origin

Pattern named by Chris Richardson in his microservices pattern
catalog (microservices.io, contributing to *Microservice Patterns*,
Manning, 2018). The concept has roots in Pat Helland, "Life Beyond
Distributed Transactions" (CIDR, 2007).

## Intent

**Atomically update a database and publish a message without using
distributed transactions.**

The problem: a service that writes to its database and then publishes
an event can fail between the two operations — the database write
succeeds but the event publication fails (data changes without
notification), or the event is published but the database write
fails (notification without data change). Both failures produce
inconsistency that is difficult to detect and expensive to repair.

The solution: write the message into an outbox table **in the same
database transaction** as the business update. A separate process
(polling publisher or change data capture) reads the outbox and
publishes the messages. The business write and the message are
atomically consistent because they are in the same transaction.

## Application in Agentic Development

Agent-generated code is particularly vulnerable to the dual-write
problem because **AI agents do not naturally reason about failure
boundaries**.

An agent asked to "process an inbound webhook and notify internal
systems" will generate code that processes the webhook and then
sends a notification. The agent does not naturally consider:

- What happens if the notification send fails *after* the processing
  succeeds?
- What happens if the processing fails *after* the notification is
  sent?

The Transactional Outbox provides a **structural solution that does
not depend on the agent's awareness of failure modes**. The generated
code writes its business state and its notification intent in the
same transaction. The outbox publisher handles the delivery.

- If the delivery fails → the outbox retries.
- If the processing fails → no outbox row is written, no notification
  is sent.

**The atomicity is structural, not cognitive.** It does not require
the agent to reason about failure boundaries because the architecture
makes the wrong behavior impossible.

## Worked Application: Fieldstone CRM Hub

In the Fieldstone CRM Hub, the Transactional Outbox appears in the
inbound webhook rebroadcast path:

1. Hub receives a HubSpot webhook
2. Validates the HMAC signature
3. Inserts into the idempotency key table
4. **In the same transaction**: inserts a rebroadcast row into the
   outbox table specifying which internal Service Bus topic should
   receive the event
5. Webhook receiver acknowledges HubSpot immediately upon
   transaction commit — within HubSpot's five-second webhook timeout
6. A separate worker reads the outbox and publishes to Service Bus
   asynchronously

This means an agent generating a new webhook handler for the Hub
**does not need to solve the dual-write problem**. The agent
generates the business logic (validate, deduplicate, transform) and
writes to the outbox. The outbox infrastructure handles the
messaging.

> The pattern is a guardrail that makes the correct behavior the
> easy behavior.

## Implementation

See [`../code-examples/transactional-outbox/`](../code-examples/transactional-outbox/):

- `schema.sql` — the outbox table DDL (PostgreSQL)
- `handler.ts` — agent-generated TypeScript webhook handler showing
  the three-step template: check idempotency → write business state
  → write to outbox, all in one transaction

The agent that generates the handler follows a three-step template
without needing to understand distributed transactions. **The
architecture makes exactly-once semantics the default path.**

## Pitfalls

- **The outbox without a publisher.** The outbox table accumulates
  rows. Nobody publishes them. Six months later, nothing has been
  notified. Always deploy the publisher with the outbox; treat them
  as one unit.
- **The publisher without idempotency.** The publisher reads a row,
  publishes the event, and fails before marking the row published.
  The next read republishes. Either the consumer must be idempotent
  (see [`anti-corruption-layer.md`](anti-corruption-layer.md) for the
  Idempotent Receiver companion) or the publisher must use exactly-
  once delivery semantics on the message bus.
- **The retention discipline that isn't.** Published rows accumulate
  forever. The table grows. Index performance degrades. Implement a
  retention policy (typically delete after publication confirmed AND
  N days have elapsed for audit purposes).
- **The mixed-database trap.** If the business write is in one
  database and the outbox is in another, you're back to the
  dual-write problem. Outbox lives in the same database as the
  business state.

## Related

- [`../code-examples/transactional-outbox/`](../code-examples/transactional-outbox/)
  — runnable SQL schema + TypeScript handler
- **Idempotent Receiver** (Hohpe & Woolf, 2003) — the companion
  pattern on the consumer side; see `README.md` for the chapter
  reference
- [`anti-corruption-layer.md`](anti-corruption-layer.md) — the
  outbox row's payload should be in domain terms, not vendor terms

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
