# Ordered Blank Governed-Session Pack

Use this pack for one full governed change. It mirrors the completed fictional
[worked example](../worked-example/README.md), but links only the blank forms
you must fill with local facts. Read the matching example stage before filling
each form for the first time.

| Order | Blank artifact | Required for | May be deliberately skipped only when |
| --- | --- | --- | --- |
| 0 | [Project context checklist](../01-context-file-checklist.md) | every session | never; record the applicable project instruction location |
| 1 | [Work Order](../02-work-order-template.md) | every session | never |
| 2 | [SPEC](../../spec-templates/spec-md.md) | every session | never; a short change may use the compact scaffold instead |
| 3 | [DESIGN](../../spec-templates/design-md.md) | interfaces, data, dependencies, or material operational change | a local change has no such boundary; state that in the Work Order |
| 4 | [Structured prompt](../../prompts/structured-prompt.md) | AI-assisted generation | a human-only implementation; record who implemented it |
| 5 | [Implementation notes](../../spec-templates/impl-notes-md.md) | every change | never; a concise entry is enough |
| 6 | [REVIEW](../../spec-templates/review-md.md) | every change | never; a fresh adversarial reviewer is the minimum when a second human is unavailable |
| 7 | [Metrics and learning](../06-metrics-baseline.md) | every completed session | never; record “not yet observed” rather than inventing an outcome |
| 8 | [Session decision](../SESSION_DECISION.md) | every completed session | never |

## Decision vocabulary

The reviewer makes a recommendation: **RECOMMEND_SHIP**, **RECOMMEND_REVISE**,
or **RECOMMEND_STOP**. The accountable decision owner then records the final
**SHIP**, **REVISE**, or **STOP** outcome in `SESSION_DECISION.md`. A green
test or a reviewer recommendation is evidence, not an automatic release.

## Deliberate skip rule

Do not silently omit a form. Record every allowed omission, the reason it is
safe for this specific change, the evidence considered, and the owner who
accepted the remaining risk in the Work Order and Session Decision. If a new
interface, data, dependency, deployment, or consequence appears during the
session, stop and move to the full applicable artifact chain.

## Compact alternative

For one local, reversible change with no new dependency, external interface,
data-classification change, or production rollout, use the
[Small Change Session](../small-change-session.md). It does not authorize
skipping independent review, a visible decision, or recorded learning.
