# Definition of Done for Agentic Development

> **Chapter:** ch10 — Compounding Practices (Section 10.4, "The
> Definition of Done for Agentic Development")
> **Last revised:** 2026-06-16
> **Run when:** Before any agent-generated change is merged.

Every team needs a shared understanding of what "done" means. In
agentic development, done arrives not when the code compiles, nor
when the tests pass, nor even when the reviewer approves —

**done is when every artifact is complete, every gate has passed, and
the loop is closed.**

The seven-item checklist below. Items marked ⛔ **BLOCKING** — changes
that do not meet blocking requirements must not be merged regardless
of other factors.

---

## DN1 — Specification Complete ⛔ BLOCKING

- [ ] `SPEC.md` exists
- [ ] Contains binary acceptance criteria (see
      `../spec-templates/acceptance-criteria-template.md`)
- [ ] Contains a MUST-NOT list (six categories considered, per
      Standard 1)
- [ ] Contains a scope boundary (file-level)
- [ ] Has been reviewed by the feature owner

> **No generation without a reviewed spec.**

## DN2 — Design Validated ⛔ BLOCKING

- [ ] `DESIGN.md` exists
- [ ] Task decomposition meets session scope rules (each task < 400
      lines, < 60 minutes of review)
- [ ] Dependency graph is a clean DAG (directed acyclic graph)
- [ ] Interface contracts are explicit (see
      `../spec-templates/interface-spec.md`)

> **No generation without a validated design.**

## DN3 — Implementation Documented

- [ ] `IMPL_NOTES.md` captures all design decisions
- [ ] Deviations from spec are documented with rationale
- [ ] Scope expansion requests are logged
- [ ] Discovery log is complete
- [ ] Every non-obvious choice is justified
- [ ] Every deviation is flagged

## DN4 — Quality Gates Passed ⛔ BLOCKING

- [ ] All BLOCKING gates pass:
  - [ ] Linting
  - [ ] Type checking
  - [ ] Unit tests
  - [ ] Integration tests
  - [ ] Security scans
- [ ] ADVISORY findings are documented in `REVIEW.md` for
      reviewer attention
- [ ] INFORMATIONAL data is captured for trend analysis
- [ ] ASYNC gates are resolved before merge
- [ ] See `deployment-safety-checklist.md` for the full classification

> **No merge with unresolved blocking findings.** Permitted dispositions follow
> the escalation protocol; non-waivable security classes must be fixed.

## DN5 — Review Complete ⛔ BLOCKING

- [ ] `REVIEW.md` exists
- [ ] Review findings match the selected track: both agent adversarial and human
      disprove-only modes for Full; designated human review for Standard; expedited human review for Hotfix
- [ ] All BLOCKING findings are resolved
- [ ] The reviewing engineer can explain the algorithm
- [ ] The reviewing engineer can explain the failure modes
- [ ] The reviewing engineer can explain the test gaps
- [ ] The reviewing engineer can explain the architectural rationale

> **No merge without completed review.**

## DN6 — Provenance Captured

- [ ] Commit metadata links to `SPEC.md` and `DESIGN.md`
- [ ] Agent session information is recorded (model, date,
      session ID if available)
- [ ] The engineer who merged is identified
- [ ] `IMPL_NOTES.md` decisions are linked to specific code locations

## DN7 — Loop Closed

- [ ] `AGENTS.md` / `CLAUDE.md` is updated with any new learnings,
      patterns, or constraints discovered during implementation
- [ ] The session loop is complete: context was loaded, work was
      done, context was saved
- [ ] Knowledge flows forward, not just code

> **The most commonly skipped step.** Teams merge code and move on
> without updating context files. Every time this happens, the next
> agent session starts with stale context — and the same mistakes
> repeat.

---

## Why DN7 matters most

Closing the loop is what transforms a series of isolated agent
sessions into a learning system. It is the practice that makes the
compound interest metaphor real: each session's knowledge investment
pays dividends across every future session.

Without DN7, you have agent sessions. With DN7, you have an agentic
development practice that compounds.

## The blocking discipline

The four BLOCKING items (DN1, DN2, DN4, DN5) are non-negotiable. They
exist because catastrophic failure modes have already been observed
when teams treat them as soft preferences:

- **DN1 violated** → generation without a spec → "we built the wrong
  thing"
- **DN2 violated** → generation without a design → architectural
  drift, unreviewable PRs
- **DN4 violated** → merge despite failing gates → production
  incidents
- **DN5 violated** → "looks good to me" merges → dark code
  accumulation

## Related

- `../spec-templates/spec-md.md` — DN1 artifact
- `../spec-templates/design-md.md` — DN2 artifact
- `../spec-templates/impl-notes-md.md` — DN3 and DN6 artifact
- `../spec-templates/review-md.md` — DN5 artifact
- `../spec-templates/claude-md-template.md` — DN7 artifact
- `deployment-safety-checklist.md` — DN4 gate classification
- `../exercises/maturity-assessment.md` — consistently meeting DN1–7
  is a Level 3 (Defined) maturity indicator

## Provenance

Adapted from Chapter 10 of *Harnessing the Horse*, Section 10.4 (DN1
through DN7).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
