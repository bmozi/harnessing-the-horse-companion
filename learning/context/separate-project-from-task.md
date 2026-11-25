# Lesson 1: Separate project rules from the current task

Choose what must survive the session and what belongs only to this change.

## Start with a small job

In this constructed exercise, a fictional task service must add an optional CSV export field. Its access-control boundary and API contract must remain intact. The requested field belongs in the current task brief; the access-control boundary is a durable project constraint.

A context file is maintained information that helps an agent make the right decisions. It does not need to contain every detail the repository can supply, and it cannot enforce a permission by itself.

## Your turn

Choose a small task or use the fictional export. Make two lists: durable project constraints and temporary task instructions. Name the public or safely discussable artifact you will inspect. Do not copy credentials, personal records, or production customer data into the exercise.

```text
Task and intended result:
Durable constraints:
Temporary instructions:
Outside this task:
```

## Compare your work

A useful distinction explains why an item should persist. “Preserve tenant isolation” belongs with durable constraints. “Add the optional region column in this change” belongs in the current brief. If a line could go stale, identify its maintained source before making it a permanent rule.

## Retrieval check

Which item most clearly belongs in the temporary task brief?

1. Add the optional region column for this export change.
2. Never commit credentials.
3. Preserve tenant isolation.
4. Use the maintained API contract to identify response compatibility.

<details>
<summary>Check your answer</summary>

Answer: 1. The requested export change is temporary task scope. The other items describe ongoing boundaries or ways to find maintained project information.

</details>

## Return later

Tomorrow, sort three instructions from a different task without looking at your first list.
