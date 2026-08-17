# Task Specification Template

> **Chapter:** ch06 — Task Division and Agent Scope (Standards 2, 4–5)
> **Last revised:** 2026-06-16
> **Use this for:** Decomposing a SPEC.md into agent-sized tasks. One
> task per file. One file per agent session.

Each task must be completable in a single agent session (30–60 minutes
of agent time), produce output reviewable in under 60 minutes (fewer
than 400 lines of changed code), and have explicit interfaces consumed
and produced.

---

```markdown
# Task [N]: [short task name]

## Files

- [path/to/file] — [create / modify]
- [path/to/file] — [create / modify]

## Interfaces Produced

[What this task creates that other tasks/services will consume. Be
precise. An AI agent reading an API contract will implement exactly
what is specified and hallucinate what is not.]

- [function signature, REST endpoint, event schema, etc.]

## Interfaces Consumed

[What this task depends on from elsewhere. Reference the producing task
where applicable.]

- [function signature, endpoint, schema] — produced by [Task N or
  existing module path]

## Dependencies

### External
- [package@exact-version] — already in manifest, or new (justify in
  IMPL_NOTES.md)

### Internal
- [module path] — existing
- [shared service] — accessed via [defined integration interface, not
  direct import]

### Implicit
- Database schema: [tables/columns read or written]
- Environment variables: [VAR_NAME — type — default]
- External APIs: [endpoint — version — availability expectations]

## MUST-NOT

- MUST-NOT [scope-specific prohibition]
- MUST-NOT [scope-specific prohibition]
- MUST-NOT modify files outside the Files list above
- MUST-NOT change existing public API signatures
- MUST-NOT add dependencies not listed above

## Definition of Done

[Binary criteria. Each is either met or not met. Derived from SPEC.md
acceptance criteria but scoped to this task.]

- [ ] [Binary criterion 1]
- [ ] [Binary criterion 2]
- [ ] [Binary criterion 3]
- [ ] Project linter passes
- [ ] Project test suite passes
- [ ] Post-generation verification checklist completed (see below)

## Estimated Output

~[N] lines of code. If this exceeds 400 lines, decompose further before
generation.
```

---

## Post-Generation Verification Checklist

After the agent generates code, before merge, the agent (or the
engineer) runs through four checks:

1. **Scope Boundary.** List every file the agent created or modified.
   Compare against the Files list above. Any file outside scope is a
   deviation — stop and report.
2. **Interface Integrity.** Confirm no existing function signatures,
   API endpoints, or data schemas were modified unless explicitly
   specified in this task's scope.
3. **Dependency Delta.** List every import or dependency added,
   modified, or removed during generation. Compare against the
   pre-generation Dependencies list. Any delta must be pre-authorized
   or flagged for review.
4. **Constraint Check.** Review the MUST-NOT list. Confirm the
   generated code does not violate any constraint.

Present the verification report alongside the generated code. Any
deviation must be explicitly documented and justified.

---

## Worked Example: User Search Endpoint (Five Tasks)

For a full worked example showing how a single feature ("add user
search to the User service") decomposes into five tasks of ~30–120
lines each, see Chapter 6, Section 6.3 in the book.

The naive single-session prompt for this feature would produce 400–800
lines across the controller, service, repository, test files, database
migration, and audit integration — internally consistent but externally
coupled, with two hours of review time spanning four architectural
layers.

The disciplined decomposition produces five clean, verifiable PRs
instead of one sprawling PR. Total cost of decomposition: ~30 minutes
of design time. The economics are not close.

## The Three Standards This Template Implements

- **Standard 2 — Scope Definition and Session Boundaries.** One task,
  one session, one reviewable unit. No "while I'm here" expansion.
- **Standard 4 — Interface-First Design.** Define the contracts (the
  Interfaces Produced and Consumed sections) before implementing the
  behavior. If the interface is not explicit, it does not exist.
- **Standard 5 — Dependency Discipline.** Every external, internal,
  and implicit dependency declared. If it is not in the manifest, it
  does not exist.

## Related

- `spec-md.md` — the SPEC.md this task is decomposed from
- `../prompts/structured-prompt.md` — the generation prompt that
  consumes this task spec
- `../prompts/disprove-only-review.md` — the review prompt that
  verifies output against this task spec

## Provenance

Adapted from Chapters 5 and 6 of *Harnessing the Horse*, Standards 2,
4, and 5.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
