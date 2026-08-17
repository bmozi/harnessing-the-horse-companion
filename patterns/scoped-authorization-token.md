# Scoped Authorization Token

> **Chapter:** ch13 — Designing AI Agent Infrastructure (Section
> 13.1)
> **Last revised:** 2026-06-16

## Origin

The pattern applies **Jerome Saltzer and Michael Schroeder's
Principle of Least Privilege** ("The Protection of Information in
Computer Systems," *Proceedings of the IEEE*, 1975) to session
tokens. Formalized in **OAuth 2.0 scope** (RFC 6749, 2012).

## Intent

Access control for agent-consumed infrastructure operates at the
**tool level**, not the server level.

An agent session authorized to read customer data should not
automatically be authorized to modify it. An agent session
authorized to query scheduling availability should not automatically
be authorized to book appointments.

Each agent session receives a token whose scope specifies which
tools it can invoke and with what parameters. The MCP server
validates the scope on every tool invocation.

## The Four Scope Levels

The scope specification should be as narrow as the task requires:

| Scope | What it permits | Appropriate for |
| --- | --- | --- |
| **Read-only** | Query tools only, no mutation | Research, analysis, reporting tasks |
| **Domain-scoped mutation** | Mutation tools within a specific domain (e.g., "create and update contacts but not delete") | Data entry, record management |
| **Record-scoped mutation** | Mutation tools for specific records identified by ID | Targeted update tasks where records are pre-identified |
| **Full access** | Any tool | Administrative tasks with full human oversight |

## The Principle

**An agent should operate with the minimum scope required to complete
its task.**

Broader scope does not help the agent work better — it only
**increases the blast radius if the agent makes a mistake**.

## Application in Agentic Development

Without scoped tokens:

- A single compromised or hijacked session has full system access.
- A misinterpreted task can affect anything in the agent's
  reach.
- The audit log shows that an action was authorized but cannot
  explain why this specific scope was appropriate.

With scoped tokens:

- A compromised session is bounded by the scope.
- A misinterpreted task fails at the scope check rather than
  succeeding incorrectly.
- The audit log includes the scope, providing a complete
  authorization story.

This pattern is the **session-level companion** to the structural
guardrails in `.claude/settings.json`
(see [`../code-examples/claude-settings/`](../code-examples/claude-settings/)).
The settings file constrains what the *tool can do*. The scoped
token constrains what *this session can ask the tool to do*.

## Implementation

See [`../code-examples/mcp-tool-pattern/`](../code-examples/mcp-tool-pattern/)
— the TypeScript example shows `context.requireScope('appointments:write')`
as the first line of the tool handler. The scope check runs before
validation, before any side effect, and before the dry-run gate.

Scope strings follow the format `<resource>:<action>` (OAuth
convention):

- `contacts:read`
- `contacts:write`
- `contacts:delete`
- `appointments:write`
- `metrics:read`

For record-scoped mutation, the scope can carry an identifier:
`contacts:write:cust_12345`.

## Granularity Decisions

The right scope granularity is a project-specific decision balancing
two concerns:

- **Too coarse** (one scope per server) → reverts to all-or-nothing
  authorization; the pattern loses its value.
- **Too fine** (one scope per tool per field) → unmaintainable;
  every session needs a complex scope spec, and the spec becomes the
  bottleneck.

A reasonable default is:

- One scope per *tool* for read operations (e.g., `contacts:read`)
- One scope per *domain* for write operations
  (e.g., `contacts:write`)
- Record-scoped variants only when the task requires it

## Pitfalls

- **The session that gets broad scope "to be safe."** The scope
  becomes meaningless. If every session receives `full_access`, the
  pattern provides no protection. The discipline is at session
  initiation: justify the scope based on the task, not on
  convenience.
- **The "scope check" that doesn't actually fail.** A scope check
  that logs a warning but allows the operation is theater.
  Scope-check failures must reject the tool call with an error
  the agent can reason about.
- **The scope that grants more than its name suggests.** A
  `contacts:read` scope that also allows reading billing data is a
  silent privilege escalation. Scopes should grant exactly what
  their name implies.
- **The session token without expiration.** A long-lived token with
  broad scope is a credential leak waiting to happen. Scope and
  duration are two halves of session safety.

## Related

- [`dry-run-default.md`](dry-run-default.md) — the layer that runs
  after the scope check passes
- [`../code-examples/mcp-tool-pattern/`](../code-examples/mcp-tool-pattern/)
  — runnable example with `requireScope` enforcement
- [`../code-examples/claude-settings/`](../code-examples/claude-settings/)
  — the structural-guardrail companion (tool-level constraints)
- [`../prompts/escalation-protocol.md`](../prompts/escalation-protocol.md)
  — what to do when a session needs broader scope than initially
  authorized

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
