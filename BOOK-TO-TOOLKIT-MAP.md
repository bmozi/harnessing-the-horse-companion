# Book-to-Toolkit Map

The toolkit helps you perform the work. *Harnessing the Horse* teaches you how
to judge the work. Use this map to keep the reusable artifact connected to the
reason it exists.

| Production-readiness step | Practice in this repository | Read in the book for the missing judgment | Proof you should leave behind |
| --- | --- | --- | --- |
| Frame the request | [`02-work-order-template.md`](factory-bootstrap/02-work-order-template.md) | Chapters 5–6: requirements, task division, interfaces, and blast radius | A bounded outcome, non-goals, owner, and stopping condition |
| Specify the change | [`spec-md.md`](spec-templates/spec-md.md) and [`design-md.md`](spec-templates/design-md.md) | Chapters 4–6: context, verifiable contracts, architecture, and implementation latitude | Acceptance criteria, invariants, prohibitions, and explicit human decisions |
| Bound the agent | [`01-context-file-checklist.md`](factory-bootstrap/01-context-file-checklist.md) and [`task-spec.md`](spec-templates/task-spec.md) | Chapters 4, 6, and 17: context hierarchy, scope, permissions, and security | Allowed files and tools, forbidden actions, interfaces, and escalation path |
| Build the smallest slice | [`structured-prompt.md`](prompts/structured-prompt.md) and [`04-session-loop-runbook.md`](factory-bootstrap/04-session-loop-runbook.md) | Chapters 7–8: generation, iteration, integration, and execution discipline | A traceable candidate plus implementation notes and test output |
| Challenge the claim | [`disprove-only-review.md`](prompts/disprove-only-review.md) and [`adversarial-validation.md`](prompts/adversarial-validation.md) | Chapters 7 and 10: falsification, review asymmetry, apprenticeship, and dissent | Findings that try to disprove correctness instead of merely describing it |
| Prove the release boundary | [`quality-gate-configuration-reference.md`](references/quality-gate-configuration-reference.md), [`deployment-safety-checklist.md`](checklists/deployment-safety-checklist.md), and [`rollback-readiness-checklist.md`](checklists/rollback-readiness-checklist.md) | Chapters 8, 12, and 17: gate strength, integration risk, migration, and security | Evidence bound to the candidate, unresolved limitations, and a recovery plan |
| Decide and learn | [`review-md.md`](spec-templates/review-md.md), [`06-metrics-baseline.md`](factory-bootstrap/06-metrics-baseline.md), and [`07-factory-readiness-review.md`](factory-bootstrap/07-factory-readiness-review.md) | Chapters 18–20: measurement, adoption, professional identity, and honest limits | A recorded **SHIP**, **REVISE**, or **STOP** decision and one change to the next session |

## Why the book remains essential

The files above can tell you what to record. They cannot determine whether the
requested outcome is worth pursuing, whether the evidence is proportionate,
whether an exception is legitimate, or whether a team has earned more
autonomy. Those decisions depend on the book's integrated argument, failure
patterns, case evidence, and adoption guidance.

If your team fills every field but cannot explain the engineering reason behind
the field, return to the paired chapter before treating the artifact as a gate.

## One bounded first win

For a first use, do not attempt to install the whole repository as a process.
Choose one reversible change, follow the
[`START-HERE.md`](START-HERE.md) governed-session path, and leave with one
explicit decision. That result is complete enough to be useful and small
enough to review honestly.
