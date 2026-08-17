# Work Order: Per-Channel Reminder Preferences

## Status

Approved

## Owner

- Requester: Product owner
- Implementing engineer: Pilot engineer
- Reviewer: Senior engineer outside the generation session
- Date opened: 2026-08-16

## Problem Statement

Users can disable all reminders but cannot keep email reminders while disabling
SMS. Support currently applies manual account overrides. This creates delay and
untraceable exceptions.

## Success Criteria

- [ ] A user can independently enable or disable email and SMS reminders.
- [ ] Existing accounts retain their current effective behavior.
- [ ] Preference updates create a non-sensitive audit record.
- [ ] Existing scheduling and delivery behavior remains unchanged.

## Scope Boundary

### In Scope

- domain preference type;
- preference update use case;
- existing API request and response contract;
- migration defaulting both channel flags from the existing global value;
- unit and contract tests.

### Out of Scope

- new channels;
- user-interface changes;
- delivery-provider changes;
- retry, scheduling, or queue behavior;
- preference analytics.

## Pipeline Track

Full. The change includes a data migration and modifies a public API contract.

## Gate Expectations

- Blocking: type check, unit tests, migration test, API contract, secret scan.
- Advisory: coverage delta and complexity.
- Informational: changed-file and test-duration records.
- Async: full integration suite must resolve before merge.

## Close-the-Loop Target

Record the migration-defaulting rule in the project context if review confirms
that the rule is reusable for future preference migrations.
