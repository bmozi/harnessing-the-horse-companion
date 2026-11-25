# How do you limit what an AI tool can do?

Define the allowed action, enforce identity and scope outside the model, and plan for ambiguous outcomes and recovery.

## The short answer

Give a tool a narrow job and enforce its permissions in code or the service boundary. A prompt saying “be careful” is not authorization, and an agent's confirmation flag is not independent human approval.

## How it works

Name the operation, caller, permitted records or tenant, allowed effects, and limits. The tool or underlying API must check those conditions when the operation executes. Keep a clear distinction between describing a proposed change and committing it.

For operations with consequential effects, specify what happens when the caller times out without knowing whether the operation succeeded. A safe response may require looking up an operation record rather than blindly retrying the write.

## A constructed example

A fictional customer-support agent may prepare a refund proposal for one order. A separate authorized operation commits an approved refund within the allowed amount. The service checks identity, tenant, amount, and the approval record. Giving the agent a tool called approve_everything would erase the boundary that the workflow needs.

## When to use it

Apply this when an assistant can write data, send messages, spend money, change permissions, or invoke another system. Read-only tools still need data-access and cost boundaries.

## What to watch for

- A generic proxy tool that exposes more authority than its task needs.
- A preview that leaks private data or produces hidden side effects.
- A confirmation field treated as proof of independent approval.
- Retries creating duplicate effects after an ambiguous timeout.
- Logs that cannot connect the request to the resulting action.

## Try it

Choose one tool and write its allowed action in one sentence. Identify where identity and scope are enforced, which effects are withheld, and how an owner can stop or reconcile the operation. Mark unknowns instead of inventing a successful control test.

## Check your understanding

Tool discovery answers “what can this interface expose?” Authorization answers “what may this caller do now?” Keep those questions separate when using MCP or any other tool protocol.

## Source and further practice

Book connection: Harnessing the Horse, Chapter 13; Agentic Systems Architecture, Chapters 6 and 11.

- [Dry-run-default pattern](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/patterns/dry-run-default.md)
- [Scoped authorization token](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/patterns/scoped-authorization-token.md)
- [Integration pattern catalog](https://github.com/bmozi/harnessing-the-horse-companion/blob/main/references/pattern-catalog.md)
- [Governed tool contract](https://github.com/bmozi/agentic-systems-architecture-companion/blob/main/governed-tool-contract.md)

Author: John Briggs. Updated 2026-11-25. This is original companion learning material; constructed examples are labeled.
