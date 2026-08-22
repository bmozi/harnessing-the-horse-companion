# Chapter 20: The Road Ahead — Study Guide

Student and self-study material moved from Chapter 20 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why the specify-generate-verify-record structure persists as model capabilities improve.
2. Distinguish the review tasks agents perform reliably from the judgments that remain human, and construct a division-of-labor review protocol.
3. Classify a chapter's claims across the descriptive, practiced-but-unmeasured, and prescriptive evidence categories.
4. Construct a study design capable of falsifying the book's central hypothesis — that discipline is the differentiator.
5. Evaluate the chapter's labeled bets against evidence available at the time of reading.
6. Explain the recursive dark code problem and the defense-in-depth principle: self-improvement is confined by application rails, while approval and enforcement authority remain outside the writable process.

## Key Terms

- **Harness Framework (this book)** — Scope, Prove, Enforce, Communicate: the four disciplines for governing agentic development, applied in this chapter from solo practice to model-training infrastructure.
- **Multi-person adversarial advantage (this book)** — The structural argument that two engineers cross-reviewing each other's AI-assisted work catch assumption errors originating in the human's mental model — errors no agent configuration can replicate.
- **Recursive dark code problem (this book)** — The risk that AI companies using AI to build model infrastructure without discipline accumulate dark code in the systems that train the next model generation; the harness on the harness.
- **Discipline dividend (this book)** — The compounding advantage disciplined teams accumulate; whether it compounds or plateaus is Bet One and an open research question.
- **Dark code (this book)** — Code that exists, compiles, and possibly passes tests, but that no one understands or can maintain; unexamined rather than merely indebted.
- **Adoption gap (this book)** — The observation that the productivity gap between disciplined-AI and undisciplined-AI teams widens faster than organizations can adopt the discipline; organizational maturity, not technology, is the constraint — this chapter extends the gap to the engineering team itself, where colleagues' mental models lagged the practice.
- **Generation-review asymmetry (this book)** — The gap between machine-speed generation and human-cognition-bounded review; the structural problem that persists through every model improvement this chapter forecasts.

## Review Questions

1. Why does the chapter argue that the discipline compensates for an information asymmetry rather than for model limitations, and what follows for teams as models improve?
2. What does agent review do reliably, what can it not do, and what division of labor results?
3. What class of error does the multi-person adversarial advantage catch that same-person, multi-agent review cannot, and why?
4. Name Merlin's four structural governance constraints and state the general principle they implement.
5. State the book's central falsifiable hypothesis and the evidence Section 20.7 says is still missing.

## Discussion Questions

1. The book places itself in the practitioner-account tradition of the Gang of Four, Beck, and Fowler, and invites replication. Should teams adopt frameworks on practitioner evidence ahead of controlled studies? Propose a decision rule for when N=1 depth justifies adoption and when it requires waiting — and apply it to this book.
2. If teams compress to two or three engineer-architects whose scarce skills are specification, review, and architectural judgment, where does the next generation acquire those skills — historically learned through the implementation work agents now do? Sketch what a deliberate junior pipeline would look like.
3. Bet Two implies small organizations increasingly build rather than buy domain-specific software. Consider year five: who stewards those systems against dark code when the builder leaves? Argue whether the recomposition expands the discipline problem or concentrates it.

## Exercises

**Exercise 20.1 (Challenge) — Design the falsification study.** The book's central falsifiable hypothesis: engineering discipline is the variable that separates the METR slowdown from the acceleration this book documents. Design a study that could falsify it. Specify the population and recruitment, the task design, the treatment and control conditions (what "disciplined" and "undisciplined" AI-assisted development mean operationally), the measures (drawing on Chapter 18's definitions), the randomization and controls, the threats to validity — selection effects, learning-curve confounds, expectancy effects, measurement validity — with mitigations, and, decisively, the result pattern that would falsify the book's claim. *(~4 h+)*

*Deliverable:* A study design document of five to eight pages.
*Assessment:* Judged against the open research questions of Section 20.7 and the measurement definitions of Chapter 18. The gate is falsifiability: a design under which no plausible result would count against the hypothesis fails, however rigorous it looks. The threats-to-validity section must address at least the confound the book concedes in its own acceleration arc (Chapter 1): model improvement entangled with practitioner learning.

**Exercise 20.2 (Core) — Evaluate a labeled bet twelve months on.** Choose Bet One (the discipline dividend compounds) or Bet Two (the SaaS recomposition). Gather the evidence available at the time you complete this exercise — industry reports, published replications, your own organization's build-versus-buy decisions — and render a verdict: strengthened, weakened, or unresolved. Date every piece of evidence. *(~2 h)*

*Deliverable:* An evidence memo of at most two pages with a dated source list.
*Assessment:* Judged on evidentiary discipline rather than on the verdict: every claim dated and sourced, the verdict following from the assembled evidence rather than from the book, and "unresolved" accepted as a full-credit answer when the evidence is genuinely mixed.

**Exercise 20.3 (Core) — Classify claims across the evidence boundary.** Apply Section 20.7's three-way taxonomy — descriptive (practiced and measured), practiced but not measured at scale, prescriptive (extrapolated) — to Chapter 19. Select eight to ten of that chapter's specific claims, classify each, and flag any claim the chapter states with more confidence than its evidence class warrants. *(~2 h)*

*Deliverable:* A classification table with a one-paragraph justification per flagged claim.
*Assessment:* Judged for consistency with Section 20.7's own classifications where they overlap (the crawl-walk-run model is classified there explicitly). Departures from the book's self-classification are permitted and must be argued.

**Exercise 20.4 (Core) — Design the division-of-labor review protocol.** A six-engineer team adopting agent-assisted review asks you to specify which review checks are delegated to the adversarial agent and which remain human. Using Section 20.2's analysis of what agent review can and cannot do, write the protocol: the delegated checks, the reserved judgments, the handoff between them, and the escalation rule when the agent's findings and the human's judgment conflict. *(~2 h)*

*Deliverable:* A review protocol document.
*Assessment:* Judged against Section 20.2: mechanical verification delegated, alignment judgments reserved, and every assignment justified by the can/cannot analysis rather than by convenience. A protocol that delegates specification-fitness judgment to the agent fails.
