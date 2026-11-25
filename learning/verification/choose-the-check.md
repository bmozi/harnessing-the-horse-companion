# Lesson 2: Choose evidence that can challenge the claim

Match a claim to a check, run it, and retain the observed result.

## Pick a check that reaches the result

For the CSV example, checking the generated file against the selected record identifiers can challenge the completeness claim. Running a formatter cannot. A unit test of a helper may be useful, but it may not exercise the actual exported file.

## Your turn

Extend your record with the check you will run and the observation you actually receive. Use a disposable local fixture if you do not have an appropriate real task. If you cannot run the check, mark it unrun and explain what that prevents you from concluding.

```text
Claim:
Revision or artifact:
Check or procedure:
Observed result:
What this result supports:
Still untested:
```

## Compare your work

“The comparison found these 25 expected identifiers and no extras” is an observation. “The export must therefore be secure” is a different claim and needs different evidence. Keep those boundaries visible.

For a failure, retain the result and revise the change or the check. Do not edit a failing fixture solely to make the report green.

## Retrieval check

Your build passes. Which conclusion is justified?

1. Every acceptance criterion passed.
2. The change is safe to deploy anywhere.
3. The build completed under the recorded conditions; behavior may still need checks.
4. A separate reviewer is no longer useful.

<details>
<summary>Check your answer</summary>

Answer: 3. A successful build supports the build claim under its actual conditions. It does not automatically establish behavior, authorization, recovery, or deployment readiness.

</details>

## Return later

Without looking, list the difference between a planned check, an observed result, and the conclusion that result supports.
