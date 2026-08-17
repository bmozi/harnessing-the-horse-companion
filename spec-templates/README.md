# SPEC Templates

Fill-in scaffolds derived from Chapters 5 and 6 of *Harnessing the
Horse*. These are the discovery, decomposition, and contract artifacts
that precede any code generation.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and case-study
> context that make these scaffolds useful in practice. Written content
> in this directory is licensed under CC BY-NC-SA 4.0
> ([see `../LICENSE-CONTENT`](../LICENSE-CONTENT)).

## Templates

### The four pipeline artifacts (ch04)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`claude-md-template.md`](claude-md-template.md) | ch04 — §4.1 (Context File) | The minimum viable project-root context file (CLAUDE.md / AGENTS.md) — Project Overview, Conventions, Constraints, Architecture Boundaries |
| [`agents-md-template.md`](agents-md-template.md) | ch04 — §4.1 (Context File) / companion tool-configuration reference | The same context file under the vendor-neutral `AGENTS.md` filename, with tool-agnostic loading notes. Either filename works; pick the one your tools read. |
| [`spec-md.md`](spec-md.md) | ch05 — Std 1 / ch04 — §4.6 | The SPEC.md document: what you're building and why |
| [`design-md.md`](design-md.md) | ch04 — §4.6 | The DESIGN.md document: how you plan to build it — Approach, Module Boundaries, Data Model, API Contracts, Tradeoffs, Risks |
| [`impl-notes-md.md`](impl-notes-md.md) | ch04 — §4.6 / ch09 — Std 10 | The IMPL_NOTES.md running log: what actually happened during implementation, plus the three-severity tech debt register |
| [`review-md.md`](review-md.md) | ch04 — §4.6 | The REVIEW.md document: the reviewer's evidence-backed verdict, with Gate Status, Specification Compliance, MUST-NOT Compliance, Findings, Disposition, Sign-off |

### Discovery and decomposition (ch05 + ch06)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`acceptance-criteria-template.md`](acceptance-criteria-template.md) | ch05 — Std 1 | Writing machine-readable acceptance criteria the agent can self-verify and the reviewer can validate via a test run |
| [`task-spec.md`](task-spec.md) | ch06 — Stds 2, 4–5 | Decomposing a SPEC.md into agent-sized tasks with explicit Interfaces Produced/Consumed, Dependencies, and Definition of Done |
| [`interface-spec.md`](interface-spec.md) | ch06 — Std 4 | Detailed templates for REST endpoint, internal function, and event/message interface specifications |
| [`blast-radius-template.md`](blast-radius-template.md) | ch05 — Std 3 | Pre-generation blast-radius estimation across five dimensions |
| [`cagan-four-risk-assessment.md`](cagan-four-risk-assessment.md) | ch05 — Merlin Enhancement | Supplement for complex features: Value / Usability / Feasibility / Business Viability risk assessment |

### Architectural stewardship (ch09)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`adr-template.md`](adr-template.md) | ch09 — §9.3 | Architecture Decision Record with the Agent Implications section that distinguishes agentic-era ADRs. Includes Tier 1 (Full) / Tier 2 (Lightweight) / Tier 3 (Implicit) approaches. |

### Migration at scale (ch12)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`migration-plan-template.md`](migration-plan-template.md) | ch12 — §12.2 | Multi-phase migration plan template applying Strangler Fig discipline: Current State, Target State, Phase Sequence, Acceptance Criteria per phase, Rollback Procedure per phase, Credential Plan, Sync Loop Prevention, Monitoring Plan |

### Strategic direction (ch16)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`strategic-pivot-template.md`](strategic-pivot-template.md) | ch16 — §16.1 | STRATEGIC_PIVOT.md template for documenting a significant architectural course correction so future contributors (human and AI) understand why the original design was abandoned, not just that it was. Larger than an ADR, smaller than the project SPEC. |

### Personal calibration (ch18)

| File | Chapter | Use it for |
| --- | --- | --- |
| [`calibration-journal.md`](calibration-journal.md) | ch18 — §18.1 | Weekly five-minute honest journal to close the gap between **felt** and **measured** productivity. Three sections + weekly metrics rollup. Catches the METR 40-pp gap at the individual level. |
| [`personal-eval-set.md`](personal-eval-set.md) | ch18 — §18.1 | Personal benchmark suite of 5–20 representative tasks with scoring rubric. Re-runnable on every new model / tool. Worked example for a web engineer's auth-endpoint eval. |

## How to use

1. Copy the template into your project.
2. Fill the bracketed sections — `[ ... ]` markers indicate required
   input.
3. Commit it alongside the code change it scopes. The SPEC document
   and the code share git history.

## The flow

```
       spec-md.md
           │
           ├──► blast-radius-template.md         (run alongside SPEC)
           │
           ├──► cagan-four-risk-assessment.md    (only for complex features)
           │
           ▼
      task-spec.md  (×N, one per agent session)
           │
           ├──► interface-spec.md                (per inter-task boundary)
           │
           ▼
   ../prompts/structured-prompt.md  (the generation prompt)
           │
           ▼
   ../prompts/disprove-only-review.md
           │
           ▼
   ../prompts/adversarial-validation.md  (high-risk escalation)
           │
           ▼
   ../checklists/integration-verification-checklist.md
           │
           ▼
   ../checklists/deployment-safety-checklist.md
           │
           ▼
   ../checklists/rollback-readiness-checklist.md
```

## Conventions

- One SPEC per change. Don't bundle.
- Acceptance criteria are testable. "Works correctly" is not an
  acceptance criterion.
- An empty MUST-NOT list is a red flag — six categories must be
  considered.
- Interface specs must be precise enough that two sessions generating
  against them produce code that integrates on the first try.
