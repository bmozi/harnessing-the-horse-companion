# Chapter 8: Execution Discipline — Study Guide

Student and self-study material moved from Chapter 8 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why individually correct components fail at integration, and apply the three-level integration verification protocol to separately generated components.
2. Apply the six-dimension refactoring pass and the five architectural review questions to assembled agent output.
3. Classify changes into the four rollback categories and construct a rollback plan that is documented, tested, and owned before deployment.
4. Design a progressive delivery plan that composes canary, dark launch, ring, and flag patterns with explicit success criteria and rollback triggers.
5. Evaluate deployment health using the DORA four key metrics, tracked separately for agent-generated and human-written code.
6. Construct CI/CD checks across the four automation levels, including the cross-artifact consistency checks that catch failures between artifacts.

## Key Terms

- **DORA metrics** — Deployment frequency, lead time for changes, change failure rate, and mean time to restore — throughput and stability, positively correlated in the Accelerate research — with deployment rework rate added as a fifth metric in 2024.
- **Four-tier gate classification** — BLOCKING, ADVISORY, INFORMATIONAL, ASYNC, defined in Chapter 7 and applied at the deployment stage by Standard 9.
- **Pipeline tracks** — The Hotfix, Standard, and Full tracks (Chapter 4) that determine which verification chain a change rides to production.
- **Trust boundary** — A point where your code interacts with a system you do not control; where integration tests catch failures that unit tests with mocks miss.
- **BLOCKING gate** — A gate whose failure halts the pipeline; deploying past one chooses speed over safety.
- **ASYNC gate** — A gate that runs in the background but must resolve before merge; where release discipline absorbs the slow-but-required checks.
- **IMPL_NOTES.md** — The running implementation log; at this tier, the destination for mid-build rollback documentation and failure patterns.

## Review Questions

1. Name the three levels of the integration verification protocol and the class of failure each catches.
2. List the four rollback classifications. Why must the classification be determined before merge rather than during the incident?
3. Which two post-merge monitoring thresholds trigger automatic rollback with no human decision, and what justifies removing the human from those two?
4. What do DORA's four key metrics measure, in their throughput and stability pairs, and what did the Accelerate research find about the relationship between the pairs?
5. What distinguishes Level 4 (cross-artifact consistency) checks from Level 3 (automated analysis), and why does the chapter call them the most valuable?

## Discussion Questions

1. An error budget structurally slows agent-generated deployments once the quarter's budget is spent — regardless of what the business wants shipped. Is a constraint that cannot be negotiated better than one that can? What failure mode does each version produce?
2. The chapter prescribes tighter monitoring for agent-generated code "until the review process earns confidence," which requires tracking agent and human code as separate classes. What are the costs of a two-class system, and what evidence should retire the distinction?
3. "The cost of an unnecessary rollback is always lower than the cost of an extended incident." Construct the strongest counterexamples — consider rollbacks that lose data or re-trigger external side effects — and restate the rule with the qualifications it actually needs.

## Exercises

**Exercise 8.1 (Core) — Classify five changes by rollback category and plan the hardest.** *(~90 min)* Classify each change: (a) a refactor of pure application code with no schema, configuration, or external-state changes; (b) a migration adding a NOT NULL column with a backfill; (c) a change to how currency amounts are serialized in stored order records; (d) dropping a deprecated column and deleting its archived rows; (e) a feature that sends SMS notifications to customers at signup. Then write the complete rollback plan for the hardest change that still admits one, and state explicitly what makes the remaining changes harder or impossible to reverse.
*Deliverable:* A five-row classification table with one-sentence justifications, plus the full rollback plan (procedure, test evidence required, owner) for your chosen change.
*Assessment:* Judged against §8.2's rollback classification and protocol and the companion repository's `checklists/rollback-readiness.md`. Full credit requires: (c) identified as data-dependent with correction scripts and validation queries in the plan; (d) and (e) identified as non-reversible with the consequences acknowledged rather than a revert asserted.

**Exercise 8.2 (Core) — Design integration verification for three separately generated components.** *(~2 h)* Component brief: session A generated a search API endpoint; session B generated the indexing worker that populates the search table; session C generated the frontend results component. The sessions shared a DESIGN.md but never saw each other's output. Design the integration verification: the contract checks to run before any code executes, the cross-component tests with real dependencies, and the system-level smoke tests. List every assumed-interface risk you can find in the arrangement.
*Deliverable:* An integration verification plan organized by the three protocol levels, plus the assumed-interface risk list.
*Assessment:* Judged against §8.1 and the companion repository's `checklists/integration-verification-checklist.md`: each of the three levels contains concrete checks (not restated goals); the pagination-shape and field-naming mismatches between sessions A, B, and C appear in the risk list; smoke tests are scoped to critical paths and bounded in time.

**Exercise 8.3 (Core) — Run the refactoring pass on assembled output.** *(~90 min)* Changeset brief: a week of agent sessions merged the following — two independently generated retry-with-backoff utilities in different modules; functions named `getUserById`, `fetchUser`, and `loadUserRecord` for the same operation; a handler importing a helper from another module's `internal/` directory; a configuration parser no remaining code references; and a third occurrence of the same try/catch/retry/log structure. Run the six-dimension refactoring pass, then answer the five architectural review questions for the changeset as a whole.
*Deliverable:* A findings table (dimension, finding, disposition) plus written answers to the five questions with evidence.
*Assessment:* Judged against §8.1's refactoring dimensions and the companion repository's `checklists/simplicity-review.md`: every seeded issue is mapped to its dimension; the `internal/` import is treated as a coupling violation requiring remediation, not a style note; question 3 ("does this make the next change harder?") is answered with specifics.

**Exercise 8.4 (Core) — Design a progressive delivery plan.** *(~2 h)* Change brief: a checkout service is replacing its pricing engine with an agent-generated implementation; a pricing error in production means mischarged customers. Design the rollout: which progressive delivery patterns you compose and in what order, the success criteria and rollback trigger at each stage, the post-merge observation window and its thresholds (automatic versus manual rollback), and the SLO with the error-budget policy that governs further agent-generated deployments to this service.
*Deliverable:* A staged rollout plan with per-stage criteria and triggers.
*Assessment:* Judged against §8.2 and the companion repository's `checklists/deployment-safety-checklist.md`: at least two patterns composed with a stated rationale; dark launch considered (and adopted or explicitly rejected) given that pricing output can be compared offline; every automatic-rollback trigger is a measurable threshold, not a judgment call.

**Exercise 8.5 (Challenge) — Run the 2 AM tabletop.** *(~3 h)* Incident brief: an agent-generated change deployed Friday at 4:10 PM included a schema migration and the serialization change from Exercise 8.1(c). At 6:20 PM the error rate reaches 2.4x baseline; the on-call engineer is not the change's author; the author is unreachable. On paper, execute the response: determine the rollback classification, write the runbook as the on-call engineer would execute it (order of operations, data correction, validation), and identify where the response is impossible because a required artifact was never produced. Then write the postmortem's process findings: which failure modes from §8.2 occurred, and the three specific pipeline or policy changes that would prevent recurrence.
*Deliverable:* An incident timeline, the executed runbook, and the three-change postmortem.
*Assessment:* Judged against the rollback protocol and the §8.2 failure-mode catalog: the Friday-afternoon deploy, the untested rollback, and the orphaned-migration risk must all be identified; each proposed change maps to a named mechanism in this chapter (scheduling policy, tested down migration, rollback owner) rather than to "be more careful."

