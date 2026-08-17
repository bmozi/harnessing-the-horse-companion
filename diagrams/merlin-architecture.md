# Merlin Software Factory: Historical Architecture Note

> **Historical comparison only.** This note preserves the lesson of Merlin's
> original multi-agent pipeline without publishing its former implementation
> topology. For the current operating model, read the
> [public teaching architecture](merlin-architecture-v2.md).

## What the Original Blueprint Tried to Achieve

The original factory divided discovery, design, implementation, review,
deployment, and learning among multiple specialized agents connected by an
explicit pipeline. The design made governance visible and treated every
quality concern as a named checkpoint.

That architecture produced valuable prompt discipline, review criteria,
observability practices, memory patterns, and bounded-rework rules. It also
revealed a structural problem: every additional handoff created another place
to lose context, duplicate reasoning, stall execution, or confuse ownership.

## What Changed

| Original tendency | Current direction |
| --- | --- |
| Several specialized agents on the critical path | One accountable agent owns the delivery arc. |
| Quality represented mainly as orchestrated handoffs | Deterministic checks, independent proof, and async observers preserve rigor. |
| Process completion emphasized | Shipped, reviewable outcomes and clean human handoffs matter. |
| Learning stages could delay completion | Learning and improvement move outside the delivery path when safe. |
| More states and coordinators appeared safer | Simpler ownership and bounded recovery reduce failure modes. |

## The Durable Lesson

The pivot did not discard engineering discipline. It moved that discipline to
the places where it creates leverage: a strong single-agent prompt, executable
proof, explicit safety boundaries, observable state, independent challenge,
and verified learning.

The detailed historical diagrams and implementation snapshots are retained in
the author's private research archive. They are not part of the public
companion distribution.
