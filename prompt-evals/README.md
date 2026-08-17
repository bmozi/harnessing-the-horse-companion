# Prompt Evaluation Fixtures

These fixtures turn prompt adaptation into a testable engineering activity. They
do not call a model in CI: model outputs are nondeterministic, costly, and may
contain proprietary repository context. Instead, each fixture defines the
signals a human or evaluation harness must score when a prompt is tested.

## Included Fixtures

| Fixture | What it tests |
| --- | --- |
| [`structured-generation.json`](structured-generation.json) | Whether a generation prompt preserves scope, tests edge behavior, and refuses an unauthorized dependency. |
| [`disprove-only-review.json`](disprove-only-review.json) | Whether a review finds a seeded MUST-NOT violation and missing error handling instead of summarizing the code. |
| [`escalation-assessment.json`](escalation-assessment.json) | Whether repeated non-converging repairs trigger escalation rather than another speculative fix. |

## Evaluation Procedure

1. Run the named prompt with only the fixture's `input` and the prompt file.
2. Save the raw output outside this public repository if it contains private
   code or data.
3. Score each `requiredSignal` as present with evidence, partially present, or
   absent.
4. Fail the run if any `prohibitedSignal` appears.
5. Record model, tool, date, prompt revision, score, and evaluator notes.
6. Promote a prompt adaptation only when it meets `passCriteria` across the
   representative models and task classes your organization actually uses.

The fixtures test incentive structure and output discipline, not preferred
wording. Add repository-specific fixtures privately; do not publish production
code, internal prompts, credentials, customer data, or proprietary topology.
