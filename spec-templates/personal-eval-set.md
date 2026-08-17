# Personal Eval Set Template

> **Chapter:** ch18 — Measuring What Matters (Section 18.1, "The
> Personal Eval Set")
> **Last revised:** 2026-06-16
> **Use this for:** Building a personal benchmark suite of 5–20
> representative tasks you can re-run on every new model release,
> every new tool, and every quarterly calibration cycle.

The quarterly self-A/B and the calibration journal capture **trends**.
The personal eval set captures **baseline capability** — yours and
the tools'.

> The eval set is the only continuity that lets you say with
> evidence — not vibes — whether the practice is improving over
> time.

The hour per quarter you invest in personal evals pays back across
years — and it teaches you more about your workflow's actual
strengths and weaknesses than any vendor benchmark.

---

## The Directory Structure

Create a directory in a personal repo or your home directory.
Each task is a folder.

```
evals/personal/
├── README.md                              # Index of tasks and your scoring conventions
├── 01-auth-endpoint/
│   ├── prompt.md                          # The task specification
│   ├── success.md                         # 1–5 scoring rubric with criteria per level
│   ├── gold/                              # Optional: a reference implementation
│   │   ├── handler.py
│   │   └── handler_test.py
│   └── runs/
│       ├── 2026-01-15_claude-sonnet-4-6/  # Timestamped run with model name
│       │   ├── output/
│       │   ├── wall_time.txt
│       │   ├── score.txt                  # 1–5
│       │   └── notes.md                   # What worked, what didn't
│       └── 2026-04-20_claude-opus-4-7/
│           └── ...
├── 02-refactor-monolith/
│   └── ...
└── 03-fix-flaky-test/
    └── ...
```

---

## The Task Specification (`prompt.md`)

Each task is a **representative example** of the kind of work you
actually do. Not artificial benchmarks; not LeetCode problems;
your real work.

The prompt should be specific enough that:

- You can grade the output unambiguously
- The agent has a clear target
- The same prompt can be run against multiple models / tools and
  results compared

### Example: Web engineer's "Add Authenticated Endpoint" task

```markdown
# Task: Add Authenticated POST /api/items Endpoint

## Context
FastAPI app at the standard location. Existing patterns:
- Auth middleware in `app/middleware/auth.py`
- Pydantic models in `app/schemas/`
- Repository pattern in `app/repositories/`
- Tests use pytest with the existing `client` fixture

## Requirements
- Add `POST /api/items` endpoint that creates a new item
- Use the existing auth middleware (require auth)
- Use Pydantic models for request and response
- Persist via the existing repository pattern (add `create_item`
  if needed)
- Return 401 if auth is missing or invalid
- Return 422 if the request body is invalid
- Add four tests:
  - Happy path (creates item, returns 200 + item)
  - Missing auth (returns 401)
  - Invalid auth (returns 401)
  - Invalid body (returns 422)

## Constraints
- Do not modify existing endpoints or models
- Follow the existing code style
- The diff should be clean (no extraneous changes)
```

---

## The Scoring Rubric (`success.md`)

Define **specific criteria at each level**. Without specific
criteria, scoring drifts over time and the eval set loses
continuity.

### Example rubric for the auth endpoint task

```markdown
# Scoring: Add Authenticated POST /api/items Endpoint

## Score 5 (Excellent)
- All four tests pass
- Test coverage on new code ≥ 90%
- Diff is clean: no extraneous changes, no formatting noise
- Wall time < 30 minutes
- IMPL_NOTES.md or equivalent captures any tradeoffs

## Score 4 (Good)
- All four tests pass
- Test coverage ≥ 85%
- Diff has minor style issues or 1–2 extraneous changes
- Wall time < 45 minutes

## Score 3 (Acceptable with caveats)
- Tests pass after I manually fix something
- Some scope drift (unexpected file changes)
- Wall time < 60 minutes

## Score 2 (Poor)
- Tests fail and require non-trivial manual fix
- Significant scope drift
- Wall time > 60 minutes

## Score 1 (Unusable)
- Output doesn't compile, OR
- Output takes a fundamentally wrong approach (e.g., creates new
  auth middleware instead of using existing)
- I would not have used this even as a starting point
```

---

## The Run Discipline

### When to run the eval set

- **Monthly** at minimum — a routine cadence catches model
  regressions and drift
- **Before adopting a new model** — produce evidence, not vibes,
  about whether to switch
- **Before recommending a new tool** to your team — the eval is
  your evidence base
- **At each quarterly calibration cycle** — the eval results feed
  into your quarterly self-A/B

### What to record per run

In `runs/[YYYY-MM-DD]_[model-or-tool]/`:

- [ ] **Wall time** — total time from prompt-sent to output-final
- [ ] **Score** — 1–5 per the rubric
- [ ] **Notes** — what worked, what didn't, any surprises
- [ ] **Output** — the actual generated code (so you can re-grade
      later if your rubric evolves)

### What to NOT do

- **Don't grade your own runs the same day.** Wait at least a few
  hours. Same-day grading is biased by the experience of running
  the task; next-day grading is biased only by the output itself.
- **Don't change the prompt mid-quarter.** If you change the
  prompt, you've changed the test; comparisons across runs become
  meaningless. Version the prompt and keep old versions for
  historical comparison.
- **Don't grade against your gold standard for style.** Grade
  against the rubric. The gold is for understanding what "correct"
  looks like; it is not the only valid answer.

---

## The Trend Line

Plot wall time and score per task across runs:

```
Task: 01-auth-endpoint

| Date       | Model              | Wall time | Score |
| ---        | ---                | ---       | ---   |
| 2025-10-15 | claude-sonnet-4-5  | 38m       | 3     |
| 2026-01-15 | claude-sonnet-4-6  | 28m       | 4     |
| 2026-04-20 | claude-opus-4-7    | 22m       | 5     |
```

The trend shows you:

- Which task classes are getting easier (models are improving)
- Which task classes are stagnant (the task may be at the edge of
  current capability)
- Which task classes are regressing (model swap may be wrong, or
  your codebase's complexity has grown)

---

## How to Pick Your 5–20 Tasks

The set should be **representative**, not exhaustive. Include:

- **2–3 task classes you do weekly** (your bread and butter)
- **2–3 task classes you find difficult** (where you want to know
  if AI helps)
- **1–2 task classes that recently surprised you** (a recent
  win or loss is fresh material for the eval)
- **1–2 "stretch" task classes** that you don't currently delegate
  to AI but might (good leading indicator of capability growth)

**Avoid:**

- Trivial tasks that any model passes easily (no information)
- Task classes you'll never actually do (no relevance)
- Tasks so large the score reflects time-budget more than
  capability

---

## When to Add or Retire Tasks

### Add a new task when

- A new task class becomes a regular part of your work
- You want to track a specific capability you suspect is improving
  or regressing
- A recent surprise (good or bad) is worth instrumenting

### Retire a task when

- It's been at score 5 for three consecutive runs (you've learned
  what you can; the task is solved)
- It's no longer representative of your work
- The rubric has drifted enough that comparisons across versions
  are meaningless

---

## Related

- [`calibration-journal.md`](calibration-journal.md) — the weekly
  journal that complements this monthly/quarterly benchmark
- [`../exercises/quarterly-self-ab-test.md`](../exercises/quarterly-self-ab-test.md)
  — the quarterly hand-coded vs. agentic comparison that uses your
  eval tasks
- [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)
  — the team-level dashboard this personal layer complements

## Provenance

Adapted from Chapter 18 of *Harnessing the Horse*, Section 18.1.
The personal eval set structure and the scoring rubric format are
the book's framework for individual-engineer baseline capability
measurement.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
