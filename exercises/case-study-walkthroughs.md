# Case Study Walkthroughs

> **Chapters:** ch14–ch16 (Part IV — Practice), plus the Appendix D
> design study and the Chapter 13 MCP-fleet implementation notes
> **Last revised:** 2026-06-16
> **Use this for:** A structured exploration of each case study in
> the book, organized for self-study and classroom use. Each
> walkthrough applies the
> [Case Study Analysis Framework](case-study-analysis-framework.md)
> and points at the companion artifacts that ground each case.

The book's three case studies are real engineering engagements
with documented outcomes and concrete artifacts. Each carries a
Status and Evidence box in the book — deployed, measured, or
projected — and every walkthrough below expects you to hold the
evidence to that labeling. Each walkthrough helps you:

1. **Locate the central thesis** of the case
2. **Map the case to the framework** (apply the Case Study
   Analysis Framework's eight sections)
3. **Identify the patterns** that recur and the patterns that are
   unique
4. **Find the companion artifacts** the case is grounded in

---

## Chapter 14 — CRM Integration Hub

### Central thesis

Governance and architectural discipline prevent integration
fragmentation. A single mediating service with hexagonal ports,
anti-corruption layers, and verifiable ADRs solves credential
incidents and data quality gaps before regulatory deadlines force
migration.

### Apply the framework

- **Section 3 (Architectural Pattern Analysis)** —
  Anti-Corruption Layer + Hexagonal Architecture + Strangler Fig.
  See [`../patterns/anti-corruption-layer.md`](../patterns/anti-corruption-layer.md)
  and [`../patterns/hexagonal-architecture.md`](../patterns/hexagonal-architecture.md).
- **Section 6 (Governance and Safety)** — Verification stance
  markers (`verified` / `ASSUMPTION` / `VERIFY`) catch briefing
  errors before they become load-bearing. See
  [`../prompts/verification-stance-markers.md`](../prompts/verification-stance-markers.md).

### Companion artifacts grounding this case

- TypeScript port/adapter implementation:
  [`../code-examples/anti-corruption-layer/`](../code-examples/anti-corruption-layer/)
- License-class triage worksheet (from the 22-project evaluation):
  [`../checklists/oss-license-triage.md`](../checklists/oss-license-triage.md)

### Key question

The six-path integration inventory (Sentinel, hubspot-adapter,
customer-service layer, vendor card, MCP server, .NET
HubSpotProcessor) is case-specific. **What about it generalizes?**
The pattern of "multiple uncoordinated integrations to the same
vendor" exists at most enterprises. The mediating-service solution
applies regardless of vendor.

---

## Chapter 15 — The E-Commerce Platform and Its Checkout

### Central thesis

Recursive specification (AI-generated build guide evaluated and
refined by human judgment) enables a senior architect with no
frontend expertise to build a production e-commerce platform
(150,915 lines, 18 integrations, 47 active development days).
The gap between scaffolding and product is user-centered judgment
work, not code volume. The checkout (§15.6–15.9) grounds the
platform story in transaction safety: patterns from Part III
(CAS-Guarded Distributed Commit, Idempotent Receiver, Scoped
Authorization Token, Anti-Corruption Layer) applied where the
money moves.

### Apply the framework

- **Section 5 (Generation-Review Asymmetry)** — The build guide
  is the recursive specification at scale. AI generates the
  specification, human evaluates and refines, AI implements,
  human reviews.
- **Section 1 (Scale Indicators)** — 150,915 LOC, 18 integrations,
  66 database models, dual payment gateways. **Use these numbers
  carefully** — Section 7 (Outcomes Assessment) asks whether
  codebase size alone validates the discipline thesis.
- **Section 3 (Architectural Pattern Analysis)** — The checkout
  interleaves multiple patterns:
  - **CAS-Guarded Distributed Commit** (§15.7, the double-charge
    problem):
    [`../patterns/cas-guarded-distributed-commit.md`](../patterns/cas-guarded-distributed-commit.md)
  - **Anti-Corruption Layer** applied to ATTOM property data
    quality
  - **Scoped Authorization Token** for the Magic Link customer
    session (§15.9)
- **Section 7 (Outcomes and Evidence)** — Quantified economic
  impact at projected scale: **$30k–$40k/year** in avoided
  chargebacks ($5.5k + $7k), operator cleanup ($1k), self-serve
  deflection ($10.2k), and retention lift ($12k). Note these are
  **projected** for 1,000 subscriptions, not measured — §15.9
  recomputes the economics with stated assumptions.

### Companion artifacts grounding this case

- SPEC.md template (the building block of recursive
  specification): [`../spec-templates/spec-md.md`](../spec-templates/spec-md.md)
- Cagan four-risk assessment (for complex feature decisions):
  [`../spec-templates/cagan-four-risk-assessment.md`](../spec-templates/cagan-four-risk-assessment.md)
- CAS-Guarded Distributed Commit reference card:
  [`../patterns/cas-guarded-distributed-commit.md`](../patterns/cas-guarded-distributed-commit.md)
- Scoped Authorization Token reference card:
  [`../patterns/scoped-authorization-token.md`](../patterns/scoped-authorization-token.md)

### Key questions

1. The "capable of more" multiplier is **distinct from "faster."**
   The architect did not build faster than a frontend team; he
   built solo what normally requires a team. **What is the
   difference, exactly?** This is the central question of the
   agentic-development economic model.

2. **"Default-safe configuration is a pattern, not a preference."**
   Sandbox-by-default tenant routing (§15.8),
   simulation-mode-on-by-default, production-as-explicit-opt-in.
   **Where else does this pattern apply?** Find three examples in
   your own codebase where the default could become a safety
   pattern.

---

## Appendix D — Design Study: Platform Modernization (FieldstoneOS)

A design study, not a case study: Appendix D documents an
architecture and migration plan for replacing a vendor platform,
none of it yet built. Analyze it with Section 7's status-honesty
lens active throughout.

### Central thesis

Multi-year Strangler Fig replacement of a vendor platform requires
event sourcing for audit-by-construction, CQRS with dual-ORM
separation for independent evolution, bounded-context discipline
for semantic clarity, and five-phase phasing with parallel-run
validation. Dollar value at full migration is projected only, with
assumptions stated in the appendix.

### Apply the framework

- **Section 3 (Architectural Pattern Analysis)** — Event
  Sourcing + CQRS + Bounded Contexts + Transactional Outbox +
  Strangler Fig. See [`../patterns/event-sourcing.md`](../patterns/event-sourcing.md)
  and [`../patterns/transactional-outbox.md`](../patterns/transactional-outbox.md).
- **Section 6 (Governance)** — The dual-ORM rule
  (architecture-as-code enforced by TypeScript path mappings and
  CI lint) is the pattern designed to make the architecture
  survive team turnover.
- **Section 4 (Quality Gate Analysis)** — The plan specifies
  equivalence tests running continuously through the parallel-run
  phase (§D.4). See
  [`../checklists/equivalence-test-checklist.md`](../checklists/equivalence-test-checklist.md).

### Companion artifacts grounding this case

- Event Sourcing reference card:
  [`../patterns/event-sourcing.md`](../patterns/event-sourcing.md)
- Migration plan template:
  [`../spec-templates/migration-plan-template.md`](../spec-templates/migration-plan-template.md)
- Migration phase gate checklist:
  [`../checklists/migration-phase-gate.md`](../checklists/migration-phase-gate.md)
- Equivalence test checklist:
  [`../checklists/equivalence-test-checklist.md`](../checklists/equivalence-test-checklist.md)

### Key question

**"The Strangler Fig at platform scale is the same pattern as at
integration scale — the difference is duration, not discipline."**
Compare Ch14 (CRM Hub, 6 months) and Appendix D (FieldstoneOS, 5
planned years). What changes when the same pattern scales by 10×?
And what can a design study establish that only execution can
confirm?

---

## Chapter 13 — MCP Server Fleet (Implementation Notes, §13.6)

The MCP fleet appears in the book as an implementation section of
Chapter 13 rather than a standalone case study; it still rewards
the same structured analysis.

### Central thesis

A centralized MCP server fleet (not per-agent integration)
mediates operational systems through domain-named tools with
typed contracts. Cross-engagement pattern reuse with file-and-line
citations produces $15k–$30k in avoided re-invention per reused
pattern.

### Apply the framework

- **Section 3 (Architectural Pattern Analysis)** — Per-capability
  MCP servers + per-tool RBAC + dry-run-default. See
  [`../patterns/dry-run-default.md`](../patterns/dry-run-default.md)
  and [`../patterns/scoped-authorization-token.md`](../patterns/scoped-authorization-token.md).
- **Section 6 (Governance)** — Authentication architecture
  (Entra ID JWT for internal, API keys for partners,
  unauthenticated rejection, per-tool RBAC).
- **Section 5 (Generation-Review Asymmetry)** —
  Cross-engagement citation discipline. File-and-line citations
  (e.g., `fieldroutes-scheduling.ts:634–655`) carry context
  between projects, dramatically reducing the agent's "discover
  the API quirk again" cost.

### Companion artifacts grounding this case

- TypeScript MCP tool implementation:
  [`../code-examples/mcp-tool-pattern/`](../code-examples/mcp-tool-pattern/)
- Dry-Run-Default pattern reference:
  [`../patterns/dry-run-default.md`](../patterns/dry-run-default.md)
- Merlin architecture diagrams (the system this fleet operates
  within): [`../diagrams/merlin-architecture-v2.md`](../diagrams/merlin-architecture-v2.md)

### Key question

**"Domain-named tools (`schedule_appointment`) are dramatically
more effective than vendor-named tools
(`fieldroutes_create_appointment`) for agent tool selection."**
Why? What does the domain name communicate to the agent that the
vendor name does not?

---

## Chapter 16 — The Merlin Software Factory

### Central thesis

One architect + AI discipline = production infrastructure that
normally requires a 10-person team. The economic shift is not
"faster code" but **"clarity is advantage now, headcount is
not."** Self-improvement within bounded constraints enables
institutional learning without runaway modification.

### Apply the framework

- **Section 2 (Harness Framework Mapping)** — SPEC.md (language-
  agnostic RFC 2119 contract), STRATEGIC_PIVOT.md (architectural
  course correction), CLAUDE.md (working conventions). The
  three-document foundation.
- **Section 3 (Architectural Pattern Analysis)** — The **Express
  Arc**: single agent owns end-to-end delivery. See
  [`../patterns/express-arc.md`](../patterns/express-arc.md).
- **Section 4 (Quality Gates)** — G1–G9 with
  BLOCKING / ADVISORY / INFORMATIONAL / ASYNC classification,
  fired inline.
- **Section 6 (Governance)** — Four safety rails for
  self-improvement. See
  [`../checklists/self-improvement-safety-rails.md`](../checklists/self-improvement-safety-rails.md).

### Companion artifacts grounding this case

- Express Arc pattern reference:
  [`../patterns/express-arc.md`](../patterns/express-arc.md)
- STRATEGIC_PIVOT.md template:
  [`../spec-templates/strategic-pivot-template.md`](../spec-templates/strategic-pivot-template.md)
- Iteration caps checklist:
  [`../checklists/iteration-caps.md`](../checklists/iteration-caps.md)
- Self-improvement safety rails:
  [`../checklists/self-improvement-safety-rails.md`](../checklists/self-improvement-safety-rails.md)
- Merlin architecture diagrams:
  [`../diagrams/merlin-architecture-v2.md`](../diagrams/merlin-architecture-v2.md)

### Key questions

1. **"Fixing Merlin with Merlin"** — The system processed its
   own Work Orders and found six bugs in its own pipeline. **What
   governance constraints prevent this from becoming a recursive
   self-improvement loop?** Use the four safety rails as your
   framework.

2. **The express arc pivot.** The original design used a
   multi-agent pipeline; the pivot moved to a single primary
   agent owning the entire arc. **What problem did multi-agent
   orchestration create, and how does the express arc address
   it?**

3. **The system diagnosed its own bug better than the human.**
   When Merlin built the `/security.txt` endpoint, the
   pipeline terminated at `partial_completion` due to a verdict-
   aggregation bug. The retrospective agent's diagnosis was
   more precise than the human's initial read. **What does this
   event tell us about agent capability, and what should it
   NOT be taken to prove?**

---

## Cross-Case Comparisons

The case studies reward comparative analysis. Three particularly
productive comparisons:

### CRM Hub (Ch14) vs. FieldstoneOS (Appendix D)

**Same pattern, different scale.** Strangler Fig migration over
6 months vs. 5 planned years. What changes when discipline must
survive team turnover, model evolution, and business priority
shifts?

### Checkout (Ch15) vs. MCP Fleet (Ch13)

**Same pattern, different consumer.** Scoped Authorization Token
applied to customer sessions (one subscription scope) vs. agent
sessions (per-tool RBAC). The principle — Saltzer & Schroeder's
least privilege — is the same. The consumer differs.

### Merlin (Ch16) vs. E-Commerce (Ch15)

**Same architect, different domains.** Two solo projects: one
infrastructure (Merlin, Python), one consumer (E-commerce,
TypeScript/Next.js). Different tech stacks, different problem
domains, **same engineering discipline, same outcome**.

### What does the cross-case consistency prove?

The thesis the case studies test is **"engineering discipline
scales across domains"** — not "AI makes code faster." Each
case is one data point from a single practitioner's portfolio,
and the book says so plainly. The consistency across the three
cases and the design study — different scales, different stacks,
different consumers, different domains — is what gives the
thesis weight beyond anecdote.

## How to Use These Walkthroughs

### For self-study

Read one case fully, then complete the
[Case Study Analysis Framework](case-study-analysis-framework.md)
for that case. Compare your analysis to the walkthrough's
suggested framework mappings. Identify what you saw that the
walkthrough did not, and what the walkthrough surfaced that you
missed.

### For classroom use

Assign each student/group a different case study. Have them
present their framework analysis to the class. The
cross-case-comparison exercises (above) are particularly
productive for capstone discussion.

### For practitioners

Pick the case study closest to a project you're working on now.
Walk through which patterns from the case apply directly, which
apply with adaptation, and which do not apply. The "does not
apply" answers are often the most informative — they help you
locate where your context is genuinely different from the case.

## Related

- [`case-study-analysis-framework.md`](case-study-analysis-framework.md)
  — the eight-section framework these walkthroughs guide you
  through
- [`../patterns/README.md`](../patterns/README.md) — the catalog
  of named patterns referenced across the case studies
- [`maturity-assessment.md`](maturity-assessment.md) — self-assess
  where your team is relative to the discipline these case
  studies demonstrate

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
