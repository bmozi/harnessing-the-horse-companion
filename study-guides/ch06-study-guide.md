# Chapter 6: Interfaces and Dependencies — Study Guide

Student and self-study material moved from Chapter 6 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why explicit, written interface contracts replace conversation as the integration mechanism between agent sessions.
2. Construct interface specifications — an endpoint contract, a function contract with preconditions, postconditions, and invariants, and an event schema — precise enough for two independent sessions to integrate on the first try.
3. Classify dependencies as external, internal, or implicit, and apply the declare-before-generation, audit-after-generation discipline to each.
4. Analyze a generated change's dependency delta to detect phantom packages, transitive vulnerabilities, license conflicts, and version pin drift.
5. Apply Hyrum's Law to a generated API to decide which observable behaviors are contract and which are implementation detail, and specify how the boundary is enforced.
6. Construct a session-sized task decomposition with explicit interfaces, dependencies, and MUST-NOT lists, following the worked example.

## Key Terms

- **DESIGN.md** — The pipeline artifact capturing how the system will satisfy the specification; in this tier, the home of interface contracts and the task decomposition.
- **SPEC.md** — The specification artifact whose acceptance criteria define what is contractual about a generated interface; everything else is implementation detail.
- **MUST-NOT list** — The negative-space section of SPEC.md, with six required categories (Standard 1); in this tier, scoped per task in the decomposition (e.g., "MUST-NOT use raw SQL string concatenation").
- **Context file** — `AGENTS.md` or `CLAUDE.md`: the project-root document capturing conventions, constraints, and architecture boundaries; in this chapter, the agent's "team" under Conway's Law — the communication structure that determines the system structure the agent produces.
- **Slopsquatting** — The supply chain attack in which attackers register package names AI agents hallucinate; the threat behind the phantom-package failure mode and the manifest-verification rule.
- **Blast radius** — The impact surface estimated at planning time; task boundaries that cross fewer modules keep each task's radius small.

## Review Questions

1. The chapter states that between agent sessions, "if the interface is not explicit, it does not exist." What structural fact of agentic development makes this true, and what informal mechanism did it replace?
2. Define preconditions, postconditions, and invariants in the Design by Contract sense, and for each, name an inference the agent no longer has to make when it is stated.
3. Name the three dependency categories and explain why implicit dependencies are the most dangerous of the three.
4. What is the stated test of a sufficient interface specification?
5. In the worked decomposition, why can Task 5 (audit logging) run in parallel with Task 4 (controller), and what makes that parallelism safe?

## Discussion Questions

1. Interface-first design shifts the engineer's primary investment from writing code to designing contracts. If agents write most implementation code, where do junior engineers acquire the experience that interface-design judgment traditionally came from — and what should a team change about mentoring as a result?
2. Hyrum's Law implies that every observable behavior of a generated API will eventually be depended on. Contract tests, consumer-driven tests, and dependency audits all cost maintenance effort. Where would you draw the line between behaviors worth enforcing as contract and drift worth accepting — and does agent-scale generation move that line?
3. Postel's Robustness Principle says be liberal in what you accept; Allman's reconsideration says validate aggressively. Which stance should govern agent-generated services, and does the answer change when the caller is another agent's generated code rather than a human-written client?

## Exercises

**Exercise 6.1 (Core) — Write integration-grade interface specifications.** *(~2 h)* Feature brief: an order service must expose order history — `GET /api/orders?customerId=...` with pagination, an internal `getOrderHistory` function the endpoint calls, and an `order.history.viewed` audit event. Write all three interface specifications in the formats shown in §6.1, including preconditions, postconditions, invariants, error types, and consumers. Then exchange with a peer: each of you lists every question an implementing session would still have to guess at.
*Deliverable:* The three interface specifications plus the peer's underspecification findings.
*Assessment:* Judged against the companion repository's `spec-templates/interface-spec.md` and the sufficiency test in §6.1 — a specification passes when the peer audit finds no gap that would cause two independently generated sides to fail integration.

**Exercise 6.2 (Core) — Audit a dependency delta.** *(~1 h)* A generated change to a Node service adds these imports: `express-rate-limit` (in the manifest), `fast-csv` (not in the manifest), `left-pad-utils` (not on the registry), and a direct import from `../../billing/internal/invoice-calculator`; it also reads a new environment variable `CSV_TMP_DIR` and queries the `contacts_staging` table. Produce the post-generation dependency delta report: classify each item as external, internal, or implicit; mark it authorized or deviation; and prescribe the disposition.
*Deliverable:* A dependency delta report with classification, risk, and disposition per item.
*Assessment:* Judged against the dependency delta check in the companion repository's `checklists/post-generation-verification.md` and the §6.2 categories — `left-pad-utils` must be identified as a phantom package (supply chain risk, not a mere typo), the cross-boundary billing import as an architectural violation, and both implicit dependencies as documentation-required.

**Exercise 6.3 (Core) — Repair implicit contracts.** *(~90 min)* Take three signatures as given: `parseAmount(input: string): number`, `retryRequest(fn, times)`, and `mergeAccounts(sourceId, targetId): Promise<void>`. For each, write the full Design by Contract specification — preconditions, postconditions, invariants, error behavior, side effects — and list the specific inferences an agent would otherwise have made (rounding, currency, retry backoff, idempotency, what happens to the source account).
*Deliverable:* Three completed contracts plus the inference list per function.
*Assessment:* Judged against §6.1's contract elements: each contract eliminates every listed inference; `mergeAccounts` explicitly addresses idempotency and partial-failure behavior, the two inferences agents most reliably get wrong.

**Exercise 6.4 (Challenge) — Re-decompose under changed requirements and defend the contract boundary.** *(~3 h)* The §6.3 feature changes after shipping: administrators must be able to search soft-deleted users, and audit events must be delivered synchronously to a new compliance service instead of the existing event bus. Produce the revised decomposition: which of the five tasks' interfaces survive unchanged, which contracts break, and what new tasks are required. Then apply Hyrum's Law to the shipped search endpoint: enumerate at least five observable behaviors, classify each as contract or implementation detail, and specify the mechanism (contract test, acceptance criterion, documentation) that enforces each classification.
*Deliverable:* A revised DESIGN.md decomposition with a contract-impact table, plus the Hyrum's Law classification with enforcement mechanisms.
*Assessment:* Judged against the five decomposition rules (Standard 2), `spec-templates/design-md.md`, and §6.2's Hyrum's Law discipline — full credit requires recognizing that the audit change breaks Task 5's consumed interface but not Task 3's produced one, and that response field ordering and error message text must be classified with an explicit enforcement decision rather than left ambient.

