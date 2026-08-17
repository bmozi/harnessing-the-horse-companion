# Interface Specification Templates

> **Chapter:** ch06 — Task Division and Agent Scope (Standard 4:
> Interface-First Design)
> **Last revised:** 2026-06-16
> **Use this for:** Defining the contracts between the task's code and
> the rest of the system *before* any implementation code is generated.

The interface is the contract that allows separately-generated tasks
to integrate correctly. In agentic development, there is no
conversation between sessions. Each session starts fresh. The only
shared understanding between Task A's session and Task B's session is
the explicit, written interface specification in this document.

**If the interface is not explicit, it does not exist** — and Tasks A
and B will produce code that does not integrate.

An AI agent reading an API contract will implement exactly what is
specified and hallucinate what is not. Therefore: interface specs for
agentic development must be more detailed than typical API contracts.

## The Test of a Sufficient Interface Specification

If two sessions generating against the same interface produce code
that works together on the first try, the interface is sufficiently
specified. If they don't, the spec was the problem — not the agents.

---

## Template 1: REST API Endpoint

```
Endpoint: [HTTP method] [path]
Parameters:
  - [name] ([type], required/optional, default): [description and
    constraints]
  - [name] ([type], required/optional, default): [description and
    constraints]

Response [status code]:
  {
    "[field]": [type — be precise: string | null, not "any"],
    "[field]": [type]
  }

Response [error status]: { "error": [string], "code": "[ENUM_VALUE_1]" |
  "[ENUM_VALUE_2]" }

Error handling:
  - Return [status] for [condition].
  - Return [status] for [condition].
  - Never return [forbidden status] for [forbidden condition].
```

### Worked example

```
Endpoint: GET /api/users/search
Parameters:
  - q (string, required): Search query. Minimum 2 characters.
  - cursor (string, optional): Pagination cursor from previous response.
  - limit (integer, optional, default 20, max 100): Results per page.
Response 200:
  {
    "users": [{ "id": string, "name": string, "email": string }],
    "next_cursor": string | null
  }
Response 400: { "error": string, "code": "INVALID_QUERY" |
  "MISSING_PARAMETER" }
Response 401: { "error": string, "code": "UNAUTHORIZED" }
Error handling: Return 400 for invalid input. Return 401 for
  missing/invalid auth. Never return 500 for input validation failures.
```

---

## Template 2: Internal Function

```
Function: NAME(PARAM: TYPE, OPTIONS?: TYPE): RETURN_TYPE
OptionsType: { field?: type, field?: type }
ReturnType: { field: type, field: type }

Preconditions:
  - [What must be true about inputs before this is called]
  - [What environmental state must be present — DB connection, etc.]

Postconditions:
  - [What guarantees this function makes about its output]
  - [Bounded properties — e.g. result.length <= options.limit]

Side effects:
  - [Read-only, or specific writes/notifications/etc.]

Performance:
  - [Latency budget at specific percentile with specific load profile]
```

### Worked example

```
Function: searchUsers(query: string, options?: SearchOptions):
  Promise<SearchResult>
SearchOptions: { cursor?: string, limit?: number }
SearchResult: { users: User[], nextCursor: string | null }

Preconditions:
  - query.length >= 2 (caller must validate; function throws
    InvalidQueryError if not)
  - Database connection must be available (function throws
    DatabaseUnavailableError if not)

Postconditions:
  - users.length <= (options.limit ?? 20)
  - If nextCursor is null, no more results exist

Side effects: None. This is a read-only operation.

Performance: Must complete within 200ms at p99 with 10,000 users.
```

---

## Template 3: Event / Message Schema

```
Event: [namespace.action.tense]
Payload: { [field]: [type], [field]: [type] }
Published to: [queue/topic/bus]
Consumers: [list of consuming services]
Schema version: [N] (follow schema evolution policy in [doc reference])
```

### Worked example

```
Event: user.search.executed
Payload: { query: string, resultCount: number, durationMs: number,
  userId: string }
Published to: events.user-activity (SQS queue)
Consumers: analytics-service, audit-service
Schema version: 1 (follow schema evolution policy in AGENTS.md
  section 4.2)
```

---

## Interface Verification Protocol

After each task is generated, the post-generation gate
(`task-spec.md` post-generation checklist) includes an **interface
integrity check**: confirm that no existing function signatures, API
endpoints, or data schemas were modified unless explicitly specified
in the task scope.

The check is simple:

1. List the interface contracts defined here.
2. List the interfaces present in the generated code.
3. Any delta is a potential integration failure.
4. Any unauthorized modification is a scope violation.

The discipline is in performing the check consistently, not in the
sophistication of the check itself.

---

## Common Failure Modes

- **The Hallucinated Interface.** The agent generates code that calls
  a function or endpoint that does not exist. The function name is
  plausible — it follows the codebase's naming conventions — but it
  was never defined. The most common and most expensive interface
  failure. Fix: pre-generation gate (Standard 1) requires the agent
  to verify every interface reference against the actual codebase
  before generating code.
- **The Implicit Interface.** Two tasks communicate through a shared
  side effect — a global variable, a file on disk, a database row —
  rather than through an explicit interface. The dependency is
  invisible in the import graph. Task A writes to the database. Task
  B reads from it. Neither task's spec mentions the other. When Task
  A changes the column name, Task B breaks. Fix: every inter-task
  dependency declared here as an explicit interface, even if the
  mechanism is a shared database table.
- **The Evolving Interface.** The agent modifies an interface during
  generation because the original spec was insufficient. The
  modification is reasonable — it adds a parameter the implementation
  needs — but it was not authorized. Every other consumer is now
  broken. Fix: interface changes require a scope change, which
  requires a new session. The agent should stop, flag the
  insufficiency, and ask for a revised spec rather than modifying the
  interface unilaterally.

## Why Interface-First in the Agentic Era

The shift from manual to agentic development changes the engineer's
primary time investment. In the pre-agentic era, the engineer's time
went to writing code. In the agentic era, the engineer's time goes to
designing interfaces — the contracts that constrain what the agent
produces and ensure that separately-produced components integrate.

This is the practical manifestation of the book's thesis:
**Code is the receipt. Clarity is the product.** The interface spec
is the clarity. The generated code is the receipt. The engineer's
value is in the spec, not in the implementation.

## Related

- `task-spec.md` — the Interfaces Produced and Consumed sections
  reference this template
- `spec-md.md` — the SPEC that scopes the change these interfaces
  define
- `../prompts/structured-prompt.md` — the generation prompt that
  consumes the interface spec

## Provenance

Adapted from Chapter 6 of *Harnessing the Horse*, Standard 4.
Interface-first design is not new — Sam Newman, *Building
Microservices*, 2nd ed., O'Reilly, 2021; Kent Beck,
*Test-Driven Development*, Addison-Wesley, 2003. What is new is its
*criticality* in agentic development, where each task is generated in
an independent session with no shared state.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
