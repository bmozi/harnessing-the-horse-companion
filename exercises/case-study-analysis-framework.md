# Case Study Analysis Framework

> **Source:** Academic Supplement to *Harnessing the Horse*, Part 3
> **Last revised:** 2026-06-16
> **For:** Senior-level and graduate students; team-based capstone
> projects; practitioners analyzing their own systems.

A structured template for analyzing AI-augmented software systems
through the lens of the book's discipline framework. Designed for
analyzing the book's primary case studies (the Merlin Software
Factory, Chapter 16; the consumer mobile application from Chapters 1
and 3) and adaptable for any external case — your own
project, an open-source project with documented AI-assisted
development, or a published industry case.

---

## How to Use

1. Pick a case study — your own project, one in the book, or one you
   are researching.
2. Work through Sections 1–8 in order. Each section builds on the
   previous one.
3. Cite evidence — chapter and section, file and line, commit hash,
   public source.
4. Deliver as a 15–20 page write-up plus a Harness Framework matrix
   and three prioritized recommendations.

---

## Analysis Template

### Section 1: System Context and Constraints

1. **System description:** What does the system do, who are its
   users, and what stage is it at (design, development, production)?
2. **Team structure:** How many engineers are involved? What is the
   human-to-agent ratio?
3. **Scale indicators:** Lines of code, number of files, number of
   commits, deployment frequency, and other quantitative measures of
   system scope.
4. **Constraint environment:** What constraints does the system
   operate under? (Regulatory, performance, security, budget,
   timeline, team size.)

### Section 2: Harness Framework Mapping

For each Harness discipline, identify and evaluate the practices
employed:

| Discipline | Practice Identified | Maturity Tier (1-6) | Evidence (cite chapter/section) | Gap Assessment |
|---|---|---|---|---|
| **Scope** | | | | |
| **Prove** | | | | |
| **Enforce** | | | | |
| **Communicate** | | | | |

**Analysis questions:**
- Which Harness discipline is strongest? What specific practices
  create that strength?
- Which Harness discipline is weakest? What risks does the weakness
  create?
- Does the maturity level appear consistent across disciplines, or is
  there significant variation?

### Section 3: Architectural Pattern Analysis

1. **Patterns employed:** List every named architectural pattern
   applied in the case study (e.g., Hexagonal Architecture, Strangler
   Fig, Circuit Breaker, Saga, Event Sourcing, CQRS).
2. **Pattern-to-problem mapping:** For each pattern, explain (a) the
   specific problem it addresses, (b) the alternatives that were
   considered, and (c) the trade-offs accepted.
3. **Pattern interaction:** Identify any patterns that interact with
   each other (e.g., Hexagonal Architecture enabling safer Strangler
   Fig migration) and explain the interaction.

### Section 4: Quality Gate and Verification Analysis

1. **Verification layers:** Enumerate every verification mechanism
   (automated gates, review practices, testing strategies) described
   or implied in the case study.
2. **Coverage assessment:** Map verification layers to the Harness
   Framework — which layers serve Prove, which serve Enforce?
3. **Gap identification:** Identify any failure modes that the
   verification layers would not catch. Explain why the gap exists
   and propose a mitigation.

### Section 5: Generation-Review Asymmetry Assessment

1. **Generation rate:** What was the approximate code generation
   rate? How was it measured?
2. **Review strategy:** How was the generation-review asymmetry
   managed? (Automated gates, adversarial review, human review, or a
   combination.)
3. **Regeneration rate:** What evidence exists about regeneration
   rate? Was it measured? What does the evidence suggest about
   specification quality?
4. **Dark code risk:** Is there evidence of dark code accumulation?
   What structural safeguards prevent it?

### Section 6: Governance and Safety Analysis

1. **Human-in-the-loop boundaries:** At what points does human
   judgment override agent autonomy? Are these boundaries enforced by
   code or by policy?
2. **Self-improvement governance (if applicable):** If the system
   includes self-improving capabilities, what constraints prevent
   unbounded self-modification? Are the constraints enforceable or
   advisory?
3. **Security posture:** Map the system's security model to the
   generation trifecta and its six-vector extension (Chapter 17).
   For deployed agents, also consider Willison's lethal trifecta —
   the runtime combination of private-data access, untrusted
   content, and external communication, a distinct threat model the
   chapter separates from the generation trifecta. Which threats
   are addressed? Which remain as accepted risk?

### Section 7: Outcomes and Evidence Assessment

1. **Claimed outcomes:** What outcomes are claimed (productivity,
   quality, cost, team satisfaction)?
2. **Evidence quality:** For each claimed outcome, assess: Is it
   measured or estimated? Is the measurement methodology described?
   Are baselines established? Could the outcome be attributed to
   factors other than the practices described?
3. **Status honesty:** Are outcomes framed appropriately for their
   stage? (Proposed/expected for design-stage systems;
   achieved/measured for production systems.)

### Section 8: Synthesis and Recommendations

1. **Thesis validation:** Does this case study support or challenge
   the book's central thesis that engineering discipline, not model
   capability, determines whether AI acceleration is productive?
2. **Transferability:** Which practices from this case study would
   transfer to a different team, technology stack, or domain? Which
   are context-specific?
3. **Recommendations:** If you were advising this team, what three
   improvements would you recommend, ranked by expected impact?

---

## Applying the Framework to the Book's Case Studies

### Merlin Software Factory (Chapter 16)

**Recommended focus areas:** Sections 4 (quality gate analysis —
G1-G9), 5 (generation-review asymmetry — 340K LOC in 31 days), and 6
(self-improvement governance — the four safety constraints).

**Key analysis questions:**

- The Merlin system was used to fix itself ("fixing Merlin with
  Merlin"). Analyze this self-referential development process through
  the lens of Section 6. What governance constraints prevent this
  from becoming a recursive self-improvement loop?
- The express single-agent path replaced a multi-agent pipeline.
  Using Section 3, analyze this architectural pivot: what problem did
  multi-agent orchestration create, and how does the express path
  address it?
- Six bugs were discovered during self-processing runs. One
  post-mortem, written by the system's own retrospective agent,
  diagnosed a verdict-aggregation bug more precisely than the human's
  initial read. Analyze this through Section 7: what does this event
  tell us about agent capability, and what should it not be taken to
  prove?

### The Consumer Mobile Application (Chapters 1 and 3)

**Recommended focus areas:** Sections 1 (scale indicators — 462K+
LOC of Dart, 1,533 commits — volume, not value), 2 (Harness
Framework mapping — specification-driven mobile development), and 5
(generation-review asymmetry — solo development at scale).

**Key analysis questions:**

- The application was developed by a single engineer using AI
  agents, with no co-developers. Using Section 5, analyze how the
  generation-review asymmetry is managed when there is only one
  reviewer (the developer themselves). What practices compensate for
  the absence of peer review?
- At 462,000+ lines of Dart across 803 source files, the codebase
  is larger than many team-developed applications.
  Using Section 7, evaluate the evidence: does codebase size alone
  validate the discipline thesis, or are additional quality
  indicators needed?
- Compare the mobile-application case to the Merlin case using
  Sections 2 and 3. Both were solo-developed with AI agents, but
  they serve different domains (mobile app vs. infrastructure
  platform). What practices are shared? What differs?
- The application was built from personal conviction before any
  commercial or enterprise application existed. Using Section 7
  (Outcomes and Evidence Assessment), evaluate whether personal
  conviction as a motivating force produces different engineering
  outcomes than organizational mandates.
- The book documents a three-project compounding arc: consumer
  mobile application → enterprise field service platform →
  enterprise architecture. Using Section 3 (Architectural Pattern
  Analysis), trace three specific patterns (Provider interface,
  Anti-Corruption Layer, Circuit Breaker) across these projects and
  evaluate whether the cross-domain transfer validates or challenges
  the compounding practices thesis from Chapter 10.

---

## Capstone Project Specification

For senior-level and graduate courses: apply the Case Study Analysis
Framework to an AI-augmented software project of your own choosing —
your own project, an open-source project with documented AI-assisted
development, or a published industry case study.

### Deliverables

1. Completed analysis template (Sections 1–8) — 15–20 pages
2. Harness Framework assessment matrix with evidence citations
3. Three specific, prioritized recommendations with expected impact
4. 10-minute presentation to the class

### Grading criteria

| Criterion | Weight |
| --- | --- |
| Rigor of evidence assessment (Section 7) | 25% |
| Quality of Harness Framework mapping (Section 2) | 20% |
| Depth of architectural pattern analysis (Section 3) | 20% |
| Actionability of recommendations (Section 8) | 20% |
| Clarity of presentation | 15% |

## Related

- `../spec-templates/spec-md.md` — the SPEC artifact whose mapping
  Section 2 evaluates
- `../checklists/integration-verification-checklist.md` — Section 4's
  verification-layer enumeration can use this as a baseline

## Provenance

Adapted from Part 3 of the Academic Supplement to *Harnessing the
Horse*. The full instructor package — solutions, grading rubrics,
discussion prompts — is distributed separately to verified instructors
by the author.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
