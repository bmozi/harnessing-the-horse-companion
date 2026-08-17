# Chapter 9: Architectural Stewardship — Study Guide

Student and self-study material moved from Chapter 9 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why agent-generated code accelerates architectural erosion and why boundaries must be both documented for agent context and automated for enforcement.
2. Construct machine-readable boundary rules — dependency-rule suites and CODEOWNERS entries — for a described architecture.
3. Analyze drift-scan findings and classify each as violation, evolution, or ambiguity, with the correct disposition for each class.
4. Evaluate AI-generated technical debt using Fowler's quadrant, the three-tier debt register, and empirical hotspot analysis.
5. Apply the four simplicity tests to agent-generated abstractions and justify which should be deleted.
6. Construct an ADR in MADR format whose Agent Implications section functions as a specific, actionable, testable guardrail for future sessions.

## Key Terms

- **Architecture-as-code** — Architectural constraints expressed as enforceable rules in CI/CD, not as documentation; the mechanism that prevents drift at the speed of generation.
- **Drift scan** — Periodic comparison of the actual dependency graph against the documented architecture, with findings classified as violation, evolution, or ambiguity.
- **Fitness function** — An automated test that evaluates the architecture's adherence to its design principles; in agentic development, run continuously rather than quarterly.
- **ADR (Architecture Decision Record)** — A short document capturing context, decision, alternatives, and consequences; augmented in this book with an Agent Implications section.
- **Dark code** — Code that exists and possibly passes tests but that no one understands; the comprehension face of AI-generated debt.
- **IMPL_NOTES.md** — The running implementation log; home of the debt register and of Tier 2 lightweight ADRs.
- **AGENTS.md** — The context file where module conventions (Tier 3 implicit ADRs) and active architectural constraints reach every session.

## Review Questions

1. Why does the chapter argue that an agent writing perfect code across an architectural boundary is worse than an agent writing mediocre code within it?
2. Name the three drift-scan classifications and the correct organizational response to each.
3. In what three ways does AI-generated debt differ from traditional debt, and in which Fowler quadrant does it cluster? Why there?
4. State the four simplicity tests and the threshold at which generated code is flagged for simplification.
5. What does the Agent Implications section add beyond Nygard's format and canonical MADR, and what three properties make an Agent Implications entry effective?

## Discussion Questions

1. "AI does not replace architecture; it pressure-tests it." If only machine-enforceable architecture survives agentic development, what happens to architectural principles that are valuable but resist encoding — conceptual integrity, domain alignment, taste? Are they doomed to erode, or is there a mechanism the chapter underweights?
2. The debt register asks engineers to capture debt as it is created, but the chapter also argues most AI-generated debt is Inadvertent — nobody knows it happened. Is the register solving the wrong quadrant? What mixture of conscious capture and empirical hotspot detection would you fund, and what does each cost?
3. Teams historically abandon ADR practices within months. Does the tiered ADR system fix the incentive problem or merely relabel it? What would make the practice survive contact with a two-hundred-PR month?

## Exercises

**Exercise 9.1 (Core) — Decide the event-publishing architecture and write the ADR.** *(~2 h)* Decision brief: after losing order events during a deploy, your team must choose how the order service publishes events. Options on the table: publish directly to the message broker inside the request handler; a transactional outbox table drained by a relay; or change data capture on the orders table. Constraints: the team already operates PostgreSQL and the broker but has never run a CDC stack; one downstream consumer — fraud screening — needs events within two seconds of commit; the ops rotation is two people; and a platform team has offered to run Debezium "sometime next quarter." Choose, and write the complete ADR in MADR format, including machine-parseable frontmatter and the Agent Implications section. Under these constraints both the outbox and CDC are defensible, and the direct-publish option is what caused the incident; your Considered Options section must carry the real weight of that comparison.
*Deliverable:* The complete ADR.
*Assessment:* Judged against the companion repository's `spec-templates/adr-template.md` and §9.3: frontmatter parseable (status, date, applies_to); the fraud-screening latency requirement addressed explicitly by the chosen option (relay polling budget or CDC lag budget) rather than absorbed silently; the Consequences section states the chosen option's real costs; and an Agent Implications section that is specific (names the module agents must use), actionable (import path), and testable (the check that verifies compliance). Either defensible choice earns full credit; Considered Options written as strawmen, or an Agent Implications section that restates rationale without constraints, fails.

**Exercise 9.2 (Core) — Encode boundaries as machine-readable rules.** *(~2 h)* Architecture brief: a system has three modules — `orders`, `payments`, and `notifications`. Rules: `payments` may be called only through its public API, never its `internal/` package; `notifications` receives work only via the event bus, never direct calls; nothing imports `orders/legacy/`; the payments team must review any change under `payments/`. Express these rules in the enforcement tool for a language of your choice (ArchUnit, dependency-cruiser, import-linter, or depguard) plus a CODEOWNERS file. Then identify which of the four rules your tooling cannot fully express, and specify what covers the gap.
*Deliverable:* The rule files plus a coverage note.
*Assessment:* Judged against §9.1: rules are syntactically plausible for the chosen tool; the event-bus-only rule is recognized as only partially expressible by import rules (a direct HTTP call crosses no import boundary), with the gap covered by a named mechanism — fitness function, contract test, or review checklist — rather than left implicit.

**Exercise 9.3 (Core) — Classify drift-scan findings.** *(~45 min)* A drift scan of the Exercise 9.2 system reports six discrepancies: (a) `orders` imports `payments/internal/validators`; (b) a new `refunds` module exists with no entry in the architecture documentation; (c) `notifications` calls the payments public API synchronously to enrich messages; (d) a sub-package of `orders` imports another `orders` sub-package the docs say nothing about; (e) eighteen modules now import a helper that was approved once as an exception; (f) `payments` gained a scheduled-reconciliation responsibility described nowhere. Classify each as violation, evolution, or ambiguity, and prescribe the disposition.
*Deliverable:* A six-row classification table with dispositions.
*Assessment:* Judged against §9.1's drift taxonomy: (a) is a violation requiring code change or a deliberate architectural decision; (b) and (f) are evolution requiring documentation; (d) is ambiguity requiring more precise boundary definition; (e) must be recognized as the approved-exception-become-norm failure mode requiring a whole-pattern review, not eighteen individual approvals.

**Exercise 9.4 (Core) — Run a simplicity review and stock the debt register.** *(~90 min)* Code brief (as described by your instructor or taken as given): a generated changeset contains (a) a `UserServiceWrapper` that delegates every method unchanged; (b) an adapter converting a DTO into an identically shaped object; (c) an abstract `PaymentProviderBase` with one concrete implementation; (d) a repository class whose one-line interface hides connection pooling, retry, and statement caching; (e) a hardcoded API key in a test helper; (f) missing retry logic on a network call in a nightly job. Apply the four simplicity tests to (a)–(d); then place (a)–(f) in the debt register tiers and Fowler's quadrant.
*Deliverable:* A simplicity-test matrix for the four abstractions plus a debt register with tier, quadrant, and remediation timing per item.
*Assessment:* Judged against §9.2 and the companion repository's `checklists/simplicity-review.md`: (d) must survive as a legitimate deep module; (a)–(c) must fail at least two tests each; (e) must be must-fix-before-merge; the quadrant placements must be defended, not asserted.

**Exercise 9.5 (Challenge) — Produce a hotspot map and prioritization memo.** *(~4 h+)* Select a repository with at least six months of history — one of your own or an active open-source project. Compute change frequency per file from the git log and a complexity measure per file (lines of code is acceptable; McCabe complexity is better), plot the two dimensions, and identify the hotspot quadrant. Where the data exists, add the third dimension: files repeatedly touched by agent sessions (or, in its absence, by many distinct authors). Write a one-page prioritization memo for the top hotspots. *Paper variant:* your instructor provides the per-file frequency and complexity table.
*Deliverable:* The hotspot map (table or plot) and the prioritization memo.
*Assessment:* Judged against §9.2's hotspot method: the memo distinguishes hotspots that block delivery from those accumulating silent risk; every prioritization claim traces to the data; and at least one high-complexity, low-change file is explicitly deprioritized with the reasoning stated.

