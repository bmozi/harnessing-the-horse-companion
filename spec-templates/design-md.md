# DESIGN.md Template

> **Chapter:** ch04 — Foundations (Section 4.6, the four pipeline
> artifacts)
> **Last revised:** 2026-06-16
> **Use this for:** The "how" document. Follows an approved SPEC.md;
> precedes any agent generation session.

The DESIGN.md is what distinguishes agentic development from "asking
the AI to code." Without it, the agent makes every design decision —
which data structures, which patterns, which module organization,
which API shape. With it, the agent implements a design a human
created, and the reviewer evaluates against a design a human approved.

**When created:** After SPEC.md is approved, before generation begins.
**Who creates it:** The architect, senior engineer, or implementing
engineer — whoever defines *how* the system will satisfy the spec.

---

```markdown
# DESIGN: [Feature or Change Name]

## Spec Reference
[Link to SPEC.md]

## Approach
[1-2 paragraphs: how this change will be implemented.
Which patterns, which modules, which layers.]

## Module Boundaries
[Which modules will be modified. How the changes respect the
architecture diagram. Any new modules being introduced.]

## Data Model
[New or modified tables, fields, types. Migration strategy if
schema changes are involved.]

## API Contracts
[New or modified endpoints, event schemas, or interface
definitions. Include request/response shapes.]

## Tradeoffs
[What alternatives were considered and why this approach was
chosen. This is the most important section — it captures the
design rationale that no other artifact preserves.]

## Risks
[What could go wrong with this approach. What assumptions does
it rely on. What is the blast radius if those assumptions are
wrong.]
```

---

## Why the Tradeoffs section deserves emphasis

This is the section most teams skip and that provides the most value.
When a future agent session encounters the code generated from this
design, the Tradeoffs section explains *why* the design was chosen —
which prevents the future agent from "improving" the code in a
direction the original design explicitly rejected.

## Related

- `spec-md.md` — the SPEC this design references
- `interface-spec.md` — fills in the API Contracts section
- `task-spec.md` — decomposes this design into agent-sized tasks
- `impl-notes-md.md` — captures deviations from this design during
  implementation

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.6.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
