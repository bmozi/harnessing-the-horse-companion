# The Twelve Standards — Quick Reference

All Twelve Standards from *Harnessing the Horse* in a single-page reference, organized by tier. Each standard includes its chapter home, one-line description, quality gate classification, and the key artifact or practice it requires.

This reference is the canonical companion to Chapter 4 §4.4's "Framework Mapped to the Twelve Standards" table. Standard names, tier assignments, and Harness discipline mappings on this page match the book exactly.

For the full treatment — rationale, failure modes, prompts, and worked examples — see the referenced chapters.

---

## Tier 1: Plan (Chapter 5)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 1 | Requirements as Verifiable Contracts | SPEC.md provides the durable, machine-verifiable contract. A structured generation prompt projects its requirements, constraints, interfaces, dependencies, MUST-NOT list, output format, and review criteria into one bounded session. | BLOCKING (existence, structure, and traceability) | SPEC.md; structured generation contract; pre/post-generation verification gates |
| 2 | Scope Definition and Session Boundaries | Agent sessions scoped to under 400 LOC and under 60 minutes of review time; one task per session. Tasks decomposed into a clean DAG — decomposition and single-responsibility sessions are one standard, in planning and execution views. | BLOCKING | DESIGN.md with task decomposition; session protocol |
| 3 | Blast Radius Analysis | Quantify impact surface across five dimensions: direct, dependency, data, external, rollback. One template, used twice — estimated at planning, verified at review. Drives review effort and pipeline track selection. | BLOCKING (at plan and at review) | Blast Radius Estimate in SPEC.md; review-time verification |

## Tier 2: Design (Chapter 6)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 4 | Interface-First Design | Define the interface contract before implementation. Three forms: REST endpoint, internal function, event/message schema. | BLOCKING (interface-first for multi-module work) | Interface specification |
| 5 | Dependency Discipline | Declare all dependencies — external, internal, and implicit — before generation, against an explicit allowlist. Undeclared dependencies fail the gate. | BLOCKING (allowlist) | Dependency manifest / allowlist |

## Tier 3: Generate & Verify (Chapter 7)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 6 | Automated Quality Gates and Governed Exceptions | Four-tier classification: BLOCKING / ADVISORY / INFORMATIONAL / ASYNC. No silent bypass. Contested findings and thrashing route through documented authority, mitigation, and remediation; the default trigger is 30 minutes or 3 non-converging iterations. | BLOCKING configuration and exception record | CI/CD gate configuration; ESCALATION.md when triggered |
| 7 | Falsification Review | One falsification principle, two modes. Human mode: disprove-only review with the three-question form. Agent mode: a fresh agent instance with zero shared context adversarially challenges the output. | BLOCKING (human mode); agent mode BLOCKING on the Full track | REVIEW.md with three-question form and dispositioned adversarial findings |

## Tier 4: Ship (Chapter 8)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 8 | Integration Verification | Contract verification, cross-component testing, system-level smoke testing, refactoring pass, five architectural questions. | BLOCKING (first integration) | Integration verification checklist |
| 9 | Release and Rollback Readiness | Pipeline track assignment (Full, Standard, Hotfix), post-merge monitoring thresholds, and rollback classification (clean revert, migration, data-dependent, non-reversible) with a documented, tested procedure. | BLOCKING | Pipeline track assignment + rollback plan |

## Tier 5: Steward (Chapter 9)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 10 | Architectural Stewardship and Debt Governance | Architecture fitness functions enforce boundaries mechanically. A three-tier debt register in IMPL_NOTES.md records must-fix-before-merge, should-fix-soon, and can-defer decisions. | BLOCKING (fitness functions, must-fix debt); ADVISORY (debt metrics) | Architecture fitness functions + IMPL_NOTES.md debt register |

## Tier 6: Compound (Chapter 10)

| # | Standard | Description | Gate | Key Artifact |
| --- | --- | --- | --- | --- |
| 11 | The Knowledge Loop | Capture, context-file lifecycle, and close-the-loop are one discipline. Keep root context lean, decompose by bounded context when necessary, load relevant knowledge deterministically, and save new knowledge after each discovery. | ADVISORY | AGENTS.md / CLAUDE.md + pattern library / ADR index / postmortem catalog |
| 12 | Continuous Improvement of the Standards | Every standard is a hypothesis tested against measured outcomes. Bounded autonomous improvement requires a human approval gate; the standards are reviewed on a quarterly cadence. | ADVISORY (quarterly) | Improvement proposals + quarterly standards review |

---

## The Harness Framework

The Twelve Standards map to the four disciplines of the Harness Framework — Scope, Prove, Enforce, Communicate. Every standard strengthens one or more disciplines. Mapping below matches Chapter 4 §4.4 exactly.

| Standard | Chapter | Primary Discipline |
| --- | --- | --- |
| 1: Requirements as Verifiable Contracts | 5 | Scope + Prove |
| 2: Scope Definition and Session Boundaries | 5 | Scope |
| 3: Blast Radius Analysis | 5 | Scope + Prove |
| 4: Interface-First Design | 6 | Scope + Enforce |
| 5: Dependency Discipline | 6 | Scope + Enforce |
| 6: Automated Quality Gates and Governed Exceptions | 7 | Enforce + Communicate |
| 7: Falsification Review | 7 | Prove |
| 8: Integration Verification | 8 | Prove + Enforce |
| 9: Release and Rollback Readiness | 8 | Enforce + Communicate |
| 10: Architectural Stewardship and Debt Governance | 9 | Enforce + Communicate |
| 11: The Knowledge Loop | 10 | Communicate |
| 12: Continuous Improvement of the Standards | 10 | All four |

Standard 1 also supplies the generation contract demonstrated in Chapter 7. Standard 12 strengthens all four disciplines and is the only standard mapped to every column.

---

## Quality Gate Classification (Four-Tier)

The book teaches the four-tier classification, canonical in Chapter 7 §7.2 and applied in Chapter 8 (deployment) and Chapter 10 (Definition of Done).

| Tier | Behavior | When Gate Fails |
| --- | --- | --- |
| **BLOCKING** | Halts pipeline; PR cannot merge | Resolution required before proceeding |
| **ADVISORY** | Pipeline proceeds; finding surfaced for reviewer judgment | Documented in REVIEW.md; reviewer exercises judgment |
| **INFORMATIONAL** | Pipeline proceeds; data captured for dashboards and trend analysis | No merge impact; informs longer-term improvement |
| **ASYNC** | Runs outside the synchronous PR pipeline; the PR remains pending until the result returns | Failure blocks merge; resolution is required before approval |

Existing CI pipelines using "NON-BLOCKING" should rename to ADVISORY and consider whether INFORMATIONAL is a more appropriate classification for noisy gates that should not gate any decision.

---

## Pipeline Tracks

| Track | When to Use | Gates Applied |
| --- | --- | --- |
| **Full** | High-risk, cross-boundary, data-migration changes | All standards, adversarial validation (Standard 7, agent mode), staged rollout |
| **Standard** | Typical feature work | Core standards, disprove-only review (Standard 7, human mode) |
| **Hotfix** | Isolated, contained, time-sensitive fixes | Automated gates and reviewer retained; documentation may follow within 24 hours |

---

## Definition of Done (DN1–DN7)

Per Chapter 10 §10.4.

| # | Item | Blocking? |
| --- | --- | --- |
| DN1 | Specification complete (SPEC.md with the six canonical sections, acceptance criteria, MUST-NOT list, scope boundary) | Yes |
| DN2 | Design validated (DESIGN.md with task decomposition, clean DAG, interface contracts) | Yes |
| DN3 | Implementation documented (IMPL_NOTES.md with deviations, constraints, tech debt) | No |
| DN4 | Quality gates passed (all BLOCKING gates pass; ADVISORY findings documented in REVIEW.md; INFORMATIONAL data captured; ASYNC gates resolved before merge) | Yes |
| DN5 | Review complete (REVIEW.md with three-question form filled, falsification findings from both modes dispositioned, all CRITICAL findings resolved) | Yes |
| DN6 | Provenance captured (commit metadata links to SPEC, DESIGN, session ID, model identifier, reviewer name — every line traces to its origin) | No |
| DN7 | Loop closed (AGENTS.md / CLAUDE.md updated with session learnings; honest assessment recorded) | No |

---

## Maturity Model

| Level | Name | Key Indicators |
| --- | --- | --- |
| 1 | Ad Hoc | No SPEC.md, no AGENTS.md, no consistent review, defects found in production |
| 2 | Repeatable | SPEC.md exists but quality varies, reviews happen but thoroughness varies |
| 3 | Defined | All artifacts produced consistently, quality gates automated, metrics tracked |
| 4 | Measured | Metrics drive improvement, declining defect rates, DORA metrics tracked |
| 5 | Optimizing | Multi-agent orchestration, automated drift detection, continuous standard evolution (Standard 12 in production) |

30-day path to Level 3: Week 1 (context file + SPEC.md), Week 2 (DESIGN.md + scope constraints + CI gates), Week 3 (adversarial validation + REVIEW.md + metrics), Week 4 (first retrospective + close the loop).
