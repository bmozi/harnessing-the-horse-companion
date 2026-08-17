# Chapter 14: Case Study — The CRM Integration Hub — Study Guide

Student and self-study material moved from Chapter 14 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Analyze how ungoverned integration paths accumulate concrete defects — data-quality gaps, credential exposure, deadline risk — and trace each architectural decision in a real engagement to its driver.
2. Evaluate a build-vs-buy decision using license-class triage evidence that the reader can independently verify.
3. Defend sequential, phase-gated migration under deadline pressure using rate-budget and integration-testing arguments.
4. Apply verification stance markers to AI-generated architectural claims and explain what each of the engagement's three catches prevented.
5. Distinguish an engagement's process outputs from its outcomes, and identify the phase gate at which each projection converts to a measurement.

## Key Terms

- **Hub (CRM Hub)** — The Fieldstone engagement's CRM integration mediating layer, applying Hexagonal Architecture, the Anti-Corruption Layer, and Strangler Fig at integration scale.
- **Verification stance markers** — The `verified` / `ASSUMPTION` / `VERIFY` marker convention for factual claims in agent-generated code and documentation.
- **Strangler Fig** — Migration pattern (Fowler, 2004) that incrementally builds new components alongside the legacy system and gradually routes traffic from old to new.
- **ADR (Architecture Decision Record)** — A short document capturing the context, decision, alternatives, and consequences of a significant architectural choice.
- **Anti-Corruption Layer (ACL)** — A translation boundary that keeps an external system's data model from leaking into the domain.
- **Hexagonal Architecture** — Ports and Adapters (Cockburn, 2005); the Hub's `CRMPort` is the pattern's central instance in this chapter.
- **Blast radius** — The set of components, services, and users that could be affected if a change contains a defect; the constraint that drives sequential migration here.

## Review Questions

1. What were the three production data-quality gaps in the legacy estate, and what shared root cause did reading the source code reveal?
2. Why does the Hub expose exactly two surfaces, and what would be lost by forcing either consumer class onto the other's surface?
3. What is the decisive constraint behind migrating the six sources sequentially, and what would a mis-estimated rate budget look like under a parallel cutover?
4. Describe the three verification catches during ADR drafting and what class of error each round caught.
5. Why does Section 14.5 classify the 43 review findings and the license discoveries as process outputs rather than outcomes, and what does that distinction guard against?

## Discussion Questions

1. HUB_PRINCIPLES.md allows no exceptions "by precedent, by urgency, or by 'it's only read-only'" — exceptions require an approved ADR. Suppose a Hub defect surfaces during a deadline cutover window and a one-day direct-to-HubSpot bypass would protect the cutover. Does a governed exception process rescue the principle or hollow it out? What should the ADR for that exception have to contain?
2. The chapter's evidence is one practitioner, private repositories, self-reported metrics — stated openly in the Status and Evidence box. What would meaningful external replication of this case look like in practice, and which of the seven Lessons would survive intact even if every at-cutover projection failed?

## Exercises

**Exercise 14.1 (Core) — Defend or attack Decision Point 14.2.** Take a position on the author's choice of sequential migration at Decision Point 14.2, for or against, using only information available at the time of the decision — you may not use hindsight the author lacked (no appeals to how the phases actually went). If you attack, propose the alternative sequencing or parallelization you would have run and its risk controls. *(~2 h)*
*Deliverable:* A one-page position memo, including the specific facts you would have demanded before deciding (quota mechanics, per-source volume estimates, rollback rehearsal results) and how each would have moved your decision.
*Assessment:* Rubric: ex-ante information only; engages the rate-quota and integration-testing arguments directly rather than around them; states what evidence would change the writer's mind.

**Exercise 14.2 (Core) — Critique the Status and Evidence box.** Audit this chapter's Status and Evidence box and Section 14.5. Classify every claim as measured, projected, or unverifiable by the reader; then, for each projection, name the evidence that would upgrade it and the specific phase gate where the chapter says the conversion happens. *(~2 h)*
*Deliverable:* An evidence audit table (claim, classification, upgrade evidence, conversion point) plus a short paragraph identifying the claim whose failure would damage the chapter's argument most.
*Assessment:* Judged on completeness against Sections 14.5's three categories and on correctly identifying the externally checkable claims (licenses, deprecation dates, quotas) as the exception to the private-evidence limits.

**Exercise 14.3 (Core) — Re-run the license triage against current sources.** The chapter's five license discoveries — Airbyte (ELv2), Nango (ELv2), Restate (BSL), Convoy (MPL 2.0 → ELv2), Inngest (SSPL) — are presented as externally checkable. Check them: verify each against the project's current published license, and note anything that has changed since August 2026. *(~45 min)*
*Deliverable:* A verification memo with a primary-source citation per project and a verification stance marker (`verified` / `ASSUMPTION` / `VERIFY`) on every claim.
*Assessment:* Standard 7's verification stance applied to the book itself: pass requires primary sources (repository LICENSE files or official announcements), not aggregator summaries, and honest markers where verification was inconclusive.

**Exercise 14.4 (Challenge) — Write, then break, a principles document.** Draft a HUB_PRINCIPLES-style normative policy (at most seven principles, each with a why and a how-to-apply) for a telephony hub mediating all Genesys interaction, compact enough to fit in an agent session's context. Then switch roles: as an engineer under deadline pressure, find the loophole — the expedient integration your own principles fail to forbid — and close it. *(~4 h+)*
*Deliverable:* The principles document plus a loophole appendix documenting the attack and the revision it forced.
*Assessment:* Judged against Lesson 5's criteria (short normative policy governing agent behavior) and Standard 1's MUST-NOT coverage: the loophole appendix is graded on whether the attack would genuinely have passed the original text.

