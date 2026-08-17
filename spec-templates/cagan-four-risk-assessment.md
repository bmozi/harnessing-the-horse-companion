# Four-Risk Evidence Contract

> **Chapter:** ch05 - Discovery and Planning (Section 5.1, "Assessing
> the Risk Before Writing the Spec: Cagan's Four Risks")
> **Last revised:** 2026-08-16
> **Use this for:** Deciding whether a complex feature has enough evidence to
> enter specification and generation.

Marty Cagan's four product risks ask whether a solution is valuable, usable,
feasible, and viable. Those questions are widely known. The distinctive value
of this companion is turning them into an **evidence contract** that controls
what the team may generate next.

For each risk, this artifact requires a falsifiable claim, sourced evidence,
an evidence grade, a next test with a threshold, a named owner, engineering
constraints, and a gate disposition. The result is a decision instrument, not
a four-box brainstorming exercise.

## When to Use It

Use this assessment when a feature introduces a new user capability, crosses
module or organizational boundaries, changes a data model, creates material
operational cost, or depends on assumptions that would be expensive to discover
after implementation.

Do not require it for a bounded defect whose desired behavior is already proven,
a mechanical dependency update with established gates, or a local refactor with
no product decision. Use the SPEC and normal verification path instead.

## Rules of Evidence

### Evidence grades

| Grade | Meaning | What it can support |
| --- | --- | --- |
| E0 - Assertion | Opinion, intuition, model output, or an unsourced claim | A hypothesis only; never closes a material risk |
| E1 - Signal | A small number of interviews, tickets, examples, or an exploratory spike | A reason to test, not a reason to scale |
| E2 - Observed | Repeatable behavior in a prototype, representative workflow, or multiple independent sources | A bounded decision with explicit limitations |
| E3 - Measured | Quantified evidence from a representative sample or production-like environment | A release-relevant decision within the measured population |
| E4 - Production | Sustained real-world behavior with monitored outcomes | Continued operation while conditions remain comparable |

An AI-generated analysis is not independent evidence. It may identify a
hypothesis, test, or missing question; it does not raise the evidence grade.

### Risk ratings

- **LOW:** credible evidence supports the claim and the downside is bounded by
  tested controls.
- **MEDIUM:** a material evidence gap or consequential downside remains, but a
  time-bounded test or mitigation can resolve it before the relevant gate.
- **HIGH:** a critical claim rests on weak evidence, the downside is
  unacceptable, or the proposed control is untested.

Do not average the four risks. One unmitigated HIGH risk blocks generation even
if the other three are LOW. An unknown is not a LOW risk.

---

```markdown
# Four-Risk Evidence Contract: [Feature Name]

## 1. Decision Context

- Decision owner: [name and role]
- Assessment date: [YYYY-MM-DD]
- Proposed outcome: [what would change for whom]
- Cost of a false positive: [what happens if we build the wrong thing]
- Cost of a false negative: [what happens if we reject a useful thing]
- Decision deadline and why it is real: [date and evidence]
- Related discovery, metrics, and architecture: [stable links]

## 2. Decision Summary

Complete this table after the four detailed assessments. Each row links to
evidence below.

| Risk | Decision at risk | Rating | Best evidence | Falsifier | Next test / control | Owner | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value | [decision] | [LOW/MEDIUM/HIGH] | [E0-E4 + link] | [result that disproves the claim] | [action] | [owner] | [OPEN/CONTROLLED/BLOCKING/ACCEPTED] |
| Usability | [decision] | [LOW/MEDIUM/HIGH] | [E0-E4 + link] | [result] | [action] | [owner] | [status] |
| Feasibility | [decision] | [LOW/MEDIUM/HIGH] | [E0-E4 + link] | [result] | [action] | [owner] | [status] |
| Business viability | [decision] | [LOW/MEDIUM/HIGH] | [E0-E4 + link] | [result] | [action] | [owner] | [status] |

## 3. Value Risk

**Decision at risk:** [Should we solve this problem for this population now?]

**Falsifiable claim:** [Specific population] experiences [specific problem] at
[measured frequency / consequence], and [proposed outcome] would materially
improve [measurable behavior].

### Current evidence

| Source and date | Population / environment | Finding | Grade | Limitation |
| --- | --- | --- | --- | --- |
| [link] | [who / where] | [finding] | [E0-E4] | [bias, age, sample, proxy] |

### What would prove the claim wrong?

- [Observable result that would cause the team to stop or change direction]

### Unknowns and next evidence-producing test

- Unknown: [material unknown]
- Method: [interview, behavior analysis, concierge test, prototype, experiment]
- Success threshold: [numeric or binary threshold fixed before the test]
- Failure threshold: [result that stops or pivots the feature]
- Sample / environment: [representative population]
- Owner and deadline: [owner, YYYY-MM-DD]

### Engineering implications while value remains uncertain

- MUST NOT [build irreversible infrastructure, automate broadly, or expand
  scope before the threshold is met].
- Permitted work: [smallest reversible artifact that produces evidence].

**Disposition:** [LOW/MEDIUM/HIGH] - [OPEN/CONTROLLED/BLOCKING/ACCEPTED]

## 4. Usability Risk

**Decision at risk:** [Can the intended users complete the critical workflow
without hidden expert knowledge or unsafe error recovery?]

**Falsifiable claim:** [Population] can complete [critical task] with [success
rate, time, error rate, or assistance threshold].

### Current evidence

| Source and date | Population / environment | Finding | Grade | Limitation |
| --- | --- | --- | --- | --- |
| [link] | [who / where] | [finding] | [E0-E4] | [limitation] |

### What would prove the claim wrong?

- [Failure, confusion, abandonment, or unsafe recovery threshold]

### Unknowns and next evidence-producing test

- Critical workflow: [workflow]
- Method: [prototype or task test]
- Success threshold: [completion / time / error / assistance target]
- Accessibility and edge population: [who must be represented]
- Owner and deadline: [owner, YYYY-MM-DD]

### Engineering implications while usability remains uncertain

- MUST NOT harden [unvalidated navigation, terminology, API, or workflow] into
  a difficult-to-reverse contract.
- Permitted work: [prototype, instrumented pilot, or reversible interface].

**Disposition:** [LOW/MEDIUM/HIGH] - [OPEN/CONTROLLED/BLOCKING/ACCEPTED]

## 5. Feasibility Risk

**Decision at risk:** [Can the system deliver the required behavior within its
architecture, security, reliability, performance, and delivery constraints?]

**Falsifiable claim:** The inspected system can satisfy [critical technical
claims] within [measurable constraints] without violating [named boundaries].

### Current evidence

| Source and date | Environment | Finding | Grade | Limitation |
| --- | --- | --- | --- | --- |
| [repository evidence, test, benchmark, or spike] | [where] | [finding] | [E0-E4] | [limitation] |

### What would prove the claim wrong?

- [Performance, integration, data, security, cost, or operability result that
  invalidates the approach]

### Unknowns and next evidence-producing test

- Highest-risk assumption: [assumption]
- Method: [code-reading proof, compatibility test, benchmark, migration
  rehearsal, threat model, operational simulation]
- Success threshold: [fixed threshold]
- Failure threshold: [pivot or stop threshold]
- Timebox: [duration; a spike does not silently become production code]
- Owner and deadline: [owner, YYYY-MM-DD]

### Engineering implications while feasibility remains uncertain

- MUST NOT add production authority, persistent data, or a new dependency to
  answer a question a disposable test can answer.
- Spike output permitted for reuse: [none, or explicitly reviewed artifacts].

**Disposition:** [LOW/MEDIUM/HIGH] - [OPEN/CONTROLLED/BLOCKING/ACCEPTED]

## 6. Business Viability Risk

**Decision at risk:** [Can the organization legally, economically, ethically,
and operationally offer and support this capability?]

**Falsifiable claim:** The capability fits [strategy / policy], costs no more
than [threshold], can be supported by [owner / process], and satisfies [legal,
privacy, security, accessibility, contractual, and regulatory obligations].

### Current evidence

| Source and date | Authority / environment | Finding | Grade | Limitation |
| --- | --- | --- | --- | --- |
| [approval, policy, cost model, support analysis] | [owner / jurisdiction] | [finding] | [E0-E4] | [limitation] |

### What would prove the claim wrong?

- [Cost, policy, support, compliance, or strategic result that blocks the
  capability]

### Unknowns and next evidence-producing test

- Required decision: [decision]
- Evidence / approval needed: [specific artifact or named authority]
- Economic threshold: [build, run, support, or opportunity-cost threshold]
- Operational owner: [team / role]
- Owner and deadline: [owner, YYYY-MM-DD]

### Engineering implications while viability remains uncertain

- MUST NOT collect [data], grant [authority], sign [vendor commitment], or make
  an irreversible architecture choice before [approval / threshold].
- Permitted work: [reversible analysis, prototype, or bounded pilot].

**Disposition:** [LOW/MEDIUM/HIGH] - [OPEN/CONTROLLED/BLOCKING/ACCEPTED]

## 7. Cross-Risk Interactions

Record where reducing one risk increases another.

| Proposed mitigation | Risk reduced | Risk increased | Decision |
| --- | --- | --- | --- |
| [example: add human approval] | [feasibility / viability] | [usability / cost] | [accept, test, or reject] |

## 8. Generation Decision

- [ ] **PROCEED TO SPEC:** no unmitigated HIGH risk; every material assumption
      has sufficient evidence or a control that resolves before its gate.
- [ ] **PROCEED WITH BOUNDED DISCOVERY:** only reversible work that produces
      the named evidence is authorized.
- [ ] **PIVOT:** evidence disproves a core claim; revise the proposed outcome.
- [ ] **STOP:** the expected value does not justify resolving the remaining
      risks.
- [ ] **ESCALATE:** a named human authority must accept or reject a residual
      consequence.

### Authorized next work

- [Specific artifact, experiment, SPEC, or task now authorized]

### Work not authorized

- [Generation, integration, data collection, purchase, or rollout that remains
  outside the decision]

### Residual-risk acceptance

- Accepted risk: [risk]
- Accepted by: [name and role with authority]
- Evidence considered: [links]
- Expiration / review trigger: [date or condition]

## 9. Review Cadence

Reopen this contract when evidence expires, the target population changes, a
threshold fails, architecture or policy changes, or production behavior
contradicts a claim.

- Next review: [date or trigger]
- Evidence owner: [name / role]
```

---

## Compact Worked Example

For a fictional per-channel reminder-preference feature:

| Risk | Evidence | Honest disposition | Authorized next step |
| --- | --- | --- | --- |
| Value | Repeated support requests from a narrow customer segment (E1) | MEDIUM / CONTROLLED | Measure frequency and affected-account retention before broadening scope |
| Usability | Existing settings pattern plus five successful prototype tasks (E2) | LOW / ACCEPTED for the pilot population | Preserve the existing interaction pattern and test accessibility |
| Feasibility | Domain design inspected, but migration lock behavior unmeasured (E1) | HIGH / BLOCKING | Rehearse the migration on production-scale synthetic data |
| Viability | Support owner identified; retention policy review incomplete (E1) | MEDIUM / OPEN | Obtain the named privacy decision before audit data is stored |

The correct decision is **bounded discovery**, not full generation. Three risks
look promising, but the blocking migration assumption prevents the team from
converting optimism into production code.

## Common Failure Modes

- **The four opinions.** Each category contains thoughtful prose but no source,
  falsifier, threshold, or owner.
- **The averaged risk.** Three LOW ratings are used to cancel one HIGH rating.
  Consequences do not average away.
- **The prototype promotion.** A spike written to answer a feasibility question
  silently becomes production code without design or review.
- **The model as evidence.** An agent's plausible market, legal, or technical
  analysis is treated as verification.
- **The test after the decision.** The team chooses a direction, then selects a
  threshold that makes the evidence appear supportive.
- **The mitigation without a gate.** A future test is promised but no owner,
  deadline, or work restriction makes it consequential.
- **The stale population.** Evidence from one user group, jurisdiction, system
  version, or operating condition is generalized beyond its limits.

## Related

- [`spec-md.md`](spec-md.md) - receives the outcome authorized by this contract
- [`acceptance-criteria-template.md`](acceptance-criteria-template.md) - turns
  validated claims into executable criteria
- [`blast-radius-template.md`](blast-radius-template.md) - estimates the
  consequence if the implementation fails
- [`design-md.md`](design-md.md) - fixes technical decisions after discovery
- [`personal-eval-set.md`](personal-eval-set.md) - applies repeatable evidence
  discipline to model and tool selection

## Provenance

The four product risks originate with Marty Cagan, *Inspired: How to Create
Tech Products Customers Love*, 2nd ed., Wiley, 2018. This evidence-grading,
falsification, gate-disposition, engineering-constraint, and authorized-work
format is the companion's adaptation of Chapter 5 of *Harnessing the Horse* for
agentic engineering.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
