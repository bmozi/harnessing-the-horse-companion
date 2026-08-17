# Checklists

Human-facing review checklists for the execution-discipline standards
in Chapter 8 of *Harnessing the Horse*. These run between generation
and production — verifying that separately-built components fit
together, that the deployment is safe, and that rollback is real.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and case-study
> context that make these checks meaningful rather than ritual. Written
> content in this directory is licensed under CC BY-NC-SA 4.0
> ([see `../LICENSE-CONTENT`](../LICENSE-CONTENT)).

These are not prompts (those live in `../prompts/`) and not pre-gen
artifacts (those live in `../spec-templates/`). They are the
checklists a human reviewer or release manager runs against an
agent-generated change.

## Checklists

### Pre-generation gates (ch05)

| File | Chapter | Run when |
| --- | --- | --- |
| [`pre-generation-verification.md`](pre-generation-verification.md) | ch05 — Std 1 | Before generation begins: Scope Boundary, Interface Contracts, Dependency Check, Constraint Check |
| [`post-generation-verification.md`](post-generation-verification.md) | ch05 — Std 1 | After generation, before review: File Inventory, Interface Integrity, Dependency Delta, Test Coverage, MUST-NOT Verification |

### Architectural stewardship (ch09)

| File | Chapter | Run when |
| --- | --- | --- |
| [`impact-boundary-assessment.md`](impact-boundary-assessment.md) | ch09 — §9.1 | Before any generated change is merged: the five questions that determine whether the change requires architectural review |
| [`architecture-drift-scan.md`](architecture-drift-scan.md) | ch09 — Std 10 (companion complete prompt library §A.18) | Periodically, and before merging boundary-adjacent changes: compare the actual dependency graph against the documented architecture; classify findings as Violation / Evolution / Ambiguity |
| [`simplicity-review.md`](simplicity-review.md) | ch09 — §9.2 | When the agent has produced multiple wrapper / adapter / factory classes: the four Ousterhout-derived tests (deep module, YAGNI, comprehension, delete) |

### Pre-merge / pre-deploy (ch08)

| File | Chapter | Run when |
| --- | --- | --- |
| [`integration-verification-checklist.md`](integration-verification-checklist.md) | ch08 — Std 8 | Before merge: prove separately-generated components work together |
| [`deployment-safety-checklist.md`](deployment-safety-checklist.md) | ch08 — Std 9 | Before deploy: classify the change, pick the pipeline track, confirm post-merge monitoring is configured |
| [`rollback-readiness-checklist.md`](rollback-readiness-checklist.md) | ch08 — Std 9 | Before deploy: confirm every change is reversible and the rollback is documented, tested, and owned |

### Closing the loop (ch10)

| File | Chapter | Run when |
| --- | --- | --- |
| [`definition-of-done.md`](definition-of-done.md) | ch10 — §10.4 | Before any agent-generated change is merged: the seven-item DN1–DN7 checklist with four BLOCKING items |

### Migration discipline (ch12 / Appendix D)

| File | Chapter | Run when |
| --- | --- | --- |
| [`migration-phase-gate.md`](migration-phase-gate.md) | ch12 — §12.2 | Before transitioning between migration phases: pre-conditions, acceptance criteria, rollback triggers, sign-off |
| [`oss-license-triage.md`](oss-license-triage.md) | ch12 — §12.3 | Before accepting any AI-recommended open-source dependency: five license classes (Permissive / Weak copyleft / Strong copyleft / Source-available / No license) with per-dependency triage worksheet |
| [`equivalence-test-checklist.md`](equivalence-test-checklist.md) | Appendix D — §D.4 | Multi-system migration: three test categories (equivalence, temporal replay, migration regression) for asserting the new system produces the same results as the old |

### Autonomous-system governance (ch16)

| File | Chapter | Run when |
| --- | --- | --- |
| [`iteration-caps.md`](iteration-caps.md) | ch16 — §16.1 | Configuring every loop in an agent-driven system so failure is cheap and visible (2 CI fix iterations, 25 tool-use iterations, daily token budgets) |
| [`self-improvement-safety-rails.md`](self-improvement-safety-rails.md) | ch16 — §16.3 | Designing or auditing a system that autonomously improves itself: the four non-negotiable constraints (daily cap, permanent human approval, forbidden paths, self-referential loop detection) |

### Security (ch17)

| File | Chapter | Run when |
| --- | --- | --- |
| [`security-review.md`](security-review.md) | ch17 — §17.1 / §17.6 | Reviewing agent-generated code for security. The generation trifecta extended to six vectors (dependency verification, vulnerability scan, auth, prompt injection propagation, excessive tool authorization, memory store integrity) + memory poisoning defenses + MCP supply-chain defense + OWASP Agentic Top 10 mapping |

### Measurement (ch18)

| File | Chapter | Run when |
| --- | --- | --- |
| [`metrics-dashboard.md`](metrics-dashboard.md) | ch18 — §18.5 | Specifying the dashboard for an agentic team. Five metric groups, weekly refresh, agent-vs-human attribution, quality throughput formula, regeneration-rate thresholds with diagnostic intervention guidance |

## The Flow

```
   generation completes
        │
        ▼
   integration-verification-checklist  (Std 8)
        │      ├─ Contract verification
        │      ├─ Cross-component testing
        │      ├─ System-level smoke testing
        │      ├─ Refactoring pass (6 dimensions)
        │      └─ Five architectural review questions
        ▼
   deployment-safety-checklist  (Std 9)
        │      ├─ Quality gate classification (BLOCKING / ADVISORY / ASYNC)
        │      ├─ Pipeline track selection (Hotfix / Standard / Full)
        │      └─ Post-merge monitoring thresholds configured
        ▼
   rollback-readiness-checklist  (Std 9)
        │      ├─ Rollback classification (Clean / Migration / Data-dependent / Non-reversible)
        │      ├─ Rollback procedure documented and tested
        │      └─ Rollback owner identified and signed off
        ▼
   merge / deploy
```

## Conventions

- Every item is binary. "Yes" or "No." If you find yourself answering
  "kind of," the item needs further decomposition or you are
  rationalizing.
- An unchecked item is a deviation, not an oversight. Document the
  reason in the PR or in `ESCALATION.md` (see
  `../prompts/escalation-protocol.md`).
- These checklists are minimum bars, not ceilings. Add
  project-specific items as you discover them through production
  incidents.
