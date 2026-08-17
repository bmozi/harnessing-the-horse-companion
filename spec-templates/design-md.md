# DESIGN.md: Agent Execution Contract

> **Chapter:** ch04 - Foundations (Section 4.6, the four pipeline
> artifacts)
> **Last revised:** 2026-08-16
> **Use this for:** Converting an approved SPEC into a reviewable technical
> design before any agent generation session begins.

A useful design document does more than describe an approach. It fixes the
decisions an agent must not reinterpret, identifies the decisions the agent may
make, and states what evidence will prove the implementation matches the
design.

That makes DESIGN.md an **agent execution contract**:

- the SPEC defines the outcome and constraints;
- the DESIGN fixes architecture, interfaces, failure behavior, and proof;
- the task specification bounds one implementation session;
- IMPL_NOTES records what changed when reality challenged the design;
- REVIEW verifies the result against all four artifacts.

## When to Use It

Use the full template when a change crosses a module boundary, changes an
interface or data model, introduces operational risk, or leaves consequential
choices open to an implementation agent.

For a small, local change, complete at least: references and ownership,
traceability, invariants, approach and change surface, verification, agent
execution contract, and open decisions. Mark other sections `N/A` with one
sentence explaining why. Empty headings are not evidence.

Do not use this document to repeat the SPEC, paste implementation code, or
manufacture certainty before inspecting the repository.

---

```markdown
# DESIGN: [Feature or Change Name]

## 1. References and Decision Ownership

- SPEC: [stable link]
- Blast-radius assessment: [stable link]
- Relevant architecture diagrams / ADRs: [links]
- Design owner: [name and role]
- Required approver: [name and role]
- Status: [Draft / Approved / Superseded]
- Last evidence review: [YYYY-MM-DD]

## 2. Evidence Read Before Design

Record the project facts that shaped this design. An uninspected interface or
assumed convention becomes a `VERIFY` item, not a fact.

| Source | Relevant fact | How verified | Freshness / limitation |
| --- | --- | --- | --- |
| `[path, diagram, ADR, test, metric]` | [fact] | [inspection or command] | [date or limitation] |

## 3. Acceptance-Criterion Traceability

Every acceptance criterion must reach a design element and a proof mechanism.
No orphaned criterion may proceed to generation.

| Criterion | Designed behavior | Component / interface | Planned evidence |
| --- | --- | --- | --- |
| AC-1 | [behavior] | [boundary] | [test, gate, or measurement] |

## 4. Invariants and Boundaries

State what must remain true while the system changes. Carry forward every
relevant SPEC MUST-NOT constraint.

### Invariants

- [Property that must remain true before, during, and after the change]
- [Compatibility, ordering, atomicity, authorization, or latency invariant]

### Boundaries

- [Module / layer] may depend on [allowed dependency] and MUST NOT depend on
  [forbidden dependency].
- [Data or authority boundary the implementation must not cross]

## 5. Chosen Approach

[Explain the design in enough detail that a reviewer can challenge it before
code exists. Name the pattern, flow, ownership boundaries, and why the approach
fits the inspected system.]

## 6. Change Surface

| Component / path | Current responsibility | Proposed change | Why it belongs here |
| --- | --- | --- | --- |
| `[module or path]` | [current role] | [change] | [boundary rationale] |

Explicitly list surfaces inspected but intentionally unchanged:

- `[surface]` remains unchanged because [evidence-backed reason].

## 7. Interface Contracts

Link the detailed interface specification where one exists. For every changed
interface, record:

- exact request, response, function, or event shape;
- error and timeout behavior;
- compatibility rule and versioning strategy;
- producer and consumers;
- authorization boundary;
- contract test or other verification method.

Unauthorized interface changes are stop conditions, not implementation
latitude.

## 8. Data Lifecycle and Migration

- Data created, read, updated, or deleted: [list]
- Classification / sensitivity: [classification]
- System of record and owner: [system and owner]
- Atomicity and consistency requirement: [requirement]
- Migration / backfill sequence: [sequence or N/A with reason]
- Coexistence and sync-loop protection: [mechanism or N/A]
- Retention and deletion behavior: [rule]
- Rollback data implications: [what is reversible and what is not]

## 9. Dependency and Capability Delta

| Dependency / capability | Existing or new | Approved version / interface | Reason | Removal or exit condition |
| --- | --- | --- | --- | --- |
| [name] | [existing/new] | [exact version or contract] | [need] | [condition] |

An empty delta means no dependency or new runtime capability is authorized.

## 10. Failure, Recovery, and Convergence

| Failure or trigger | Expected system behavior | Detection | Recovery / rollback | Owner |
| --- | --- | --- | --- | --- |
| [credible failure] | [bounded behavior] | [signal] | [action] | [role] |

Include partial failure, retry and idempotency behavior, timeout handling,
repeated-failure limits, and the point where automation must stop for a human.

## 11. Security, Privacy, and Abuse Cases

- Trust boundaries crossed: [boundaries]
- Minimum authority required: [permissions / scopes]
- Untrusted inputs and validation: [inputs and controls]
- Sensitive data exposure: [risk and control]
- Abuse or misuse case: [case and defense]
- Secret and credential lifecycle: [creation, use, rotation, revocation]
- Security evidence required: [test, scan, review, or threat model]

## 12. Observability and Operational Readiness

| Signal | Baseline | Success / failure threshold | Operator action | Owner |
| --- | --- | --- | --- | --- |
| [metric, log, trace, alert] | [value] | [threshold] | [action] | [role] |

State how operators distinguish healthy behavior, degraded behavior, and a
failed rollout without reading source code.

## 13. Verification, Rollout, and Rollback

| Claim to prove | Test / gate | Environment or fixture | Evidence retained | Classification |
| --- | --- | --- | --- | --- |
| [AC, invariant, boundary, or risk] | [check] | [where] | [artifact / result] | [BLOCKING / CONDITIONAL / ADVISORY / ASYNC] |

- Rollout sequence: [stages]
- Go / no-go authority: [name or role]
- Rollback trigger: [measurable condition]
- Rollback procedure: [tested steps or stable link]
- Irreversible step, if any: [step and required approval]

## 14. Agent Execution Contract

### Fixed decisions

The implementation agent must follow these choices exactly:

- [pattern, interface, boundary, migration order, or existing utility]

### Permitted latitude

The agent may choose among these implementation details without redesign:

- [local naming, private helper structure, equivalent test organization]

### Stop and escalate

The agent must stop and request a design decision if:

- inspected code contradicts a stated design fact;
- satisfying one criterion would violate another criterion or MUST-NOT rule;
- an interface, dependency, permission, data migration, or file outside the
  approved surface must change;
- required evidence cannot be produced;
- repair exceeds the project's time or iteration cap.

## 15. Human Decisions and `VERIFY` Items

| Item | Why automation cannot decide it | Evidence needed | Owner | Due before |
| --- | --- | --- | --- | --- |
| [decision or unknown] | [judgment boundary] | [evidence] | [person / role] | [generation / merge / release] |

No blocking `VERIFY` item may silently become an agent assumption.

## 16. Alternatives and Tradeoffs

| Alternative | Advantage | Cost / risk | Evidence considered | Disposition |
| --- | --- | --- | --- | --- |
| [option] | [benefit] | [cost] | [source] | [chosen / rejected / deferred] |

Record what the chosen approach gives up. This prevents a future agent from
"improving" the design toward an option already rejected for a known reason.

## 17. Residual Risks

| Risk | Likelihood / consequence | Mitigation | Detection | Accepted by |
| --- | --- | --- | --- | --- |
| [risk remaining after controls] | [assessment] | [control] | [signal] | [name / role or unresolved] |

## Design Completion Gate

- [ ] Every acceptance criterion maps to designed behavior and planned proof.
- [ ] Relevant SPEC MUST-NOT rules appear as invariants or boundaries.
- [ ] Changed interfaces, data, dependencies, permissions, and operational
      behavior are explicit.
- [ ] Failure, rollback, and human-escalation behavior are defined.
- [ ] Fixed decisions and permitted agent latitude are distinguishable.
- [ ] Every blocking `VERIFY` item has an owner and due point.
- [ ] The reviewer can explain how the implementation will be disproved if it
      is wrong.
```

---

## The Value Test

Every completed section must do at least one of four things:

1. fix a design decision;
2. constrain what the agent may change;
3. define evidence for a gate;
4. identify a decision that belongs to a human.

If a paragraph does none of these, delete it. A shorter design with explicit
decisions is stronger than a longer design full of description.

## Common Failure Modes

- **The decorative design.** It summarizes the intended code but creates no
  constraints or proof obligations.
- **The orphaned criterion.** A SPEC criterion has no component responsible for
  it or no planned evidence.
- **The hidden redesign.** The document leaves consequential choices open, so
  the implementation agent silently becomes the architect.
- **The rollback fantasy.** A rollback is named but its data effects,
  irreversible steps, and trigger are absent.
- **The evidence-free `N/A`.** A section is deleted because it is inconvenient,
  not because repository evidence shows it is irrelevant.
- **The stale fact.** An old ADR or assumed interface is treated as current
  without inspection.

## Related

- [`spec-md.md`](spec-md.md) - defines the outcome and constraints
- [`blast-radius-template.md`](blast-radius-template.md) - estimates affected
  systems before design
- [`interface-spec.md`](interface-spec.md) - expands changed contracts
- [`task-spec.md`](task-spec.md) - bounds the implementation sessions
- [`impl-notes-md.md`](impl-notes-md.md) - records deviations and discoveries
- [`review-md.md`](review-md.md) - verifies the implementation against the
  design
- [`../checklists/rollback-readiness-checklist.md`](../checklists/rollback-readiness-checklist.md)
  - tests rollback credibility

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.6. The explicit
agent-execution contract, acceptance-to-evidence traceability, fixed-decision
versus permitted-latitude boundary, and human-decision register are companion
extensions for applying the book's Harness Framework.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
