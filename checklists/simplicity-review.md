# Simplicity Review Checklist

> **Chapter:** ch09 — Architectural Stewardship (Section 9.2,
> "Debt Governance")
> **Last revised:** 2026-06-16
> **Run when:** Reviewing agent-generated code for over-abstraction.
> Especially relevant when the agent has produced multiple wrapper,
> adapter, or factory classes.

AI agents, left unchecked, produce **clever code**. They reach for
design patterns, abstractions, and indirections that demonstrate
capability but reduce comprehensibility. Simplicity is not a
nice-to-have in agentic development — it is a hard requirement for
managing technical debt.

Every unnecessary abstraction is a debt item: it must be understood,
maintained, and defended against future changes that may invalidate
its assumptions.

The litmus test comes from John Ousterhout, *A Philosophy of
Software Design* (Yaknyam Press, 2018): **a deep module has a simple
interface that hides significant implementation complexity.** If a
module's interface is as complex as its implementation, the
abstraction is adding cost without adding value.

---

## The Four Tests

Apply all four to every abstraction in generated code.

### Test 1: The Deep Module Test

- [ ] Is this module's **interface simpler than its implementation?**
- [ ] If the interface is as complex as the internals, the
      abstraction is **not justified**.

> A deep module's interface is the cost (developers must learn it).
> The hidden complexity is the value (developers are shielded from
> it). Equal cost and value = no net benefit.

### Test 2: The YAGNI Test

- [ ] Is this abstraction needed for **the current requirements**, or
      is it **pre-emptive generalization**?
- [ ] In agentic development, where requirements can be implemented
      rapidly, pre-emptive generalization is **almost never
      justified** — when the future requirement arrives, it can be
      implemented then.

> "You Aren't Gonna Need It" (Beck / XP). Code that prepares for
> hypothetical future requirements adds cost today with uncertain
> future benefit.

### Test 3: The Comprehension Test

- [ ] Can a **mid-level engineer understand this code in one
      reading**?
- [ ] If it requires tracing through multiple layers of indirection to
      understand what it does → it is **too complex**.

> Particularly important for agent-generated code, where the "author"
> cannot be consulted for explanation.

### Test 4: The Delete Test

- [ ] If you deleted this abstraction and **inlined the logic**,
      would the code be **simpler**?
- [ ] If yes → the abstraction is **not justified**. Delete it.

---

## Verdict

| Tests failed | Verdict |
| --- | --- |
| 0 | Abstraction is justified. |
| 1 | Reviewer's judgment — may be borderline. |
| **2 or more** | **Flag for simplification.** Refactor before merge. |

The refactoring is not cosmetic — it is a deliberate reduction of
technical debt that makes the codebase more comprehensible and more
maintainable.

---

## What Triggers This Review

The simplicity review is most useful when you see any of the
following in agent-generated code:

- **Wrapper classes** that add no functionality
- **Adapter layers** that transform data from one format to an
  identical format
- **Factory methods** that construct a single concrete type
- **Abstract base classes** with a single implementation
- Pattern names appearing in class names ("StrategyFactory",
  "ManagerService", "HandlerWrapper") — these are signals, not
  always defects, but worth reviewing.

Each of these patterns has legitimate uses in specific contexts. But
an agent does not distinguish between "this pattern is appropriate
here" and "this pattern exists in my training data and could be
applied here." The result is pattern overuse — code that is
structurally complex without being functionally complex.

## What This Review Is NOT

- **Not** a stylistic preference for terse code. Long, clear code
  passes all four tests.
- **Not** an objection to all abstraction. Deep modules (complex
  internals, simple interfaces) pass all four tests trivially.
- **Not** an objection to design patterns generally. The Strategy
  pattern with three real strategies passes; the Strategy pattern
  with one strategy fails.

## Related

- `../prompts/disprove-only-review.md` — the broader review that this
  checklist supplements
- `../spec-templates/impl-notes-md.md` — flag findings here as debt
  register items at "should-fix-soon" severity at minimum
- `integration-verification-checklist.md` — refactoring-pass step in
  Standard 8 covers similar ground at integration time

## Provenance

Adapted from Chapter 9 of *Harnessing the Horse*, Section 9.2. The
deep module concept is from John Ousterhout, *A Philosophy of
Software Design*, Yaknyam Press, 2018. The four tests are the book's
operationalization for agentic development.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
