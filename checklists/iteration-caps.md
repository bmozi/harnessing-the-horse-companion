# Iteration Caps Checklist (Bounded Iteration Discipline)

> **Chapter:** ch16 — Case Study: The Merlin Software Factory
> (Section 16.1, "Gates, Bounds, and Backends")
> **Last revised:** 2026-06-16
> **Use this for:** Configuring every loop in an agent-driven
> system so failure is cheap and visible, not expensive and silent.

Every loop in the system — gate rework, CI fix, agent retries — has
a **hard maximum iteration count**.

These bounds implement the blast-radius containment that Standard 5
(Chapter 6) prescribes. **An agent session that enters a rework
loop without bounded iteration can consume thousands of dollars in
API costs producing increasingly divergent output.**

The bounds ensure that failure is **cheap and visible** — a session
that exhausts its iteration count surfaces the failure to the
operator rather than continuing to thrash.

---

## The Standard Caps (from the Merlin Software Factory)

These are the bounds that worked in practice. Tune to your context,
but **start conservative**; relaxation should be data-driven.

| Loop | Cap | Rationale |
| --- | --- | --- |
| **CI fix iterations** | **2** | Diminishing returns set in after the second attempt. A third attempt almost never converges. |
| **Agent tool-use iterations** | **25** | Far above normal task length; serves as a runaway guard, not a normal limit. |
| **Self-improvement proposals per day** | **5** (or **3** for proactive discoverers) | Small enough that a single operator can review every proposal in a morning. |
| **Daily token budget per session** | Project-specific | Forces visibility of cost. A session that exhausts its budget surfaces the failure. |

---

## Configuration Checklist

For every loop or retry mechanism in your system, answer all four
questions:

### Loop 1: [name the loop]

- [ ] What does this loop do? [one sentence]
- [ ] What is the maximum iteration count? [number]
- [ ] What is the cost per iteration? [tokens / API calls /
      seconds]
- [ ] What happens when the cap is reached?
  - [ ] Failure surfaces to the operator with the iteration history
  - [ ] No silent retry beyond the cap
  - [ ] Partial state is recoverable (no permanent corruption)

### Loop 2: [name the loop]

(Repeat the four questions.)

### Loop 3: [name the loop]

(Repeat.)

---

## The "Failure Should Be Cheap and Visible" Discipline

When a session exhausts its iteration count:

- [ ] The failure is **surfaced** — the operator sees what was
      attempted, what failed, and what the iteration history was
- [ ] The failure is **inexpensive** — the cap was low enough that
      the wasted cost is acceptable as a learning signal
- [ ] The failure is **recoverable** — no permanent state corruption
      from the partially-completed work
- [ ] The failure leaves a **diagnostic trail** — logs, partial
      artifacts, and iteration history are preserved for the
      operator to investigate

If any of these four properties is missing, **the cap is set
wrong** — either too high (cost > learning signal), too low (cap
fires before the work could plausibly have completed), or the
cleanup is incomplete.

## The Anti-Patterns to Watch For

### The "just one more retry" loop

A retry policy that increases the cap when the work "is close to
completing" is a retry policy that does not have a cap. The cap is
hard. If a retry needs more attempts, the *task* needs to be
redesigned, not the cap relaxed.

### The unbounded "background" loop

A background process that does not have a maximum cycle count or
a maximum duration. Background loops should fail visibly too — a
silent background loop that runs forever consuming API budget is
indistinguishable from a healthy system until the bill arrives.

### The cap that fires after the damage is done

A cap that fires *after* the destructive action (charge, send,
delete) has been retried 5 times. The cap must fire **before** the
destructive action retries past a safe threshold. See
[`../patterns/cas-guarded-distributed-commit.md`](../patterns/cas-guarded-distributed-commit.md)
for the per-step idempotency discipline that pairs with iteration
caps.

### The cap with no observability

A cap that fires silently into a logs directory nobody reads.
Caps firing must alert. A cap that fires is a signal that
something is wrong; treating it as routine guarantees the next
genuine failure is invisible.

## Worked Example: Merlin Quality-Gate Rework

From the Merlin Software Factory (ch16):

- **CI fix iterations capped at 2**. Standard 9's "max 2 CI fix
  iterations — bounded iteration, diminishing returns."
- **Agent tool-use loops cap at 25 iterations.** A normal task uses
  3–10 iterations; the cap is a runaway guard.
- **Daily token budgets** enforced at the session level. A session
  that hits its budget gracefully exits with partial state and
  surfaces to the operator.
- **Self-improvement proposals capped at 5 per day.** Small enough
  that a human can review every proposal in a morning; large enough
  to allow meaningful progress.

The system gracefully surfaces a `partial_completion` state with the
full iteration history when caps fire — see
[`../patterns/express-arc.md`](../patterns/express-arc.md) for the
companion pattern.

## Related

- [`../patterns/express-arc.md`](../patterns/express-arc.md) — the
  single-agent delivery pattern that requires this iteration
  discipline
- [`../patterns/cas-guarded-distributed-commit.md`](../patterns/cas-guarded-distributed-commit.md)
  — pair the iteration cap with per-step idempotency so retries
  are safe
- [`../prompts/escalation-protocol.md`](../prompts/escalation-protocol.md)
  — what to do when caps fire and the work is genuinely blocked
- [`self-improvement-safety-rails.md`](self-improvement-safety-rails.md)
  — companion governance for autonomous self-improvement systems

## Provenance

Adapted from Chapter 16 of *Harnessing the Horse*, Section 16.1.
The specific caps (2 CI fix iterations, 25 tool-use iterations, 5
self-improvement proposals/day) are from the Merlin Software
Factory.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
