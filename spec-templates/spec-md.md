# SPEC.md Template

> **Chapter:** ch05 — Discovery and Planning (Standard 1: Requirements
> as Verifiable Contracts)
> **Last revised:** 2026-06-16
> **Use this for:** Writing the specification document before any code
> generation session begins.

The SPEC.md is the contract between intent and implementation. It is the
document the prompt references — not the prompt itself. Six months from
now, the prompt is gone; the SPEC.md is still there.

The minimum viable SPEC.md has six sections. A ten-line spec that
clearly states the acceptance criteria and the MUST-NOT list is worth
more than a ten-page spec that describes the problem without defining
the constraints.

---

```markdown
# SPEC: [feature or change name]

## Problem Statement

[What problem does this solve? Who experiences it? What is the current
workaround? The problem statement must be specific enough that two
engineers would independently agree on whether the problem has been
solved.]

[Counter-example: "Improve the user experience" — not a problem
statement.]
[Example: "The /api/users endpoint returns HTTP 500 when the bearer
token is malformed; it should return HTTP 401 with a descriptive error
message." — a problem statement.]

## Proposed Solution

[One paragraph describing the approach. Not a design document — a
directional statement that establishes the general approach before the
engineer invests in detailed design. Reference existing architecture
from CLAUDE.md / AGENTS.md so the approach is compatible with the
system's current structure.]

## Acceptance Criteria

[Numbered list of binary conditions. Each criterion is either met or
not met. No subjective language. Each criterion must be translatable
into a test assertion, API contract check, or measurable performance
threshold — the acceptance-criteria half of Standard 1; see
`acceptance-criteria-template.md`.]

1. [Binary, testable criterion]
2. [Binary, testable criterion]
3. [Binary, testable criterion]

Counter-examples to avoid:
- "The endpoint should be fast" — not testable.
- "The UI should look good" — not testable.

Replacement examples:
- "The endpoint responds within 200ms at the 99th percentile under the
  standard load test."
- "The UI matches the Figma mockup in design-doc-47 at all breakpoints
  defined in the design system."

## MUST-NOT List

[Explicit constraints on what the implementation must not do. This is
the most critical section and the most commonly omitted. An empty
MUST-NOT list is a red flag — it means either you have not thought
about failure modes, or you are so experienced with the codebase that
the constraints are invisible to you. In the second case, the
constraints are also invisible to the agent — which is exactly the
problem.]

Address all six categories. Delete any that are genuinely not
applicable, with a one-line note explaining why.

### Architectural boundaries
- MUST-NOT [modify which modules, services, or layers]

### Dependency constraints
- MUST-NOT [add, upgrade, or replace which packages]

### Data constraints
- MUST-NOT [access which tables, schemas, or data stores directly]

### Security constraints
- MUST-NOT [perform which operations — raw SQL, eval, dynamic imports,
  etc.]

### Performance constraints
- MUST-NOT [use which patterns — N+1 queries, synchronous I/O in hot
  paths, etc.]

### Behavioral constraints
- MUST-NOT [change which existing behaviors — backward compatibility
  requirements]

## Out of Scope

[What this feature explicitly does not include. The fence that prevents
helpful overreach from the agent. If the spec says "add a new API
endpoint for user search," the agent may helpfully also add a user
analytics dashboard, a search indexing service, and a cache invalidation
strategy — each individually reasonable, collectively a tripled review
burden.]

- [Specific capability that is NOT part of this change]
- [Specific capability that is NOT part of this change]

## Affected Components

[The files, modules, and architectural boundaries this change touches,
cross-referenced with the architecture diagrams. This forces blast
radius thinking before generation begins.]

- [path/to/file or module] — [what kind of change]
- [path/to/file or module] — [what kind of change]
```

---

## Areas of Critique

When reviewing a SPEC.md — your own or a teammate's — apply these
questions:

1. Is the problem statement specific enough that two engineers would
   agree on whether it is solved? If the answer is "it depends," the
   problem statement is insufficiently precise.
2. Are the acceptance criteria truly binary? Search for subjective
   language: "should be fast," "should handle edge cases," "should be
   user-friendly." Each is a criterion-shaped opinion, not a criterion.
   Replace each with a measurable condition.
3. Does the MUST-NOT list address the most likely failure modes for
   this type of change? If the change touches the database, are there
   data constraints? If it touches authentication, are there security
   constraints?
4. Is the scope narrow enough to be completed in a single agent
   session, or a well-defined set of sessions? If the answer is
   "probably two or three sessions, depending on how it goes," the
   scope needs further decomposition — see `task-spec.md`.

## Related

- `task-spec.md` — decompose the SPEC into agent-sized tasks
- `cagan-four-risk-assessment.md` — for complex features, supplement
  the spec with explicit risk assessment
- `../prompts/structured-prompt.md` — the prompt the SPEC feeds into

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Standard 1
(Requirements as Verifiable Contracts). The Merlin Software Factory experience
showed that the most costly defects in AI-generated code came not from
what the code did wrong, but from what it should not have done at all.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
