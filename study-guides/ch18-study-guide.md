# Chapter 18: Measuring What Matters — Study Guide

Student and self-study material moved from Chapter 18 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain which DORA metrics carry over to agentic development unchanged and how lead time must be reinterpreted.
2. Define regeneration rate, distinguish it from DORA's rework rate, and diagnose the three failures a high rate indicates.
3. Analyze the METR study's design and state precisely what it establishes and what it leaves open.
4. Apply the personal calibration kit — the quarterly self-A/B, the honest journal, and the personal eval set — to your own practice.
5. Construct a team dashboard that separates agent-generated from human-generated changes and resists Goodhart's Law.
6. Evaluate a metrics program for productivity theater using the quality-throughput lens.

## Key Terms

- **DORA metrics** — Deployment frequency, lead time for changes, change failure rate, and mean time to restore (Forsgren, Humble, Kim, 2018), with deployment rework rate added in 2024.
- **Regeneration rate (this book)** — The percentage of agent-generated changes requiring more than one generation cycle before passing review; pre-merge waste, deliberately distinct from DORA's post-merge rework rate.
- **Calibration delta (this book)** — The gap between felt speedup and measured speedup, tracked through the quarterly self-A/B and the honest journal.
- **Self-A/B test (quarterly)** — The personal calibration protocol: one task hand-coded, one with the standard agentic workflow, both measured on the same criteria.
- **Honest journal** — The weekly three-section calibration artifact: what AI saved time on, what AI cost time on, and one pattern to try differently.
- **Quality throughput (this book)** — The rate at which a team ships production-quality changes without regressions, read as a joint lens on deployment frequency, change failure rate, and regeneration rate rather than as a single formula.
- **METR studies (2025–2026)** — The 2025 randomized controlled trial found experienced developers 19% slower with AI tools while feeling roughly 20% faster; the 2026 follow-ups suggest newer tools may now produce speedups while preserving the warning against unmeasured self-reports.
- **Generation-review asymmetry (this book)** — The gap between machine-speed generation and human-cognition-bounded review; the structural reason review, not generation, is the binding constraint this chapter measures around.

## Review Questions

1. Which DORA metric requires reinterpretation in agentic development, and what does its new reading reveal about where the bottleneck sits?
2. Define regeneration rate and DORA's rework rate, and state which side of the merge each measures.
3. What did the METR study measure, and what does the chapter claim the result does and does not establish?
4. A team's regeneration rate is 65%. Name the three candidate diagnoses and the intervention each one calls for.
5. Why does the chapter decline to offer a formula for quality throughput?

## Discussion Questions

1. The chapter forbids using these metrics as individual targets, yet most performance-review systems demand individual numbers. Reconcile the two — or argue that they cannot be reconciled and something has to give. What survives contact with an executive who wants a per-engineer AI-productivity figure?
2. Is the discipline-differentiator explanation of the METR gap the most parsimonious reading? Argue both sides using METR's own candidate explanations — repository familiarity, high implicit quality standards, tool friction — and state what evidence would settle the question.
3. The honest journal claims felt speedup converges toward measured speedup over quarters — as measured by the same engineer keeping the journal. Can self-measurement correct the bias it exists to detect, or does the calibration kit need an external check?

## Exercises

**Exercise 18.1 (Core) — Instrument a described team.** A twelve-engineer team is two quarters into agentic adoption. Today it tracks two numbers — PR count and lines changed — both trending up while stakeholders report no faster delivery. Design the team's measurement program: select the metric groups from Section 18.5, define exactly how regeneration rate will be measured (what event begins a generation cycle, what ends one, what the denominator is, and which systems supply the data), and specify the weekly dashboard layout with agent/human splits and trend windows. *(~2 h)*

*Deliverable:* A measurement plan plus a dashboard specification.
*Assessment:* Judged against the Goodhart-resistance criteria of Section 18.4: metrics are read jointly, none is an individual target, agent and human changes are split, and every metric has a named counter-metric that would expose gaming it. The regeneration-rate definition must be operational — a second engineer could implement it without asking questions.

**Exercise 18.2 (Core) — Design and run your quarterly self-A/B.** Select a task class you perform regularly and design your first self-A/B: the two comparable tasks, their comparability constraints, the four measures from Section 18.1, and where you will record your predicted speedup before measuring. Run the pair if tool access permits. Paper variant: submit the full protocol with your pre-registered prediction and a worked example showing how you would compute your calibration delta. *(~2 h)*

*Deliverable:* A one-page protocol plus either a completed first run or the pre-registered paper variant.
*Assessment:* Judged against the self-A/B protocol in Section 18.1: the same criteria applied to both conditions, felt speedup recorded before measured speedup, and a stated calibration delta. Honesty over rigor — a protocol that hides the felt-versus-measured comparison fails regardless of polish.

**Exercise 18.3 (Core) — Build a personal eval set.** Construct a personal eval set of five representative tasks for your own practice, following the structure in Section 18.1: per task, a prompt file, a success file with specific 1–5 scoring criteria per level, and a runs-directory format recording model, wall time, and score. Paper variant: complete task specifications and scoring rubrics without executing any runs. *(~2 h)*

*Deliverable:* The eval set directory, or its complete paper specification.
*Assessment:* Judged against the eval-set structure in Section 18.1. Each scoring level must be decidable by a second person from the criteria alone; a rubric two graders would score differently fails the gate.

**Exercise 18.4 (Challenge) — Red-team your own dashboard.** Take the dashboard from Exercise 18.1 and play the adversary: an engineer whose bonus depends on it. For each metric, find the cheapest gaming strategy. Then show, metric by metric, where the joint reading of Section 18.4 exposes the strategy — and identify at least one strategy the joint reading fails to catch, with a proposed countermeasure and its cost. *(~2 h)*

*Deliverable:* A red-team memo covering every dashboard metric.
*Assessment:* Judged against Section 18.4's paired-metric defense: each gaming strategy must name the counter-metric that would move in response, and the uncaught strategy must be plausible rather than exotic. Full credit requires pricing the countermeasure, not just proposing it.

