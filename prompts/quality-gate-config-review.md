# Quality Gate Configuration Review Prompt

> **Chapter:** ch07 — Generation, Verification, and Review (Standard 6:
> Automated Quality Gates)
> **Last revised:** 2026-06-16
> **Model assumed:** Frontier model
> **Use this for:** Auditing a project's CI configuration against the
> four-tier gate classification (Blocking / Advisory / Informational /
> Async).

Human discipline degrades under pressure. Automated quality gates
remove the human from the enforcement loop for every check that can be
automated. The four-tier classification matters because not every
check justifies halting a deployment, but every check that does justify
it must be impossible to skip.

---

```markdown
## Quality Gate Configuration Review

Review the project's quality gate configuration against these
requirements:

### Blocking Gates (must be present and enforced)
- [ ] Compilation / type-check passes with zero errors
- [ ] All unit tests pass (zero failures, zero skipped without
      documented reason)
- [ ] Security scan: zero CRITICAL, zero HIGH findings
- [ ] License scan: all dependencies in approved license list
- [ ] Architecture boundaries: no prohibited cross-module imports
- [ ] API contract: generated OpenAPI matches implementation signatures

### Advisory Gates (must be present, findings surfaced in PR)
- [ ] Code coverage: delta reported, threshold violations highlighted
- [ ] Complexity: functions exceeding [threshold] flagged
- [ ] Performance: benchmark regressions above [tolerance]% flagged
- [ ] Documentation: public APIs missing doc comments listed

### Informational Gates (must be present, logged to dashboard)
- [ ] LOC delta tracked
- [ ] Dependency inventory updated
- [ ] Test execution time recorded
- [ ] AI-generation metadata captured

### Async Gates (must be present; results required before merge, but the
synchronous pipeline does not block on them)
- [ ] Full integration / e2e test suite scheduled
- [ ] Performance regression benchmark vs. baseline scheduled
- [ ] SAST deep analysis scheduled
- [ ] License compliance + dependency vulnerability deep scan scheduled
- [ ] PR held in "pending ASYNC" state until results return; failure
      blocks merge

### Enforcement
- [ ] Blocking gates are configured as required status checks in the
      branch protection rules
- [ ] Blocking gates CANNOT be bypassed by repository administrators
      without a documented override
- [ ] Advisory gate results appear in the PR review interface (not
      buried in CI logs)
- [ ] Informational gate data feeds the project metrics dashboard

Identify any gaps and recommend specific configurations to close them.
```

---

## The Four Tiers

**BLOCKING gates** — the build fails, the PR cannot merge, the
deployment is halted. These enforce invariants that, if violated, would
cause production incidents, security vulnerabilities, or architectural
corruption.

**ADVISORY gates** — the result is surfaced to the reviewer as a
finding but does not block merge. These catch issues that require human
judgment to evaluate.

**INFORMATIONAL gates** — the result is logged and available for
dashboard analysis but requires no per-PR action. These track trends
meaningful at the project level but not actionable at the individual
PR level.

**ASYNC gates** — the check must pass before merge, but it executes
asynchronously so the synchronous PR pipeline stays fast. The PR is
held in a "pending ASYNC" state until results return; failure blocks
merge. These handle the slow-but-required checks that would create
unacceptable latency inline.

## Related

- `../spec-templates/task-spec.md` — the gates verify against the
  Definition of Done
- `disprove-only-review.md` — Question 1 of the review confirms
  blocking-gate status

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 6. The
classification system originated in the Merlin Software Factory and
was refined through approximately 400 deployment cycles.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
