---
name: adversarial-review
description: Falsify a proposed change against its specification, repository constraints, security posture, and verification evidence before declaring it ready.
---

# Adversarial Review

Use this workflow when a change is described as complete or ready for a pull request.

1. Read the task specification, affected files, repository guidance, and actual diff.
2. Trace every acceptance criterion to implementation and evidence.
3. Search specifically for MUST-NOT violations, unsafe defaults, unhandled partial failures, secret exposure, missing authorization, and architectural boundary drift.
4. Run the smallest relevant automated checks, then broaden verification in proportion to blast radius.
5. Separate observed facts from assumptions and unresolved questions.
6. Report findings by severity with file-and-line evidence. Do not repair findings unless the user or workflow authorizes implementation.
7. Declare ready only when blocking findings are resolved and required checks actually ran.

Never treat plausible output, a clean summary, or an agent's prior claim as proof.

