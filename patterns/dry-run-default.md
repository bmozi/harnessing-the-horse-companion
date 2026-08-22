# Dry-Run-Default on Write Tools

> **Chapter:** ch13 — Designing AI Agent Infrastructure (Section 13.1)
> **Last revised:** 2026-06-16

## Origin

This book (2026). The pattern is named here for the first time as a
design discipline specific to MCP servers and other agent-facing
write tools. It applies the principle of dry-run mode (long-standing
in CLI tools like `rsync --dry-run` and `terraform plan`) as the
**default** for any tool that modifies state.

## Intent

When an AI agent invokes a tool that modifies state — creating a
record, updating a field, canceling a subscription, sending a
notification — **the default behavior is a dry run**: the tool
validates the inputs, verifies permissions, and returns what *would*
happen if the operation were executed, **without actually executing
it**.

The agent and reviewer can inspect the dry-run result before requesting actual
execution. The actual execution requires an explicit `confirm: true` parameter
(or a separate confirmation tool invocation). That flag separates preview from
execution; it is not human approval unless an independently authenticated
approval record gates it.

## Application in Agentic Development

This pattern addresses the fundamental safety concern with
agent-operated infrastructure: **agents make mistakes that are
difficult to reverse**.

- An agent that misinterprets a user's request and deletes the wrong
  customer record has caused a data loss incident.
- An agent that sends a notification to the wrong distribution list
  has caused a communication incident.

Dry-run-default makes the first operation a preview on the normal path. Even a
preview can expose sensitive data, consume quota, or create validation/audit
side effects, so it still needs authorization, redaction, rate limits, and cost
bounds. Irreversible execution requires a deliberate second step and, where
risk warrants, independent approval.

## Concrete Example

```
Tool: create_contact
Input: { name: "Jane Smith", email: "jane@example.com" }

Default response (dry_run: true):
  { action: "create_contact",
    would_create: { id: "(new)", name: "Jane Smith",
                    email: "jane@example.com" },
    validation: "passed",
    conflicts: [],
    confirm_required: true }

Confirmed execution:
Input: { name: "Jane Smith", email: "jane@example.com", confirm: true }
Response: { id: "ct_12345", created: true }
```

## The Rule

**The pattern is not optional for production MCP servers.**

- Every tool that creates, updates, or deletes state should
  implement dry-run-default.
- Tools that only read state do not need it — reads are inherently
  safe.

## Why API Design Discipline Becomes More Critical, Not Less

Consider a billing API that provisions a subscription:

- A human operator calling the API understands that "provision" is
  an irreversible financial commitment and acts accordingly.
- An AI agent calling the same API treats it as another tool
  invocation. If the agent retries on timeout (a reasonable default
  behavior), the customer is billed twice.

The fix is not better prompting. **The fix is better API design:
idempotency keys on every write operation**, so that a retry produces
the same result as the original call.

This is standard API engineering (Stripe pioneered the pattern), but
it shifts from "nice to have" to **load-bearing** when the consumer
is an autonomous agent that makes retry decisions without human
judgment.

> Structure enables intelligence. Sloppy APIs that survived human
> operators will not survive agent operators.

## Implementation

See [`../code-examples/mcp-tool-pattern/`](../code-examples/mcp-tool-pattern/)
— TypeScript MCP tool skeleton showing the three-layer pattern:

1. **Scope check** — reject if token lacks permission
2. **Validate** — check inputs, business rules, availability
3. **Dry-run gate** — return what *would* happen unless
   `confirm: true`

The three-layer pattern maps directly to the Harness Framework's
four disciplines:

- **Scope** check constrains the action surface
- **Prove** through validation
- **Enforce** preview-before-execute separation through dry-run default
- **Communicate** the action through audit logging

## Pitfalls

- **The "always confirm" agent.** The agent learns that every call needs
  `confirm: true` and starts setting it automatically. Prompt instructions can
  improve the normal path but are not an authorization boundary. For
  high-impact writes, require a separately authenticated approval token or
  protected workflow transition that the calling process cannot mint.
- **The validation-only "dry run."** A dry run that doesn't actually
  simulate the operation provides a false sense of safety. The
  dry-run output must include exactly what would be created /
  updated / deleted, with current state for comparison.
- **The dry-run that creates side effects.** Some validation
  inherently has side effects (rate-limited external API calls,
  audit log entries). The dry run should distinguish "validation
  side effects" (logged, rate-limited) from "operation side effects"
  (writes, deletes, sends), and only the former should occur in
  dry-run mode.

## Related

- [`scoped-authorization-token.md`](scoped-authorization-token.md) —
  the scope-check layer that runs before the dry-run gate
- [`../code-examples/mcp-tool-pattern/`](../code-examples/mcp-tool-pattern/)
  — runnable MCP tool example
- [`../prompts/structured-prompt.md`](../prompts/structured-prompt.md)
  — agent prompts should include the "first call without confirm,
  verify, then confirm" rule

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
