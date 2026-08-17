# Structured Generation Prompt

> **Chapter:** ch07 — Generation, Verification, and Review (Standard 1
> generation practice: the structured generation contract)
> **Last revised:** 2026-06-16
> **Model assumed:** Frontier model (Claude Sonnet 4.6+, GPT-4-class)
> **Feeds from:** `../spec-templates/task-spec.md`

This is the prompt that consumes a task specification and produces
reviewable code. The structure is not optional — it is the precision
instrument that directs the model's attention to the constraints that
matter.

Every section is required. An empty section is a bug. A missing
MUST-NOT list is the single most reliable predictor of scope drift.

---

```markdown
## Task
[One-sentence description of what to implement.]

## Functional Requirements
- [ ] [Testable requirement 1]
- [ ] [Testable requirement 2]
- [ ] [Testable requirement 3]

## Constraints

### Interface
- Implement the interface defined in [file:line]
- Accept inputs as: [type definitions]
- Return outputs as: [type definitions]
- Error responses must follow [RFC 7807 / project error contract]

### Dependencies
- ALLOWED: [list of approved packages with version constraints]
- MUST-NOT introduce: [list of prohibited packages]
- MUST-NOT add new dependencies without documenting the rationale in
  IMPL_NOTES.md

### Patterns
- Follow [Hexagonal Architecture / Repository Pattern / etc.] as
  established in [reference file]
- Place business logic in [domain layer path]
- Place infrastructure concerns in [adapter layer path]

### Security
- All user input must be validated at the [boundary layer] before
  reaching domain logic
- [Specific auth/authz requirements]
- No secrets in source; use [environment variable / vault reference
  pattern]

### Performance
- Response latency budget: [Xms at p99]
- Memory allocation budget: [limit]

## MUST-NOT List
- MUST-NOT modify files outside [scope boundary]
- MUST-NOT change existing public API signatures
- MUST-NOT add global state or singletons
- MUST-NOT bypass the [error handling / logging / auth] middleware
- MUST-NOT use [specific anti-patterns relevant to context]

## Output Format
- Place implementation in: [directory path]
- Place tests in: [directory path]
- Include: unit tests for all public methods, integration test for the
  happy path
- Update IMPL_NOTES.md with: what you built, what tradeoffs you made,
  what you were uncertain about

## Review Criteria
The reviewer will evaluate:
1. Does the implementation satisfy every functional requirement?
2. Does it violate any constraint or MUST-NOT item?
3. Are edge cases (empty input, max-size input, concurrent access,
   network failure) handled?
4. Is the error handling consistent with the project's error contract?
5. Do the tests actually verify the requirements (not just exercise the
   code)?
```

---

## Areas of Critique

When reviewing a prompt's compliance with this standard, examine:

- **Completeness of the MUST-NOT list.** An empty or perfunctory
  MUST-NOT list is the single most reliable predictor of scope drift.
  If you could not think of anything the agent should avoid, you have
  not thought carefully enough about the boundaries of the task.
- **Testability of requirements.** "The system should handle errors
  gracefully" is not testable. "When the upstream service returns HTTP
  503, the handler must return HTTP 502 with a retry-after header
  calculated from the circuit breaker state" is testable. The
  difference is the difference between a spec and a wish.
- **Alignment between review criteria and constraints.** If the prompt
  specifies latency budgets but the review criteria do not include
  performance verification, the constraint is unenforceable. Every
  constraint must trace to a review criterion.
- **Scope creep signals.** Watch for prompts that bundle unrelated
  concerns: "implement the payment endpoint and also clean up the
  logging configuration and fix that flaky test." Each is a separate
  agent session.

## Common Failure Modes

- **The "You Know What I Mean" Prompt.** Three sentences of context,
  expecting the agent to infer the rest from the codebase. The agent
  obliges — and infers incorrectly. Fix: write the convention down, in
  the prompt, every time.
- **The Copy-Paste Prompt.** Reusing a prompt from a previous task,
  changing only the functional requirements. The previous task's
  constraints do not apply, but nobody notices until review.
- **The Constraint-Free MUST-NOT List.** A single entry like "MUST-NOT
  introduce breaking changes." This constrains nothing. Effective
  MUST-NOT items are specific: "MUST-NOT modify the `events` table
  schema."
- **The Missing Performance Constraint.** Functional requirements
  thorough, performance silent. The agent generates code that is
  functionally correct and catastrophically slow.

## Related

- `../spec-templates/task-spec.md` — the task spec that feeds this
  prompt
- `disprove-only-review.md` — the review prompt that closes the loop
- `adversarial-validation.md` — second-agent review for high-risk
  changes
- `subagent-challenge-clauses.md` — clauses to embed inside this
  prompt for proactive uncertainty surfacing

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 1. In the
Merlin Software Factory, structured prompts are not written by hand —
they are generated from pipeline artifacts (SPEC.md, CLAUDE.md, the
module's interface definitions, and the dependency manifest).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
