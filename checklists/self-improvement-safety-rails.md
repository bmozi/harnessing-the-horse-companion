# Self-Improvement Safety Rails

> **Chapter:** ch16 — Case Study: The Merlin Software Factory
> (Section 16.3, "The Safety Rails", and Section 16.4)
> **Last revised:** 2026-06-16
> **Use this for:** Designing or auditing a system that
> autonomously improves itself. The four non-negotiable
> constraints that distinguish productive self-improvement from
> unconstrained self-modification.

**Self-improvement without governance is self-destruction.**

The Merlin Software Factory's improvement system enforces four
non-negotiable constraints through a `SafetyRails` class whose
design is **intentionally resistant to relaxation**.

These four rails answer the question every architect should ask
when designing a self-modifying system:

> **What happens when the system decides to improve the part of
> itself that decides what to improve?**

In Merlin, the answer is: **nothing**. That path is structurally
blocked. The system improves within the harness; it does not
modify the harness.

---

## Rail 1: Daily Proposal Cap

- [ ] The system generates **at most N improvement proposals per
      calendar day** (UTC)
- [ ] The cap is **deliberately conservative** — small enough that
      a single operator can review every proposal in a morning,
      large enough to make meaningful daily progress
- [ ] More autonomous components (proactive discoverers) cap at
      **lower** numbers than reactive observers

**Why this matters:**

- Prevents runaway Work Order creation from a noisy signal (a
  widespread but minor metric regression cannot trigger dozens of
  self-modification work orders overnight)
- Preserves attribution clarity — if too many improvement
  experiments run concurrently, outcome changes cannot be
  attributed to specific changes, and the A/B testing framework
  loses its ability to distinguish signal from noise

**Reference numbers from Merlin:**
- `ImprovementObserver`: 5 proposals per day
- `ProactiveDiscoverer`: 3 proposals per day

---

## Rail 2: Permanent Human Approval

- [ ] `REQUIRE_HUMAN_APPROVAL` is a **class-level constant**, not
      a configuration setting
- [ ] It is set to `True` and **cannot be overridden** by
      environment variable, constructor argument, or runtime
      monkey-patching
- [ ] The code contains a **defensive guard**: even if the constant
      were somehow mutated at runtime, the check would fail and
      block the proposal
- [ ] Every improvement proposal is a **Work Order dict**, not a
      persisted ORM object, until a human explicitly approves it

**Why this matters:**

The approval step is the point where human judgment evaluates
whether a proposed change is aligned with the system's goals —
the **"should we?"** question that agents cannot answer.

A configuration setting can be flipped under pressure. A
class-level constant requires a code change, a review, and a
deploy. That friction is the feature.

---

## Rail 3: Forbidden Paths

- [ ] The safety module maintains a **list of file paths** that
      improvement proposals must not reference
- [ ] The list **starts with the safety module itself** (e.g.,
      `safety.py`) — the system cannot propose modifications to
      its own safety constraints
- [ ] The list includes any **meta-improvement** modules (e.g.,
      `harness/meta_improvement.py`)
- [ ] When an improvement proposal is evaluated, the `SafetyRails`
      class **scans every string value in the proposal dict
      recursively** (depth-limited to 5 levels) for any mention of
      a forbidden path
- [ ] A match **blocks the proposal immediately**

**Why this matters:**

The system can improve its prompts, its agent configurations, its
pipeline parameters — **but it cannot weaken its own guardrails**.

Recursive depth-limited scanning catches the case where a
forbidden path is embedded inside a nested structure, not just at
the top level. The depth limit (5) prevents infinite recursion on
self-referential structures.

---

## Rail 4: Self-Referential Loop Detection

- [ ] The `SafetyRails` class detects **self-referential
      proposals** by scanning the problem statement and origin
      source for markers like:
  - `improvement_observer`
  - `improvement/proposer`
  - `merlin.improvement` (or your equivalent namespace)
- [ ] A match **blocks the proposal**

**Why this matters:**

An improvement proposal about the improvement system itself would
create a recursive loop:

- The observer proposes changes to the observer
- The proposer proposes changes to the proposer

The system can observe everything and improve almost everything —
**except itself**.

This is distinct from Rail 3 (forbidden paths). Rail 3 blocks
modifications to the safety module by path. Rail 4 blocks the
improvement system from proposing improvements to its own
improvement logic, even when those improvements would not touch
the safety module.

---

## The Distinction This Enforces

These four rails are the governance model for **autonomous
self-improvement**. They make the distinction — enforced in code,
not just stated in documentation — between:

| Self-improvement (productive) | Self-modification (runaway) |
| --- | --- |
| The system observes its work, generates proposals, and waits for human approval | The system modifies itself without bounded review |
| Improvements affect prompts, configurations, pipeline parameters | Improvements affect safety constraints, decision logic, or the improvement system itself |
| Daily caps and forbidden paths constrain scope | No bounds on what can be proposed or how often |
| Every proposal is observable, attributable, and reversible | Proposals compound silently |

The system improves **within** the harness. It does not modify the
harness.

## When to Use This Framework

This pattern applies to any system with autonomous improvement
capability — not just AI agent systems:

- Self-tuning ML pipelines that modify their own hyperparameters
- CI/CD systems that propose changes to their own pipeline
  configuration
- Monitoring systems that modify their own thresholds
- Documentation systems that update their own architecture

The same four rails (cap, human approval, forbidden paths,
self-referential detection) apply with minor adaptation.

## Audit Checklist

When auditing an existing autonomous-improvement system, ask:

- [ ] **Where is the daily cap implemented?** (Find the actual
      enforcement code, not just the constant.)
- [ ] **Can the cap be raised at runtime?** (If yes, it's a
      configuration setting, not a rail.)
- [ ] **Where is the human-approval requirement enforced?** (Find
      the actual guard, not just the documented intent.)
- [ ] **Is the approval requirement a class-level constant?** (If
      it's a config flag, it can be flipped.)
- [ ] **Where is the forbidden-paths list?** (Find it, read it,
      verify it contains the safety module itself.)
- [ ] **How are paths scanned?** (Recursive with depth limit? Top
      level only? Any chance of bypass via nested structure?)
- [ ] **Where is self-referential detection?** (Find the actual
      check, with the actual marker list.)

If any of these questions cannot be answered by pointing to a
specific code path, the system **does not have these rails**, even
if the documentation says it does.

## Worked Example: Merlin Improvement Plane

From the Merlin Software Factory (ch16):

- `ImprovementObserver` monitors pipeline metrics, generates ≤ 5
  proposals/day
- `ImprovementProposer` drafts Work Order dicts (not persisted
  ORM objects) for proposals
- `SafetyRails.REQUIRE_HUMAN_APPROVAL = True` (class-level
  constant)
- `SafetyRails.FORBIDDEN_PATHS` includes `safety.py` and
  `harness/meta_improvement.py`
- `SafetyRails.detect_self_referential()` scans for
  `improvement_observer`, `improvement/proposer`,
  `merlin.improvement`
- A/B testing via `VariantAgent` and `ABTestRunner` validates
  improvements against baselines before adoption
- `PlaybookEvolution` applies validated improvements to agent
  prompts

The system improves itself daily, demonstrably, **without ever
having modified its own safety constraints**.

## Pitfalls

- **The rail with the override flag.** "But what if we need to
  raise the cap temporarily?" If the cap has an override flag,
  it's not a rail. Genuine rails require a code change and a
  deploy to relax.
- **The rail that exists only in documentation.** Stating "the
  system requires human approval" in the README without enforcing
  it in code is theater. Every rail must be enforced in code.
- **The forbidden-paths list that nobody updates.** When a new
  safety-critical module is added, it must be added to the
  forbidden-paths list at the same time. CI should check this.
- **The self-referential detection that misses indirect
  references.** If the marker list is "improvement_observer" but
  the proposal references "the observer that observes
  improvements," the detection fails. Use multiple synonymous
  markers; bias toward false positives.

## Related

- [`iteration-caps.md`](iteration-caps.md) — companion discipline
  for bounded iteration in the same system
- [`../patterns/express-arc.md`](../patterns/express-arc.md) — the
  single-agent delivery pattern that pairs with self-improvement
- [`../prompts/escalation-protocol.md`](../prompts/escalation-protocol.md)
  — what to do when a proposal is blocked and the operator must
  decide whether to escalate
- `../spec-templates/adr-template.md` — every adoption of an
  improvement proposal should produce an ADR

## Provenance

Adapted from Chapter 16 of *Harnessing the Horse*, Sections 16.3
and 16.4.
The four rails (daily cap, permanent human approval, forbidden
paths, self-referential detection) are the design of the Merlin
Software Factory's `SafetyRails` class.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
