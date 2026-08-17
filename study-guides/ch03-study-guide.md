# Chapter 3: The Economics of AI-Generated Code — Study Guide

Student and self-study material moved from Chapter 3 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Compute the review burden implied by a team's code-generation rate and explain why the review model, rather than reviewer effort, must change.
2. Explain the AI productivity paradox — individual output up, organizational delivery flat — and the amplifier mechanism DORA identified behind it.
3. Analyze GitClear's four findings (duplication, churn, refactoring collapse, copy-paste over refactoring) as leading indicators of technical debt.
4. Define dark code and distinguish it from traditional technical debt.
5. Apply the disciplined-versus-undisciplined cost model to compute a break-even point for stated parameters, identifying which inputs are the author's and which must be your own.
6. Construct a stakeholder-specific business case for governance using honestly framed evidence.

## Key Terms

- **Dark code** — Code that exists, compiles, and possibly passes tests, but that no one understands or can maintain; distinct from traditional technical debt because it is unexamined and leaves no artifact marking its creation.
- **Generation-review asymmetry** — The gap between the rate at which code can be generated (thousands of LOC per hour) and the rate at which it can be meaningfully reviewed (bounded by human cognition); the structural problem that motivates the book's standards, and the foundation of every economic argument in this chapter.
- **AI is an amplifier (DORA 2025)** — DORA's central finding that AI magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones.
- **DORA metrics** — Deployment frequency, lead time for changes, change failure rate, and mean time to restore, with deployment rework rate added as a fifth metric in 2024.
- **Cui et al. (2025)** — The field experiment of 4,867 developers finding ~26% average productivity gains — 27–39% for junior developers, 8–13% for senior — with only ~60% adoption after a year.
- **Faros AI 10,000-developer telemetry (2025)** — The telemetry analysis finding 21% more tasks completed and 98% more pull requests merged at the individual level while organizational delivery metrics stayed flat.
- **Code churn** — Lines revised or deleted within two weeks of being written; GitClear's clearest signal of low-quality commits, rising from 5.5% to 7.9% across the AI adoption period.

## Review Questions

1. Reproduce the Section 3.1 arithmetic: at roughly 300 LOC/hour of effective review, what does 10,000 lines of daily agentic output cost a single reviewer, and what does it cost a team of five all generating at that rate? Why does the chapter call the result structural rather than a failure of diligence?
2. State the productivity paradox using the DORA 2024 and Faros AI numbers, and explain the role rework plays in resolving it.
3. Which of GitClear's four findings does the chapter suggest may be the most alarming, and what does a refactoring rate below 10% of changes imply about a codebase's debt repayment?
4. What exactly did Veracode's 45% figure measure, what caveat does the chapter attach to it, and how does the Stanford finding of Perry et al. make the security economics worse rather than better?
5. In the Section 3.5 cost model, identify the line items that make the disciplined path 60% more expensive in week one and the line items that make it 38% cheaper by month three.

## Discussion Questions

1. The 15–25% discipline overhead is paid today by identifiable engineers on identifiable features; the rework spiral is paid later and appears in no budget line. Given how organizations actually allocate cost, which side of that asymmetry usually wins, and what would it take to make the deferred cost visible enough to compete?
2. Dark code, by definition, leaves no artifact at the moment of its creation. If it cannot be inventoried, can it be governed at all? What proxies — churn, review latency versus PR size, provenance metadata — would you accept as evidence of its presence, and where would those proxies mislead you?
3. Section 3.6 tells the skeptical senior engineer: "If the numbers do not support the discipline in our environment, the numbers win." Is that offer honest? What organizational conditions would have to hold for a team to actually let its own measurements overrule a practice its leadership has already invested in?

## Exercises

**Exercise 3.1 (Core) — Compute the economics for a team of N.** *(~2 h)* Parameterize the chapter's model: a team of N engineers (choose N = 5, 10, or your own team's size), each generating R LOC per day with agentic tools (choose R from the Section 1.2 table), reviewed at ~300 LOC/hour, with discipline overhead of 15–25% of cycle time. Compute (a) the daily review burden in reviewer-days, (b) the Section 3.5 per-feature costs with your own inputs replacing the author's, and (c) the week at which the disciplined path breaks even. Break-even here means the *cumulative*-cost crossover — the week the disciplined path's total hours to date fall below the undisciplined path's, not the per-feature comparison, which crosses only at month three. Section 3.5 gives snapshots at month one and month three only, so you must assume the shape of the rework ramp between them; linear interpolation is acceptable, but state and label whatever you assume. Different labeled assumptions legitimately yield different break-even weeks. Vary the month-three rework estimate ±50% and report how the break-even moves.
*Deliverable:* A worksheet (spreadsheet or table) plus a half-page memo stating the break-even conclusion and its sensitivity.
*Assessment:* Arithmetic correct; every input labeled as measured, author's model, or your estimate; the rework-ramp assumption stated and labeled — any labeled assumption with a consistent crossover computation earns credit, since the labeling is what is graded; the sensitivity analysis is present and changes the memo's confidence accordingly. No AI tool required.

**Exercise 3.2 (Core) — The dark-code hunt.** *(~3 h)* In a repository you have the right to inspect — your own project or a public open-source repository with visible AI-assisted contribution — locate candidate dark code. Useful signals: large diffs merged with implausibly short review windows, lines churned within fourteen days, duplicated blocks, and AI-generation markers in commit metadata. Classify each finding as (1) reviewed and comprehended, (2) reviewed but comprehension doubtful, or (3) merged without meaningful review, defending each classification from observable artifacts.
*Deliverable:* An inventory of 5–10 findings with classifications and evidence, plus one remediation proposal for the worst finding.
*Assessment:* Classifications rest on observable evidence (review timestamps, comment substance, churn history), not intuition; the write-up distinguishes dark code from ordinary known-shortcut debt per Section 3.3; the remediation cites comprehension-preserving review (Standard 7, Chapter 7).

**Exercise 3.3 (Challenge) — Replicate a GitClear indicator.** *(~4 h+)* Choose one repository with history spanning the AI adoption period and measure either churn (percentage of lines revised or deleted within fourteen days of being written) or duplication across two comparable time windows. Compare your result with GitClear's baselines and discuss the confounds — team composition, domain shifts, tooling changes — that your two-window design cannot remove.
*Deliverable:* A methodology note, the measurements, and a comparison against the GitClear findings.
*Assessment:* Window definitions and measurement scripts are explicit and reproducible; confounds are named; conclusions are sized to what a single-repository comparison can support.

**Exercise 3.4 (Challenge) — The business-case brief.** *(~90 min)* Choose one stakeholder from Section 3.6 — CFO, CTO, VP of Engineering, or skeptical senior engineer — and write the one-page brief using the four components of the business case, populated with parameters from your organization or from a chosen open-source project.
*Deliverable:* A one-page stakeholder brief.
*Assessment:* The honest-evidence bar: every number is sourced or labeled as an estimate; the ~26% Cui et al. figure is presented as the evidence floor and the ~4.3x figure as a tested hypothesis, never a promise; no unlabeled projections. Peer review against Section 3.6's four components. No AI tool required.

