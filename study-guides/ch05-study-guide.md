# Chapter 5: Discovery and Planning — Study Guide

Student and self-study material moved from Chapter 5 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Construct a SPEC.md with machine-readable acceptance criteria and a six-category MUST-NOT list for a given feature.
2. Apply the pre-generation and post-generation verification gates to a specification and to a generated change.
3. Decompose a feature into single-session tasks that satisfy the five decomposition rules and form a clean dependency DAG.
4. Analyze a change's blast radius across the five dimensions, classify the review effort, and verify the estimate against an actual diff.
5. Apply STRIDE and FMEA to identify and rank the security threats and failure modes a functional specification does not surface.
6. Evaluate a defective specification against the five discovery anti-patterns and repair it.

## Key Terms

- **SPEC.md** — The first pipeline artifact, with six required sections: problem statement, proposed solution, machine-readable acceptance criteria, MUST-NOT list, out of scope, affected components.
- **MUST-NOT list** — The negative-space section of SPEC.md, covering six constraint categories; the most critical section and the most commonly omitted.
- **Blast radius** — The set of components, modules, services, and users that could be affected if a change contains a defect; distinct from scope, which is what the change intends to modify.
- **Context contamination** — The condition in which assumptions from one part of a session's reasoning leak into another, defeating independent review within the same session and degrading multi-task sessions.
- **DESIGN.md** — The pipeline artifact capturing how the system will satisfy the specification, including the task decomposition governed by the five rules.
- **Context file** — `AGENTS.md` or `CLAUDE.md`: the project-root document that captures conventions, constraints, and architecture boundaries every agent session needs to know; conventions absent from it do not exist for the agent.
- **Generation-review asymmetry** — The gap between the rate at which code can be generated and the rate at which it can be meaningfully reviewed (bounded by human cognition); at this tier, the arithmetic behind the 400-line, 60-minute session constraint.
- **Kiro** — AWS's spec-driven agentic IDE, whose requirements.md (EARS notation) and tasks.md pipeline independently validate Standards 1 and 2.

## Review Questions

1. Standard 1 has two halves, traceability and verifiability. What failure does each half prevent when the other is present alone?
2. The 400-line, 60-minute review constraint is described as a property of the reviewer, not of the code. What evidence supports the constraint, and why does it bind at agentic speeds when it rarely bound at manual speeds?
3. Distinguish scope from blast radius, using the chapter's database-migration example.
4. Name the six categories every MUST-NOT list must address.
5. Describe the three stages of the scope trap. Why does the chapter say the fix is structural rather than motivational?

## Discussion Questions

1. The chapter calls specification essential-complexity work "no tool can substitute for" — then Section 5.5 describes AI drafting the decomposition. Where exactly is the line between legitimate AI-assisted specification and the vague-spec anti-pattern, and who is accountable when an AI-drafted spec ships a defect?
2. The review-hour constraint rests on a 2006 study of humans reviewing human-written code. Does that evidence transfer to reviewing agent-generated code, which fails in different ways? What experiment would test whether the 400-line threshold is right for agentic review?
3. A startup lead argues that writing a spec and MUST-NOT list for every task will destroy their velocity, and that regeneration is cheap enough to skip planning. Defend or attack that position using this chapter's account of what vague specifications cost at agentic speeds.

## Exercises

**Exercise 5.1 (Core) — Write a complete SPEC.md that passes the pre-generation gate.** *(~2 h)* Feature brief: an existing REST API needs a password-reset flow. `POST /api/auth/reset-request` accepts an email address and always returns HTTP 202 (whether or not the account exists); it emails a single-use token valid for 30 minutes. `POST /api/auth/reset` accepts the token and a new password, enforces the existing password policy, invalidates all active sessions on success, and rejects reused or expired tokens. Known constraints: the existing authentication middleware must not be modified, tokens must never appear in logs, and no new dependencies are permitted. Write the full six-section SPEC.md.
*Deliverable:* A complete SPEC.md.
*Assessment:* Run the companion repository's `checklists/pre-generation-verification.md` against it, with `spec-templates/spec-md.md` as the structural reference. Gate-pass requires: every acceptance criterion translates directly into a test assertion; the MUST-NOT list addresses all six categories (not only the three constraints given in the brief); the out-of-scope section fences at least two plausible overreaches.

**Exercise 5.2 (Core) — Decompose a feature into single-responsibility sessions.** *(~2 h)* Feature brief: a contacts application needs CSV import — an upload endpoint, a background parsing job, per-row validation with error reporting, deduplication against existing contacts, an import-summary view, and a completion-notification email. Decompose this into agent sessions. For each task, specify: task ID and title, files to create or modify, interface contracts to preserve, a task-scoped MUST-NOT list, test requirements, and a Definition of Done. Draw the dependency DAG.
*Deliverable:* A DESIGN.md task decomposition with the DAG.
*Assessment:* Judged against the five decomposition rules in §5.2 and the companion repository's `spec-templates/design-md.md`: every task is estimated under 400 changed lines; the DAG has no cycles; no task crosses more than two module boundaries; every inter-task dependency is expressed as an interface contract, not as "task B needs to see task A's code."

**Exercise 5.3 (Core) — Produce a blast radius analysis, both passes.** *(~90 min)* Change brief: in an event-driven system, alter the `events` table's `payload` column from TEXT to JSONB and add payload validation in the publisher before insert. Known context: three internal services consume the event queue, a nightly analytics job reads the table directly, and a shared serialization helper formats payloads. First, complete the blast radius template as a planning estimate. Then verify: the generated diff (as described by your instructor, or assume it) also modified the shared serialization helper, which the estimate may not have covered. Complete the review pass and flag every delta.
*Deliverable:* The template completed twice — planning estimate and review verification — with deltas flagged.
*Assessment:* Judged against the companion repository's `spec-templates/blast-radius-template.md` and `checklists/impact-boundary-assessment.md`: all five dimensions addressed in both passes; the serialization-helper delta identified as a finding; the rollback section honestly classifies the column conversion as non-trivially reversible.

**Exercise 5.4 (Core) — Repair a defective specification.** *(~1 h)* Take this spec as given: "Improve the search feature. It should be fast, handle edge cases appropriately, and follow our standard API conventions. Use the usual authentication pattern. We'll refine the details during review." Identify every discovery anti-pattern it exhibits, then rewrite it as a spec for a bounded search improvement of your choosing.
*Deliverable:* An annotated critique (anti-pattern by anti-pattern) plus the rewritten SPEC.md.
*Assessment:* The critique names all five anti-patterns from §5.4 with the phrase that evidences each; the rewrite passes the companion repository's `checklists/pre-generation-verification.md`.

**Exercise 5.5 (Challenge) — Threat-model a change with STRIDE and FMEA.** *(~3 h)* Change brief: a document-management product adds public sharing links — any authenticated user can generate a URL that grants read access to a document without login, with optional expiry. Walk all six STRIDE categories for this change, then build an FMEA table of at least six failure modes with Severity, Occurrence, and Detection scores and computed RPNs. Write a remediation plan for the top two RPNs.
*Deliverable:* The STRIDE walk, the ranked FMEA table, and the two remediations as SPEC.md-ready MUST-NOT or acceptance-criteria entries.
*Assessment:* Every STRIDE category is either mapped to a concrete threat or explicitly ruled out with a reason; Detection scores are defended with reference to how agent-generated code fails (confident, plausible, hard to catch); the two remediations are binary and testable.

