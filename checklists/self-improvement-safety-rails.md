# Self-Improvement Safety Rails

> **Chapter:** ch16 — Case Study: The Merlin Software Factory
> (Section 16.3, "The Safety Rails", and Section 16.4)
> **Last revised:** 2026-06-16
> **Use this for:** Designing or auditing a system that
> autonomously proposes improvements. Four application controls, plus the
> independent approval and enforcement boundary needed to make them credible.

**Self-improvement without governance is self-destruction.**

The Merlin Software Factory's improvement system implements four controls in a
`SafetyRails` class. They harden the normal proposal path, but code cannot make
itself immutable to a privileged maintainer or another process with write
access. Treat them as application-layer defense in depth.

For a production design, keep approval identity, repository permissions,
protected CI, and any signed policy or artifact verification outside the
process that proposes improvements. The application can request authority; it
must not be able to mint or rewrite it.

These four rails answer the question every architect should ask
when designing a self-modifying system:

> **What happens when the system decides to improve the part of
> itself that decides what to improve?**

On Merlin's normal path, proposals targeting this surface are blocked and
logged. Independent controls must prove that the proposing process cannot
bypass that path or modify the enforcement boundary.

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

## Rail 2: Human Approval on the Normal Path

- [ ] `REQUIRE_HUMAN_APPROVAL` is a **class-level default**, not a runtime
      feature flag on the normal path
- [ ] Environment variables and constructor arguments cannot disable it
- [ ] The code contains a defensive guard that fails closed on the normal path
- [ ] A separately authenticated approval record is verified before persistence
      or execution; the proposing process cannot mint that record
- [ ] Every improvement proposal remains an unprivileged draft until that
      approval is verified

**Why this matters:**

The approval step is the point where human judgment evaluates
whether a proposed change is aligned with the system's goals —
the **"should we?"** question that agents cannot answer.

A runtime flag can be flipped under pressure. A class-level default adds useful
friction, but only protected review, repository permissions, and independent
approval verification prevent the proposing process from granting itself
authority.

---

## Rail 3: Forbidden Paths

- [ ] The safety module maintains a **list of file paths** that the normal
      proposal path must reject
- [ ] The list **starts with the safety module itself** (e.g., `safety.py`)
- [ ] The list includes any **meta-improvement** modules (e.g.,
      `harness/meta_improvement.py`)
- [ ] When an improvement proposal is evaluated, the `SafetyRails`
      class **scans every string value in the proposal dict
      recursively** (depth-limited to 5 levels) for any mention of
      a forbidden path
- [ ] A match blocks and logs the proposal on the normal path
- [ ] Repository permissions and protected CI independently reject changes to
      the protected surface from the proposing identity

**Why this matters:**

The application check rejects direct attempts to weaken its guardrails. It is
not sufficient by itself: aliases, generated paths, encoding, or another
writable process can bypass string matching, so independent path protection is
required.

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
- [ ] A match blocks and logs the proposal on the normal path

**Why this matters:**

An improvement proposal about the improvement system itself would
create a recursive loop:

- The observer proposes changes to the observer
- The proposer proposes changes to the proposer

This heuristic catches named forms of self-reference. It does not prove the
absence of indirect or novel references; pair it with protected ownership and
CI controls over the improvement implementation.

This is distinct from Rail 3 (forbidden paths). Rail 3 blocks
modifications to the safety module by path. Rail 4 blocks the
improvement system from proposing improvements to its own
improvement logic, even when those improvements would not touch
the safety module.

---

## The Distinction This Enforces

These four application rails are one layer in the governance model for
autonomous improvement. With independent approval and enforcement, they make
the following distinction operational rather than merely documented:

| Self-improvement (productive) | Self-modification (runaway) |
| --- | --- |
| The system observes its work, generates proposals, and waits for human approval | The system modifies itself without bounded review |
| Improvements affect prompts, configurations, pipeline parameters | Improvements affect safety constraints, decision logic, or the improvement system itself |
| Daily caps and forbidden paths constrain scope | No bounds on what can be proposed or how often |
| Every proposal is observable and attributable; reversibility is proved or an exception plan is approved | Proposals compound silently |

The intended operating rule is that the system proposes improvements within the
harness. Independent authority must enforce changes to the harness itself.

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
- [ ] **Who can mint and verify approval?** (The proposing process must not
      control both.)
- [ ] **Where is the forbidden-paths list?** (Find it, read it,
      verify it contains the safety module itself.)
- [ ] **How are paths scanned?** (Recursive with depth limit? Top
      level only? Any chance of bypass via nested structure?)
- [ ] **Where is self-referential detection?** (Find the actual
      check, with the actual marker list.)
- [ ] **Which independent control protects these mechanisms?** (Verify
      repository ownership, protected CI, execution identity, and override
      audit rather than trusting application checks alone.)

If any application question cannot be answered by pointing to a specific code
path, the system does not have that application rail. If the independent-control
question has no answer, the rails are bypassable defense in depth rather than a
security boundary.

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

The reported operating history had not modified its own safety constraints as
of the case-study observation. That observation does not prove the application
controls are immutable or unbypassable.

## Pitfalls

- **The rail with the override flag.** "But what if we need to
  raise the cap temporarily?" If the cap has an override flag,
  it's not a rail. Genuine rails require a code change and a
  deploy to relax.
- **The rail that exists only in documentation.** Stating "the system requires
  human approval" in the README without enforcement is theater. Application
  checks need code; authority-bearing controls need an independent boundary.
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
