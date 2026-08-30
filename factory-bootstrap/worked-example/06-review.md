# REVIEW: Per-Channel Reminder Preferences

## Gate Status

| Gate | Tier | Status | Review evidence |
| --- | --- | --- | --- |
| Type check | Blocking | PASS | recorded command and exit status |
| Unit tests | Blocking | PASS | all flag combinations covered |
| Migration test | Blocking | PASS | legacy true/false cases covered |
| API contract | Blocking | PASS | schema and handler agree |
| Secret scan | Blocking | PASS | no findings |
| Full integration | Async | PASS | eligibility verified through adapters |
| Coverage delta | Advisory | PASS | changed domain paths covered |

## Acceptance-Criterion Traceability

- AC-1 through AC-4: table-driven domain eligibility test.
- AC-5: migration true/false fixture test.
- AC-6: transaction test proves preference and audit atomicity; log assertion
  proves contact data and message content are absent.
- AC-7: API contract check.

## MUST-NOT Compliance

- No dependency or manifest change.
- Scheduler, retries, and provider adapters unchanged.
- Migration copies the prior global value to both flags.
- Sensitive logging test passes.
- Legacy field retained; rollback instructions tested.
- Integration evidence is recorded separately from unit evidence.

## Disprove-Only Findings

1. **MAJOR, resolved:** the first migration draft made new fields non-null before
   backfill. It was replaced with expand-migrate-contract ordering.
2. **MINOR, accepted:** the update response returns both booleans even when one
   is unchanged. This is consistent with the existing full-resource response.
3. **VERIFY, resolved:** adapter eligibility was initially inferred from domain
   tests; the async integration test supplied direct evidence.

## Disposition Recommendation

- [ ] RECOMMEND_SHIP
- [ ] RECOMMEND_REVISE
- [ ] RECOMMEND_STOP

- Final recommendation: **RECOMMEND_REVISE** for expand/backfill phase safety.
  Switching reads and removing the legacy field require separate evidence and
  Work Orders.

Reviewer: Independent senior engineer
