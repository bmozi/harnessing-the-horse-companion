# Chapter 11: Integration Patterns for Agent-System Boundaries — Study Guide

Student and self-study material moved from Chapter 11 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain the optimization principle — agents favor the instruction over the constraint — and why it makes structural containment more reliable than contextual explanation.
2. Apply the Anti-Corruption Layer to contain vendor data-model corruption so that agent-generated code never encounters it.
3. Construct a port-and-adapter boundary in which agent-generated business logic targets ports, never adapters, and remains testable without vendor access.
4. Select the appropriate messaging pattern — Message Bus, Idempotent Receiver, Dead Letter Channel, or Content-Based Router — for a given composition or failure-handling problem.
5. Analyze an agent-generated vendor integration for retry-storm and shared-rate-budget failure modes, and contain them with the Circuit Breaker and Centrifuge patterns.
6. Evaluate whether a webhook or event handler achieves exactly-once side effects, and apply the Transactional Outbox where it does not.

## Key Terms

- **Anti-Corruption Layer (ACL)** — A translation boundary that keeps an external system's data model from leaking into the domain (Evans, 2003); in agentic development, it removes the need for each session to re-learn vendor quirks.
- **Hexagonal Architecture** — Ports and Adapters (Cockburn, 2005): application core decoupled from infrastructure so agent-generated business logic survives infrastructure changes without modification.
- **Port** — In Hexagonal Architecture, an interface defined in the application's own terms; the contract agent-generated code targets.
- **Adapter** — The implementation of a port for a specific external technology; the containment boundary for vendor specificity.
- **Circuit Breaker** — Resilience pattern (Nygard, 2007) that stops calling a failing service and fails fast, periodically probing for recovery.
- **Transactional Outbox** — Pattern that pairs a database write with message publication in one transaction, solving the dual-write problem without distributed transactions.
- **Idempotency** — The property that processing the same request multiple times produces the same result as processing it once.
- **Blast radius** — The set of components, services, and users that could be affected if a change contains a defect; distinct from scope.
- **Trust boundary** — A point where your code interacts with a system you do not control.

## Review Questions

1. The chapter identifies exactly two strategies for handling vendor corruption when agents generate integration code. What are they, and why does the chapter argue that only one of them scales?
2. In the CRM Hub example, why is the port named `CRMPort` rather than `HubSpotPort`, and what does that naming decision protect when a session generates new business logic?
3. What operational failure mode does the Centrifuge pattern address that a basic circuit breaker does not?
4. What is the dual-write problem, and how does the Transactional Outbox make correct behavior structural rather than dependent on the agent's awareness?
5. Why does the chapter's operational discipline treat dead-letter channel contents as test cases rather than as messages to patch and replay?

## Discussion Questions

1. The ACL-amnesia argument rests on the claim that agents cannot accumulate tribal knowledge across sessions. Context files, skill documents, and the Knowledge Loop (Standard 11, Chapter 10) all attempt to build exactly such an accumulation channel. To what extent do those mechanisms weaken the argument, and where does structural containment still beat a well-maintained context file?
2. Every pattern in this chapter adds infrastructure a team must build and operate before its agents produce their first integration — the 15–25% discipline overhead made concrete. For a two-person team shipping a single-vendor integration, which of the five patterns would you defer, and what evidence would tell you the deferral had become a mistake?
3. The chapter states that the patterns are decades old and only their application to agentic constraints is new. Does the ACL-amnesia argument describe a genuinely new engineering problem, or a familiar one (onboarding, turnover, contractor churn) at higher frequency? What follows from each answer?

## Exercises

**Exercise 11.1 (Core) — Design an Anti-Corruption Layer for a messy vendor API.** A payments vendor's API has these documented behaviors: a misspelled field `recepient_id` that cannot be renamed; two names for the same merchant identifier (`mrch_ref` in older endpoints, `merchant_uid` in newer ones); HTTP 200 responses carrying `{"ok": false, "err": "..."}` on failure; and amounts returned as strings in major units on reads but required as integers in minor units on writes. Design the boundary that keeps all four quirks out of your domain. *(~2 h)*
*Deliverable:* A port interface in domain terms, an adapter skeleton showing where each translation happens, and corruption containment notes mapping each quirk to the exact code location that absorbs it.
*Assessment:* Judged against the ACL card in `references/pattern-quick-reference.md` §1 and the port/adapter examples in the companion repository (`examples/hexagonal-crm-port.ts`, `examples/hubspot-adapter.ts`); interface quality per Standard 4 (Interface-First Design). Pass requires that no vendor name, spelling, or unit convention appears in the port.

**Exercise 11.2 (Core) — Pattern selection under realistic ambiguity.** For each of five scenarios, name the pattern from this chapter you would apply and justify the choice in three or four sentences: (a) two agent-generated services must react to each other's changes without either appearing in the other's generation context; (b) a webhook handler occasionally receives payload versions the specification never mentioned; (c) a nightly sync job written by an agent is exhausting the vendor's account-wide rate quota and starving three other integrations; (d) a handler writes an order to the database and then publishes an event, and a crash between the two has already produced an unnotified order; (e) a vendor retries webhooks aggressively and support has logged duplicate welcome emails. *(~45 min)*
*Deliverable:* A one-page decision memo covering all five scenarios, including at least one scenario where you argue two patterns must compose.
*Assessment:* Judged against `references/pattern-quick-reference.md` and the companion repository's `references/pattern-catalog.md`; each justification must name the failure mode the pattern removes, not just the pattern.

**Exercise 11.3 (Core) — Specify idempotency as a constraint, not an instruction.** Write a SPEC.md for an inbound webhook handler (vendor of your choice) whose acceptance criteria make idempotency, failure boundaries, and rate behavior explicit, machine-checkable constraints. The chapter predicts agents omit exactly these; your specification's job is to make omission impossible. *(~2 h)*
*Deliverable:* A SPEC.md using the companion repository template, with a MUST-NOT list covering all six Standard 1 categories.
*Assessment:* The pre-generation gate for Standard 1 (Chapter 5): every acceptance criterion verifiable, no empty MUST-NOT categories, idempotency stated as an acceptance criterion rather than a design suggestion.

**Exercise 11.4 (Challenge) — Attack your own outbox.** Implement (or design on paper, with pseudocode) a webhook handler following the three-step outbox template in Section 11.5. Then switch roles: enumerate every failure window (crash between idempotency insert and business write, between business write and outbox insert, between commit and publisher pickup, publisher crash after publish before marking published) and demonstrate for each that the system converges to a consistent state — or document the window where it does not. *(~4 h+)*
*Deliverable:* The handler plus a REVIEW.md recording each failure window as a disprove-only finding with verification stance markers (`verified` / `ASSUMPTION` / `VERIFY`).
*Assessment:* Standard 7 (Falsification Review) using the companion repository's REVIEW.md template and `examples/transactional-outbox.sql`; pass requires at least one finding the happy-path reading would have missed.
