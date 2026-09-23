# Agentic Development Metrics Dashboard

> **Chapter:** ch18 — Measuring What Matters (Sections 18.1, 18.3,
> 18.5)
> **Last revised:** 2026-06-16
> **Use this for:** Specifying the dashboard for an agentic
> development team. Five metric groups, refreshed weekly, with
> agent-vs-human attribution.

The metric that best captures the value of agentic development is
**quality throughput**: the rate at which an engineering team ships
production-quality changes that move the product forward without
causing regressions.

**Raw output produces theater.** If you measure lines of code, AI
tools produce a dramatic improvement. If you measure merged,
production-quality changes per unit of calendar time, the
improvement depends entirely on the engineering discipline around
the tools.

---

## The Quality Throughput Formula

```
Quality Throughput = Deployment Frequency × (1 − Change Failure Rate)
                   ÷ (1 + Regeneration Cost Multiplier)
```

A team that deploys 20× per week with 5% failure rate and 15%
regeneration rate has **higher quality throughput** than a team that
deploys 50× per week with 20% failure rate and 40% regeneration
rate — even though the second team's raw activity metrics are
dramatically higher.

The formula matters because it exposes the trap of optimizing for
raw output at the expense of quality. Chapter 18 (Section 18.4)
treats quality throughput primarily as a lens for reading deployment
frequency, change failure rate, and regeneration rate jointly; any
composite formula like this one must publish its weights and
assumptions explicitly.

---

## The Five Metric Groups

All metrics refresh **weekly** with **12-week trend lines minimum**.
All delivery and quality metrics split **agent-generated vs.
human-generated** (see the Attribution section below).

### Group 1: Delivery Metrics (DORA, agentic-extended)

| Metric | Measurement | Notes |
| --- | --- | --- |
| **Deployment Frequency** | Deployments per day/week, split by source | Agentic: higher is expected if discipline holds |
| **Lead Time for Changes** | Time from first commit to production | In agentic dev, this is **review-bottleneck-dominated**, not coding-bottleneck. A team whose agentic lead time is *longer* than its traditional lead time has a review bottleneck. |
| **Change Failure Rate** | % of deployments causing a failure | Must match or beat human baseline before adopting Run-stage practices |
| **Mean Time to Restore** | Time from failure detection to restoration | Agentic dev does not change MTTR's meaning |

### Group 2: Quality Metrics

| Metric | Measurement | Healthy threshold |
| --- | --- | --- |
| **Regeneration Rate** | % of agent-generated changes requiring more than one generation cycle before passing review | Uncalibrated starting bands: aim **< 20%**; investigate **40–60%**; **> 60%** prompts a pause in expansion and diagnosis of failed cycles |
| **Review Findings by Category** | Per-PR finding count split by: security / correctness / style / architecture | Trends matter more than absolute numbers |
| **Test Coverage on New Code** | Coverage % on agent-generated vs. human-generated changes | Agent code often has lower edge-case coverage; track the gap |
| **Post-Merge Defect Rate** | Defects per merged PR within 30 days of deployment | Trend by source (agent vs. human) |

### Group 3: Cost Metrics

| Metric | Measurement | Use |
| --- | --- | --- |
| **Tokens per Merged PR** | Total agent tokens / merged PRs in window | Rising trend = generation thrashing; investigate |
| **Cost per Quality-Adjusted Deployment** | Total agent cost / (deployments × (1 − CFR)) | The dollar number that ties cost to value |
| **Review Hours per Agent-Generated PR** | Median and p90 reviewer time | Rising trend = reviewer fatigue or scope creep |
| **Token Budget Utilization** | Daily/weekly budget consumed | Hitting cap = thrashing or under-budgeted |

### Group 4: Team Health Metrics

| Metric | Measurement | Watch for |
| --- | --- | --- |
| **Review Turnaround Time** | Median + p90 time from PR open to first review | Rising = bottleneck |
| **Review Queue Depth** | Number of PRs waiting for first review | Growing queue = generation outpacing review |
| **Reviewer Concentration** | % of reviews done by single most-active reviewer | > 40% = bus factor risk |
| **Specification-to-First-Generation Time** | Time from SPEC.md approval to first agent session | Long delay = generation is the gate, not spec |

### Group 5: Maturity Indicators

(See [`../exercises/maturity-assessment.md`](../exercises/maturity-assessment.md))

- [ ] All four pipeline artifacts produced consistently
      (SPEC, DESIGN, IMPL_NOTES, REVIEW)
- [ ] Quality gates automated in CI/CD
- [ ] Context files (CLAUDE.md / AGENTS.md) updated within last
      month
- [ ] Metrics drive process improvement (Level 4) — not just
      tracked

---

## The Companion Metric: Regeneration Rate

The four DORA metrics were designed for an era where code was
written once and reviewed once. **Agentic development introduces a
failure mode the original four do not capture: regeneration.**
Regeneration rate is the book's own pre-merge metric — distinct
from DORA's 2025 fifth metric, a post-merge rework measure:
regeneration is waste before the merge, DORA's metric is waste
after it.

An agent generates code, the review finds issues, the agent
regenerates, the review finds different issues, the agent
regenerates again. Each iteration consumes:

- Reviewer time
- Agent tokens
- Calendar time

**Diagnostic signals:**

| Regeneration Rate | Diagnosis | Intervention |
| --- | --- | --- |
| **< 20%** | Initial aim, not proof of health | Check acceptance rigor and escaped defects |
| **20–40%** | Local investigation band | Inspect comparable work and trend |
| **40–60%** | Possible crawl investigation band, not inherently acceptable | Inspect failed cycles and consequences |
| **> 60%** | Pause expansion and investigate | Diagnose the cause before choosing a remedy |

These are uncalibrated starting bands, not established healthy rates. A high
regeneration rate raises several hypotheses:

1. **Specification underspecified** (Standard 1 failure)
2. **Agent's context file insufficient** (Standard 11 failure)
3. **Quality gates catching issues too late** (Standard 6 failure)

Task difficulty, tool failures, changed requirements, and review criteria
can also affect the rate. Inspect rejected changes to distinguish causes;
the rate alone cannot identify one.

---

## Attribution: Separating Human and AI Contributions

The goal of attribution is **calibration, not blame**. Agent-
generated code and human-generated code fail in different ways, at
different rates, and for different reasons. Aggregating them into
a single metric set obscures the signal each provides.

### Attribution mechanisms

- [ ] **Commit metadata** — agent sessions tag commits with
      session identifiers, agent model, and specification reference
      in a structured footer
- [ ] **Branch naming convention** — agent-generated branches
      follow `agent/[task-id]/[description]`; CI pipelines key on
      this convention to route through extra gates
- [ ] **Review metadata** — the REVIEW.md captures whether the
      change was agent-generated or human-authored

### Separate dashboards, not separate standards

Both agent-generated and human-generated code must pass the **same
quality gates**. Attribution does not relax standards for the
agent. It enables targeted intervention: if agent-generated code
has a 3× higher rate of missing edge-case tests, add a specific
edge-case-coverage gate **without** burdening human-generated
changes that do not exhibit the pattern.

---

## The Personal Calibration Layer

The team-level dashboard tells you whether the **system** is
working. The personal calibration layer tells each engineer
whether **they** are working effectively within the system. See:

- [`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md)
  — the weekly journal template
- [`../spec-templates/personal-eval-set.md`](../spec-templates/personal-eval-set.md)
  — the personal benchmark suite
- [`../exercises/quarterly-self-ab-test.md`](../exercises/quarterly-self-ab-test.md)
  — the quarterly hand-coded vs. agentic comparison

The METR study (July 2025) found experienced developers were **19%
slower with AI tools while feeling 20% faster** — a 40-percentage-
point calibration gap. The personal layer is what catches this gap
for individual engineers.

## What This Dashboard Replaces

This dashboard **replaces**, not supplements, the following common
but misleading metrics:

- Lines of code (without quality denominator)
- Commits per day (without merge or quality context)
- Tokens consumed (without merged PR denominator)
- Velocity points (which agentic dev distorts beyond recognition)

These metrics should appear in the dashboard **only** as
denominators — `commits per successful deployment`, `lines per
merged PR` — never as standalone productivity measures.

## Related

- [`../exercises/maturity-assessment.md`](../exercises/maturity-assessment.md)
  — the maturity-level indicators that this dashboard tracks
- [`../spec-templates/calibration-journal.md`](../spec-templates/calibration-journal.md)
  — the personal-level companion to this team-level dashboard
- [`../spec-templates/personal-eval-set.md`](../spec-templates/personal-eval-set.md)
  — baseline capability measurement that pairs with this dashboard

## Provenance

Adapted from Chapter 18 of *Harnessing the Horse*, Sections 18.1
through 18.5. The four DORA metrics are from Forsgren, Humble, and
Kim, *Accelerate* (IT Revolution, 2018). Regeneration Rate, the
quality throughput lens, and the attribution discipline are the
book's framework.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.

## Interpretation boundary

Capture a comparable pre-adoption baseline before the pilot. Record mixed and unknown authorship explicitly. Execution coverage does not measure assertion quality. Read failure, regeneration, review time and delivered value jointly: lower failure rates alone do not establish that one team outperforms another. Keep modeled labor, elapsed CI latency and observed outcomes separate.
