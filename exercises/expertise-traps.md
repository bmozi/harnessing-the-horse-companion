# Expertise Traps by Level

> **Chapter:** ch19 — Team Transformation (Section 19.1, "Expertise
> Levels and Their Traps")
> **Last revised:** 2026-06-16
> **Use this for:** Each engineer on your team operates at a
> different expertise level. Each level has a **distinct trap** that
> the others don't face. Recognizing your trap is more valuable
> than skipping to the next level's practices.

The crawl-walk-run model (see
[`maturity-assessment.md`](maturity-assessment.md)) describes the
**team's journey**. But within each team, individual engineers
operate at different expertise levels.

**A team at the Crawl stage will have engineers at all four
levels.** What changes as the team progresses is the
organizational infrastructure that supports each level.

---

## Beginner: Task-Scale Operation

### How they work
Delegates individual tasks to agents — a function, a test, a
configuration file.

### Critical discipline
**Reading every diff line by line.**

### The trap: "It looks right"

The agent will produce code that:
- Looks correct
- Compiles
- Often passes tests

**Code that looks right and code that is right are not the same
thing.** The gap is where dark code enters the codebase.

### Countermeasure

Build a **personal evaluation set** of ten tasks where you know
the correct answer. Run each through the agent. Compare the
output to your known-good solution.

See [`../spec-templates/personal-eval-set.md`](../spec-templates/personal-eval-set.md).

The eval set teaches you where the agent is **reliable** and
where it is **not** — calibration through direct observation
rather than assumption.

### Self-check questions
- [ ] Have I read this entire diff, not just the parts that
      changed obviously?
- [ ] If I had to explain why each line is correct, could I?
- [ ] Does the test suite actually verify the requirement, or
      does it just exercise the code?
- [ ] Have I tested this against my personal eval set in the
      last month?

---

## Mid-Level: Feature-Scale Operation

### How they work
Delegates **features** — multi-file changes that span several
modules.

### Critical discipline
**Specification files: writing SPEC.md before generation, not
after.**

### The trap: Tool-of-the-week churn

Adopting a new agent, a new MCP server, a new prompt template
every week. **Never building the muscle memory** that makes any
single workflow productive.

### Countermeasure

Pick **one agent workflow**, **one set of context files**, and
**one specification template**.

Use them consistently for **at least one sprint** before
evaluating alternatives.

**Consistency is more valuable than optimization at this level.**

### Track personal metrics

- Cycle time from spec to merged PR
- Defect rate in review
- Regeneration iterations

See [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)
for definitions, and
[`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md)
for personal weekly tracking.

### Self-check questions
- [ ] Have I changed my agent workflow in the last sprint?
- [ ] Did I write the SPEC.md before opening the agent session,
      or did I "specify by example" through the conversation?
- [ ] Are my regeneration iterations trending up or down?
- [ ] If a teammate asked me to teach them my workflow, could I?

---

## Senior: Multi-Agent Patterns and Mentorship

### How they work

Operates with multi-agent patterns:
- Adversarial validation
- Parallel generation on isolated branches
- Architecture-as-code rules that constrain agent behavior at
  CI level

### Critical responsibility
**Mentoring mid-level engineers in the practices.**

### The trap: The METR gap

Experienced developers who **feel 20% faster while measuring 19%
slower** (METR study, July 2025).

The trap is **most dangerous at the senior level** precisely
because expertise creates confidence, and **confidence resists
calibration**.

### Countermeasure

The **quarterly self-A/B** described in Chapter 18. Measure, do
not estimate.

See [`quarterly-self-ab-test.md`](quarterly-self-ab-test.md).

The **honest journal** (three lines weekly: what saved time,
what cost time, what to try differently) is the senior
engineer's defense against the comfortable assumption that their
expertise makes them immune to the productivity paradox.

See [`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md).

### Self-check questions
- [ ] What was my measured speedup last quarter? (Not felt
      speedup — measured.)
- [ ] Have I done a quarterly self-A/B in the last 90 days?
- [ ] Am I writing the honest journal weekly, or am I making
      excuses for skipping it?
- [ ] When was the last time my honest-journal "cost me time"
      entry was a substantial loss, not a minor one? (If you can't
      remember, you're not being honest.)

---

## Principal: Organizational Standards and Institutional Judgment

### How they work

Authors organizational conventions:
- The context files every project uses
- The architecture-as-code rules every CI pipeline enforces
- The quality gate configurations every review evaluates
- The evaluation harnesses teams use to assess agent
  effectiveness

### The trap: The n=1 generalization

**"It worked on my project, therefore it works everywhere."**

A principal engineer's project is typically:
- Well-typed
- Well-tested
- Well-documented

This is **the ideal substrate for agentic development**.
Generalizing practices from this substrate to projects without
types, tests, or documentation produces recommendations that
**fail on contact with reality**.

### Countermeasure

**Test every standard on the team's weakest codebase, not its
strongest one.**

If the practice does not work on the codebase with the worst
test coverage and the least documentation, it is **not ready to
be a standard**.

### Self-check questions
- [ ] When I propose a standard, have I tested it on the worst
      codebase in the org, not just my own?
- [ ] Have I asked the engineers on the legacy / under-resourced
      projects whether this standard helps them?
- [ ] Is the standard light enough that adopting it doesn't
      require a separate engineering investment first?
- [ ] If the standard requires a substrate the team doesn't have
      (types, tests, docs), have I documented that prerequisite
      explicitly, instead of pretending the standard "just
      works"?

---

## The Four Levels Map to Crawl-Walk-Run

A team at any stage will have engineers at all four levels. What
changes is the **organizational infrastructure** that supports
each level.

| Level | Crawl-stage support | Walk-stage support | Run-stage support |
| --- | --- | --- | --- |
| **Beginner** | Context files + pre-commit hooks | + spec templates | + adversarial review |
| **Mid-level** | Same + spec habit | + spec templates + pipeline tracks | + multi-agent patterns |
| **Senior** | Same + mentoring | + standards authorship | + multi-agent orchestration |
| **Principal** | Authors the standards | Refines on team's worst codebase | Designs evaluation harnesses |

The **principal engineer operates across stages**, authoring the
standards that define each one.

---

## Why "Recognize Your Trap" Matters More Than "Skip Levels"

Engineers often want to jump to higher levels of practice. The
attraction is understandable — multi-agent patterns, architecture-
as-code, adversarial validation all sound more sophisticated than
"read every diff."

But the **trap at each level only becomes visible once you're
operating at that level**. A beginner skipping to multi-agent
patterns will still fall into the "it looks right" trap on every
generated diff — the trap they would have learned to handle at
the beginner level.

**The disciplines compound.** A senior engineer who skipped the
mid-level focus on consistency may produce excellent multi-agent
patterns but lose them to tool-of-the-week churn six months later.

---

## Application: Team Composition Awareness

If you're leading a team or a transformation, **audit your team's
composition by level**:

- [ ] How many beginners do you have? They need context files,
      hooks, and direct mentorship on reading diffs.
- [ ] How many mid-level? They need spec templates, workflow
      consistency, and personal metrics.
- [ ] How many seniors? They need the quarterly self-A/B and the
      honest journal — and they need to be mentoring.
- [ ] How many principals? They need to be testing on the worst
      codebase, not the best.

A team with too many beginners and no senior mentorship will
stall at the Crawl stage. A team of seniors with no principal
standards-authorship will produce inconsistent practices across
projects.

The traps are different. The countermeasures are different. The
infrastructure required is different.

## Related

- [`maturity-assessment.md`](maturity-assessment.md) — the team-
  level Crawl-Walk-Run model that pairs with these per-engineer
  levels
- [`30-day-transformation-roadmap.md`](30-day-transformation-roadmap.md)
  — the team-level Crawl-stage adoption sequence
- [`quarterly-self-ab-test.md`](quarterly-self-ab-test.md) — the
  senior engineer's countermeasure for the METR gap
- [`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md)
  — the senior engineer's weekly discipline
- [`../spec-templates/personal-eval-set.md`](../spec-templates/personal-eval-set.md)
  — the beginner's "it looks right" countermeasure

## Provenance

Adapted from Chapter 19 of *Harnessing the Horse*, Section 19.1
(Expertise Levels and Their Traps). The four-level framework and
the trap-per-level model are the book's contribution.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
