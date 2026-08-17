# Appendix D — Platform Modernization Design Study — Study Guide

Student and self-study exercises moved from the design-study appendix so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Exercises

**Exercise D.1 (Core) — Defend or attack Decision Point D.1.** Take a position on the author's choice at Decision Point D.1 — committing to full platform replacement rather than a read-only data layer on the vendor — using only what was knowable at design time; you may not use hindsight the author lacked, and you may not assume the $3M–$8M model is accurate, since the appendix itself brackets it as unmeasured intent. Note that Phase 1 of the plan builds something very close to the read-only alternative; address whether that weakens or strengthens the commitment to replacement. *(~2 h)*
*Deliverable:* A position memo naming the three facts you would demand before authorizing the program, and the earliest phase gate at which you would expect the replacement decision to be revisited.
*Assessment:* Rubric: ex-ante reasoning only; treats the business case as a model to interrogate rather than a fact; engages the Phase-1-as-off-ramp observation directly.

**Exercise D.2 (Core) — Attack the phase gates.** For each of the five gates in the D.3 checklist, construct a failure that would pass the gate as written: a projection bug the hourly comparison jobs normalize away, a divergence class the reconciliation threshold hides, a domain cutover whose "business outcomes match" while a rarely exercised workflow breaks, a compliance export gap that surfaces only at an annual reporting boundary, or a Phase 5 irreversibility the entry gate fails to test. Propose the tightening each attack forces. *(~2 h)*
*Deliverable:* A gate-critique table: gate, attack scenario, why the written gate passes it, proposed tightening.
*Assessment:* Standard 7 (Falsification Review) applied to a plan and Standard 9's rollback discipline: attacks are graded on whether a reviewer can trace the failure through the gate's literal wording, not on rhetorical plausibility.

**Exercise D.3 (Challenge) — Outline the honest sequel.** Section D.5 states five commitments the design would test if built. Write the outline of the case study that would report on them: for each commitment, the measurement or observation that would count as evidence, the phase at which it becomes collectible, the result that would falsify the commitment, and the disclosure the Status and Evidence box of that future chapter would owe the reader if results are mixed. *(~2 h)*
*Deliverable:* A two-page case-study outline with a per-commitment evidence table.
*Assessment:* Judged on honest-evidence criteria: every commitment gets a falsifiable check tied to a specific phase; projections and measurements are kept in separate categories exactly as Chapter 14's evidence discipline prescribes.

