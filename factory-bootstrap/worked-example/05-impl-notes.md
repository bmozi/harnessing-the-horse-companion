# IMPL_NOTES: Per-Channel Reminder Preferences

## Implementation Log

- Added the domain preference value and table-driven eligibility tests.
- Added nullable storage fields and a backfill migration; retained the legacy
  field and legacy reads for the first deployment phase.
- Updated the API schema and request adapter for explicit channel flags.
- Reused the existing transaction wrapper for preference and audit writes.

## Deviations

No deviation from the approved DESIGN. The discovery-stage proposal originally
combined expand, backfill, and switching reads. The four-risk evidence contract
and DESIGN narrowed authorization before generation because the repository has
no production-scale migration dataset in CI. The implementation preserved that
boundary and left the read switch for a later Work Order.

## Evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Type check | PASS | command exited 0 |
| Unit tests | PASS | all four flag combinations and validation cases passed |
| Migration test | PASS | true and false legacy values copied correctly |
| API contract | PASS | generated schema matched handler types |
| Integration suite | PENDING ASYNC | required before merge |
| Dependency delta | PASS | no manifest change |

## Uncertainty

- `VERIFY`: backfill duration and lock behavior on a production-sized copy.
- `VERIFY`: integration suite confirms adapters receive no newly ineligible
  channel.

## Debt Register

- **Must fix before merge:** none currently known; pending async failures would
  enter this tier.
- **Should fix soon:** add a production-volume migration rehearsal dataset.
- **Can defer:** dashboard split by channel after the migration observation
  window; outside this Work Order.
