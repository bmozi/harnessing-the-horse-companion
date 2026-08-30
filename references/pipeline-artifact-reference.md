# Pipeline Artifact Reference

The four artifacts of the agentic delivery pipeline, printed
in full for in-book reference. The expanded versions with usage
guidance live in the companion repository
(`spec-templates/spec-md.md`, `spec-templates/design-md.md`,
`spec-templates/impl-notes-md.md`, `spec-templates/review-md.md`).

Use these as the canonical artifact shapes when starting a new
project. Project conventions may extend the templates; they
should not omit the required sections. For SPEC.md, the
six required sections of Standard 1 (Problem Statement,
Proposed Solution, Acceptance Criteria, MUST-NOT List, Out of
Scope, Affected Components) are all present. DESIGN.md must
retain Tradeoffs; REVIEW.md must retain Disposition. Every
template carries the provenance footer required by DN6
(Chapter 10).

---

## SPEC.md

```markdown
# SPEC: [feature or change name]

## Status
Draft | In Review | Approved | Superseded by [link]

## Owner
[Name and role]

## Date
[Created date] | Last updated: [date]

## Problem Statement
[Specific enough that two engineers would independently agree
on whether the problem has been solved. Who experiences it?
What is the current workaround? What is the cost of leaving
it unsolved?]

## Proposed Solution
[One paragraph describing the approach. Directional, not
detailed — design lives in DESIGN.md. Reference existing
architecture from the context file (AGENTS.md / CLAUDE.md) so
the approach is compatible with the system's current
structure.]

## Acceptance Criteria
Binary, machine-readable per Standard 1. Each criterion is
either met or not met — no subjective language.
- [ ] AC-1: [Observable, executable condition — translatable
      to a test assertion, contract check, or measurable
      threshold]
- [ ] AC-2: [Observable condition]
- [ ] AC-3: [Observable condition]

## MUST-NOT List
All six categories must be addressed (Standard 1). An empty
category is an explicit statement that no constraint applies,
not an oversight.

### Architectural boundaries
- MUST-NOT [modify which modules, services, or layers]

### Dependency constraints
- MUST-NOT [add, upgrade, or replace which packages]

### Data constraints
- MUST-NOT [access which tables, schemas, or data stores
  directly]

### Security constraints
- MUST-NOT [perform which operations]

### Performance constraints
- MUST-NOT [use which patterns]

### Behavioral constraints
- MUST-NOT [change which existing behaviors]

## Out of Scope
- [Specific capability that is NOT part of this change]
- [Specific capability that is NOT part of this change]

## Affected Components
Cross-referenced with the architecture diagrams maintained
per Chapter 4.
- [path/to/file or module] — [what kind of change]
- [path/to/file or module] — [what kind of change]

---
<!-- Provenance footer (DN6, Chapter 10) -->
- SPEC reference: [self]
- Session ID: [agent session identifier, if AI-assisted]
- Model identifier: [model + version, if AI-assisted]
- Author: [engineer name]
- Reviewer: [name and date, on approval]
```

---

## DESIGN.md

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

---
<!-- Provenance footer (DN6, Chapter 10) -->
- SPEC reference: [path to SPEC.md]
- Session ID: [agent session identifier, if AI-assisted]
- Model identifier: [model + version, if AI-assisted]
- Author: [engineer name]
- Reviewer: [name and date, on approval]
```

---

## IMPL_NOTES.md

```markdown
# IMPL_NOTES: [Feature or Change Name]

## Spec Reference
[Link to SPEC.md]

## Design Reference
[Link to DESIGN.md]

## Implementation Log

### [Date/Time]
- Implemented [component]. Followed the design as specified.
- Deviated from design in [area]: [description of deviation
  and reason].
- Discovered constraint: [something learned during
  implementation that the spec/design did not anticipate].
- Tech debt introduced: [description of shortcut taken and
  why, with ticket reference for remediation].
- Agent uncertainty: [area where the agent was uncertain and
  the implementing engineer made a judgment call].

### [Date/Time]
- [Continue logging as implementation proceeds]

## Deviations from Design
[Summary list of all deviations, with rationale for each]

## Discovered Constraints
[Summary list of constraints discovered during implementation
that were not in the spec or design]

## Tech Debt Register

### Must-fix-before-merge (BLOCKING)
- [Items unacceptable in production — hardcoded credentials,
  missing error handling on critical paths, placeholder
  implementations, known security vulnerabilities]

### Should-fix-soon
- [Items acceptable for initial merge but tracked with
  specific remediation deadlines]

### Can-defer
- [Items acknowledged, documented, and deprioritized for
  batch resolution during refactoring cycles]

---
<!-- Provenance footer (DN6, Chapter 10) -->
- SPEC reference: [path to SPEC.md]
- DESIGN reference: [path to DESIGN.md]
- Session ID(s): [agent session identifier(s)]
- Model identifier: [model + version]
- Author: [engineer name]
- Commit(s): [commit hashes, linked to specific code locations
  per DN6]
```

---

## REVIEW.md

```markdown
# REVIEW: [Feature or Change Name]

## Spec Reference
[Link to SPEC.md]

## Reviewer
[Name and role — must not be the implementing engineer]

## Review Date
[Date]

## Question 1 — Does it compile and pass the automated gates?
Per Standard 7, Question 1 is a prerequisite. If any BLOCKING
gate fails, the review does not start.
- [ ] Compilation / type-check: PASS / FAIL
- [ ] Unit tests: PASS / FAIL
- [ ] Security scan: PASS / FAIL (findings: [count by severity])
- [ ] Architecture boundaries: PASS / FAIL
- [ ] Adversarial validation (Std 7, agent mode): PASS / FAIL
      (findings: [count by severity])
- [ ] ASYNC gates scheduled and tracked

## Question 2 — Does it do what the specification says it should do?
Traceability exercise per Standard 7. Every acceptance
criterion in SPEC.md must be mapped to its implementation and
its test.
- AC-1: [SATISFIED / NOT SATISFIED — implementation at
  file:line, test at file:line]
- AC-2: [SATISFIED / NOT SATISFIED — evidence]
- AC-3: [SATISFIED / NOT SATISFIED — evidence]

## Question 3 — Does it do anything the specification says it should NOT do, or anything the specification does not mention?
The disprove-only question. Enumerate every failure dimension
checked. A skipped dimension is itself a finding; record
"not applicable because [specific reason]" rather than
omitting it (Standard 7).

### The Eight Failure Dimensions (Standard 7, Chapter 7)
- [ ] MUST-NOT violations — for each item in the SPEC.md
      MUST-NOT list: COMPLIANT / VIOLATED with evidence
- [ ] Unauthorized side effects (network, file I/O, state
      mutation not in spec)
- [ ] Scope creep (functionality not described in spec)
- [ ] Hidden assumptions (hardcoded values, environment-
      specific behavior, magic numbers)
- [ ] Error handling gaps (null, empty, maximum, malformed,
      concurrent inputs)
- [ ] Security surface expansion (new endpoints, new input
      parsing, new privilege paths)
- [ ] Resource management (unclosed connections, unbounded
      allocations, missing timeouts)
- [ ] Concurrency (race conditions, deadlock potential,
      shared mutable state)

### Findings
Classify each as CRITICAL / MAJOR / MINOR with file:line
references and the failure scenario.

## Adversarial Validation Findings
[Findings from the adversarial agent (Standard 7, agent mode),
with disposition: FIXED / ACCEPTED / FALSE POSITIVE / DEFERRED]

## Disposition
- [ ] RECOMMEND_SHIP — requirements and MUST-NOT controls pass for this run
      (the accountable decision owner records the final outcome)
- [ ] RECOMMEND_REVISE — [specific revisions required; return to generation]
- [ ] RECOMMEND_STOP — [reason; return to design or spec phase]

## Sign-off
[Reviewer name, date]

---
<!-- Provenance footer (DN6, Chapter 10) -->
- SPEC reference: [path to SPEC.md]
- DESIGN reference: [path to DESIGN.md]
- IMPL_NOTES reference: [path to IMPL_NOTES.md]
- Adversarial review session ID: [agent session identifier]
- Model identifier: [model + version]
- Reviewer: [name]
- Merging engineer: [name, on approval]
```

---

The four artifacts compose a complete trail from intent to
deployment. The SPEC says what to build. The DESIGN says how.
The IMPL_NOTES says what actually happened. The REVIEW says
whether it is correct. Every line of production code should
trace through this sequence.

For per-section guidance, worked examples, and the rationale
behind each section's inclusion, see the `spec-templates/`
directory of the companion repository:
<https://github.com/bmozi/harnessing-the-horse-companion/tree/main/spec-templates>
