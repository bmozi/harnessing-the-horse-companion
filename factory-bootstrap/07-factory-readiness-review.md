# Factory Readiness Review

Read Chapter 19 before using this review. This is the expansion gate after the first repository has run the minimum viable factory.

## Repository

- Name:
- Review date:
- Reviewer:
- Measurement window:

## Crawl Criteria

- [ ] Context file exists.
- [ ] Context file has been updated from real session learnings.
- [ ] Pre-commit hooks or equivalent guardrails block on the repository.
- [ ] Specifications exist for at least 80% of non-trivial agent-generated changes.
- [ ] Practices have been used for at least two sprints.
- [ ] Metrics baseline exists.

## Gate Reliability

| Gate | Tier | False positives | False negatives | Decision |
| --- | --- | ---: | ---: | --- |
|  |  |  |  | Keep / Reclassify / Remove / Fix |

## Review Quality

- [ ] REVIEW artifacts trace acceptance criteria to implementation and tests.
- [ ] MUST-NOT compliance is checked explicitly.
- [ ] Skipped checks are named with a reason.
- [ ] Findings have dispositions.
- [ ] Recurring review findings have been converted into context, gates, or templates.

## Expansion Decision

Stay in crawl | Expand crawl to another repo | Prepare walk rollout | Stop and diagnose

Rationale:

## Do Not Advance If

- Regeneration rate is rising without explanation.
- Blocking gates are flaky.
- Review artifacts are being filled after the fact.
- Context files are stale.
- Engineers cannot explain the generated changes they approve.
- The team wants orchestration because the manual loop feels slow rather than because the manual loop is reliable.
