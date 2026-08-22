# CAS-Guarded Distributed Commit

> **Chapter:** ch15 — Case Study: The E-Commerce Platform and Its Checkout (Section 15.7)
> **Last revised:** 2026-06-16

## Origin

Maurice Herlihy, "Wait-Free Synchronization," *ACM Transactions on
Programming Languages and Systems*, 1991. The compare-and-swap (CAS)
primitive applied to distributed workflow coordination.

## Intent

**Serialize local workflow ownership and make retries safe after outcomes have
been durably observed, while explicitly containing ambiguous outcomes from
non-idempotent services.**

Despite the pattern's name, this is not a distributed transaction and does not
make the cross-service sequence atomic.

Two patterns interleaved in a single API route:

1. **A state machine** with an atomic compare-and-swap on entry
2. **Per-step checkpoints** that persist intermediate results so a
   retry can skip already-completed steps

## When to Use This

When you have:

- A multi-step commit that crosses **transaction boundaries that
  cannot be made atomic** (multiple third-party APIs, no distributed
  transaction coordinator)
- At least one step where a duplicate execution has **financial,
  legal, or reputational consequences** (charging a card, sending
  a notification, creating an account)
- Network failures, vendor 5xx responses, or container restarts are
  realistic failure modes (they always are in production)

## The State Machine

The aggregate row (the entity carrying the commit) has a status field that
transitions through **five states**:

```
IDLE → SUBMITTING → SUBMITTED
        ├─ known failure → FAILED → SUBMITTING (retry)
        └─ unknown outcome → INDETERMINATE → reconcile or human disposition
```

Transition from `IDLE` or `FAILED` to `SUBMITTING` is an **atomic
compare-and-swap** — in Postgres, a `Prisma updateMany` with a
`WHERE status IN ('IDLE', 'FAILED')` clause. Only the request whose
CAS operation succeeds may proceed with the commit sequence. A
concurrent retry sees the `SUBMITTING` state and backs off.

### The stale window

A **5-minute stale window** prevents a crashed-in-flight commit from
permanently locking the aggregate. If the row has been in `SUBMITTING` for more
than 5 minutes, a retry may re-claim it only when the last durable checkpoint
proves the next step safe. A timeout alone does not prove that an external call
failed.

This handles the container-restart scenario: the original request
crashed mid-commit, the customer waits a few minutes, and the retry
picks up from where the original left off.

## The Per-Step Checkpoints

Inside the `SUBMITTING` window, walk through the non-idempotent calls.
**After each call succeeds, write the resulting ID to the aggregate
row before starting the next.**

```
1. customerCreate() → persist customerID to row
2. paymentProfileCreate() → persist paymentProfileID
3. paymentCharge() → persist paymentID  ← CRITICAL CHECKPOINT
4. subscriptionCreate() → persist subscriptionID
5. appointmentCreate() → persist appointmentID
```

Each step reads its ID from the aggregate at the start and **skips if present**.
A retry after step 4 fails sees the saved `paymentID`, skips the charge step,
and jumps straight to subscription creation. The persisted checkpoint prevents
a known-successful charge from being repeated.

There is still an **ambiguity window**: the payment provider may accept the
charge and the response may be lost before `paymentID` is persisted. CAS and a
local checkpoint cannot determine what happened inside an uncontrolled
provider. Close that window with a provider idempotency key or a stable
correlation ID plus a provider lookup/reconciliation operation. If neither is
available, move the workflow to an explicit `INDETERMINATE` state and require
manual disposition before retrying the charge.

## The Critical Checkpoint

In any multi-step commit, identify the **one step where the failure
mode is unrecoverable** — the charge, the notification, the
external-system mutation that cannot be undone.

That step is the critical checkpoint. The architecture gives the most
dangerous operation the strongest locally enforceable retry guard: if its ID is
already persisted, the step is skipped on retry. This is not an idempotency
guarantee for the provider call itself.

Later steps follow the same rule: retry a known failure; reconcile an unknown
provider outcome before deciding whether a replay is safe.

## Worked Example: Fieldstone Booking Flow

From the booking-wizard case study (Ch15):

- The `BookingSession` row carries `crmSubscriptionStatus` (the
  state machine field)
- The five-write sequence: `customerID` → `paymentProfileID` →
  **`crmSubscriptionPaymentId`** (critical) → `subscriptionID` →
  appointment
- Once `crmSubscriptionPaymentId` is persisted, the charge step is skipped on
  retry; lost-response cases enter reconciliation rather than automatically
  charging again
- Projected impact: ~$5,500/year support labor + ~$7,000/year
  avoided chargebacks at 100 bookings/day

## Why This Matters for Agentic Development

An AI agent generating a multi-step checkout flow without this
pattern produces code that **works correctly on the happy path and
double-charges on the first retry**.

The agent does not naturally reason about:
- What state the aggregate is in when a retry arrives
- Which steps must be skipped on retry
- Where the critical checkpoint is

This pattern structurally serializes local ownership and prevents replay of
durably checkpointed steps. With provider idempotency or reconciliation, it can
produce an **effectively-once business outcome** despite retries. It cannot
promise exactly-once execution across a provider that offers neither. The
review prompt should require these controls, an explicit ambiguity state, or a
documented alternative for any multi-step commit across services.

## Pitfalls

- **The "almost CAS" check.** Using `WHERE status = 'IDLE'` for the
  guard is not atomic if you do a `SELECT` then `UPDATE` separately
  — that's a TOCTOU race. The CAS guarantee comes from a single
  `UPDATE … WHERE status IN (…)` that returns row-count > 0.
- **The forgotten stale window.** Without it, a single crash
  permanently bricks the aggregate. The customer's session is dead
  and only manual ops intervention recovers it.
- **The checkpoint without persistence.** Persisting the intermediate
  ID to an in-memory cache or to the request context is not a
  checkpoint — it must survive a crash.
- **The lost response treated as failure.** A timeout after a non-idempotent
  provider call is an unknown outcome, not proof that nothing happened. Query
  by a stable correlation ID, reconcile externally, or stop for human
  disposition before retrying.
- **The wrong critical checkpoint.** If you treat "appointment
  creation" as critical but "payment charge" as recoverable, you
  have inverted the priority. Identify the unrecoverable step
  explicitly.
- **The retry without bounded attempts.** A retry loop without an
  iteration cap turns transient failure into permanent thrash. Pair
  CAS-guarded commit with bounded iteration (see
  [`../checklists/iteration-caps.md`](../checklists/iteration-caps.md)).

## Related

- [`transactional-outbox.md`](transactional-outbox.md) — companion
  pattern for the "publish event after commit" half of the problem
- [`../checklists/iteration-caps.md`](../checklists/iteration-caps.md)
  — bounded retry discipline that pairs with the state machine
- [`../code-examples/transactional-outbox/`](../code-examples/transactional-outbox/)
  — the simpler "single-database write + event" case
- **Idempotent Receiver** (Hohpe & Woolf, 2003) — see
  [`README.md`](README.md) for the catalog reference

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
