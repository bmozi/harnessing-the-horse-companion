# Competency Map and Curriculum Alignment

This appendix serves two audiences: competency-based education (CBE) programs that need the book's standards expressed as demonstrable competencies with objective assessments, and instructors who need the book mapped to the curriculum frameworks their programs answer to. The premise carries over from the book itself — each standard names an observable work product, and the book's quality gates double as assessments: the gate either passes or it does not. Seat time is irrelevant; the artifact chain is the evidence.

---

## 1. The Twelve Competencies (C1–C12)

Each competency corresponds to one of the Twelve Standards. A competency is achieved when its evidence artifact exists and its gate passes — binary at the gate level, portfolio-based overall. The mapping is program-agnostic and works under both direct-assessment and credit-hour-equivalent CBE structures. Chapter study guides supply the evidence-producing tasks; the references below point to those exercise sets.

### Tier 1 — Plan

**C1 — Requirements as Verifiable Contracts (Standard 1).**
*Statement:* The learner produces a durable specification with machine-verifiable acceptance criteria, a MUST-NOT list, and an explicit scope boundary, then assembles a structured generation contract whose instructions trace to that specification.
*Evidence artifact:* SPEC.md plus the session's structured generation prompt.
*Objective assessment:* The pre-generation gate (DN1, Specification Complete) passes; every prompt constraint traces to a requirement, interface, dependency declaration, or MUST-NOT item in the durable artifacts; no unconstrained generation request remains.
*Chapter home:* Chapter 5, with the generation practice demonstrated in Chapter 7; see Exercises 5.1, 5.4, and 7.1.

**C2 — Scope Definition and Session Boundaries (Standard 2).**
*Statement:* The learner decomposes a feature into single-responsibility agent sessions with explicit scope boundaries.
*Evidence artifact:* A task decomposition within DESIGN.md.
*Objective assessment:* The decomposition checklist (DN2): each task under 400 lines and under 60 minutes of review, dependencies forming a clean DAG.
*Chapter home:* Chapter 5, with the worked decomposition example in Chapter 6; see Exercise 5.2, and Exercise 6.4 for re-decomposition under changed requirements.

**C3 — Blast Radius Analysis (Standard 3).**
*Statement:* The learner estimates a change's blast radius at planning time and verifies the estimate at review time.
*Evidence artifact:* A completed blast radius template, estimated and verified.
*Objective assessment:* Template completeness across the five dimensions, plus a review-time verification entry; the estimate-versus-actual comparison is the gradeable record.
*Chapter home:* Chapter 5; see Exercise 5.3, and the six-vector threat-modeling Exercise 17.2, which applies the same reachability question to security.

### Tier 2 — Design

**C4 — Interface-First Design (Standard 4).**
*Statement:* The learner defines interface contracts before implementation and demonstrates that generated code conforms to them.
*Evidence artifact:* Interface definitions committed before generation, plus conforming generated code.
*Objective assessment:* Contract tests or compilation against the pre-committed interfaces pass; interface commit timestamps precede generation.
*Chapter home:* Chapter 6; see Exercises 6.1 and 6.3.

**C5 — Dependency Discipline (Standard 5).**
*Statement:* The learner declares every dependency before generation and passes a dependency audit with zero undeclared additions.
*Evidence artifact:* The dependency declaration in SPEC.md/DESIGN.md plus the audit output.
*Objective assessment:* The dependency audit gate: zero imports outside the declared list, lockfile integrity verified.
*Chapter home:* Chapter 6; see Exercise 6.2, the license-class triage in Exercise 12.3, and the supply-chain classification in Exercise 17.1.

### Tier 3 — Generate & Verify

**C6 — Automated Quality Gates and Governed Exceptions (Standard 6).**
*Statement:* The learner configures quality gates across the four tiers (BLOCKING, ADVISORY, INFORMATIONAL, ASYNC), demonstrates a blocking gate rejecting defective output, and follows the documented exception path when a finding is contested or an iteration cap is reached.
*Evidence artifact:* The gate configuration and captured rejection; where the exercise triggers an exception, ESCALATION.md with the authority and remediation record.
*Objective assessment:* A deliberately defective change is stopped by a reproducible BLOCKING gate. A contested finding or thrashing scenario produces the required record at the protocol trigger, with root cause, authority level, and remediation plan; silent bypass fails the competency.
*Chapter home:* Chapter 7; see Exercises 7.2 and 7.4, and the crawl-stage guardrail work in Exercise 19.1.

**C7 — Falsification Review (Standard 7).**
*Statement:* The learner conducts a falsification review — human disprove-only review plus adversarial agent validation — that surfaces documented findings on seeded defects.
*Evidence artifact:* REVIEW.md with verification stance markers and adversarial findings.
*Objective assessment:* The seeded-defect gate: known planted defects are found and documented (DN5); a review with no substantive findings on defective input fails.
*Chapter home:* Chapter 7; see Exercises 7.3 and 7.6, which supply the human and agent modes respectively.

### Tier 4 — Ship

**C8 — Integration Verification (Standard 8).**
*Statement:* The learner verifies integration at trust boundaries with automated tests that fail on contract violations.
*Evidence artifact:* Trust-boundary integration tests.
*Objective assessment:* The tests demonstrably fail when a boundary contract is violated (a mutation of the contract breaks the suite) and pass otherwise.
*Chapter home:* Chapter 8; see Exercise 8.2.

**C9 — Release and Rollback Readiness (Standard 9).**
*Statement:* The learner ships behind a rollback-ready release plan and demonstrates a successful rollback.
*Evidence artifact:* The release plan plus the recorded rollback demonstration.
*Objective assessment:* The rollback executes successfully against the deployed change; the plan states the rollback trigger in advance.
*Chapter home:* Chapter 8; see Exercises 8.1 and 8.4, with the rollback executed under incident conditions in Exercise 8.5.

### Tier 5 — Steward

**C10 — Architectural Stewardship and Debt Governance (Standard 10).**
*Statement:* The learner detects architectural drift with a CI-enforced fitness function and records debt decisions in an ADR.
*Evidence artifact:* The fitness function configuration plus an ADR.
*Objective assessment:* The fitness function fails the build on a seeded boundary violation; the ADR captures context, decision, alternatives, and consequences.
*Chapter home:* Chapter 9; see Exercises 9.1 and 9.2.

### Tier 6 — Compound

**C11 — The Knowledge Loop (Standard 11).**
*Statement:* The learner closes the loop after every session — context files and retrospective findings updated.
*Evidence artifact:* The context-file diff and retrospective entries across a sequence of sessions.
*Objective assessment:* Artifact inspection (DN7): each session in the assessed sequence ends with a traceable update; an unchanged context file across the sequence fails.
*Chapter home:* Chapter 10; see Exercises 10.1, 10.2, and 10.5, whose close-the-loop artifact chain is the DN7 evidence.

**C12 — Continuous Improvement of the Standards (Standard 12).**
*Statement:* The learner proposes, tests, and documents one measured improvement to the standards themselves.
*Evidence artifact:* The improvement proposal with before/after measurement.
*Objective assessment:* The proposal states a hypothesis, the measurement design is sound (Chapter 18's definitions), and the documented outcome — adopted or rejected — follows from the data.
*Chapter home:* Chapter 10; see Exercises 10.3 and 10.4, and the measurement-design work in Exercises 18.1 and 18.2, which supplies the instrumentation this competency depends on.

**Portfolio completion.** A learner completes the portfolio when all twelve competencies are evidenced by artifacts whose gates pass. The chapter exercises are designed so that a single sustained project can produce most of the portfolio; the case-study and Part V exercises supply the analysis and governance evidence a single project cannot.

### The Sustained Project

The competency model assumes one project that persists across the course. The reference brief below is a shape that works, offered so a program does not have to invent one; any project matching the shape criteria at the end of this section serves equally well. The brief is program-agnostic and requires no specific vendor.

**Reference brief: a bookings-and-notifications service.** A small but real multi-component service — for a tutoring center, a clinic, a rehearsal space. Four parts: a *bookings module* exposing an API (create, reschedule, cancel, with capacity and cutoff rules); a *notifications module* that sends confirmations and reminders; a persistence layer that undergoes at least one schema migration during the course; and exactly one external integration — a calendar, email, or SMS provider — wrapped in an adapter. The service is small enough to hold in one head and real enough that every competency's artifact lands naturally:

- The booking rules supply binary acceptance criteria, a six-category MUST-NOT list, and a scope boundary worth stating (C1), plus a genuine blast radius across the bookings–notifications boundary (C3).
- Two modules with a documented boundary give the task decomposition (C2), the interface contracts (C4), and the fitness-function and drift work (C10) something true to enforce.
- The external integration exercises dependency discipline (C5) and trust-boundary integration tests that fail on contract violations (C8).
- State that matters — a lost booking is a lost booking — makes the rollback classification and the recorded rollback demonstration honest (C9).
- The remaining workflow competencies (C1, C6–C7, C11–C12) arise in any sustained project; a sequence of sessions on the same codebase is what makes the C11 context-file diff and C12 improvement measurement meaningful.

Programs may substitute freely — an inventory-and-alerts service, a lab-equipment lender, a submission-grading queue — provided the substitute keeps the shape: at least two modules with a documented boundary, one datastore with at least one migration, one external integration behind an adapter, and state a defective deployment could actually damage.

**Minimum infrastructure.** Four items, all available at no cost:

1. **A repository host with branch protection and pull-request reviews enabled.** The review competencies and provenance capture assume merges happen through reviewed PRs, not direct pushes to the main branch.
2. **One CI runner executing the companion tool-configuration reference's quality-gate workflow.** A single hosted runner on any mainstream host's free tier suffices; the four-tier gate structure is the requirement (C6), not the vendor.
3. **A deploy target.** As simple as a container on a free tier — but real enough that the C9 rollback is an action performed and recorded, not a paragraph describing one.
4. **An agentic coding tool of the student's choice.** The labs are tool-agnostic. Where tool access is blocked entirely, the paper variants noted in the chapter study guides keep every artifact-producing exercise runnable; only live generation itself is lost.

---

## 2. Curriculum Alignment

The tables below condense the chapter-by-chapter mapping in the Academic Supplement, which remains the instructor-facing deep version with Bloom's levels and per-topic detail. Table J.1 maps chapters to ACM/IEEE-CS/AAAI Computer Science Curricula 2023 (CS2023) knowledge areas, concentrated in Software Engineering (SE), Artificial Intelligence (AI), Security (SEC), and Society, Ethics, and Professionalism (SEP). Table J.2 maps chapters to SWEBOK v4 (IEEE Computer Society, 2024) knowledge areas; the book's coverage concentrates in three areas new to v4 — Software Architecture, Software Security, and Software Engineering Operations — alongside the classical KAs.

### Table 1 — Chapters to CS2023 Knowledge Areas

| Chapter | CS2023 knowledge areas |
|---|---|
| 1 | SE: Process; SEP: Professional Ethics |
| 2 | AI; SE: Process |
| 3 | SE: Project Management (economics); SEP |
| 4 | SE: Design; SE: Process |
| 5 | SE: Requirements Engineering |
| 6 | SE: Construction; SE: Design |
| 7 | SE: Verification and Validation |
| 8 | SE: Construction (CI/CD); SE: Process |
| 9 | SE: Design (architecture, drift, governance) |
| 10 | SE: Process (improvement, organizational learning) |
| 11 | SE: Design (integration patterns) |
| 12 | SE: Evolution (modernization) |
| 13 | SE: Design (agent infrastructure); SEC |
| 14 | SE: Design; SE: Process; SEP |
| 15 | SE: Design; SE: Construction |
| 16 | SE: Process (factory design and governance) |
| 17 | SEC; SEP (governance, shadow AI) |
| 18 | SE: Project Management (measurement) |
| 19 | SE: Project Management (adoption); SEP |
| 20 | SE: Process; SEP (evidence, professional judgment) |
| Appendix B | SE: Design; SE: Evolution |

### Table 2 — Chapters to SWEBOK v4 Knowledge Areas

| Chapter | SWEBOK v4 knowledge areas |
|---|---|
| 1 | Software Engineering Process; Software Quality; Professional Practice |
| 2 | Software Engineering Models and Methods; Software Engineering Process |
| 3 | Software Engineering Economics; Software Engineering Management |
| 4 | Software Engineering Process; Software Requirements; Software Design |
| 5 | Software Requirements; Software Design |
| 6 | Software Design; Software Construction |
| 7 | Software Testing; Software Quality |
| 8 | Software Construction; Software Engineering Operations |
| 9 | Software Architecture; Software Quality; Software Maintenance |
| 10 | Software Engineering Process; Software Engineering Management |
| 11 | Software Architecture; Software Design; Software Construction |
| 12 | Software Maintenance; Software Engineering Process |
| 13 | Software Architecture; Software Security; Software Engineering Operations |
| 14 | Software Architecture; Software Design |
| 15 | Software Architecture; Software Construction; Software Quality |
| 16 | Software Engineering Process; Software Quality; Software Engineering Management |
| 17 | Software Security; Professional Practice |
| 18 | Software Engineering Management; Software Quality |
| 19 | Software Engineering Management; Software Engineering Process; Professional Practice |
| 20 | Professional Practice; Software Engineering Process |
| Appendix B | Software Architecture; Software Maintenance |

---

## 3. Assessment Philosophy

The assessment model rests on the same premise as the engineering discipline it teaches: verification beats judgment wherever verification is possible. The gates make the pass/fail floor objective. A SPEC.md either contains binary acceptance criteria or it does not; a BLOCKING gate either rejects the seeded defect or it does not; a rollback either executes or it does not. Grading disputes at that floor reduce to checking the artifact against the gate — a check a second instructor, or the student, can repeat. Above the floor, quality differentiation happens at the portfolio level, where the instructor reviews the accumulated artifact chain the way the book's own reviewers work: against the specification, with a falsification posture, on the evidence.

Portfolio completion means all twelve competencies are evidenced by gate-passing artifacts. Completion is deliberately binary per competency and cumulative overall — a learner who has eleven competencies has eleven competencies, not a percentage of a grade. Programs that require letter grades can map portfolio depth and exercise performance onto their scale; the competency record underneath stays binary.

One note on academic integrity, because this course eats its own cooking. AI use is expected in this coursework — the subject of the book is using it well — and students are held to the same standards the book prescribes for professional practice. Students must disclose their AI use and govern it: pipeline artifacts accompany AI-assisted submissions, attribution names the tool and model, reviews contain genuine findings, and reflections report what actually happened. Submitting AI-assisted work without its governance artifacts is the integrity violation — ungoverned use, not use itself. The policy is the pedagogy: a student who fabricates a REVIEW.md has failed the very competency the artifact was meant to evidence.
