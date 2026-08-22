# Chapter 15: Case Study — The E-Commerce Platform and Its Checkout — Study Guide

Student and self-study material moved from Chapter 15 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Distinguish the capability multiplier from the speed multiplier, and explain what the chapter's line counts can and cannot evidence.
2. Analyze the recursive specification pattern's strengths and its blind spot — whatever the specification omits, the amplification omits at scale.
3. Use a CAS-guarded state machine and durable checkpoints to prevent concurrent local execution, and design reconciliation for ambiguous non-idempotent vendor writes.
4. Apply default-safe configuration design — sandbox-by-default, session pinning, explicit production opt-in — to systems with production side effects.
5. Evaluate the chapter's economic projections against their stated assumptions and identify which assumption each figure is most sensitive to.

## Key Terms

- **CAS-Guarded Distributed Commit** — Combining an atomic local ownership guard with durable checkpoints. It prevents replay after known outcomes; vendor idempotency or reconciliation is required for an effectively-once outcome when a response is lost.
- **Saga** — Multi-step transaction coordination pattern composing forward steps with compensating transactions; the checkout's per-step checkpoints are its close relative.
- **Idempotency** — The property that processing the same request multiple times produces the same result as processing it once.
- **Scoped Authorization Token** — Least privilege applied at the session level; the management-hub token authorizes exactly one subscription.
- **Anti-Corruption Layer (ACL)** — A translation boundary that keeps an external system's model from leaking into the domain; applied here to ATTOM's data quality, not just its wire format.
- **Capable of more (thesis)** — Distinguishes "AI makes developers faster at known tasks" from "AI makes developers capable of previously impossible tasks"; this chapter is its primary exhibit.
- **Adoption gap (this book)** — The observation that development capacity can increase faster than an organization can absorb it; illustrated here by the interval between the initial platform foundation and the planned launch window, during which engineering hardening and stakeholder readiness continued in parallel.

## Review Questions

1. Why does the checkout need its own retry and reconciliation machinery — what specifically do Braintree and FieldRoutes fail to provide, and why is a distributed transaction unavailable?
2. Trace a retry after `createSubscription` fails in two cases: the failure is known before the call succeeds, and the provider accepts the call but its response is lost. Which steps may be skipped, retried, reconciled, or stopped for human disposition?
3. What three design decisions make sandbox-by-default safe, and what failure class does each one close?
4. The chapter calls the ATTOM layer an Anti-Corruption Layer against data quality rather than wire format. What three defenses implement it, and what mispricing does each prevent?
5. According to Section 15.4, what is the root cause of the 1:61 test-to-code ratio, and what is the structural fix?

## Discussion Questions

1. Lesson 6 reports that the initial platform foundation arrived months before the planned launch window while substantial engineering hardening continued. How much of the interval reflects organizational absorption, how much reflects unfinished engineering, and what evidence would be required before calling either one the binding constraint?
2. Section 15.9 stacks explicitly labeled assumptions into dollar ranges. Argue both sides: labeled speculation gives decision-makers a model they can interrogate and check against launch data, versus any dollar figure — however bracketed — anchoring readers to numbers the evidence cannot support. Which failure is worse in an engineering case study?
3. Does Section 15.4's disclosure of the coverage gap strengthen or weaken your confidence in the rest of the chapter? Would you trust the CAS-guarded checkout design more if the platform had systematic tests — and what does your answer imply about how case-study evidence should be weighed?

## Exercises

**Exercise 15.1 (Core) — Defend or attack Decision Point 15.2.** Take a position on the author's choice at Decision Point 15.2 — proceeding toward launch with targeted tests and disclosure rather than pausing to backfill coverage — using only what was knowable at the time; you may not use hindsight the author lacked (launch outcomes, later incident history). Whichever side you take, specify the triage: which surfaces get tests first, and by what risk ranking. *(~2 h)*
*Deliverable:* A decision memo with your position, your test-priority ranking of the platform's surfaces (payment flows, booking wizard, API routes, admin pages), and the launch-blocking threshold you would set.
*Assessment:* Rubric: ex-ante reasoning only; explicitly weighs Standard 6's coverage requirement against the deadline economics; the triage ranks by blast radius rather than by ease of testing.

**Exercise 15.2 (Core) — Critique the Status and Evidence box.** Audit this chapter's Status and Evidence box and the economics of Section 15.9. Classify each claim as measured, projected, or unverifiable; identify the assumption each dollar range is most sensitive to; then design the measurement plan that launch data should run against — which metric, collected how, checked at what milestone, and what result would falsify each projection. *(~2 h)*
*Deliverable:* An evidence audit table plus a one-page post-launch measurement plan.
*Assessment:* Judged on honest-evidence criteria: correct classification, sensitivity analysis that identifies the retention-lift assumption as load-sensitive or argues otherwise, and falsifiable checks rather than vanity metrics (Chapter 18's measurement discipline).

**Exercise 15.3 (Core) — Design a CAS-guarded commit for a different domain.** An event-ticketing checkout performs five steps: vault the card, reserve the seat (reservations auto-expire in 10 minutes), charge the card, issue the ticket, send the confirmation email. The seat-reservation and charge endpoints are non-idempotent; the vendor systems share no transaction boundary. Design the commit machinery. *(~2 h)*
*Deliverable:* The state machine (states, CAS transition, stale-window duration with justification, and an `INDETERMINATE` state), per-step checkpoint order, provider correlation and lookup plan, and manual disposition rule. Defend how you order the charge and expiring reservation.
*Assessment:* Judged against Section 15.7 and the CAS-Guarded Distributed Commit card in `references/pattern-quick-reference.md` §8: known outcomes must converge safely, while a lost response after provider acceptance must enter reconciliation rather than automatic retry. Document any residual window that the providers make impossible to close.

**Exercise 15.4 (Challenge) — Specify the missing end-to-end suite.** Write the SPEC.md the platform never had: an automated E2E test suite for the eight-step booking wizard's critical path, including partial-failure injection at each of the five FieldRoutes writes, sandbox-tenant enforcement, and TCPA consent verification. *(~4 h+)*
*Deliverable:* A SPEC.md (companion repository template) with machine-readable acceptance criteria and a test-case table mapping each wizard step and each injected failure to an expected observable outcome.
*Assessment:* The pre-generation gate for Standard 1 plus Standard 8 (Integration Verification): pass requires pre-call, known-failure, and lost-response injection for every non-idempotent write; tests must assert either a verified single business outcome or an `INDETERMINATE` stop awaiting reconciliation, and no test may require the production tenant.
