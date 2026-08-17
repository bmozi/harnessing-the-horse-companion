# Chapter 1: The Inflection Point — Study Guide

Student and self-study material moved from Chapter 1 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain the generation-review asymmetry and compute the review burden implied by a given code-generation rate.
2. Analyze the historical analogies the chapter offers — the compiler era, Agile, microservices — identifying what the loose pattern predicts and where the analogy breaks on speed.
3. Summarize the four converging lines of third-party evidence (Peng et al., Dell'Acqua et al., McKinsey, DORA) and identify what each study can and cannot show.
4. Evaluate the evidentiary strength of the author's acceleration arc using the chapter's own methodological caveats and the METR randomized controlled trial.
5. Define the four disciplines of the Harness Framework — Scope, Prove, Enforce, Communicate — and apply them to diagnose a failure in an agentic workflow.
6. Explain the thesis "code is the receipt, clarity is the product" and its consequences for where the engineer's value concentrates.

## Key Terms

- **Generation-review asymmetry** — The gap between the rate at which code can be generated (thousands of LOC per hour) and the rate at which it can be meaningfully reviewed (bounded by human cognition); the structural problem that motivates the book's standards.
- **The 70% problem** — Addy Osmani's observation that AI tools rapidly produce the predictable ~70% of a solution, while the remaining 30% — edge cases, security hardening, production integration, architectural coherence — is where the bugs and the value live.
- **Jagged technological frontier** — Dell'Acqua et al.'s finding that AI capability is unevenly distributed across tasks, with real gains inside the frontier, degraded output outside it, and no visible marking on the boundary.
- **METR studies (2025–2026)** — The 2025 randomized controlled trial found experienced developers 19% slower with AI tools while reporting they felt about 20% faster; METR's 2026 follow-ups suggest newer tools may now produce speedups while reinforcing the need to distinguish measured effects from self-reports.
- **Acceleration arc** — The author's documented three-phase throughput progression, led by the conservative ~4.3x post-learning-curve figure, governed by stated caveats, and offered as hypothesis rather than proof.
- **Harness Framework** — Scope, Prove, Enforce, Communicate: the four disciplines for governing agentic development.
- **MUST-NOT list** — The negative-space section of SPEC.md: explicit prohibitions constraining what the agent may touch, modify, or assume. Standard 1 (Chapter 5) requires six categories, and an empty MUST-NOT list is a reliable predictor of scope drift.
- **AI is an amplifier (DORA 2025)** — DORA's central finding that AI magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones.

## Review Questions

1. State the generation-review asymmetry in one sentence, then reproduce the arithmetic behind the third row of the Section 1.2 table: starting from a representative day of ≈10,000 LOC of accepted output and the ~300 LOC/hour review ceiling, show why one day of agentic output demands roughly 33 hours of conventional review — 10 to 50 across the honest range of working days.
2. What did the assembly programmers of the FORTRAN era get right, and what did the 1968 NATO conference add to the picture that the compiler alone did not?
3. According to Dell'Acqua et al., what happened on tasks outside the AI's capability frontier, and why does the jaggedness of that frontier argue for verifying output regardless of which side you believe you are on?
4. List the three methodological caveats Section 1.6 attaches to the author's acceleration arc, and explain why ~4.3x rather than 41x is the figure the chapter asks you to carry.
5. What did the METR July 2025 trial measure, what did it find, and what does the roughly 40-percentage-point gap between felt and measured speed imply about self-reported productivity numbers — including the author's?

## Discussion Questions

1. Section 1.1 argues that at current speeds "the governance must exist before you turn the tool on." Under real delivery pressure — a demo tomorrow, a competitor shipping weekly — is that achievable, or does discipline always trail capability? What would you sacrifice to make it true on your team?
2. The chapter answers METR's 19%-slower finding by declining the rebuttal that the study's developers simply lacked discipline, calling that argument unfalsifiable. Was declining the right move? What experiment or measurement could actually settle whether the book's discipline changes the METR result?
3. Section 1.7 claims the engineer who "clings to code-as-identity enters a losing competition with a tool that types faster." Where does this argument overreach, if anywhere? What parts of code authorship carry judgment that the receipt-versus-product framing undervalues?

## Exercises

**Exercise 1.1 (Core) — Close the review arithmetic, or show that it cannot close.** *(~45 min)* This exercise uses the review-capacity model from Chapter 3, Section 3.1 (the ~300 LOC/hour ceiling from the SmartBear/Cisco study); the two chapters are assigned together in weeks 1–2 of the course plan, and the Section 1.2 table plus that ceiling are the only numbers you need. Compute the daily review burden for: (a) a solo engineer generating four hours per day at the low agentic bound (2,000 LOC/hour); (b) a team of six with two designated reviewers at the mid agentic bound; (c) the same team after METR's seven-month capability doubling has run twice. For each scenario, state whether conventional line-by-line review can keep pace and what must change if it cannot.
*Deliverable:* A one-page review-load analysis with all arithmetic shown.
*Assessment:* Calculations consistent with the Section 1.2 table and the SmartBear/Cisco review-rate ceiling; conclusions follow from the computed numbers, not from the book's rhetoric. No AI tool required.

**Exercise 1.2 (Core) — Grade the acceleration arc as evidence.** *(~2 h)* Section 1.6 presents the author's three-phase arc and then arms you against it: three methodological caveats and the METR randomized controlled trial. Write a referee-style critique that assigns the arc an evidentiary grade. Your critique must address the baseline choice (a learning period), the co-evolution confound (model improvement versus discipline), LOC as a volume-not-value metric, and the self-report problem METR documents. End by stating the strongest version of the claim the evidence actually supports.
*Deliverable:* A 600–900 word critique memo with an explicit graded verdict.
*Assessment:* Engages all three stated caveats plus the METR finding; the verdict distinguishes what the data can and cannot support rather than accepting or dismissing wholesale; no evidence invented beyond the chapter's.

**Exercise 1.3 (Core) — Write the MUST-NOT list for a system you know.** *(~90 min)* Choose a codebase you know well — a course project, an open-source repository you contribute to, or a work system you may discuss. Draft the MUST-NOT list an agent would need before touching it. Every entry must name a concrete artifact (file, module, schema, configuration) and the failure it prevents. The six MUST-NOT categories are architectural, dependency, data, security, performance, and behavioral; they are defined in Standard 1 (Chapter 5), and the companion SPEC.md template lists them.
*Deliverable:* A MUST-NOT list of 8–15 entries in the companion SPEC.md format.
*Assessment:* All six MUST-NOT categories are represented, and entries are specific enough that a violation would be mechanically detectable. No AI tool required.

**Exercise 1.4 (Challenge, forward-looking) — Design your own before-and-after.** *(~2 h; uses Chapter 18's quarterly self-A/B design as its reference — assign alongside or after that chapter, or complete it now and revise after reading Chapter 18)* METR showed that the felt sense of speed lies. Design — do not yet run — a personal measurement protocol for your first month of disciplined agentic practice: pre-registered predictions, the metrics you will record, the comparison you will make, and the confounds you cannot remove. Chapter 18's quarterly self-A/B test is the reference design.
*Deliverable:* A one-page measurement protocol with pre-registered predictions.
*Assessment:* Predictions committed before any measurement; at least one metric beyond LOC; the confounds section names model improvement and task mix; the protocol would detect a METR-style perception gap if one exists.
