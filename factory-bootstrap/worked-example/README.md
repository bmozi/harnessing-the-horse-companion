# Completed Governed Delivery Loop Example

This fictional example shows one small change moving through the complete
governed-delivery loop. It demonstrates artifact quality and evidence flow; it
does not reproduce Merlin's implementation, private topology, prompts, or
operational configuration.

## Scenario

The fictional **Example Notifications Service** sends account reminders. Users
can already disable all reminders, but cannot choose email while disabling SMS.
The pilot change adds a per-channel preference without introducing a new
dependency or changing delivery infrastructure.

The example is deliberately modest. A team should prove the manual loop on a
bounded change before adding queues, agent routing, autonomous recovery, memory
services, or self-improvement infrastructure.

## Artifact Chain

| Order | Artifact | Question it answers |
| --- | --- | --- |
| 0 | [`00-project-context.md`](00-project-context.md) | What must every agent know about this repository? |
| 1 | [`01-work-order.md`](01-work-order.md) | What outcome is authorized, and what is outside it? |
| 1A | [`01a-four-risk-evidence-contract.md`](01a-four-risk-evidence-contract.md) | Does the feature have enough evidence to enter specification, and what work remains unauthorized? |
| 2 | [`02-spec.md`](02-spec.md) | What behavior must be proven? |
| 3 | [`03-design.md`](03-design.md) | How will the change preserve system boundaries? |
| 4 | [`04-generation-prompt.md`](04-generation-prompt.md) | What exact contract does the implementation agent receive? |
| 5 | [`05-impl-notes.md`](05-impl-notes.md) | What happened, changed, or remained uncertain? |
| 6 | [`06-review.md`](06-review.md) | What independent evidence supports the decision? |
| 7 | [`07-metrics-and-learning.md`](07-metrics-and-learning.md) | What outcome and learning feed the next run? |

## How to Use the Example

1. Read the files in order without copying them.
2. Compare each completed section with its blank companion template.
3. Copy the blank templates into your own repository.
4. Replace every fictional fact with evidence from your project.
5. Delete any section that does not apply only after recording why.

Do not copy the example's architecture, thresholds, or test commands blindly.
The reusable property is the chain of accountability from intent to evidence,
not the particular notification feature.

## What This Example Intentionally Omits

- vendor and model selection;
- internal tool inventories;
- database, deployment, or provider topology;
- autonomous agent routing;
- private prompts and operational thresholds;
- a claim that one fictional run proves productivity improvement.

Those omissions keep the example portable and protect the boundary between a
reader-facing teaching artifact and a private production implementation.
