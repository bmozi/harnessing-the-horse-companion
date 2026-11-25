# Lesson 2: Write a small context map

Give the agent constraints and reliable pointers instead of duplicating the repository.

## Point to the source that owns the detail

A useful context map tells an agent what the project is, which constraints matter, where authoritative information lives, and how to check the work. It can point to a contract or test command without copying the full contract and every test into the file.

In the constructed task service, the API contract defines export fields, the contribution guide explains local setup, and the acceptance fixture names the selected records. A short project file points to these maintained sources.

## Your turn

Draft a context map for your bounded task. Use the companion context-file checklist. Give each pointer a purpose and verify that the target exists. Choose a real validation command from the repository; do not invent one because it looks conventional.

```text
Project purpose:
Constraints to preserve:
Source path and the question it answers:
Validation command and what it checks:
```

## Compare your work

A pointer is useful when it lets the next person or agent answer a concrete question. A long list of files with no stated purpose is not yet a useful map. A fixed line-count target is not a substitute for checking whether the file helps the actual task.

## Retrieval check

Which instruction best helps an agent find the current contract?

1. Copy an old contract into every prompt.
2. Load every repository file at the start.
3. Assume the contract from a similar service is close enough.
4. Point to the maintained contract and state which compatibility question it answers.

<details>
<summary>Check your answer</summary>

Answer: 4. A maintained pointer with a stated purpose supports current task decisions. Copying old versions or loading everything can hide the source that should decide the question.

</details>

## Return later

After a break, explain one decision each pointer in your map is intended to change.
