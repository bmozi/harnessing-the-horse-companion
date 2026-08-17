# Chapter 16: Case Study — The Merlin Software Factory — Study Guide

Student and self-study material moved from Chapter 16 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain the tag-text drift failure and derive the general rule for systems in which an agent expresses one judgment in two representations.
2. Analyze the express-arc pivot: why handoff compaction, rather than agent quality, drove the multi-agent pipeline's failures.
3. Evaluate safety-rail designs for self-improving systems — hardcoded approval, forbidden paths, self-referential loop detection — against the runaway modes each prevents.
4. Apply bounded iteration and escalation triggers as runtime governance that converts unbounded failures into cheap post-mortems.
5. Assess the evidentiary status of a self-reported, single-operator case: which claims are checkable by reimplementation and which are not independently auditable.

## Key Terms

- **Express Arc** — A single primary agent owns the entire delivery sequence (investigate → plan → tests → implement → audit → ship) without handoffs; quality gates fire as inline self-checks.
- **STRATEGIC_PIVOT.md** — Document recording a significant architectural course correction: the original design, why it failed with measured evidence, and the new direction.
- **Software Factory** — A continuous, instrumented loop turning external signals into reviewed, secured, shipped, monitored code; Merlin is this book's agentic instance.
- **MUST-NOT list** — The negative-space section of SPEC.md; in Merlin, the non-goals consulted as often as the goals.
- **Agent gateway** — An infrastructure layer mediating agent traffic; Merlin's five-backend failover is one agent-to-LLM instance of the pattern, distinct from the agent-to-tool gateway layer described in Chapter 13.
- **Thrashing** — Repeated fix iterations against the same failure without convergence; the condition Merlin's iteration caps convert into escalation.
- **SPEC.md** — The first pipeline artifact; Merlin's RFC 2119 service contract was the engagement's single most effective artifact.
- **Minimum Viable Software Factory** — The smallest useful factory: one governed session loop with context, Work Orders, quality gates, review artifacts, and a close-the-loop learning mechanism, before orchestration or autonomous improvement.

## Review Questions

1. Reconstruct the security.txt failure chain: which components behaved correctly, where exactly was the defect, and why did the developer agent receive an unfixable instruction?
2. What three fixes did the post-mortem propose, and at what point in the pipeline does each intervene?
3. Name the four safety-rail constraints and the specific runaway mode each prevents.
4. Why did the original multi-agent pipeline fail — what specifically was lost at handoffs, and what did eliminating them change in throughput, cost, and coherence?
5. What does the self-improvement backlog admit about Merlin's current state, and why does the chapter treat those admissions as evidence for the discipline rather than against the system?
6. What four layers make up a minimum viable software factory, and why does the chapter defer orchestration until after the manual loop is boring?

## Discussion Questions

1. `REQUIRE_HUMAN_APPROVAL` is a class constant with a defensive guard, deliberately outside configuration. As models improve and validated proposals accumulate a track record, is there a principled point at which relaxing it becomes justified — and in a system with one operator who is also the author, who has standing to make that call?
2. The express-arc evidence is a 500% increase in landed pull requests across three consecutive dogfood runs, labeled suggestive rather than statistical. Design the experiment that would make the single-agent-vs-multi-agent claim respectable, and then argue whether running it is worth the cost given how fast the underlying models and orchestration frameworks are changing.
3. Lesson 6 says governance must precede the first session, but governance costs are paid up front and its benefits arrive as incidents that never happen. How do you make the day-one case to a team that has never watched three sessions invent three error-handling conventions in a week?

## Exercises

**Exercise 16.1 (Core) — Defend or attack Decision Point 16.1.** Take a position on the author's choice at Decision Point 16.1 — collapsing to a single agent rather than hardening the handoff contracts — using only what was knowable at the time; you may not use hindsight the author lacked (the dogfood results, the later landscape evidence). If you defend, address the strongest multi-agent counterargument in Section 13.7; if you attack, specify the handoff-contract design you would have tried first. *(~2 h)*
*Deliverable:* A position memo including the measurement you would have run to falsify your own position within four weeks.
*Assessment:* Rubric: ex-ante information only; engages the compaction-loss mechanism specifically rather than arguing architecture in the abstract; the falsification measurement is observable and time-bounded.

**Exercise 16.2 (Core) — Critique the Status and Evidence box.** Audit this chapter's Status and Evidence box. Classify each claim as measured, projected, or unverifiable by the reader; identify which architectural claims are checkable by reimplementation (the box asserts the safety mechanisms are described precisely enough) and verify that assertion against Section 16.3's detail; then specify what evidence the multi-tenant and team-scale claims would require before they deserve the word "measured." *(~2 h)*
*Deliverable:* An evidence audit table plus a paragraph on whether "checkable by reimplementation" is a meaningful evidence tier between measured and unverifiable.
*Assessment:* Judged on honest-evidence criteria: correct classification, a concrete reimplementation check for at least one safety rail, and multi-tenant evidence requirements that go beyond "get more tenants."

**Exercise 16.3 (Challenge) — Design safety rails for a different self-improving system.** A prompt-optimization service rewrites its own system prompts based on evaluation scores: it observes eval results, proposes prompt edits, and applies winners. Design its safety rails using Section 16.3 as the reference: proposal caps, approval mechanics, the forbidden surface, and self-referential loop detection. *(~2 h)*
*Deliverable:* A safety-rails design document plus, for each rail, one attack scenario — a proposal that attempts to reach the protected surface — and the mechanism that blocks it.
*Assessment:* Judged against Section 16.3's criteria: every rail must live outside the system's own improvement surface, and the attack scenarios are graded on whether they would genuinely succeed against a naive design.

**Exercise 16.4 (Challenge) — Build the emission-consistency gate.** Design (or implement, if you have tooling access) the tag-text consistency check the post-mortem proposed: inputs, the method for comparing free-prose reasoning against structured severity tags, and the action on mismatch. Then attack it: list three ways an auditor's output could pass your check while its channels still disagree in substance, and either close each hole or document it as accepted residual risk. *(~4 h+)*
*Deliverable:* The gate design (or code) plus the adversarial appendix.
*Assessment:* Standard 7 (Falsification Review) and Lesson 1: pass requires the check to operate at emission, not aggregation, and requires at least one adversarial case involving hedged or self-contradictory prose rather than a clean approve/block mismatch.

**Exercise 16.5 (Core) — Bootstrap your minimum viable software factory.** Using Section 16.8 and the companion repository's `factory-bootstrap/` kit, choose one active repository and design the first thirty days of its factory. You may not introduce multi-agent orchestration or autonomous improvement. Your plan must cover the context layer, Work Order layer, gate layer, learning layer, the first pilot task, and the baseline metrics you will collect before deciding whether to expand. *(~3 h)*
*Deliverable:* A filled factory-readiness review plus the first Work Order and gate classification table.
*Assessment:* Judged against Section 16.8, `references/complete-session-loop.md`, the companion quality-gate configuration reference, and Chapter 19's crawl-stage criteria. A pass keeps the first factory small, makes every blocking gate enforceable, and explains which book chapter justifies each scaffolding decision.
