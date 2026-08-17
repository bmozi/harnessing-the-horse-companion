# Four-Risk Evidence Contract: Per-Channel Reminder Preferences

> Fictional completed example. This is the discovery decision that authorizes
> the reversible expand/backfill phase, not the full migration.

## Decision Context

- Decision owner: Product owner
- Assessment date: 2026-08-16
- Proposed outcome: Let account holders enable email and SMS reminders
  independently without changing scheduling or delivery behavior.
- Cost of a false positive: Migration and support burden for a preference few
  users need; possible reminder suppression through an incorrect default.
- Cost of a false negative: Continued manual support overrides and delayed
  customer control.
- Decision deadline: Before the next reminder-settings release; the date is a
  planning target, not authority to bypass a gate.

## Decision Summary

| Risk | Decision at risk | Rating | Best evidence | Falsifier | Next test / control | Owner | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value | Is independent control worth adding now? | LOW | Repeated support cases plus affected-account analysis (E2) | Fewer than 1% of active reminder users need split control | Measure adoption during the pilot | Product owner | ACCEPTED for pilot |
| Usability | Can users predict the two-toggle behavior? | LOW | Existing settings pattern and prototype task test (E2) | Any participant assumes one toggle overrides the other | Accessibility review and pilot telemetry | Design owner | CONTROLLED |
| Feasibility | Can legacy values migrate without changing behavior? | MEDIUM | True/false fixture migration test (E1) | Production-scale rehearsal exceeds lock or error threshold | Rehearse before switching reads | Data owner | BLOCKING before read switch |
| Viability | Can support and privacy obligations be met? | LOW | Support owner and approved non-sensitive audit schema (E2) | Audit requires contact data or lacks an operational owner | Verify production retention configuration | Privacy owner | CONTROLLED |

## Value Risk

**Falsifiable claim:** A material group of reminder users needs independent
channel control, and self-service selection will reduce manual overrides.

- Evidence: support cases from multiple accounts plus an account-level override
  analysis, E2; the data shows repeated need but not long-term adoption.
- Falsifier: pilot adoption below 1% of active reminder users after one complete
  reminder cycle.
- Engineering constraint: MUST NOT add analytics or new channels to manufacture
  a broader use case.
- Disposition: LOW / ACCEPTED for a bounded pilot.

## Usability Risk

**Falsifiable claim:** Users understand that each toggle controls only its named
channel and can preserve current behavior without assistance.

- Evidence: the design reuses an existing settings interaction; five fictional
  prototype participants completed all four flag combinations, E2.
- Falsifier: any pilot result showing that users expect one toggle to control
  both channels.
- Engineering constraint: MUST NOT create a new settings-navigation pattern or
  silently default one channel differently from the other.
- Disposition: LOW / CONTROLLED.

## Feasibility Risk

**Falsifiable claim:** An expand-migrate-contract sequence can copy the legacy
global value to both channel fields without changing effective behavior.

- Evidence: repository inspection and true/false fixture migration, E1; no
  production-scale copy exists in CI.
- Falsifier: rehearsal exceeds the approved lock-duration threshold, produces
  mismatched values, or cannot roll application reads back to the legacy field.
- Next test: production-scale synthetic rehearsal before switching reads.
- Engineering constraint: the authorized implementation may add nullable
  fields and backfill logic; it MUST NOT remove the legacy field or switch reads.
- Disposition: MEDIUM / CONTROLLED for expand/backfill; BLOCKING before the read
  switch.

## Business Viability Risk

**Falsifiable claim:** The preference can be supported and audited without
storing contact data or message content.

- Evidence: named support owner and approved actor/timestamp/changed-fields
  audit shape, E2.
- Falsifier: production policy requires sensitive data in the audit record or no
  owner accepts retention responsibility.
- Engineering constraint: MUST NOT log email addresses, phone numbers, tokens,
  or message bodies.
- Disposition: LOW / CONTROLLED pending production retention verification.

## Cross-Risk Interaction

Keeping the legacy field improves feasibility and rollback but temporarily
increases operational complexity. The team accepts that cost for the bounded
observation window; removing the field requires a separate Work Order.

## Generation Decision

- [x] **PROCEED TO SPEC:** authorize only the reversible expand/backfill phase.
- [ ] Proceed to full cutover.

Authorized next work: SPEC, DESIGN, migration fixture, nullable fields, backfill,
explicit API contract, and non-sensitive audit behavior.

Not authorized: switching application reads, removing the legacy field, adding
channels, changing retry or scheduling, or expanding analytics.

Next review trigger: production-scale migration rehearsal or any pilot signal
that contradicts the value or usability claims.
