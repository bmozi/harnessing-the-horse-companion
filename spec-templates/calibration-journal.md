# Calibration Journal Template

> **Chapter:** ch18 — Measuring What Matters (Section 18.1, "The
> Honest Journal")
> **Last revised:** 2026-06-16
> **Use this for:** Weekly five-minute honest self-calibration to
> close the gap between **felt** productivity and **measured**
> productivity.

The METR study (July 2025) — a randomized controlled trial of
experienced open-source developers — found that developers using
AI tools were **19% slower** while self-reporting that they felt
**20% faster**. The 40-percentage-point gap between felt and
measured productivity was **largest among the most experienced
developers** in their own codebases.

**The journal's value is not in the individual entries; it is in
the pattern that emerges across months.** Engineers who maintain
the journal consistently report that their initial estimates of
time saved were 2–3× too optimistic — and that recognizing the gap
led to better task selection and better specifications, which
eventually made the optimistic estimates accurate.

The template takes **five minutes per week**.

---

## The Weekly Template

```markdown
# Calibration Journal — Week of [YYYY-MM-DD]

## What AI saved me time on this week
[One concrete task. Roughly how much time saved.

NOT "everything" — one specific, named task.

Example: "ESLint config refactor for the api/ package — would have
taken ~2 hours hand-coded; agent did it in 30 minutes, including
the time I spent reviewing. Saved ~1.5 hours."]

## What AI cost me time on this week
[One concrete task. Why it backfired in retrospect.

NOT "nothing" — if every week is a win, you are not calibrating.

Example: "Tried to use agent for the migration script. Spent 90
minutes reviewing 3 attempts that each had subtle off-by-one
errors. Would have taken 45 minutes hand-coded. Lost ~45 minutes.
In retrospect: should have written the spec more carefully — I
didn't specify the index boundary clearly."]

## Pattern to try differently next week
[ONE specific change to your practice.

NOT a vague aspiration — a concrete adjustment you will make on
the next task.

Example: "For migration / data-shape work next week, write the
index/boundary conditions as binary acceptance criteria BEFORE
opening the agent session, not after seeing the agent's first
attempt."]

## Weekly metrics rollup

| Metric | This week |
| --- | --- |
| Agent-driven PRs merged | [N] |
| Hand-authored PRs merged | [N] |
| Defects in agent-authored code (post-merge, traced this week) | [N] |
| Net-positive tasks (agent helped) | [N] |
| Net-neutral tasks | [N] |
| Net-negative tasks (agent cost time) | [N] |
| Felt speedup this week (gut estimate, %) | [N]% |
| Calibration delta vs. last quarterly self-A/B | [N] pp |
```

---

## The Calibration Delta

The gap between **felt speedup** and **measured speedup** is a
named metric worth tracking. If you feel 30% faster but measure
10% faster, your **calibration delta is 20 percentage points**.

### The goal is NOT zero

Some imprecision in self-assessment is normal. The goal is a
**stable delta** that you understand and can account for.

### A growing calibration delta is a warning

You are becoming **more confident without becoming more
effective** — which is the METR pattern applied to a single
engineer.

### What stability looks like over a year

| Quarter | Felt speedup | Measured speedup | Calibration delta |
| --- | --- | --- | --- |
| Q1 | 40% | 5% | 35 pp ⚠️ |
| Q2 | 30% | 12% | 18 pp |
| Q3 | 22% | 18% | 4 pp ✓ |
| Q4 | 20% | 19% | 1 pp ✓ |

The journal's value is the convergence pattern, not any single
entry.

---

## Why the Three Sections Matter

### "What AI saved me time on"

Forces you to **specifically attribute** time savings to a concrete
task. "AI helps with everything" is the wrong answer. If you can't
name one task, you didn't save time — you felt like you did.

### "What AI cost me time on"

The hardest entry to write. If every week is a win, you are not
calibrating. **The journal's value depends on this section being
non-empty.** If you have to invent something to fill it in some
weeks, you are over-attributing wins.

Common patterns that legitimately go here:

- Time spent on agent attempts that you ultimately threw away
- Time spent debugging code the agent wrote that you didn't
  understand
- Time spent re-doing work because the agent's first answer was
  plausible but wrong
- Time spent fixing the agent's edge-case gaps that you would not
  have introduced

### "Pattern to try differently"

Concrete adjustment. Not "I should specify better" — too vague.
Instead: "For migration work, write boundary conditions as binary
criteria BEFORE the session." That is something you will
**actually do differently** on the next migration task.

---

## Defect Attribution Discipline

For teams that track production incidents, **trace each bug to its
source**:

- [ ] Was the code agent-generated or hand-authored?
- [ ] Was the spec underspecified or the review insufficient?

**Defect attribution is not blame — it is calibration.** If 80%
of agent-generated defects trace to underspecified specs, the
intervention is specification quality, not generation quality.

---

## How to Sustain the Practice

- Pick a recurring time slot (Friday afternoons work well — the
  week is fresh in memory, you have time to reflect, and the entry
  becomes a clean handoff to the weekend)
- Keep entries short. Five minutes per week, not thirty.
- Store the journal where you'll see it. A `.journal/` folder in
  your home directory, a Notion page, a Markdown file in a
  personal repo — whatever you'll actually open.
- Don't backfill. If you miss a week, write "skipped" and move on.
  The pattern across months is what matters; one missing week is
  not a problem.

## What This Journal Is NOT

- **Not a performance review tool.** This is for *your* calibration.
  It should never be shared with a manager unless you explicitly
  choose to.
- **Not a productivity-tracking system.** The metrics are for
  trend-spotting, not optimization.
- **Not a record of your wins.** The losses section is more
  important than the wins section.

## Related

- [`personal-eval-set.md`](personal-eval-set.md) — the baseline
  capability benchmark that pairs with this journal
- [`../exercises/quarterly-self-ab-test.md`](../exercises/quarterly-self-ab-test.md)
  — the quarterly hand-coded vs. agentic comparison that produces
  your measured speedup
- [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)
  — the team-level dashboard this personal layer complements

## Provenance

Adapted from Chapter 18 of *Harnessing the Horse*, Section 18.1.
The journal template and the calibration delta metric are the
book's framework for personal-level calibration.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
