# Quarterly Self-A/B Test

> **Chapter:** ch18 — Measuring What Matters (Section 18.1)
> **Last revised:** 2026-06-16
> **Use this for:** Quarterly measurement of your **measured**
> speedup (vs. your **felt** speedup from the calibration journal).

The METR study (July 2025) found experienced developers using AI
tools were **19% slower** while feeling **20% faster** — a
40-percentage-point gap between felt and measured productivity.

**The team-level dashboard tells you whether the system is
working. The quarterly self-A/B tells you whether YOU are working
effectively.**

The self-A/B does not need to be statistically rigorous; it needs
to be **honest**. A single paired comparison per quarter,
sustained over a year, gives you **four data points** — enough to
see your own trend line and enough to catch the METR gap if it
applies to you.

---

## The Protocol

### Step 1: Select the task

Pick a task from a class you **regularly perform**:

- A new API endpoint
- A refactoring
- A test suite
- An integration

The task should be:

- [ ] Representative of your normal work (not artificial)
- [ ] Small enough to complete in a few hours (not days)
- [ ] Clearly defined (you know what "done" means)
- [ ] Comparable across runs (use the same class of task each
      quarter for clean trend lines)

### Step 2: Complete it hand-coded

**No agent. No copilot. No autocomplete.** Pure manual coding.

Time yourself. Record:

- [ ] Time to first working version
- [ ] Total time including review and cleanup
- [ ] Defects you noticed (and fixed) during development
- [ ] Defects found in your own code review (be honest with
      yourself)
- [ ] Rework iterations (the agent doesn't have rework loops;
      you do — what you wrote and discarded counts)

### Step 3: Complete the same task with your standard agentic workflow

A **fresh** start. Don't reuse anything from Step 2.

Use your normal agentic workflow:
- SPEC.md
- Context files (CLAUDE.md)
- Generation prompt
- Review prompt
- Whatever discipline you normally apply

Record the **same metrics** as Step 2:

- [ ] Time to first working version
- [ ] Total time including review and cleanup
- [ ] Defect count in review
- [ ] Review time
- [ ] Rework iterations

### Step 4: Compare honestly

Side-by-side:

```markdown
# Self-A/B: [Task name] — [YYYY-MM-DD]

## Hand-coded
- Time to first working: [X]m
- Total time: [Y]m
- Defects in review: [N]
- Rework iterations: [N]

## Agentic workflow
- Time to first working: [X]m
- Total time: [Y]m
- Defects in review: [N]
- Rework iterations: [N]

## Measured speedup
[(hand_total - agent_total) / hand_total × 100] = [N]%

## Felt speedup (gut estimate before doing the math)
[N]%

## Calibration delta
felt − measured = [N] percentage points

## Insights
[1–3 bullets about what surprised you, what you'd do differently,
what this tells you about your workflow]
```

---

## The Calibration Delta

The gap between **felt speedup** and **measured speedup** is your
calibration delta.

### Tracking it over a year

| Quarter | Felt | Measured | Delta |
| --- | --- | --- | --- |
| Q1 | 40% | 5% | 35 pp ⚠️ |
| Q2 | 30% | 12% | 18 pp |
| Q3 | 22% | 18% | 4 pp ✓ |
| Q4 | 20% | 19% | 1 pp ✓ |

**The goal is not zero.** Some imprecision in self-assessment is
normal. The goal is a **stable delta** that you understand and
can account for.

**A growing delta is a warning:** you are becoming more confident
without becoming more effective.

---

## Variations

### The cross-tool quarterly self-A/B

Once you have a stable workflow, occasionally substitute the
agentic-workflow step:
- Quarter 1: Hand-coded vs. Claude Sonnet
- Quarter 2: Hand-coded vs. Claude Opus
- Quarter 3: Hand-coded vs. GPT-5 (or whatever the relevant
  comparator is)
- Quarter 4: Hand-coded vs. your current default

This tells you whether tool changes are actually moving the
needle, beyond your subjective preference.

### The cross-task-class quarterly self-A/B

Once per year, run the self-A/B across **all** the task classes
you use AI for. This catches the trap where AI is great for some
task classes (where you keep using it) and terrible for others
(which you stopped delegating but never re-tested).

---

## What This Test Is NOT

- **Not statistically rigorous.** A paired comparison of two runs
  is not a controlled experiment. The point is honest
  self-calibration, not publishable research.
- **Not a performance review tool.** This is for your calibration.
  Share results only if you choose to.
- **Not a one-time measurement.** A single quarter's result tells
  you very little. **The trend over four quarters tells you a
  lot.**

## Why the Quarterly Cadence

- **Annual is too sparse** — you can't catch a regression in time
  to course-correct
- **Monthly is too frequent** — the overhead exceeds the value;
  task classes don't change that fast
- **Quarterly fits naturally** with team-level OKR cadences and
  with model-release cycles

## Pitfalls

- **The "wrong task" test.** Picking a task you know AI is bad at
  to "prove" AI doesn't help. The point is honest comparison, not
  confirmation of bias.
- **The "wrong workflow" test.** Comparing hand-coded against a
  sloppy agentic workflow (no spec, no context file, no review).
  Use your *best* agentic workflow, not a strawman.
- **The contaminated test.** Using insights from the hand-coded
  attempt when doing the agentic attempt. Fresh start.
- **The single-run trap.** Drawing conclusions from one quarter's
  data point. Four data points minimum before trend claims.

## Related

- [`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md)
  — the weekly journal whose felt-speedup entries you compare
  against this quarterly measured speedup
- [`../spec-templates/personal-eval-set.md`](../spec-templates/personal-eval-set.md)
  — the personal benchmark suite that pairs with this quarterly
  comparison
- [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)
  — the team-level dashboard this personal layer complements

## Provenance

Adapted from Chapter 18 of *Harnessing the Horse*, Section 18.1.
The METR study (July 2025) is referenced in the chapter. The
quarterly self-A/B protocol and the calibration delta metric are
the book's framework.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
