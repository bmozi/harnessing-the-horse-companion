# Blast Radius Template (SPEC-Time)

> **Chapter:** ch05 — Discovery and Planning (Standard 3: Blast
> Radius Analysis)
> **Last revised:** 2026-06-16
> **Use this for:** Estimating the blast radius of a change *before*
> generation begins. Pairs with the SPEC.md.

The blast radius is not the same as the scope. The scope is what the
change intends to modify. The blast radius is what the change could
affect if it goes wrong.

A change to a utility function used by three services has a scope of
one file and a blast radius of three services. A change to a database
migration has a scope of one SQL file and a blast radius of every
service, report, and data pipeline that reads from the affected table.

This template forces you to think about consequences, not just
intentions, *before* you generate code.

> **Note:** A second, more detailed blast-radius template lives in
> `../prompts/blast-radius-analysis.md`. That one runs at *review*
> time to validate what was actually changed. This one runs at *SPEC*
> time to estimate what *will be* changed. Both. Not either.

---

```markdown
# Blast Radius Assessment: [feature or task name]

For each task, assess the blast radius across all five dimensions.
Mark any dimension that is genuinely not applicable with one sentence
explaining why.

## 1. Direct dependencies

[What code directly calls, imports, or references the code being
changed? Use the codebase's dependency graph; if you do not have one,
`grep` for the function name or module import is the minimum bar.]

- [caller / consumer / downstream dep]

## 2. Transitive dependencies

[What depends on the direct dependencies? Follow the chain until it
terminates — not just until it leaves the current module. In
microservice architectures, this crosses service and team boundaries.]

- [downstream consumer of a direct dep]

## 3. Data dependencies

[What data stores, schemas, queues, or event streams does this change
affect? This is the most commonly missed dimension — it is invisible
in the code's import graph.]

- [table / schema / queue / event stream — what kind of change]

## 4. User-facing impact

[Does this change affect anything users see, touch, or interact with?
If so, the blast radius includes the user — and review must include
UX validation, not just code verification.]

- [UI surface / behavior / user segment]

## 5. Operational impact

[Does this change affect monitoring, alerting, logging, deployment,
or infrastructure configuration? A change to log format breaks every
alert that parses the current format. A change to a health check
endpoint breaks every monitoring system that polls it.]

- [log / alert / dashboard / health check / deployment artifact]

## Review Effort Classification

Based on the dimensions above:

- [ ] **Single module, no external dependencies** — Standard review
      against spec, 15–30 minutes.
- [ ] **Multiple modules, same service** — Extended review with
      cross-module checks, 30–60 minutes.
- [ ] **Cross-service, or data schema change** — Deep review with
      integration verification, 60–120 minutes.
- [ ] **User-facing, or operational infrastructure** — Full review
      with UX/ops stakeholders, 120+ minutes.
```

---

## Common Failure Modes

- **The invisible blast radius.** The engineer estimates a small
  blast radius because they only considered direct code dependencies
  and missed data, event, or operational dependencies. Fix: this
  template enumerates all five dimensions explicitly, making it
  difficult to overlook a category.
- **The optimistic blast radius.** The engineer knows the blast
  radius is large but downplays it because a large radius implies a
  longer review, which implies a slower delivery. The estimate must be
  documented, visible to the reviewer, and subject to critique. An
  optimistic estimate that is documented is still better than no
  estimate at all — because the reviewer can challenge it.
- **The "it is just a small change" fallacy.** The number of lines
  changed has no reliable correlation with blast radius. A one-line
  change to a database constraint can affect every service. A one-line
  change to a feature flag can expose an unfinished feature to
  production. Estimate based on the change's position in the
  dependency graph, not on its size.

## Related

- `spec-md.md` — this template lives alongside the SPEC.md
- `../prompts/blast-radius-analysis.md` — the review-time companion
  prompt (the verification pass of Std 3)
- `../checklists/deployment-safety-checklist.md` — picks up the
  blast-radius classification at deploy time

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Standard 3. The five
dimensions and the review-effort table are the book's framework.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
