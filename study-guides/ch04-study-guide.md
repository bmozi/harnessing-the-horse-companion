# Chapter 4: Foundations — Study Guide

Student and self-study material moved from Chapter 4 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why the context file is the single most important artifact in agentic development, and construct a minimum viable context file for a given project.
2. Apply the principle of least privilege to agent configuration by classifying operations into allow and deny lists and defending each classification.
3. Analyze an agentic-development failure using the four Harness Framework disciplines — Scope, Prove, Enforce, Communicate — to identify which discipline failed and what to strengthen.
4. Define the purpose, owner, and creation timing of each of the four pipeline artifacts (SPEC.md, DESIGN.md, IMPL_NOTES.md, REVIEW.md).
5. Select the appropriate pipeline track (Full, Standard, Hotfix) for a described change and defend the selection using the decision tree.
6. Evaluate the overhead figures in the harness cost table, including their stated evidentiary limits.

## Key Terms

- **Context file** — `AGENTS.md` or `CLAUDE.md`: the project-root document that captures conventions, constraints, and architecture boundaries every agent session needs to know.
- **Harness Framework** — Scope, Prove, Enforce, Communicate: the four disciplines for governing agentic development; the specification is the artifact, the framework is the governance.
- **Scope (Harness discipline)** — Define what the agent is allowed to touch: functional requirements, the MUST-NOT list, and architectural boundaries.
- **Prove (Harness discipline)** — Validate output against the specification, not against intuition, grounded in Popperian falsification.
- **Enforce (Harness discipline)** — Automate the constraints that humans forget under pressure: quality gates, guardrails, fitness functions, CI/CD rules.
- **Communicate (Harness discipline)** — Make decisions auditable, not tribal: pipeline artifacts, ADRs, escalation records, close-the-loop updates.
- **MUST-NOT list** — The negative-space section of SPEC.md. Standard 1 requires six categories (architectural, dependency, data, security, performance, behavioral), and an empty MUST-NOT list is a reliable predictor of scope drift.
- **SPEC.md** — The first pipeline artifact, with six required sections: problem statement, proposed solution, machine-readable acceptance criteria, MUST-NOT list, out of scope, affected components. Requirements are expressed as the acceptance criteria.
- **REVIEW.md** — The pipeline artifact recording the reviewer's evidence-backed verdict: gate status, requirement-by-requirement compliance, findings, disposition.
- **Pipeline tracks** — The three deployment tracks (Hotfix, Standard, Full) that match process ceremony and gate intensity to change risk.

## Review Questions

1. Name the four sections of the minimum viable context file and, for each, describe one failure it prevents.
2. Why does the reference guardrails configuration deny `git push`, and which behavioral hygiene rule expresses the same separation of duties?
3. Describe the three levels of the context hierarchy and the question each level answers.
4. Which pipeline artifact records deviations from the design, and why can the code alone not communicate them?
5. A production emergency requires a two-file fix. Which pipeline track applies, and what three constraints does that track impose?

## Discussion Questions

1. The harness cost table estimates 20% overhead at Crawl and a mature steady state of roughly 15–25% — and labels every figure an author's estimate. What evidence would your team need before accepting that overhead, and what would you measure in the first ninety days to test whether the investment is paying back?
2. Anthropic and OpenAI independently converged on the context file as an artifact. How strong is vendor convergence as evidence that a practice works? What alternative explanations exist, and what observation would distinguish between them?
3. "Never merge your own generation" assumes a second reviewer exists. How should a solo practitioner or a two-person team preserve the rule's function — breaking confirmation bias, automation bias, and the IKEA effect — without a spare colleague?

## Exercises

**Exercise 4.1 (Core) — Construct a minimum viable context file from an over-documented handoff.** *(~1 h)* You inherit a TypeScript/Node REST service using Hexagonal Architecture: domain logic in `src/domain/`, adapters in `src/adapters/`, handlers in `src/handlers/`; PostgreSQL via the repository pattern; a team ban on raw SQL outside adapters after an injection incident; tests colocated as `*.test.ts`; deployment config in `deploy/`. The departing team's fourteen-page handoff document also contains: a full ESLint configuration that CI already enforces; a style essay on preferring `const` over `let`; a planned-but-unbuilt migration to microservices "targeted for next year"; a warning that `src/adapters/search/` wraps a vendor SDK whose client silently truncates queries over 1,024 characters; and a README claim that tests live in `test/`, contradicted by the repository, where they are colocated. Write the project's root context file using the four-section template in §4.1, deciding item by item what earns its place.
*Deliverable:* A `CLAUDE.md` (or `AGENTS.md`) of one page or less, plus an exclusion log listing each handoff item you left out and the reason.
*Assessment:* Judged against the companion repository's `spec-templates/claude-md-template.md` and §4.1's failure modes: all four sections present; the injection incident captured as a living constraint (rule plus reason); the vendor-SDK truncation captured as a known fragility; the lint duplication, the style essay, and the aspirational microservices plan excluded with reasons; the tests-location contradiction resolved in favor of the repository, never the README. A file that includes everything fails on the too-long failure mode.

**Exercise 4.2 (Core) — Negotiate the guardrails a real workflow can live with.** *(~90 min)* The team maintaining the Exercise 4.1 service wants to adopt the §4.2 reference configuration — but three workflow facts collide with it: the integration tests cannot pass unless the agent runs database migrations against a disposable Docker database; the monorepo's task runner shells out to `git push` when publishing internal preview builds, so a blanket deny breaks a command engineers run many times a day; and a teammate, citing a sprint deadline, has proposed allowing `npm install` outright "so the agent stops asking." Produce the configuration you would actually ship: resolve each collision as allow, deny, or per-session grant with conditions, and write the reply to the teammate.
*Deliverable:* An annotated allow/deny/per-session configuration in the style of §4.2's reference configuration, a paragraph per collision defending the resolution, and a three-to-five-sentence reply to the teammate.
*Assessment:* Judged against §4.2's four danger categories and its misconfiguration catalog: each resolution names both the failure it prevents and the work it preserves — a deny that breaks the test loop fails on the deny-list-that-blocks-too-much misconfiguration, and a blanket allow fails on least privilege; the migration and task-runner collisions are resolved with a concrete mechanism (scoped command pattern, disposable environment, human-executed step), never a policy hope; the reply to the teammate cites at least one OWASP Top 10 for Agentic Applications risk and offers a workable alternative rather than a bare refusal.

**Exercise 4.3 (Core) — Diagnose the failures the §4.4 table does not settle.** *(~1 h)* Six incident vignettes: (a) the agent added a dependency that was on the allow list, passed every gate, and shipped a license the legal team prohibits; (b) review approved code that satisfied every acceptance criterion, and the feature still failed users because the specification described the wrong behavior; (c) a BLOCKING gate was overridden with a documented, architect-approved escalation record, and the promised remediation never happened; (d) two agents in parallel sessions each respected their specs, and the merged output contains the same helper duplicated in two modules; (e) a reviewer rejected generated code for violating a naming convention that exists only in the reviewer's head; (f) an agent reversed a deliberate design decision recorded in an ADR that no session ever loads. For each, identify the failed discipline or pair and prescribe one concrete remedy; for (b) and (c), where the nearest row of the §4.4 diagnostic table gives an incomplete answer, explain what that row misses.
*Deliverable:* A six-row diagnosis table (symptom, failed discipline(s), remedy) plus a short note on (b) and (c).
*Assessment:* Judged against §4.4: each remedy strengthens the diagnosed discipline rather than adding unrelated process; (b) locates the failure upstream of review — a Scope failure the Prove stage inherited; (c) is diagnosed as Communicate succeeding while Enforce failed at the remediation step; (f) distinguishes the ADR existing from the ADR reaching sessions. Diagnoses copied from the nearest table row without engaging the mismatch fail.

**Exercise 4.4 (Core) — Select pipeline tracks.** *(~45 min)* Classify eight changes into Full, Standard, or Hotfix using the §4.7 decision tree: (a) new OAuth integration; (b) one-line null check where the root cause is confirmed; (c) production outage fix touching two files; (d) rename of an internal helper used in one module; (e) cross-module refactor extracting a shared validation library; (f) dependency upgrade with a changed major version; (g) "urgent" fifteen-file change requested by a stakeholder; (h) schema migration adding a nullable column.
*Deliverable:* A classification memo: one line per change with the decision-tree question that settled it.
*Assessment:* Judged against the decision tree and the track anti-patterns in §4.7 — item (g) must be identified as track shopping, and any doubt must be resolved toward the heavier track.

**Exercise 4.5 (Challenge) — Audit a repository against the six foundations.** *(~3 h)* Select a real repository — one of your own projects or an open-source project you know. Assess it against all six foundations of this chapter: context file, structural guardrails, architecture diagrams, Harness Framework coverage, behavioral hygiene (as evidenced by PR history), and pipeline artifacts. *Paper variant:* your instructor provides a repository description and directory listing instead.
*Deliverable:* A gap report (one finding per foundation, each citing file-level evidence) plus a remediation plan for the top three gaps, ordered by cost against benefit.
*Assessment:* Each finding cites specific evidence (a file that exists, is stale, or is missing); each remediation maps to a section of this chapter; the context-file finding is judged against the companion repository's `spec-templates/claude-md-template.md`.
