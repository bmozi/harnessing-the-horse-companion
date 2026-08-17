# MCP Tool Pattern (TypeScript)

> **Chapter:** ch13 — Designing AI Agent Infrastructure (Section
> 13.1)
> **Patterns:** [Dry-Run-Default on Write Tools](../../patterns/dry-run-default.md), [Scoped Authorization Token](../../patterns/scoped-authorization-token.md)

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and
> case-study context that make these patterns concrete in practice.
> **TypeScript source in this directory is licensed under the MIT
> License** ([see `../../LICENSE-CODE`](../../LICENSE-CODE)) — drop
> into your own MCP server with confidence, including commercial
> work.

## File

| File | What it is |
| --- | --- |
| [`schedule-appointment.ts`](schedule-appointment.ts) | MCP tool definition showing the three-layer pattern: **scope check** → **validate** → **dry-run gate**. |

## The three-layer pattern

Every MCP write tool follows this structure:

```
handler(input, context):
  context.requireScope('domain:action')   // 1. Scope check
  validate(input)                          // 2. Validate
  if (!input.confirm) return dryRun       // 3. Dry-run default
  return execute(input)
```

Each layer maps to a discipline of the Harness Framework:

| Layer | Harness discipline | What it guarantees |
| --- | --- | --- |
| Scope check | **Scope** | The session token has permission for this exact tool. |
| Validate | **Prove** | The input is well-formed; business preconditions hold. |
| Dry-run gate | **Enforce** | No state change unless the caller explicitly confirms. |
| Audit log | **Communicate** | Every confirmed action leaves a record naming the agent. |

## Why each layer is non-optional

### Without the scope check
A single compromised or misinterpreted session has full access to
every tool. A `contacts:read` session could schedule appointments,
cancel subscriptions, or send notifications. The scope check
contains the blast radius.

### Without validation
Agents pass plausible-looking inputs that violate business rules.
An invalid `serviceType` of `'preventive'` (when only `'initial' |
'quarterly' | 'callback'` are valid) would reach the database and
fail there, leaking the implementation detail and producing a
confusing error. Validation rejects at the boundary with a clear
message.

### Without dry-run default
An agent that misinterprets the user's request executes immediately.
Wrong customer ID → wrong appointment booked. Wrong date → customer
loses their slot. **The dry-run gate ensures the agent's first
action is always read-only and reversible.**

### Without audit log
The successful action is invisible. When something goes wrong, there
is no way to trace which agent took the action, when, with what
input. The audit log is the provenance trail.

## The agent's expected behavior

A well-prompted agent calling this tool:

1. Calls the tool **without** `confirm: true`
2. Reads the dry-run response
3. Verifies the response matches the user's intent (customer name,
   date, window, service type)
4. Calls the tool **with** `confirm: true` to execute

The prompt should explicitly require this two-step pattern. See
[`../../prompts/structured-prompt.md`](../../prompts/structured-prompt.md)
for the prompt template that enforces it.

## Run the example

From the repository root, run `npm ci && npm test`. The test suite verifies that
the first call is a non-mutating preview and that an explicitly confirmed call
executes once and leaves an audit record.

## Adapting to your MCP server

The file uses small, runnable boundary interfaces (`MCPToolDefinition`,
`MCPContext`) that you will adapt to your MCP SDK's actual types. The pattern is
independent of the SDK — the three layers (scope, validate,
dry-run) are the structural property; the type names vary.

## Related

- [`../../patterns/dry-run-default.md`](../../patterns/dry-run-default.md)
- [`../../patterns/scoped-authorization-token.md`](../../patterns/scoped-authorization-token.md)
- [`../claude-settings/`](../claude-settings/) — the structural
  guardrail companion at the agent-runtime level
- [`../../prompts/structured-prompt.md`](../../prompts/structured-prompt.md)
  — the generation prompt that should require the confirm-after-
  dry-run pattern

## Provenance

Adapted from Chapter 13 of *Harnessing the Horse* by John Briggs.

TypeScript source: © 2026 John Briggs, MIT licensed
(see [`../../LICENSE-CODE`](../../LICENSE-CODE)).
This README: CC BY-NC-SA 4.0
(see [`../../LICENSE-CONTENT`](../../LICENSE-CONTENT)).
