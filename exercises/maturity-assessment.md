# Agentic Development Maturity Assessment

> **Chapter:** ch10 — Compounding Practices (Section 10.3, "The
> Maturity Model: Crawl, Walk, Run")
> **Last revised:** 2026-06-16
> **Use this for:** Honest self-assessment of where your team is today
> in adopting agentic development discipline — and the path to the
> next level.

The maturity model is **not a judgment** — it is a map. Every team
starts somewhere. The goal is not to be at Level 5 tomorrow; the goal
is to know where you are today and have a clear path to the next
level.

Each level builds on the one below it. **Skipping levels is possible
but usually results in backsliding** because the foundational habits
are not established.

---

## How to Use This Assessment

1. Answer the **Key Indicators** questions honestly for your team
   today.
2. Find the level where you can answer "yes" to **all** key
   indicators.
3. That is your current level. Read the **risk profile** for that
   level to understand what is at stake.
4. Read the next level's key indicators and the **advancement
   trigger** — that is your path forward.

If you can answer "yes" to all key indicators of multiple levels, you
may be straddling levels. The accurate read is your *lowest*
unsatisfied level.

---

## Level 1 — Ad Hoc

Agents are used for individual tasks with no process. Prompts are
improvised. Reviews are informal. No artifacts are produced. Each
session starts from zero.

### Key Indicators (you are here if YES to all)

- [ ] No `SPEC.md` or `AGENTS.md` consistently
- [ ] No consistent review process
- [ ] Defects discovered in production with no preventive trace
- [ ] No metrics tracked
- [ ] The team uses AI tools but has not adopted AI discipline

### Risk Profile

- High technical debt accumulation
- Security vulnerabilities undetected until penetration testing or
  production incident
- Architecture eroding without visibility
- Individual productivity up, team productivity uncertain

---

## Level 2 — Repeatable

Basic process in place. `SPEC.md` exists for most changes. Review
happens before merge. `AGENTS.md` provides context. But the process is
inconsistent — some engineers follow it, some do not. No measurement.

### Key Indicators

- [ ] `SPEC.md` exists but quality varies
- [ ] Reviews happen but thoroughness varies
- [ ] `AGENTS.md` exists but is stale
- [ ] No metrics tracked
- [ ] The team has adopted some practices but has not standardized
      them

### Advancement Trigger

When the team recognizes that **inconsistent process produces
inconsistent results** and commits to standardization.

---

## Level 3 — Defined

The full pipeline is documented and consistently followed. All
artifacts (`SPEC.md`, `DESIGN.md`, `IMPL_NOTES.md`, `REVIEW.md`) are
produced for every change. Quality gates are automated. The team
tracks metrics but does not yet optimize based on them.

### Key Indicators

- [ ] All four pipeline artifacts produced consistently
- [ ] Quality gates automated in CI/CD
- [ ] `AGENTS.md` current (updated as part of PR workflow)
- [ ] Metrics tracked (defect density, coverage, session regeneration rate)
- [ ] Team retrospectives include agent-related topics

### Advancement Trigger

When the team has enough data to identify patterns and starts using
metrics to **drive process improvements**.

---

## Level 4 — Measured

The team uses metrics to optimize. Session regeneration rates drive prompt
improvement. Defect patterns drive review checklist updates. DORA
metrics are tracked **separately** for agent-generated and
human-generated code. The learning loop is active — retrospective
findings are systematically incorporated into standards and context
files.

### Key Indicators

- [ ] Metrics drive process improvement (not just tracked)
- [ ] Declining defect rates over time (measured, not asserted)
- [ ] DORA metrics for agent-generated code match or exceed
      human-generated code
- [ ] Prompt library evolves based on data
- [ ] Graduated autonomy in use — low-risk changes flow through
      lighter verification, high-risk changes receive full scrutiny

### Advancement Trigger

When the team's agent-generated code quality is consistently
indistinguishable from senior engineer output, and the team is ready
to invest in advanced orchestration.

---

## Level 5 — Optimizing

Agentic development is a competitive advantage. Multi-agent
orchestration coordinates complex work. Architectural drift is
detected automatically with fitness functions. Security is proactive
— the threat model is updated as part of the generation process, not
as a periodic audit. The team continuously improves its standards
based on outcome data. New engineers are productive within days, not
months, because the meta-layer (context files, ADRs, pattern
libraries, review checklists) is robust enough to substitute for
institutional knowledge.

### Key Indicators

- [ ] Multi-agent orchestration in production
- [ ] Automated drift detection (architecture fitness functions)
- [ ] Post-merge monitoring with auto-rollback
- [ ] Specialized sub-agents for domain-specific validation
- [ ] Continuous standard evolution (standards are updated based on
      data, not opinion)
- [ ] Agent-generated code quality indistinguishable from senior
      engineer output

### Reality check

Level 5 is **aspirational and ongoing**. It is not a destination but
a continuously-receding horizon of improvement.

---

## The 30-Day Adoption Path (Level 1/2 → Level 3)

Most teams start at Level 1 or Level 2. Level 3 is achievable within
**30 days** using the standards in this book.

| Week | Milestone |
| --- | --- |
| **Week 1** | Establish the context file (`AGENTS.md` / `CLAUDE.md`). Require `SPEC.md` for all non-trivial changes. Implement a basic review checklist. |
| **Week 2** | Add `DESIGN.md` for multi-file changes. Implement scope constraints (400 lines, 60 minutes). Set up automated quality gates in CI. |
| **Week 3** | Introduce the adversarial validator pattern. Require `REVIEW.md`. Start tracking session regeneration rate. |
| **Week 4** | Conduct the first retrospective on agent-related practices. Update `AGENTS.md` with all learnings from the first three weeks. Establish the rhythm of closing the loop after every session. |

## The 90-Day Path to Level 4

Level 4 requires **90 days of consistent practice and measurement**.
The data collected during Level 3 provides the baseline; Level 4 is
the practice of acting on that data.

## What This Assessment Is NOT

- Not a tool to grade teams against each other
- Not a checklist to game (every "yes" must be honestly evidenced —
  if you're not sure, the answer is no)
- Not a destination — Level 5 is a horizon, not a finish line
- Not the only path — teams will sometimes have particular strengths
  at higher levels and gaps at lower levels; trust the *lowest
  unsatisfied level* as the honest read

## Related

- `../checklists/definition-of-done.md` — DN1–DN7 are the operational
  evidence of Level 3 discipline
- `../spec-templates/spec-md.md`, `design-md.md`, `impl-notes-md.md`,
  `review-md.md` — the four pipeline artifacts that distinguish
  Level 2 from Level 3
- `../spec-templates/claude-md-template.md` — the context file whose
  freshness is a key Level 2/3 indicator
- `case-study-analysis-framework.md` — uses this assessment in
  Section 2 (Harness Framework Mapping)

## Provenance

Adapted from Chapter 10 of *Harnessing the Horse*, Section 10.3. The
five levels, key indicators, risk profiles, and adoption path are the
book's framework.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
