# Deployment Safety Checklist

> **Chapter:** ch08 — Execution Discipline (Standard 9: Release and
> Rollback Readiness)
> **Last revised:** 2026-06-16
> **Run when:** Before deploy. Integration verification has passed;
> rollback readiness is documented. Time to ship.

Deployment is the moment when generated code meets reality. Everything
before is rehearsal. Production has none of the controls of a staging
environment.

For agent-generated code, deployment safety requires additional rigor
beyond what human-authored code demands — for one specific reason:
**agent-generated code is less understood by the team that deploys it.**
The author of human-written code can be consulted at 2 AM. The author
of agent-generated code is a model with no memory of the session.

---

## Quality Gate Classification

Every gate is classified into one of four tiers — BLOCKING, ADVISORY,
INFORMATIONAL, or ASYNC (Standard 6, Chapter 7). Treating gates as
equal produces one of two pathologies: every warning blocks
(creating bypass incentives) or every warning is advisory (creating
ignored noise). INFORMATIONAL gates are logged for trend analysis and
require no per-deploy action, so they do not appear in the checklist
below.

### BLOCKING gates — must pass before next pipeline stage

Failure halts the pipeline. Enforces invariants that, if violated,
produce production incidents.

- [ ] Type check / compilation — zero errors
- [ ] Unit tests — 100% pass rate
- [ ] Security scan — zero CRITICAL, zero HIGH findings
- [ ] License compliance — all dependencies in approved list
- [ ] Architecture boundary enforcement — no prohibited cross-module
      imports
- [ ] API contract validation — generated OpenAPI matches
      implementation

> Unresolved blocking findings hold deployment. Permitted exceptions require
> the authority, evidence and remediation controls in the escalation protocol;
> non-waivable security classes cannot be accepted as exceptions.

### ADVISORY gates — surfaced for human judgment

Captured in review artifacts for the reviewer's attention.

- [ ] Code coverage — delta reported, threshold violations
      highlighted
- [ ] Complexity metrics — functions exceeding threshold flagged
- [ ] Performance regression — benchmarks above tolerance flagged
- [ ] Documentation coverage — public APIs missing docs listed
- [ ] Security findings at MEDIUM and LOW severity

> A codebase that ignores every ADVISORY finding accumulates debt.
> A codebase that blocks on every ADVISORY finding never ships.
> The reviewer exercises judgment.

### ASYNC gates — run in background, resolve before merge

Valuable but expensive checks.

- [ ] Full integration test suite
- [ ] Performance benchmarks
- [ ] Dependency vulnerability scan (full tree)
- [ ] License compliance (full tree)

> Synchronous = unacceptable pipeline latency. Not at all =
> unacceptable risk. ASYNC is the engineering compromise.

---

## Pipeline Track Selection

Match the deployment process to the risk level of the change.

### Eligibility screen — before selecting any track

Record affected consumers, external contracts, schemas, security boundaries,
reversibility and uncertainty. File count alone does not establish low risk.

### Hotfix track

Only for an emergency production failure with a contained, reversible fix in
three files or fewer, with no schema, external-contract or security-boundary
change. Routine typos and formatting use Standard.

- [ ] Blocking gates pass; non-waivable security gates have no exception
- [ ] Rollback plan verified before deploy
- [ ] Designated human reviewer signs the expedited review
- [ ] SPEC and full REVIEW completed within 24 hours

### Standard track

For contained enhancements and known fixes after the impact screen.

- [ ] Abbreviated SPEC with acceptance criteria and MUST-NOT list
- [ ] Blocking gates and applicable integration checks pass
- [ ] Designated human disprove-only review recorded in REVIEW.md
- [ ] Reviewer confirms the impact screen still holds

### Full track

For new features/endpoints, migrations, external contracts, new dependencies,
security boundaries, irreversible or otherwise high-risk effects, cross-module
changes or unclear root causes.

- [ ] Full SPEC and DESIGN approved before generation
- [ ] All applicable gates and blast-radius analysis complete
- [ ] Fresh adversarial agent receives SPEC and code, not implementation notes
- [ ] Separate designated human disprove-only review recorded
- [ ] Recovery plan covers committed data and external effects

---

## Post-Merge Monitoring Thresholds

Deployment safety does not end at merge. Configure these thresholds
for the post-deploy observation window (typically **15–30 minutes**,
calibrated to traffic).

- [ ] **Error rate exceeds 2x baseline within 15 minutes** →
      automatic rollback (no human decision)
- [ ] **P95 latency exceeds 1.5x baseline within 15 minutes** → alert
      raised, manual rollback decision
- [ ] **New error types appear that did not exist pre-deploy** →
      alert raised, investigation required
- [ ] **Health check failures on any critical endpoint** → immediate
      automatic rollback

> These thresholds are not punitive — they are protective. Tighter
> monitoring compensates for lower comprehension until the team
> builds confidence in its review process. Relaxation must be driven
> by data, not by optimism.

---

## Track Assignment Review

- [ ] The pipeline track is **explicitly documented** in the PR
      description or task metadata
- [ ] The assignment is **defensible** — a database migration in the
      hotfix track should raise a flag, not be quietly accepted

## Common Failure Modes

- **The "Tests Pass" Fallacy.** Green CI assumed safe. CI runs the
  tests that exist, not the tests that should exist. A component with
  100% passing tests and 40% coverage has a 60% gap CI cannot see.
  Coverage analysis as an ADVISORY gate, not just test execution
  as a BLOCKING gate.
- **The Friday Afternoon Deploy.** Change approved at 4 PM Friday.
  Engineer deploys and goes home. Monitoring alerts fire at 6 PM. No
  one is watching. By Monday, 60 hours of degradation. Policy: no
  deployments within two hours of the end of the monitored window
  unless on-call coverage is confirmed.
- **The Cascading Failure.** Generated component deployed and works.
  But it changes the response time of an API another service depends
  on. That service's timeout is tuned to the old time. It times out.
  Callers retry. Retry storm overloads the original service.
  Deployment that "passed all tests" causes cascading failure no
  individual test could predict. System-level smoke testing and
  post-merge monitoring are the defenses.

## Related

- `integration-verification-checklist.md` — must pass before this
- `rollback-readiness-checklist.md` — must pass before this
- `../prompts/quality-gate-config-review.md` — the gate
  configuration this checklist verifies
- `../prompts/blast-radius-analysis.md` — the classification that
  drives track selection

## Provenance

Adapted from Chapter 8 of *Harnessing the Horse*, Standard 9. The
gate-tier classification system originated in the Merlin Software
Factory and was refined through approximately 400 deployment cycles.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
