# First Factory Session Runbook

Read the [complete session loop](../references/complete-session-loop.md) before using this runbook. This checklist is the execution surface; the reference explains the loop.

## Before Generation

- [ ] Work Order is approved.
- [ ] SPEC exists and has binary acceptance criteria.
- [ ] Blast radius has been estimated.
- [ ] DESIGN exists for non-trivial work.
- [ ] Pipeline track is assigned.
- [ ] Context file, SPEC, DESIGN, and relevant ADRs are loaded.
- [ ] Pre-generation gate passes:
  - [ ] Scope boundary
  - [ ] Interface contracts
  - [ ] Dependency constraints
  - [ ] MUST-NOT list

## During Generation

- [ ] Agent prompt includes task, requirements, constraints, MUST-NOT list, output format, and review criteria.
- [ ] IMPL_NOTES is updated as work proceeds.
- [ ] Deviations from DESIGN are recorded when they happen.
- [ ] Agent uncertainty is surfaced, not hidden.

## After Generation

- [ ] Post-generation gate passes:
  - [ ] File inventory
  - [ ] Interface integrity
  - [ ] Dependency delta
  - [ ] Test coverage
  - [ ] MUST-NOT verification
- [ ] Automated gates run.
- [ ] REVIEW is written by someone other than the generator, or by a fresh adversarial agent when no second human is available.
- [ ] Findings have dispositions.
- [ ] Merge and deploy follow the assigned pipeline track.

## Close The Loop

- [ ] Context file updated if a new convention or failure pattern emerged.
- [ ] Prompt library updated if a reusable prompt pattern emerged.
- [ ] ADR written if a durable design decision was made.
- [ ] Retrospective written if the session failed, thrashed, or surprised the team.
- [ ] Metrics recorded in `06-metrics-baseline.md`.
