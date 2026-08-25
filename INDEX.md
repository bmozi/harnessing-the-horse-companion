# Asset Index

Complete map of *Harnessing the Horse* companion assets, organized by
chapter. Each row is a single artifact the book references by URL.

> When you cite an asset from a chapter, link to its **GitHub URL**
> here. When you add an asset, update this index — it is the single
> source of truth for what exists in the companion.

## Cross-Chapter References

| Asset | File |
| --- | --- |
| Reader start paths (30-minute orientation, one governed session, governed-loop bootstrap) | [`START-HERE.md`](START-HERE.md) |
| Book-to-toolkit practice map | [`BOOK-TO-TOOLKIT-MAP.md`](BOOK-TO-TOOLKIT-MAP.md) |
| Four-book learning progression and Book 2-to-Book 3 handoff | [`SERIES-PROGRESSION.md`](SERIES-PROGRESSION.md) |
| Printable Reader Quick Start | [`output/pdf/Harnessing-the-Horse-Reader-Quick-Start-v2.1.0.pdf`](output/pdf/Harnessing-the-Horse-Reader-Quick-Start-v2.1.0.pdf) |
| Complete fictional governed-delivery-loop path | [`factory-bootstrap/worked-example/`](factory-bootstrap/worked-example/) |
| The Twelve Standards — single-page quick reference (tiers, gate classifications, key artifacts, Harness Framework mapping) | [`references/twelve-standards-quick-reference.md`](references/twelve-standards-quick-reference.md) |
| Pattern quick reference | [`references/pattern-quick-reference.md`](references/pattern-quick-reference.md) |
| Complete session loop | [`references/complete-session-loop.md`](references/complete-session-loop.md) |
| Glossary and acronym reference | [`references/glossary.md`](references/glossary.md) |
| Complete prompt library | [`prompts/complete-prompt-library.md`](prompts/complete-prompt-library.md) |
| Machine-readable prompt manifest and evaluation fixtures | [`prompts/manifest.json`](prompts/manifest.json) and [`prompt-evals/`](prompt-evals/) |
| Pipeline artifact reference | [`references/pipeline-artifact-reference.md`](references/pipeline-artifact-reference.md) |
| Quality-gate configuration reference | [`references/quality-gate-configuration-reference.md`](references/quality-gate-configuration-reference.md) |
| Tool-configuration reference | [`references/tool-configuration-reference.md`](references/tool-configuration-reference.md) |
| Portable governance distribution example | [`governance-distribution/`](governance-distribution/) |
| Edition mapping and current companion release | [`EDITION-MAP.md`](EDITION-MAP.md) |
| Confirmed corrections | [`ERRATA.md`](ERRATA.md) |

## By Chapter

### Part I — The Landscape (ch01–ch04)

Foundation material; assets begin in Part II.

### Chapter 4 — Foundations

| Section | Asset | File |
| --- | --- | --- |
| §4.1 Context File | CLAUDE.md / AGENTS.md template | [`spec-templates/claude-md-template.md`](spec-templates/claude-md-template.md) |
| §4.1 Context File (vendor-neutral) | AGENTS.md template with tool-agnostic loading notes | [`spec-templates/agents-md-template.md`](spec-templates/agents-md-template.md) |
| §4.2 Structural Guardrails | Reference `.claude/settings.json` (MIT-licensed) | [`code-examples/claude-settings/`](code-examples/claude-settings/) |
| §4.3 Architecture as First-Class Artifact | Four baseline Mermaid diagrams (System Context, Component, Data Flow, Deployment) | [`diagrams/baseline-architecture-diagrams.md`](diagrams/baseline-architecture-diagrams.md) |
| §4.4 The Harness Framework | Twelve Standards quick reference (framework mapping table) | [`references/twelve-standards-quick-reference.md`](references/twelve-standards-quick-reference.md) |
| §4.6 Pipeline Artifacts | SPEC.md template | [`spec-templates/spec-md.md`](spec-templates/spec-md.md) |
| §4.6 Pipeline Artifacts | DESIGN.md agent execution contract (traceability, invariants, proof, rollback, latitude, and human decisions) | [`spec-templates/design-md.md`](spec-templates/design-md.md) |
| §4.6 Pipeline Artifacts | IMPL_NOTES.md template | [`spec-templates/impl-notes-md.md`](spec-templates/impl-notes-md.md) |
| §4.6 Pipeline Artifacts | REVIEW.md template | [`spec-templates/review-md.md`](spec-templates/review-md.md) |

### Chapter 5 — Discovery and Planning

| Standard | Asset | File |
| --- | --- | --- |
| Std 1 — Requirements as Verifiable Contracts | SPEC.md template | [`spec-templates/spec-md.md`](spec-templates/spec-md.md) |
| Std 1 — Acceptance Criteria | Acceptance criteria template | [`spec-templates/acceptance-criteria-template.md`](spec-templates/acceptance-criteria-template.md) |
| Std 1 — Pre-Generation Gate | Pre-generation verification checklist | [`checklists/pre-generation-verification.md`](checklists/pre-generation-verification.md) |
| Std 1 — Post-Generation Gate | Post-generation verification checklist | [`checklists/post-generation-verification.md`](checklists/post-generation-verification.md) |
| Std 3 — Blast Radius Analysis (plan-time) | Blast radius (SPEC-time) template | [`spec-templates/blast-radius-template.md`](spec-templates/blast-radius-template.md) |
| Std 3 — Blast Radius Analysis (review-time) | Review-time blast radius prompt | [`prompts/blast-radius-analysis.md`](prompts/blast-radius-analysis.md) |
| §5.1 Cagan's Four Risks | Four-Risk Evidence Contract with falsifiers, evidence grades, thresholds, owners, and generation gates | [`spec-templates/cagan-four-risk-assessment.md`](spec-templates/cagan-four-risk-assessment.md) |

### Chapter 6 — Task Division and Agent Scope

| Standard | Asset | File |
| --- | --- | --- |
| Stds 2, 4–5 — Decomposition | Task specification template | [`spec-templates/task-spec.md`](spec-templates/task-spec.md) |
| Std 4 — Interface-First Design | Interface specification templates (REST, function, event) | [`spec-templates/interface-spec.md`](spec-templates/interface-spec.md) |

### Chapter 7 — Generation, Verification, and Review

| Standard | Asset | File |
| --- | --- | --- |
| Std 1 — Structured generation contract | Generation prompt template | [`prompts/structured-prompt.md`](prompts/structured-prompt.md) |
| Std 6 — Automated Quality Gates | Quality gate configuration review prompt | [`prompts/quality-gate-config-review.md`](prompts/quality-gate-config-review.md) |
| Std 7 — Falsification Review (human, disprove-only mode) | The standard review prompt | [`prompts/disprove-only-review.md`](prompts/disprove-only-review.md) |
| Std 7 — Falsification Review (agent, adversarial mode) | Fresh-instance review prompt | [`prompts/adversarial-validation.md`](prompts/adversarial-validation.md) |
| §7.3 — Subagent Challenges | Challenge clauses to embed in generation prompts | [`prompts/subagent-challenge-clauses.md`](prompts/subagent-challenge-clauses.md) |
| §7.3 — Verification Stance | `verified` / `ASSUMPTION` / `VERIFY` marker convention | [`prompts/verification-stance-markers.md`](prompts/verification-stance-markers.md) |
| Std 6 — Governed exceptions | Quality gate failure escalation prompt + ESCALATION.md format | [`prompts/escalation-protocol.md`](prompts/escalation-protocol.md) |

### Chapter 8 — Execution Discipline

| Standard | Asset | File |
| --- | --- | --- |
| Std 8 — Integration Verification | Pre-merge checklist (contract verification, cross-component testing, smoke testing, refactoring pass, five architectural questions) | [`checklists/integration-verification-checklist.md`](checklists/integration-verification-checklist.md) |
| Std 9 — Release and Rollback Readiness | Pre-deploy checklist (gate classification, pipeline tracks, post-merge monitoring thresholds) | [`checklists/deployment-safety-checklist.md`](checklists/deployment-safety-checklist.md) |
| Std 9 — Release and Rollback Readiness | Pre-deploy checklist (rollback classification, procedure documented + tested, owner identified) | [`checklists/rollback-readiness-checklist.md`](checklists/rollback-readiness-checklist.md) |

### Chapter 9 — Architectural Stewardship (Std 10)

| Section | Asset | File |
| --- | --- | --- |
| §9.1 Impact Boundary Assessment | Five-question checklist + drift scan classification | [`checklists/impact-boundary-assessment.md`](checklists/impact-boundary-assessment.md) |
| §9.2 Simplicity Review | Four Ousterhout-derived tests (deep module, YAGNI, comprehension, delete) | [`checklists/simplicity-review.md`](checklists/simplicity-review.md) |
| §9.3 ADRs in the Agentic Era | ADR template with Agent Implications section + three-tier approach | [`spec-templates/adr-template.md`](spec-templates/adr-template.md) |

### Chapter 10 — Compounding Practices (Stds 11–12)

| Section | Asset | File |
| --- | --- | --- |
| §10.3 Crawl-Walk-Run Maturity Model | Five-level self-assessment with key indicators, risk profiles, advancement triggers, and the 30-day adoption path | [`exercises/maturity-assessment.md`](exercises/maturity-assessment.md) |
| §10.4 Definition of Done | DN1–DN7 checklist with four BLOCKING items | [`checklists/definition-of-done.md`](checklists/definition-of-done.md) |

### Chapter 11 — Integration Patterns for Agent-System Boundaries

| Section | Asset | File |
| --- | --- | --- |
| §11.1 Anti-Corruption Layer | Pattern reference card | [`patterns/anti-corruption-layer.md`](patterns/anti-corruption-layer.md) |
| §11.1 + §11.2 ACL + Hexagonal | TypeScript port/adapter (MIT) | [`code-examples/anti-corruption-layer/`](code-examples/anti-corruption-layer/) |
| §11.2 Hexagonal Architecture | Pattern reference card | [`patterns/hexagonal-architecture.md`](patterns/hexagonal-architecture.md) |
| §11.5 Transactional Outbox | Pattern reference card | [`patterns/transactional-outbox.md`](patterns/transactional-outbox.md) |
| §11.5 Transactional Outbox | SQL schema + TypeScript handler (MIT) | [`code-examples/transactional-outbox/`](code-examples/transactional-outbox/) |
| §11.3 Enterprise Integration Patterns | Pattern catalog index | [`patterns/README.md`](patterns/README.md) — Message Bus, Idempotent Receiver, Dead Letter Channel, Content-Based Router |
| §11.4 Resilience | Pattern catalog index | [`patterns/README.md`](patterns/README.md) — Circuit Breaker, Centrifuge |

### Chapter 12 — Migration at Scale with AI Agents

| Section | Asset | File |
| --- | --- | --- |
| §12.2 Migration Plan as Artifact | Migration plan template (Strangler Fig discipline) | [`spec-templates/migration-plan-template.md`](spec-templates/migration-plan-template.md) |
| §12.2 Phase Gate | Phase-transition checklist (pre-conditions, acceptance criteria, rollback triggers, sign-off) | [`checklists/migration-phase-gate.md`](checklists/migration-phase-gate.md) |
| §12.3 Build vs. Buy | OSS license-class triage worksheet (five classes + per-dependency template) | [`checklists/oss-license-triage.md`](checklists/oss-license-triage.md) |
| §12.4 Event Sourcing / CQRS / Bounded Contexts | Pattern catalog index | [`patterns/README.md`](patterns/README.md) |

### Chapter 13 — Designing AI Agent Infrastructure

| Section | Asset | File |
| --- | --- | --- |
| §13.1 Dry-Run-Default | Pattern reference card | [`patterns/dry-run-default.md`](patterns/dry-run-default.md) |
| §13.1 Scoped Authorization Token | Pattern reference card | [`patterns/scoped-authorization-token.md`](patterns/scoped-authorization-token.md) |
| §13.1 MCP Tool Pattern | TypeScript MCP tool with scope check + validate + dry-run gate (MIT) | [`code-examples/mcp-tool-pattern/`](code-examples/mcp-tool-pattern/) |
| §13.1 MCP Server Fleet | Pattern catalog index (described in prose only) | [`patterns/README.md`](patterns/README.md) |
| §13.2 Agent-Facing API Design | Catalog index (Domain-Named Operations, Composability, Consistency) | [`patterns/README.md`](patterns/README.md) |
| §13.3 Composite-Key Idempotency / CAS-Guarded Distributed Commit | Pattern catalog index | [`patterns/README.md`](patterns/README.md) |
| §13.4 Backend for Frontend for Agents | Pattern catalog index | [`patterns/README.md`](patterns/README.md) |
| §13.6 MCP Server Fleet implementation notes | Walkthrough of the fleet as built | [`exercises/case-study-walkthroughs.md`](exercises/case-study-walkthroughs.md#chapter-13--mcp-server-fleet-implementation-notes-136) |
| §13.6 Per-tool RBAC | Scoped Authorization Token (per-tool RBAC application) | [`patterns/scoped-authorization-token.md`](patterns/scoped-authorization-token.md) |

### Chapter 14 — Case Study: CRM Integration Hub

| Asset | File |
| --- | --- |
| Case study walkthrough | [`exercises/case-study-walkthroughs.md`](exercises/case-study-walkthroughs.md#chapter-14--crm-integration-hub) |
| Anti-Corruption Layer pattern (case-applied) | [`patterns/anti-corruption-layer.md`](patterns/anti-corruption-layer.md) |
| Hexagonal Architecture (case-applied) | [`patterns/hexagonal-architecture.md`](patterns/hexagonal-architecture.md) |
| TypeScript port/adapter | [`code-examples/anti-corruption-layer/`](code-examples/anti-corruption-layer/) |
| OSS license triage (developed in this engagement) | [`checklists/oss-license-triage.md`](checklists/oss-license-triage.md) |

### Chapter 15 — Case Study: The E-Commerce Platform and Its Checkout

| Asset | File |
| --- | --- |
| Case study walkthrough | [`exercises/case-study-walkthroughs.md`](exercises/case-study-walkthroughs.md#chapter-15--the-e-commerce-platform-and-its-checkout) |
| SPEC.md template (recursive specification building block) | [`spec-templates/spec-md.md`](spec-templates/spec-md.md) |
| CAS-Guarded Distributed Commit pattern reference card (§15.7, the double-charge problem) | [`patterns/cas-guarded-distributed-commit.md`](patterns/cas-guarded-distributed-commit.md) |
| Scoped Authorization Token (Magic Link customer-session application, §15.9) | [`patterns/scoped-authorization-token.md`](patterns/scoped-authorization-token.md) |
| Anti-Corruption Layer (vendor data quality application) | [`patterns/anti-corruption-layer.md`](patterns/anti-corruption-layer.md) |

### Chapter 16 — Case Study: The Merlin Software Factory

| Asset | File |
| --- | --- |
| Case study walkthrough | [`exercises/case-study-walkthroughs.md`](exercises/case-study-walkthroughs.md#chapter-16--the-merlin-software-factory) |
| Express Arc pattern reference card | [`patterns/express-arc.md`](patterns/express-arc.md) |
| STRATEGIC_PIVOT.md template | [`spec-templates/strategic-pivot-template.md`](spec-templates/strategic-pivot-template.md) |
| Iteration caps checklist (bounded iteration discipline) | [`checklists/iteration-caps.md`](checklists/iteration-caps.md) |
| Self-improvement safety rails | [`checklists/self-improvement-safety-rails.md`](checklists/self-improvement-safety-rails.md) |
| Minimum governed delivery loop bootstrap kit | [`factory-bootstrap/`](factory-bootstrap/) |
| Public teaching architecture (current operating model) | [`diagrams/merlin-architecture-v2.md`](diagrams/merlin-architecture-v2.md) |
| Premium architecture overview (recommended first view) | [`diagrams/merlin-factory-architecture-premium.png`](diagrams/merlin-factory-architecture-premium.png) |
| Software-factory conceptual and presentation visual | [`diagrams/merlin-software-factory-promo.png`](diagrams/merlin-software-factory-promo.png) |
| Five focused teaching panels (preflight, EXPRESS, proof, judgment, learning) | [`diagrams/merlin-architecture-v2-visual-1.png`](diagrams/merlin-architecture-v2-visual-1.png) |
| Five-page print-friendly teaching set | [`diagrams/merlin-architecture-v2-visual.pdf`](diagrams/merlin-architecture-v2-visual.pdf) |
| Original blueprint lesson (historical, sanitized) | [`diagrams/merlin-architecture.md`](diagrams/merlin-architecture.md) |

### Chapter 17 — Security in the Agentic Era

| Section | Asset | File |
| --- | --- | --- |
| §17.3 / §17.6 Generation Trifecta (extended to six vectors) | Six-category security review checklist + OWASP Agentic Top 10 mapping | [`checklists/security-review.md`](checklists/security-review.md) |
| §17.2 Prompt Injection Defense | Four-layer defense prompt (privilege minimization, input-output separation, output validation, human-in-the-loop) | [`prompts/prompt-injection-defense.md`](prompts/prompt-injection-defense.md) |
| §17.3 Supply Chain (MCP servers) | Security review section: MCP Server Supply-Chain Defense | [`checklists/security-review.md`](checklists/security-review.md) |
| §17.4 Memory Poisoning | Security review section: Memory Poisoning Defensive Postures | [`checklists/security-review.md`](checklists/security-review.md) |
| §17.5 Tool Misuse | Existing companion asset | [`patterns/scoped-authorization-token.md`](patterns/scoped-authorization-token.md) |

### Chapter 18 — Measuring What Matters

| Section | Asset | File |
| --- | --- | --- |
| §18.1 Personal calibration — weekly | Calibration journal template (three sections + weekly metrics rollup) | [`spec-templates/calibration-journal.md`](spec-templates/calibration-journal.md) |
| §18.1 Personal eval set | Personal benchmark suite template with scoring rubric | [`spec-templates/personal-eval-set.md`](spec-templates/personal-eval-set.md) |
| §18.1 Quarterly self-A/B | Hand-coded vs. agentic comparison protocol | [`exercises/quarterly-self-ab-test.md`](exercises/quarterly-self-ab-test.md) |
| §18.5 Building Your Dashboard | Five metric groups (Delivery / Quality / Cost / Team Health / Maturity), agent-vs-human attribution, regeneration-rate thresholds | [`checklists/metrics-dashboard.md`](checklists/metrics-dashboard.md) |

### Chapter 19 — Team Transformation

| Section | Asset | File |
| --- | --- | --- |
| §19.1 / §19.5 / §19.6 Crawl + 30 Days + Anti-Patterns | Week-by-week 30-day Crawl-stage roadmap with three anti-patterns | [`exercises/30-day-transformation-roadmap.md`](exercises/30-day-transformation-roadmap.md) |
| §19.1 Expertise Levels and Their Traps | Beginner / Mid-level / Senior / Principal framework with trap and countermeasure per level | [`exercises/expertise-traps.md`](exercises/expertise-traps.md) |
| §19.1 Maturity progression | Existing companion asset | [`exercises/maturity-assessment.md`](exercises/maturity-assessment.md) |
| §19.1 / §19.2 First governed loop | Minimum governed delivery loop bootstrap kit | [`factory-bootstrap/`](factory-bootstrap/) |

### Chapter 20 — The Road Ahead

Largely forward-looking narrative. Operational artifacts are
covered by existing companion content:

| Section | Asset | File |
| --- | --- | --- |
| §20.4 Recursive Dark Code / Self-Improvement Governance | Existing companion asset | [`checklists/self-improvement-safety-rails.md`](checklists/self-improvement-safety-rails.md) |
| §20.6 Discipline Dividend / Institutional Capital | Existing companion asset | [`exercises/maturity-assessment.md`](exercises/maturity-assessment.md) |
| §20.9 Artifact path | Minimum governed delivery loop bootstrap kit | [`factory-bootstrap/`](factory-bootstrap/) |

### Appendix B — Design Study: Platform Modernization (FieldstoneOS)

A documented architecture and migration plan, none of it yet built.

| Section | Asset | File |
| --- | --- | --- |
| Design study walkthrough | [`exercises/case-study-walkthroughs.md`](exercises/case-study-walkthroughs.md#appendix-b--design-study-platform-modernization-fieldstoneos) |
| §B.2 Event-Sourced Architecture | Event Sourcing pattern reference card | [`patterns/event-sourcing.md`](patterns/event-sourcing.md) |
| §B.3 Migration Plan | Migration plan template | [`spec-templates/migration-plan-template.md`](spec-templates/migration-plan-template.md) |
| §B.3 Phase Gates | Migration phase gate checklist | [`checklists/migration-phase-gate.md`](checklists/migration-phase-gate.md) |
| §B.4 Testing a Migration | Equivalence test checklist (three test categories) | [`checklists/equivalence-test-checklist.md`](checklists/equivalence-test-checklist.md) |
| §B.2 UCO Event Publication | Transactional Outbox pattern reference card | [`patterns/transactional-outbox.md`](patterns/transactional-outbox.md) |

### Academic / Instructor / Student

| Asset | File | Audience |
| --- | --- | --- |
| Case Study Analysis Framework | [`exercises/case-study-analysis-framework.md`](exercises/case-study-analysis-framework.md) | Students, capstone, self-study |
| Chapter Study Guides and 91 exercises | [`study-guides/`](study-guides/) | Students, instructors, self-study |
| Competency and curriculum map | [`academic/competency-curriculum-map.md`](academic/competency-curriculum-map.md) | Program leads, instructors |

The full instructor package (solutions, grading rubrics, discussion
prompts) is distributed separately to verified instructors by the
author.

---

## By Asset Category

- **SPEC templates** ([`spec-templates/`](spec-templates/)) — 17 files
- **Patterns** ([`patterns/`](patterns/)) — 8 reference cards + catalog index
- **Prompts** ([`prompts/`](prompts/)) — reusable prompt library plus a machine-readable manifest
- **Checklists** ([`checklists/`](checklists/)) — 17 files
- **Prompt evaluations** ([`prompt-evals/`](prompt-evals/)) — representative structured-generation, falsification-review, and escalation fixtures
- **Governed loop bootstrap** ([`factory-bootstrap/`](factory-bootstrap/)) — seven scaffolds plus a completed fictional golden path for building Book 2's minimum governed delivery loop
- **References** ([`references/`](references/)) — standards, patterns, the complete session loop, glossary, pipeline artifacts, quality gates, and tool configuration
- **Diagrams** ([`diagrams/`](diagrams/)) — canonical Mermaid/Markdown and
  HTML sources plus PNG, JPEG, WebP, and PDF exports for the baseline and
  Merlin Software Factory architecture sets
- **Exercises** ([`exercises/`](exercises/)) — 6 files (case-study framework + maturity + walkthroughs + quarterly self-A/B + 30-day roadmap + expertise traps)
- **Code examples** ([`code-examples/`](code-examples/)) — 4 directories (claude-settings, anti-corruption-layer, transactional-outbox, mcp-tool-pattern)
- **Compatibility examples** ([`examples/`](examples/)) — exact paths referenced by the first KDP edition, mapped to the canonical `code-examples/` and `checklists/` assets

## Licensing

This repository is dual-licensed:

- **Source code** in `code-examples/` → **MIT** ([`LICENSE-CODE`](LICENSE-CODE))
- **Written content** (templates, prompts, checklists, references,
  exercises, diagrams, prose) → **CC BY-NC-SA 4.0**
  ([`LICENSE-CONTENT`](LICENSE-CONTENT))

The dispatcher [`LICENSE`](LICENSE) explains the split. The dual setup
is intentional: code travels without friction (MIT), written
contributions are protected against commercial repackaging
(CC BY-NC-SA 4.0).

## Linking From Chapters

When a chapter in the manuscript references an asset here, use a direct
GitHub URL or a stable release tag URL:

```markdown
See the [Disprove-Only Review prompt](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/prompts/disprove-only-review.md)
in the companion repository.
```

```markdown
See [`prompts/disprove-only-review.md` in the v2.1.0 companion
release](https://github.com/bmozi/harnessing-the-horse-companion/blob/v2.1.0/prompts/disprove-only-review.md).
```
