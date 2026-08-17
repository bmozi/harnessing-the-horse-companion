# DESIGN: Per-Channel Reminder Preferences

## Approach

Add an immutable domain value with explicit email and SMS flags. The preference
use case accepts the value and persists it through the existing repository port.
Channel eligibility reads the domain value; delivery adapters remain unchanged.

Use an expand-migrate-contract sequence. First add the new nullable fields while
the old field remains authoritative. Backfill both new fields from the old value,
verify counts and samples, then switch reads and writes. Removing the old field
is a separate Work Order after the observation window.

## Module Boundaries

- Domain types contain no persistence or delivery SDK types.
- The API adapter translates request fields into the domain value.
- The repository adapter owns storage-field translation.
- Delivery adapters receive only channel eligibility decisions.

## Interface Contract

```text
updateReminderPreferences(accountId, {
  emailRemindersEnabled: boolean,
  smsRemindersEnabled: boolean
}) -> UpdatedPreference
```

## Failure and Rollback

- Reject missing or non-boolean fields at the API boundary.
- A failed audit write fails the preference transaction.
- Roll back application reads to the old field while retaining new columns.
- Do not down-migrate until the observation window confirms no new-only writes.

## Test Strategy

- table-driven unit tests for all four flag combinations;
- migration test for true and false legacy values;
- contract test comparing API schema and handler types;
- repository transaction test for preference plus audit atomicity;
- integration test proving provider adapters receive only eligible channels.

## Tradeoffs

The temporary dual representation adds complexity, but makes migration
reversible. Direct replacement is smaller but risks losing the prior effective
preference during rollback.
