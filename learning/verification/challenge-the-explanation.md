# Lesson 3: Ask what would show the explanation is wrong

Seek a different evidence path instead of collecting another confident agreement.

## Make review capable of disagreement

A second explanation is not automatically independent evidence. If a reviewer sees only the first agent's summary and repeats its reasoning, both can share the same mistake.

For the CSV example, a reviewer can inspect the agreed column contract and actual output file before reading the author's explanation. They can look for an omitted record, an unexpected column, or a value that the consumer interprets differently.

## Your turn

Write one plausible failure that your current check would miss. Choose another observation or reviewer input that could expose it. Keep the review bounded to the actual task; a small formatting change does not require an organization-wide audit.

Use the companion disprove-only prompt as a starting point, then remove checks unrelated to your acceptance claim. Record disagreement and any remaining uncertainty.

## Compare your work

A useful challenge changes the evidence available, the failure being investigated, or the method of inspection. Merely changing an agent's role name does not guarantee that independence.

## Retrieval check

Which review adds the most useful new evidence?

1. A second agent agrees with the first summary.
2. The first agent rewrites its summary more confidently.
3. A reviewer compares the actual output with the consumer contract before reading the implementation explanation.
4. A new role name is added to the original prompt.

<details>
<summary>Check your answer</summary>

Answer: 3. Comparing the actual output with an independently supplied contract creates a different evidence path. A role name or another agreement does not establish that difference.

</details>

## Return later

Next session, give one example of two reviewers sharing the same blind spot.
