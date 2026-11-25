# What belongs in an AI agent context file?

Keep durable project constraints and reliable pointers close to the agent; load task-specific detail when it is needed.

## The short answer

A useful context file tells an agent what it must preserve, where to find authoritative information, and how to check its work. It should help the current task without becoming an unmaintained copy of the whole repository.

## How it works

Separate durable project rules from a temporary task brief. Durable information includes architecture boundaries, relevant conventions, forbidden changes, and the real validation commands. The task brief identifies the requested change, affected scope, acceptance criteria, and current evidence.

Use pointers to maintained files when details change frequently. Before relying on a pointer, check that its target exists and still describes the project. Context that was once accurate can become a source of confident mistakes.

## A constructed example

A fictional billing service has a concise project file pointing to the API contract, migration rules, and test commands. A task brief asks for one response-field change and names the consumer contract that must remain compatible. The agent reads those sources before editing rather than guessing from a similar service.

## When to use it

Use a context file when work spans sessions, several assistants share a repository, or important constraints are not obvious from one source file. Use a smaller task brief for a narrow, temporary change.

## What to watch for

- Stale commands that no longer test the real application.
- Duplicated rules that disagree about the same boundary.
- Secrets or production records copied into project instructions.
- A file-size target treated as a universal rule instead of checking usefulness.
- Assuming an instruction file enforces permissions. Actual enforcement belongs in the relevant system boundary.

## Try it

Choose five lines from a current context file. For each line, name the decision it changes or the failure it prevents. Check any linked file or command. Remove or repair unsupported instructions through the repository's normal review process.

## Check your understanding

If a rule matters for a consequential action, ask two separate questions: can the agent find the rule, and what prevents the action when the rule is ignored? Better wording can help the first; it does not by itself provide the second.

## Source and further practice

Book connection: Harnessing the Horse, Chapter 4; Agentic Systems Architecture, Chapter 5.

- [Context-file checklist](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/factory-bootstrap/01-context-file-checklist.md)
- [Tool and context configuration](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/references/tool-configuration-reference.md)
- [Memory and provenance record](https://github.com/bmozi/agentic-systems-architecture-companion/blob/main/memory-and-provenance-record.md)

Author: John Briggs. Updated 2026-11-24. This is original companion learning material; constructed examples are labeled.
