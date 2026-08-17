# Transactional Outbox (PostgreSQL + TypeScript)

> **Chapter:** ch11 — Integration Patterns (Section 11.5)
> **Pattern:** [Transactional Outbox](../../patterns/transactional-outbox.md)

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and
> case-study context that make these patterns concrete in practice.
> **Source code in this directory is licensed under the MIT License**
> ([see `../../LICENSE-CODE`](../../LICENSE-CODE)) — drop into your
> own projects with confidence, including commercial work.

## Files

| File | What it is |
| --- | --- |
| [`schema.sql`](schema.sql) | The `outbox` table DDL plus the companion `idempotency_keys` table. PostgreSQL. |
| [`handler.ts`](handler.ts) | Agent-generated webhook handler showing the three-step template: idempotency check → business write → outbox write, all in **one transaction**. |

## The atomic guarantee

The outbox row is written **in the same database transaction** as
the business state. If the business write succeeds, the outbox row
exists. If the transaction rolls back, neither exists. There is no
intermediate state where one happened without the other.

A separate publisher process reads unpublished outbox rows and
delivers them to the message bus, marking them published on success.
If the publisher dies mid-deliver, the row stays unpublished and
will be retried. The consumer must be idempotent (see the
[Idempotent Receiver pattern](../../patterns/transactional-outbox.md#related)).

## Why this matters for agent-generated code

An agent generating a webhook handler **does not need to understand
distributed transactions**. The agent follows the three-step
template:

1. `tx.idempotencyKeys.findUnique` then `.create`
2. `tx.contacts.upsert` (or whatever business write)
3. `tx.outbox.create`

If the agent gets the three steps in order inside `db.transaction`,
the result is correct. The architecture makes exactly-once semantics
the **default path** — not something the agent has to reason its way
into.

## What the agent **doesn't** generate

A separate publisher process (not in this example) handles delivery:

```typescript
// publisher.ts (sketch — not the agent's job)
async function publishOutbox() {
  const rows = await db.query(`
    SELECT id, topic, payload FROM outbox
    WHERE published_at IS NULL
    ORDER BY created_at
    LIMIT 100
  `);
  for (const row of rows) {
    await messageBus.publish(row.topic, row.payload);
    await db.query(`UPDATE outbox SET published_at = now() WHERE id = $1`, [row.id]);
  }
}
```

The publisher is **infrastructure**. It's deployed once and runs
continuously. Agent sessions generating handlers don't touch it.

## Run the example

From the repository root, run `npm ci && npm test`. The in-memory test harness
shows that one transaction receives the idempotency, business-state, and outbox
writes, and that a repeated webhook does not create a second outbox record. A
real integration must also test rollback and locking against its actual
database client.

## Operational notes

- The `outbox_unpublished_idx` partial index makes the publisher's
  scan efficient even as the table grows.
- The retention policy in `schema.sql` shows a 30-day archive
  example. Adjust based on your audit requirements.
- For higher throughput, replace polling with Postgres logical
  replication (CDC) — the table schema and write path stay the same.

## Related

- [`../../patterns/transactional-outbox.md`](../../patterns/transactional-outbox.md)
- [`../anti-corruption-layer/`](../anti-corruption-layer/) — the
  outbox payload should be in **domain** terms; the ACL ensures it
- [`../../spec-templates/spec-md.md`](../../spec-templates/spec-md.md)
  — the SPEC.md acceptance criteria should call out idempotency and
  the outbox usage as MUST conditions

## Provenance

Adapted from Chapter 11 of *Harnessing the Horse* by John Briggs.

SQL and TypeScript: © 2026 John Briggs, MIT licensed
(see [`../../LICENSE-CODE`](../../LICENSE-CODE)).
This README: CC BY-NC-SA 4.0
(see [`../../LICENSE-CONTENT`](../../LICENSE-CONTENT)).
