# Code Examples

Runnable reference code from *Harnessing the Horse* — primarily Part III
(the practice chapters) and Part IV (case studies). The examples compile and
their structural properties are exercised by tests. They are still designed to
be adapted to a real project's framework, database client, and SDK types.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and case-study
> context that turn these examples from "code that runs" into "code
> that demonstrates a principle." **Source code in this directory is
> licensed under the MIT License** ([see `../LICENSE-CODE`](../LICENSE-CODE))
> — drop these into your own projects with confidence, including
> commercial work. The relaxed license is intentional: code examples
> should travel without friction. The accompanying prose in this
> directory's `README.md` files falls under CC BY-NC-SA 4.0 ([see
> `../LICENSE-CONTENT`](../LICENSE-CONTENT)).

## What's here

| Directory | Chapter | What it is |
| --- | --- | --- |
| [`claude-settings/`](claude-settings/) | ch04 — §4.2 | Reference `.claude/settings.json` with annotated allow/deny lists implementing the principle of least privilege for AI agents. Mitigates OWASP Agentic Top 10 (ASI01 / ASI02 / ASI03). |
| [`anti-corruption-layer/`](anti-corruption-layer/) | ch11 — §11.1 + §11.2 | TypeScript port/adapter implementing both the ACL and Hexagonal Architecture patterns. `CRMPort` interface + `HubSpotAdapter` + `InMemoryCRMAdapter` for tests. |
| [`transactional-outbox/`](transactional-outbox/) | ch11 — §11.5 | PostgreSQL outbox table schema + companion idempotency_keys table, plus a TypeScript agent-generated webhook handler showing the three-step template (idempotency / business write / outbox write) all in one transaction. |
| [`mcp-tool-pattern/`](mcp-tool-pattern/) | ch13 — §13.1 | TypeScript MCP tool definition (`scheduleAppointment`) implementing the three-layer pattern: scope check → validate → dry-run gate. |

## Verify the examples

From the repository root:

```bash
npm ci
npm run typecheck
npm test
```

The tests prove the examples' teaching properties: domain isolation, webhook
idempotency plus outbox intent, and dry-run-before-write behavior. They do not
replace integration tests against your selected vendors or persistence layer.

## How to use

Each example directory contains:

- `README.md` — what it demonstrates, prerequisites, and adaptation notes
- Source code with one-line license headers
- Notes on what to replace when adapting the example to a real system

These examples intentionally avoid vendor credentials and full application
scaffolding. Bring them into your own repository, wire them to your actual SDKs
and persistence layer, preserve or strengthen the included behavioral tests,
and add integration tests that prove the boundary still holds.

## Asset map (book ↔ companion)

See the per-directory READMEs and the top-level [`INDEX.md`](../INDEX.md).
