# Chapter 19: Team Transformation — Crawl, Walk, Run at Scale — Study Guide

Student and self-study material moved from Chapter 19 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Describe the three crawl-stage practices and the exit criteria that mark readiness for walk.
2. Construct a crawl-stage adoption plan for an organization with stated absorption constraints.
3. Analyze a team's stage placement and identify practices adopted prematurely.
4. Explain why organizational absorption capacity, rather than development velocity, is the binding constraint on agentic transformation.
5. Apply the diffusion-of-innovations and chasm-crossing models to locate an organization on the adoption curve.
6. Diagnose the three transformation anti-patterns and prescribe the corresponding fix.

## Key Terms

- **Context file** — `AGENTS.md` or `CLAUDE.md`: the project-root document capturing the conventions, constraints, and architecture boundaries every agent session needs; the first crawl-stage practice.
- **Architecture-as-code** — Architectural constraints expressed as enforceable CI rules rather than documentation; the walk-stage mechanism that prevents drift at the speed of generation.
- **Pipeline tracks** — The three deployment tracks (Hotfix, Standard, Full) that match gate intensity to change risk.
- **Adversarial validation** — The agent mode of Falsification Review: a fresh-instance agent attacks the generated code with a defect-finding posture; automated in CI at the run stage.
- **Dark code (this book)** — Code that exists, compiles, and possibly passes tests, but that no one understands or can maintain; the product of the mandate-without-standards anti-pattern.
- **Adoption gap (this book)** — The observation that the productivity gap between disciplined-AI and undisciplined-AI teams widens faster than organizations can adopt the discipline; organizational maturity, not technology, is the constraint.
- **Regeneration rate (this book)** — The percentage of agent-generated changes requiring more than one generation cycle before passing review; the stage thresholds in this chapter (40–60% at crawl, below 20% before run) use this metric.
- **Discipline dividend (this book)** — The compounding advantage disciplined teams accumulate; this chapter's adoption incentive, to be verified on the team's own dashboard rather than accepted on faith.

## Review Questions

1. Name the three crawl-stage practices and, for each, the standard it implements in miniature.
2. What are the four exit criteria for the crawl stage, and why does the model impose a two-sprint minimum?
3. Why must a team not adopt the run stage directly? Name the specific failure each run capability produces when its walk-stage prerequisite is missing.
4. Which two findings from DORA's 2024 research does the chapter apply to leadership, and what does each imply for agentic transformation?
5. For each of the four expertise levels, name the trap and its countermeasure.

## Discussion Questions

1. Chapter 20's Honest Reckoning records that the author did much of the change-management work this chapter prescribes — steering committee, stakeholder mapping, demonstration over mandate — and adoption still stalled because the practice had not become a shared team capability. Which barriers would a better playbook have addressed, which move only at the speed of trust and experience, and what does that split imply for any adoption timeline you commit to?
2. The crawl stage claims roughly 60–70% of the safety benefit for roughly 20% of the overhead — an author's estimate, as the chapter discloses. Design the measurement that would test that claim in your organization, and discuss what you should do at crawl if the ratio turns out to be much worse.
3. DORA 2024 finds that priorities shifting faster than teams can absorb produce productivity declines and burnout; leadership answers that markets move faster than absorption. Where does responsiveness end and churn begin, and who in the organization should hold that line?

## Exercises

**Exercise 19.1 (Core) — Write a crawl-stage adoption plan.** An organization of forty engineers in three product teams asks you to plan its agentic adoption. Constraints: a support rotation consumes 30% of one team's capacity; a second team is mid-migration and cannot absorb new process this quarter; executive priorities have historically been re-set quarterly; and the CTO wants visible progress in thirty days. Write the crawl-stage plan: the first thirty days (per Section 19.5), which practices land on which team and when, how the plan respects each stated absorption constraint, and the exit-criteria evidence you will collect before proposing walk. *(~2 h)*

*Deliverable:* An adoption plan of at most four pages.
*Assessment:* Judged against the crawl exit criteria of Section 19.1 and the first-30-days sequence of Section 19.5. The plan must introduce no walk- or run-stage practice, must state how each absorption constraint changes the rollout, and must define measurable exit evidence rather than calendar dates.

**Exercise 19.2 (Core) — Diagnose the anti-patterns under contested evidence.** Three scenarios, each already diagnosed two different ways by the people living it: (a) after a pilot team's glowing report, a CIO mandates AI tools for all teams by quarter end and ships the pilot's context files organization-wide unchanged; usage is tracked, quality is not — one director calls it a mandate without standards, another insists the standards exist and the pilot simply failed to scale; (b) after a generated migration corrupts a staging database, the VP of Engineering bans every AI tool except one approved assistant so slow nobody uses it — three months later, commit-style discontinuities suggest ungoverned usage on two teams; is that the ban overcorrection, or a mandate of the wrong tool?; (c) an infrastructure team has run the full framework for two years with excellent metrics and complete, current, published documentation — yet no other team has adopted any of it, and the tech lead still fields constant questions by pairing ad hoc. For each scenario, name your primary diagnosis and the strongest competing one, identify the observable evidence that discriminates between them, and prescribe a fix that survives the stated constraint: the CIO will not retract the mandate, the VP will not lift the ban this quarter, and the infrastructure team has no spare capacity to run an adoption program. *(~2 h)*

*Deliverable:* A diagnosis memo, one section per scenario: the differential diagnosis with its discriminating evidence, the constrained fix, and the next-quarter signal that would tell you your diagnosis was wrong.
*Assessment:* Judged against the anti-pattern catalog in Section 19.6, with credit for engaging the competing diagnosis on its merits. Scenario (c) is the trap: its documentation is complete, so the catalog's undocumented-tacit-knowledge mechanism cannot carry the diagnosis alone — a pass locates what the adoption kit still failed to transfer (Section 19.4's alignment argument applies). A fix that violates its stated constraint fails regardless of catalog fidelity.

**Exercise 19.3 (Core) — Assess your expertise level and design the countermeasure.** Place yourself at one of the four expertise levels in Section 19.1 with written justification, name your level's trap, and design a personal countermeasure plan including the metrics that would show the trap operating on you. Use the calibration instruments of Chapter 18 where they apply. *(~45 min)*

*Deliverable:* A one-page self-assessment and countermeasure plan.
*Assessment:* Judged against the level descriptions and traps in Section 19.1. The countermeasure must be the one matched to your level and must be instrumented with at least one measurable signal; an unmeasurable countermeasure fails.

**Exercise 19.4 (Challenge) — Conduct a walk-readiness audit.** Twelve months after Exercise 19.1's plan, the organization reports: context files exist on all three teams, but one team's has not changed in five months; pre-commit hooks block on every repository; specifications cover roughly 70% of non-trivial agent-generated changes on two teams and 40% on the third; regeneration rate sits at 45% organization-wide; and the CTO, citing competitor announcements, wants multi-agent orchestration next quarter. Decide, team by team, whether each may enter walk; design the walk rollout for any team that qualifies, including the six-month operating plan; and write the response to the CTO's orchestration request, citing the run prerequisites. *(~4 h+)*

*Deliverable:* A readiness audit, a walk rollout plan, and a one-page memo to the CTO.
*Assessment:* Judged against the crawl exit criteria (Section 19.1) and the run prerequisites (Section 19.3). Every stage decision must cite the stated evidence; a plan that grants the CTO's request as asked, or refuses it without the prerequisite list, fails.

