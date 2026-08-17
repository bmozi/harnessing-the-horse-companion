# SPEC: Per-Channel Reminder Preferences

## Problem Statement

The preference model exposes only `remindersEnabled`. Users need independent
control of email and SMS without changing how eligible reminders are scheduled
or delivered.

## Proposed Solution

Replace the single public preference with `emailRemindersEnabled` and
`smsRemindersEnabled`. Migrate each existing account by copying its current
global value to both new fields. Keep channel delivery behind existing ports.

## Acceptance Criteria

- **AC-1:** Given both flags are true, both existing reminder channels remain
  eligible.
- **AC-2:** Given email is true and SMS is false, only email is eligible.
- **AC-3:** Given email is false and SMS is true, only SMS is eligible.
- **AC-4:** Given both flags are false, no reminder channel is eligible.
- **AC-5:** Migrating an account with `remindersEnabled=true` produces two true
  flags; false produces two false flags.
- **AC-6:** Updating preferences records actor, timestamp, and changed fields
  without recording contact data or message content.
- **AC-7:** The API contract and implementation agree on names, types, and
  required fields.

## MUST-NOT List

- Do not introduce a third-party package.
- Do not modify scheduling, retry, or provider adapters.
- Do not default either channel to true independently of the prior global value.
- Do not log contact data or message bodies.
- Do not remove the old field until the reversible migration path is proven.
- Do not claim integration success from unit tests alone.

## Out of Scope

User-interface work, new channels, analytics, and provider configuration.

## Affected Components

| Component | Expected change | Evidence |
| --- | --- | --- |
| Preference domain type | two explicit flags | type check and unit tests |
| Update use case | validate and persist both flags | unit tests |
| API contract | two boolean fields | contract check |
| Preference migration | copy prior global value | migration test and rollback rehearsal |
