# Event Sourcing

> **Chapter:** appendix-d — Design Study: Platform Modernization
> (Section D.2)
> **Last revised:** 2026-06-16

## Origin

Greg Young, "Event Sourcing" (2006); refined through community work
on CQRS and DDD. Earlier roots in financial-systems append-only
ledgers and database transaction logs.

## Intent

**Every state change is an append-only event. The current state is
a projection.**

Instead of mutating rows in place ("UPDATE customer SET email = ?"),
record the change as an immutable event ("CustomerEmailChanged" with
timestamp, actor, old value, new value). Projections — materialized
read tables — are maintained by consumer services that subscribe to
the event stream.

## Three Properties Architecturally Significant for Agentic Development

### 1. Audit trail by construction

Every change to state is **an event that includes what changed,
when, and why**. When an AI agent generates code that modifies
data, the modification is captured as an event with the agent
session identifier in its metadata.

The audit trail that Standard 11 (Chapter 10) requires is **built
into the architecture, not added as an afterthought**. The agent
cannot forget to log; the architecture has no other path.

### 2. Temporal queries for migration validation

During a multi-year migration (e.g., Strangler Fig at platform
scale), you need to compare the old system's state at a point in
time with the new system's state at the same point.

Event sourcing enables this: **replay events up to time T and
compare**. Discrepancies indicate the migration is not producing
equivalent results. See
[`../checklists/equivalence-test-checklist.md`](../checklists/equivalence-test-checklist.md)
for the testing discipline.

### 3. Projection-based read models for AI agent access

When an MCP server needs to provide an AI agent with a customer's
complete interaction history — every service call, every billing
event, every compliance record — a projection serves that request
**from a denormalized read table in sub-second time** rather than
joining across multiple normalized tables in a query that would take
seconds or minutes.

This is why MCP server fleet architecture (Chapter 13) maps onto
event-sourced systems: one MCP server per operational domain
(customer, billing, scheduling, compliance), each querying its
domain's projection tables.

## Structure

```
Operational Service                Message Bus              Consumer Services
─────────────────                  ───────────              ──────────────────
1. State change request                                     
2. Write event to outbox table          Kafka                  
   (in same transaction as              ──► uco.customer.events ──► Analytics projection
   any other writes)                                         ──► Compliance projection
                                                             ──► Scheduling projection
3. Outbox publisher reads
   and publishes to Kafka
```

The companion pattern is the **Transactional Outbox** (see
[`transactional-outbox.md`](transactional-outbox.md)) — it ensures
event publication matches database commit ordering. Each operational
service writes events to a local outbox table inside the same
database transaction as the state change. A separate publisher
process drains the outbox to the message bus.

## Per-Aggregate Ordering Guarantee

Events are published to per-aggregate Kafka topics — e.g.,
`uco.customer.events`, `uco.subscription.events` — each **keyed by
aggregate ID** (customer ID, subscription ID) to guarantee
per-aggregate ordering.

Without per-aggregate keying, projections process events out of
order and produce inconsistent state. The aggregate ID as the
partition key is the structural property that preserves causal
ordering for the events that matter while allowing parallelism
across independent aggregates.

## Projection Consistency Model

Projections are **eventually consistent**, not strongly consistent.

Sub-second strong consistency would require synchronous projection
maintenance, which would couple every event-producing operation to
every event-consuming projection — defeating the purpose. The
architecture deliberately accepts eventual consistency in exchange
for projection independence.

For read paths that require strong consistency (the customer's
billing must agree with their payment record *right now*), use the
authoritative service's primary database, not the projection.

## When to Use This

Strong indicators:

- **Audit requirements** are first-class (regulatory, compliance,
  financial)
- **Multi-system migration** is planned where you need to validate
  equivalence over historical state
- **AI agents need rich read access** to historical events
  (customer 360, complete interaction history, pattern detection)
- The data has natural **per-aggregate event ordering** (one
  customer's events have causal order, but events across customers
  do not)

Weak indicators (probably not worth it):

- Simple CRUD application with no audit requirements
- All read access is "current state" (no temporal queries)
- No downstream consumers benefit from independent projections

## Worked Example: FieldstoneOS Unified Customer Object

From the platform modernization design study (Appendix D), a
documented architecture and migration plan:

- Per-aggregate topics: `uco.customer.events`,
  `uco.subscription.events`, `uco.appointment.events`
- Outbox-driven publication (Transactional Outbox)
- Projections per consumer: analytics for executive dashboards,
  scheduling for technician route views, compliance for regulatory
  reporting
- The projection model is what enables the MCP server fleet to
  serve AI agent queries in sub-second time

## Pitfalls

- **The schema migration trap.** Events are immutable. You cannot
  alter an old event's shape; you must version the event schema
  and have projections handle multiple versions. Plan for schema
  evolution from day one.
- **The synchronous projection.** If a projection blocks the write
  path, you've lost the independence benefit. Projections are
  **always** eventual.
- **The missing replay capability.** "We can replay" must be tested,
  not assumed. Rebuilding a projection from scratch should be a
  routine operation; if it isn't, you'll find out when you need it.
- **The event without the actor.** Every event should include
  *who* made the change (user ID, agent session ID, system). Without
  this, the audit trail is incomplete.
- **Over-eventing.** Not every internal computation needs to be an
  event. Events represent **state changes that consumers care
  about**, not every method call. Domain events, not implementation
  events.

## Related

- [`transactional-outbox.md`](transactional-outbox.md) — companion
  pattern for atomic event publication
- [`../checklists/equivalence-test-checklist.md`](../checklists/equivalence-test-checklist.md)
  — testing discipline for migrations that depend on event
  sourcing's temporal-query capability
- [`hexagonal-architecture.md`](hexagonal-architecture.md) — the
  containing pattern; the event-publishing port is a secondary
  adapter
- **CQRS** (Greg Young, 2010) — frequently paired with Event
  Sourcing; see [`README.md`](README.md) for the catalog reference

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
