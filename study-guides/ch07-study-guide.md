# Chapter 7: Generation, Verification, and Review — Study Guide

Student and self-study material moved from Chapter 7 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Construct a structured generation prompt containing testable requirements, all five constraint categories, a specific MUST-NOT list, an output format, and review criteria.
2. Classify quality checks into BLOCKING, ADVISORY, INFORMATIONAL, and ASYNC tiers and defend each classification against the worst-case consequence of shipping past it.
3. Apply the three-question disprove-only review to agent-generated code, documenting findings with location, severity, and failure scenario.
4. Explain how shared assumptions can limit self-review, and construct a fresh-context adversarial pass while recognizing its remaining biases.
5. Construct an escalation record for a gate failure, including root cause, thrashing check, authority level, and remediation plan.
6. Evaluate tasks for delegation using the Task Fit Matrix and identify conditional fits that are weak fits in disguise.

## Key Terms

- **Adversarial validation** — The agent mode of Standard 7: a fresh-instance agent attacks the generated code with an explicit mandate to find failures, reading it as a skeptical stranger.
- **Disprove-only review** — The human mode of Standard 7: the reviewer's task is to find how the code fails, structured as three questions rather than a holistic read.
- **Context contamination** — The condition in which a session's assumptions leak into its own review, limiting its value as independent evidence; fresh-instance validation reduces carryover but does not remove shared biases.
- **Four-tier gate classification** — BLOCKING, ADVISORY, INFORMATIONAL, ASYNC: the book's authoritative classification of automated quality gates, defined in this chapter.
- **Thrashing** — Repeated fix iterations against the same failure without convergence; the Standard 6 trigger is 30 minutes or three iterations, whichever comes first.
- **ESCALATION.md** — The Standard 6 artifact documenting gate overrides and thrashing escalations: failure details, root cause, thrashing check, authority, remediation plan.
- **Verification stance markers** — The `verified` / `ASSUMPTION` / `VERIFY` convention for factual claims in generated code, making claims and uncertainty inspectable; markers still require source verification.
- **Subagent challenge clauses** — Prompt clauses that shift the agent's incentive from minimizing visible uncertainty to surfacing it explicitly.
- **Fail loud** — The principle that "completed" is wrong if anything was skipped silently; uncertainty is surfaced, never hidden behind a tidy summary.
- **The 70% problem** — Osmani's observation that AI rapidly produces the happy-path 70% of a solution while the hard 30% — edge cases, hardening, integration — is where the defects live.

## Review Questions

1. Name the five constraint categories every structured prompt must include, and give a concrete example of each for a task of your choosing.
2. What is the most dangerous gate misclassification, and what question does the chapter prescribe for scrutinizing any gate's tier?
3. State the three disprove-only questions. Why does the third question remain tractable as code volume grows?
4. Why can the generating session not review its own output? What must the adversarial instance receive, and what must it not receive?
5. State the thrashing rule and the evidence that distinguishes a converging iteration from a thrashing one.

## Discussion Questions

1. Adversarial validation deploys an AI to check an AI. Which classes of failure can that arrangement never catch — consider assumption errors that originate in the human's mental model — and what does the answer imply about how many humans a disciplined pipeline still requires?
2. Level 4 of the escalation protocol declares some findings un-overridable at any authority. Should any gate be beyond the reach of a business emergency? Construct the strongest case for and against an absolute gate, and identify what a team gives up in each direction.
3. The chapter claims the four standards make review *faster* — 15–30 structured minutes replacing four to six hours of unstructured reading — but the evidence is one practitioner's portfolio. What would falsify the claim, and how would you design a pilot in your own organization to test it?

## Exercises

**Exercise 7.1 (Core) — Write a structured generation prompt, peer-audited.** *(~2 h)* Task brief: add rate-limiting middleware to an existing Express API — 100 requests per minute per API key, sliding window, HTTP 429 with a `Retry-After` header on breach, counters stored via the project's existing Redis client. Known constraints: the authentication middleware must not be modified, and no new dependencies are permitted. Write the complete structured prompt using the §7.1 template. Then swap with a peer, who audits your prompt while you audit theirs.
*Deliverable:* The structured prompt plus your peer's written audit findings.
*Assessment:* The peer audit applies the Standard 1 checklist — the §7.1 Areas of Critique and the companion repository's `prompts/structured-prompt.md` — verifying that all five constraint categories are present, every MUST-NOT item is specific enough to be checkable in a diff, and every constraint traces to a review criterion. A constraint with no matching review criterion is a defect.

**Exercise 7.2 (Core) — Configure quality gates for a described project.** *(~90 min)* Project brief: a six-engineer team maintains a TypeScript order-management service that touches payment records; CI currently runs everything serially and takes 40 minutes, and engineers have started merging with `--no-verify`. Classify each of these ten checks into BLOCKING, ADVISORY, INFORMATIONAL, or ASYNC, and defend each classification in one to three sentences: (1) type check; (2) unit test suite; (3) code coverage delta; (4) full end-to-end suite (25 minutes); (5) SAST at CRITICAL/HIGH; (6) SAST at MEDIUM/LOW; (7) dependency license scan; (8) cyclomatic complexity threshold; (9) LOC delta; (10) full transitive-tree dependency vulnerability scan (18 minutes).
*Deliverable:* A classification table with a written defense per check, plus one paragraph on how your configuration addresses the `--no-verify` behavior.
*Assessment:* Judged against §7.2 and the companion repository's `prompts/quality-gate-config-review.md`. Each defense must answer "if this check fails and the code ships anyway, what is the worst-case production impact?" Classifying (5) or (7) below BLOCKING, or leaving the two slow checks synchronous, fails the gate.

**Exercise 7.3 (Core) — Run a disprove-only review on flawed code.** *(~2 h)* Your instructor provides a small module with a specification and a MUST-NOT list; the code contains seeded defects. Conduct the human-mode falsification review using the three questions of §7.3, working from the review prompt. Do not fix anything — your task is disproof, not repair. *Self-study variant:* apply the same disprove-only method to an unfamiliar pull request of roughly 200 lines from any open-source project you do not know. You lose the seeded ground truth but keep the falsification practice: report your findings with verification stance markers, then read the project's actual review thread as partial ground truth. The seeded-module version requires the instructor package.
*Deliverable:* A completed REVIEW.md: gate status, requirement-by-requirement traceability, and Question 3 findings, each with file and line, severity, failure scenario, and remediation.
*Assessment:* Judged against the companion repository's `prompts/disprove-only-review.md` and `spec-templates/review-md.md`, scored against the instructor's seeded-defect list. Full credit requires finding the seeded MUST-NOT violation and at least one error-handling gap, and enumerating every dimension checked — including dimensions ruled out with a stated reason. A review that reports "no findings" fails.

**Exercise 7.4 (Core) — Design an escalation record for a thrashing scenario.** *(~1 h)* Scenario: an engineer has spent 55 minutes and five iterations directing an agent to fix an intermittently failing integration test in a message-consumer service. Each fix has produced a new symptom; the integration-test gate is BLOCKING; the release is scheduled for tomorrow morning, and a product manager has asked the engineer to "just get it green." Write the complete escalation record.
*Deliverable:* An ESCALATION.md entry following the §7.4 assessment structure: gate failure details, root cause analysis, thrashing check, authority-level determination, override assessment or fix decision, and remediation plan with owner and deadline.
*Assessment:* Judged against the companion repository's `prompts/escalation-assessment.md` and `spec-templates/escalation-md.md`. Full credit requires: identifying that the thrashing rule triggered roughly 25 minutes and two iterations ago; refusing the Level 1 path for a BLOCKING genuine issue; and answering the product manager with the two-option response from §7.4's Pressure Override discussion rather than a bypass.

**Exercise 7.5 (Core) — Split the tasks the Task Fit Matrix cannot classify whole.** *(~90 min)* Four incoming work items resist one-word classification: (a) an admin CRUD resource whose handlers also enforce per-row authorization; (b) a benchmarked performance optimization that requires touching a lock-protected cache; (c) a data pipeline with schema contracts in a service whose integration suite has been red for a month; (d) a compliance-adjacent report generator that reads from a PCI-scoped table but contains only formatting logic. For each: decompose the item until every fragment lands cleanly in one matrix category, state which fragments you delegate and which you hand-write, and name the substrate repair (if any) that would change the answer. Then handle the adversary: your tech lead wants all four delegated whole, "since the matrix is a guideline" — write the reply, conceding whatever genuinely is conditional.
*Deliverable:* A decomposition table (fragment, matrix category, delegate or hand-write, substrate condition) plus the reply to the tech lead.
*Assessment:* Judged against the Task Fit Matrix in this chapter's opening: the authorization logic in (a) and the lock interaction in (b) are isolated as hand-write fragments while their surrounding scaffolding is delegated; (c) is treated as weak fit until the substrate is repaired, with the red suite named as the disqualifier; (d) receives an explicit ruling on whether the compliance boundary contaminates the formatting work, defended either way; the reply refuses the whole-item delegations without surrendering the delegable fragments.

**Exercise 7.6 (Challenge) — Run both modes of Standard 7 and reconcile the findings.** *(~3 h)* Using an agent tool of your choice, run adversarial validation on the same instructor-provided module from Exercise 7.3: a fresh instance, receiving only the specification, the MUST-NOT list, and the code — not your review, not any generation history — with the §7.3 adversarial prompt. Compare the agent's findings with your human-mode findings from Exercise 7.3 and disposition every agent finding. *Paper variant:* write the complete adversarial prompt yourself *before* consulting §A.4 of the companion complete prompt library; then diff your prompt against it, justify each divergence — kept, adopted, or rejected, with reasoning — and predict what a fresh instance running your prompt would and would not catch. *Note:* the seeded module requires the instructor package; self-study readers can substitute the open-source pull request from Exercise 7.3's self-study variant.
*Deliverable:* A comparison memo — findings unique to each mode, findings shared — plus a disposition table (FIXED / ACCEPTED / FALSE POSITIVE / DEFERRED, with evidence per finding) and a description of how context isolation was achieved.
*Assessment:* Judged against the companion repository's `prompts/adversarial-validation.md` and the Areas of Critique in §7.3: context isolation must be verifiable from the description; every disposition must cite evidence rather than assertion; and the memo must identify at least one class of finding each mode caught that the other missed.
