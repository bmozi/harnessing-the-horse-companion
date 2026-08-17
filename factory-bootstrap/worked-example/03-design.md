# DESIGN: Per-Channel Reminder Preferences

> Fictional completed example using the minimum sections required by the
> DESIGN.md agent execution contract.

## References and Decision Ownership

- SPEC: [`02-spec.md`](02-spec.md)
- Four-risk evidence contract:
  [`01a-four-risk-evidence-contract.md`](01a-four-risk-evidence-contract.md)
- Project context: [`00-project-context.md`](00-project-context.md)
- Design owner: Pilot engineer
- Required approver: Senior engineer outside the generation session
- Status: Approved for expand/backfill only
- Last evidence review: 2026-08-16

## Evidence Read Before Design

| Source | Relevant fact | How verified | Limitation |
| --- | --- | --- | --- |
| Preference domain and unit tests | one global boolean controls both channels | source and test inspection | no production behavior inferred |
| API schema and handler | current contract exposes `remindersEnabled` | schema/handler comparison | client release timing needs owner confirmation |
| Repository transaction tests | preference and audit writes share a transaction | test inspection | production database behavior still requires integration evidence |
| Migration fixtures | true and false legacy values can be copied deterministically | fixture test | no production-scale rehearsal in CI |

## Acceptance-Criterion Traceability

| Criterion | Designed behavior | Component / interface | Planned evidence |
| --- | --- | --- | --- |
| AC-1 to AC-4 | explicit eligibility for all four flag combinations | domain preference value | table-driven unit test |
| AC-5 | copy the prior global value to both nullable fields | migration | true/false fixture plus later scale rehearsal |
| AC-6 | write actor, time, and changed fields atomically without contact data | update use case and repository port | transaction and logging tests |
| AC-7 | expose two required booleans with agreed names and types | API schema and request adapter | contract check |

## Invariants and Boundaries

- Existing accounts retain their effective reminder behavior throughout the
  authorized phase.
- Preference and audit writes remain atomic.
- Domain code imports no persistence, queue, email, SMS, or provider SDK.
- Scheduler, retry logic, and delivery adapters remain unchanged.
- The implementation MUST NOT remove the legacy field or switch reads in this
  Work Order.

## Chosen Approach

Add an immutable domain value with explicit email and SMS flags. The preference
use case accepts that value and persists it through the existing repository
port. The API adapter translates request fields; the repository adapter owns
storage translation. Delivery adapters continue to receive channel-eligibility
decisions rather than preference-storage details.

Use an expand-migrate-contract sequence. This Work Order covers expand and
backfill only: add nullable fields, copy the old value to both, and verify the
result. Switching reads and removing the legacy field require later Work Orders.

## Change Surface

| Component | Proposed change | Why it belongs here |
| --- | --- | --- |
| Preference domain value | represent two explicit flags | owns reminder eligibility semantics |
| Update use case | validate and persist the value | owns the authorized business operation |
| API schema and adapter | translate two booleans | owns the external contract boundary |
| Repository adapter | translate storage fields and preserve atomic audit | owns persistence details |
| Migration | add nullable fields and copy the old value | owns reversible data evolution |

Scheduler, retries, queues, and provider adapters were inspected and remain
unchanged because they consume eligibility decisions, not stored preferences.

## Interface Contract

```text
updateReminderPreferences(accountId, {
  emailRemindersEnabled: boolean,
  smsRemindersEnabled: boolean
}) -> UpdatedPreference
```

- Missing or non-boolean fields are rejected at the API boundary.
- The response returns both booleans.
- The contract check compares schema names, required fields, and handler types.
- No delivery-provider type crosses the domain boundary.

## Data Lifecycle and Migration

- System of record: preference repository.
- Audit data: actor identifier, timestamp, and changed field names only.
- Sequence: add nullable fields, deploy compatible writer, backfill both fields
  from the legacy value, verify mismatches equal zero, observe, then separately
  authorize a read switch.
- Rollback: return application behavior to the legacy field while retaining the
  new nullable columns. Do not down-migrate until no new-only write can exist.
- Coexistence invariant: both new flags equal the legacy value until a later
  Work Order explicitly authorizes independent updates.

## Dependency and Capability Delta

No package, service, queue, permission, or runtime capability is added. Existing
validation, repository, transaction, and migration utilities are required.

## Failure, Recovery, and Convergence

| Failure | Expected behavior | Detection | Recovery | Owner |
| --- | --- | --- | --- | --- |
| invalid API field | reject without a write | contract and validation tests | caller corrects request | API owner |
| audit write fails | preference transaction fails | transaction test and error signal | retry through existing policy | service owner |
| backfill mismatch | stop migration phase | mismatch query | keep legacy reads, repair script | data owner |
| lock duration exceeds threshold | stop rehearsal / rollout | database metric | reduce batch or revise design | data owner |
| design fact contradicted | stop agent session | implementation report | human design review | design owner |

## Security, Privacy, and Abuse Cases

- Existing account authorization remains the only permission path.
- The API boundary validates both values before calling the use case.
- Logs and audit records exclude email addresses, phone numbers, tokens, and
  message bodies.
- The agent may not access production data or execute a production migration.
- Secret scan and sensitive-logging assertion are blocking evidence.

## Observability and Operational Readiness

| Signal | Success / failure threshold | Action | Owner |
| --- | --- | --- | --- |
| migration mismatch count | success = 0 | stop phase and keep legacy reads | data owner |
| backfill error count | success = 0 | halt batch and investigate | data owner |
| update validation errors | baseline expected; unexpected increase triggers review | inspect client compatibility | API owner |
| reminder suppression report | any confirmed regression blocks read switch | rollback behavior and investigate | service owner |

## Verification, Rollout, and Rollback

| Claim | Evidence | Classification |
| --- | --- | --- |
| all flag combinations behave explicitly | table-driven domain tests | BLOCKING |
| legacy true/false values copy to both fields | migration fixture | BLOCKING |
| preference and audit writes are atomic | repository transaction test | BLOCKING |
| API schema and handler agree | contract check | BLOCKING |
| no sensitive logging | logging assertion and secret scan | BLOCKING |
| provider adapters receive only eligible channels | full integration suite | ASYNC, required before merge |
| production-scale lock behavior is acceptable | migration rehearsal | BLOCKING before later read-switch Work Order |

The current rollout ends after expand/backfill and verification. Its rollback is
to retain legacy reads. There is no irreversible step in this Work Order.

## Agent Execution Contract

### Fixed decisions

- Use expand-migrate-contract ordering.
- Copy the legacy value to both new fields.
- Reuse existing validation and transaction utilities.
- Keep vendor types outside the domain.
- Preserve the legacy field and reads.

### Permitted latitude

- Private helper names and local test organization.
- Equivalent batch organization that stays within the approved lock threshold.

### Stop and escalate

Stop if a new dependency, provider change, scheduling change, non-null-first
migration, production-data access, additional permission, interface expansion,
or read switch appears necessary. Stop if required evidence cannot be produced.

## Human Decisions and `VERIFY` Items

| Item | Evidence needed | Owner | Due before |
| --- | --- | --- | --- |
| client release compatibility | consumer inventory and release plan | API owner | API publication |
| production-scale lock behavior | representative rehearsal | data owner | read-switch Work Order |
| production retention configuration | policy and deployed setting | privacy owner | audit rollout |

## Alternatives and Tradeoffs

| Alternative | Advantage | Cost / risk | Disposition |
| --- | --- | --- | --- |
| direct replacement | smallest code delta | unsafe rollback and possible behavior loss | rejected |
| two new fields with staged coexistence | reversible and observable | temporary dual representation | chosen |
| new preference service | independent ownership | unjustified service and operational surface | rejected |

## Residual Risks

- Production-scale migration behavior remains unproven and blocks the later read
  switch, not the reversible expand/backfill phase.
- Client coordination may change the API publication sequence; the API owner
  must resolve it before publication.

## Design Completion Gate

- [x] Every acceptance criterion maps to design and proof.
- [x] MUST-NOT constraints appear as invariants or stop conditions.
- [x] Interfaces, data, dependencies, failure, operations, and rollback are
      explicit.
- [x] Fixed decisions and agent latitude are distinguishable.
- [x] Blocking unknowns have owners and due points.
