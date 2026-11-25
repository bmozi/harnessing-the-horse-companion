# Lesson 1: Name the result you need to prove

Replace a vague completion claim with one observable acceptance condition.

## Start with the claim

An agent reports: “The CSV export works.” Before reviewing its implementation, ask what a reader or consumer must be able to do with the exported file.

In this constructed exercise, the requirement is: the export preserves all 25 selected records, writes exactly the agreed columns, and can be opened by the intended consumer. These are three claims. A file existing on disk establishes none of them on its own.

## Your turn

Choose one recent AI-assisted task, or use the CSV example. Write one sentence describing a result you could observe. Add the revision or artifact you will inspect and one thing outside your current claim.

Use this small record:

```text
Claim:
Revision or artifact:
Expected observation:
Outside this check:
```

## Compare your work

A useful answer names a behavior and a boundary. “The export is good” does not. “The exported file contains all 25 selected records and no extra records” gives a reviewer a specific result to investigate.

Keep this record. You will choose a check for it in the next lesson.

## Retrieval check

Which claim gives you the clearest next verification step?

1. The agent is confident the export works.
2. The exported file contains exactly the 25 selected records.
3. The code looks professional.
4. The task took less time than expected.

<details>
<summary>Check your answer</summary>

Answer: 2. The second claim names a count and a selection boundary that a check can investigate. Confidence, appearance, and elapsed time do not establish the file contents.

</details>

## Return later

Tomorrow, explain why “a file was created” and “the right file was created” require different evidence.
