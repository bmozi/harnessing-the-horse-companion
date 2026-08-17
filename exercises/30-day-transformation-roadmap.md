# 30-Day Transformation Roadmap

> **Chapter:** ch19 — Team Transformation (Sections 19.1, 19.5, 19.6)
> **Last revised:** 2026-06-16
> **Use this for:** Adopting agentic development discipline at your
> team or organization. Week-by-week sequence for the Crawl stage.

The **Crawl stage delivers 60-70% of the safety benefit with
approximately 20% of the overhead.** It requires no infrastructure
changes, no new tooling beyond what Claude Code (or similar) already
provides, and no organizational restructuring.

**A team can reach the Crawl stage within a single sprint.**

This roadmap is the practical sequence for the first 30 days.

---

## Week 1 — Context Files and Hooks

**Goal:** Establish the minimum-viable discipline so that every
agent session has the context and guardrails it needs.

### Day 1–2: Context files

- [ ] Create `CLAUDE.md` (or `AGENTS.md`) at the root of your
      **three most active repositories**
- [ ] Start with the minimum four sections (see
      [`../spec-templates/claude-md-template.md`](../spec-templates/claude-md-template.md)):
  - Project Overview
  - Conventions
  - Constraints (the MUST-NOT list — six categories considered)
  - Architecture Boundaries
- [ ] Ten lines minimum. Grow as you discover what the agent
      needs to know.

> The context file does not need to be comprehensive on day one;
> it needs to **exist**.

### Day 3–4: Pre-commit hooks

Add pre-commit hooks for the three categories that catch ~80% of
common agent failures automatically:

- [ ] **Linter** appropriate to your language (ESLint, Ruff,
      golangci-lint)
- [ ] **Type checker** if the language supports it (TypeScript
      strict mode, mypy, `go vet`)
- [ ] **Secret scanner** (gitleaks, truffleHog, or detect-secrets)

These three catch style violations, type errors, and hardcoded
credentials.

### Day 5: Harness configuration (Claude Code or equivalent)

If you're using Claude Code, configure three layers:

- [ ] **Hooks configuration** — post-edit hooks that auto-fix
      lint, post-bash hooks that scan for secrets
- [ ] **Scoped rules** — rules files scoped to specific
      directories (e.g., `.claude/rules/api-routes.md` applies to
      `src/api/**`)
- [ ] **Permission policy** — default-deny with explicit
      allowlist (read, write, edit, test, lint, build,
      inspect-git) and explicit denylist (`rm -rf`, `git push to
      main`, `npm publish`, `curl | sh`). See
      [`../code-examples/claude-settings/settings.jsonc`](../code-examples/claude-settings/settings.jsonc)
      for the reference configuration.

### Week 1 outcome

Every agent session in those three repos now reads project
context, has guardrails that catch the most common failures, and
operates within a least-privilege permission boundary.

---

## Week 2 — First Pilot Task

**Goal:** Prove the Crawl stage's value on one concrete task, with
your most skeptical senior engineer as reviewer.

### Pick the task

- [ ] **Well-scoped** — single feature, single refactoring, or
      single integration
- [ ] **Non-trivial** — not a one-line fix
- [ ] **Bounded** — completable in 1–3 days of generation +
      review time
- [ ] **Visible** — the team will see the result

### Execute with full Crawl discipline

- [ ] Write a SPEC.md before the agent session (five lines
      minimum: what, what-not, success criteria) — see
      [`../spec-templates/spec-md.md`](../spec-templates/spec-md.md)
- [ ] Reference the project's CLAUDE.md from the agent session
- [ ] Use the pre-commit hooks
- [ ] **Have the most skeptical senior engineer review the
      output**

### Document the retrospective

A brief team retrospective at end of week:

- [ ] What worked
- [ ] What didn't
- [ ] What we'll change for the next pilot

---

## Week 3 — Expand and Iterate

**Goal:** Apply Crawl discipline to three more tasks across
different team members. Refine based on week 1–2 findings.

- [ ] Three tasks, distributed across at least three engineers
- [ ] Each engineer uses the same Crawl discipline
- [ ] Update the context files based on findings from weeks 1–2
- [ ] Update the rules files based on patterns you noticed
- [ ] Brief team retrospective at end of week:
  - What the agents are good at
  - What they're bad at
  - What the team wants to try next

---

## Week 4 — Baseline Metrics and Plan

**Goal:** Establish baseline metrics for measuring impact, and
plan the next phase.

### Establish baselines

These are the denominator for measuring the impact of agentic
development adoption:

- [ ] **Current deployment frequency** (per team, per week)
- [ ] **Current change failure rate** (last 30 days)
- [ ] **Current review time per PR** (median, p90)
- [ ] **Current regeneration rate** (if traceable) — see
      [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)

### Plan the next four weeks

- [ ] Which repositories will adopt context files next
- [ ] Which engineers will pilot the practices next
- [ ] What the success criteria are for **moving from Crawl to
      Walk**

---

## Crawl Stage Exit Criteria

A team is ready to advance to the Walk stage when **all four** are
true:

- [ ] Context file exists and is updated at least monthly
- [ ] Pre-commit hooks are running and **blocking** on all
      repositories
- [ ] Specifications exist for at least **80% of non-trivial
      agent-generated changes**
- [ ] The team has been practicing these three habits for at
      least **two sprints**

> The two-sprint minimum is not arbitrary — it takes approximately
> four weeks for a practice to move from "something we do because
> we were told to" to "something we do because it helps."

---

## What the Crawl Stage Does NOT Require

Resist the temptation to introduce Walk- or Run-stage practices
during the first 30 days:

- ❌ Full DESIGN.md, IMPL_NOTES.md, REVIEW.md artifacts (those
      come at Walk stage)
- ❌ Pipeline tracks (Walk)
- ❌ Graduated autonomy tiers (Walk)
- ❌ Separate metrics for agent-generated vs. human-generated
      code (Walk)
- ❌ Architectural drift scanning (Run)
- ❌ Mutation testing (Run)
- ❌ Adversarial review (Run)
- ❌ Multi-agent orchestration (Run)

> Introducing these at the Crawl stage **overwhelms the team with
> process overhead before they have experienced the productivity
> benefit that motivates compliance.**

The Crawl stage is designed to be **lightweight enough that no
engineer objects to adopting it, and productive enough that every
engineer wants to continue.**

---

## The Three Transformation Anti-Patterns

Watch for these failure modes in your transformation. Each has a
structural fix.

### Anti-pattern 1: The "Just Use AI" mandate without standards

An executive reads about AI-powered development and mandates that
all engineering teams use AI tools immediately. **No standards.
No training. No metrics.** Engineers use AI in whatever way seems
convenient, producing code of wildly varying quality with no
consistent review.

Six months later: codebase is full of dark code. Organization
blames AI rather than the absence of discipline.

**The fix:** Standards before tools. The Crawl stage takes one
sprint to establish. Mandate **context files and pre-commit
hooks** before mandating AI tool usage. The tools are used
within a minimum discipline framework.

### Anti-pattern 2: The "Ban AI" overcorrection

After an incident traced to AI-generated code — a security
vulnerability, a production outage, a data corruption —
leadership bans AI tools entirely.

The ban is counterproductive: removes legitimate productivity
benefit from engineers using tools responsibly, **and** drives
AI usage underground (shadow AI) where it operates without any
governance at all.

**The fix:** Diagnose the **process failure**, not the tool.
The incident was caused by a process that allowed AI-generated
code to reach production without adequate review. Tighten review
standards (Walk stage), add the quality gates that would have
caught the issue (architecture-as-code, adversarial validation),
and track the metrics that prove the fix is working.

### Anti-pattern 3: The "Pilot Team" that never scales

Small pilot team adopts agentic development, achieves excellent
results, writes glowing report. Organization plans to scale.
Two years later: pilot team is **still the only team** using the
practices.

The scaling failed because the pilot team's success depended on
**tacit knowledge** that was not captured in documentation. The
pilot team's senior engineer had internalized practices and
guided the team through edge cases the documentation did not
cover.

**The fix:** The pilot team's job is **not to use the practices
— it is to document them**. The context files, architecture-as-
code rules, quality gate configurations, and retrospective
findings from the pilot team become the **adoption kit for
subsequent teams**. The pilot team's senior engineer becomes the
**standards author** who maintains the practices as
organizational infrastructure.

---

## After the First 30 Days

Once Crawl exit criteria are met (typically months 2–3), proceed
to the **Walk stage** — full pipeline artifacts, pipeline tracks,
architecture-as-code. The majority of engineering organizations
should plan to **operate at the Walk stage for six months or
more** before considering the Run stage.

See [`maturity-assessment.md`](maturity-assessment.md) for the
full Crawl → Walk → Run progression with key indicators per
level.

## Related

- [`maturity-assessment.md`](maturity-assessment.md) — the
  five-level Crawl-Walk-Run model with detailed indicators
- [`expertise-traps.md`](expertise-traps.md) — the per-engineer
  traps to watch for during transformation
- [`../spec-templates/claude-md-template.md`](../spec-templates/claude-md-template.md)
  — the Crawl-stage context file template
- [`../code-examples/claude-settings/`](../code-examples/claude-settings/)
  — the Crawl-stage permission policy
- [`../spec-templates/spec-md.md`](../spec-templates/spec-md.md)
  — the spec-before-generation template
- [`../checklists/metrics-dashboard.md`](../checklists/metrics-dashboard.md)
  — the dashboard for measuring transformation impact

## Provenance

Adapted from Chapter 19 of *Harnessing the Horse*, Sections 19.1
(Crawl stage), 19.5 (The First 30 Days, in The Change Management
Playbook), and 19.6 (Common Transformation Anti-Patterns).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
