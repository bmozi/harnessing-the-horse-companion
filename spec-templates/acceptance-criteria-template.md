# Machine-Readable Acceptance Criteria Template

> **Chapter:** ch05 — Discovery and Planning (Standard 1: Requirements
> as Verifiable Contracts — the acceptance-criteria half)
> **Last revised:** 2026-06-16
> **Use this for:** Writing acceptance criteria that the AI agent can
> self-verify and the reviewer can validate via a test run.

Every acceptance criterion in SPEC.md must be written in a form that
an automated system — or the AI agent itself — can verify without
human interpretation. This is a stronger requirement than "binary
criteria": the criteria must be **executable**. Translatable into a
test assertion, an API contract check, or a measurable performance
threshold.

In manual development, binary criteria suffice because developer and
reviewer share enough context to interpret "the search endpoint
returns relevant results." In agentic development, the agent does not
share that context. "Relevant results" is meaningless to an agent —
it cannot evaluate relevance without a concrete definition.

## The Transform: Human-Readable → Machine-Readable

### Human-readable (insufficient)

1. The search endpoint returns relevant results.
2. The endpoint performs well under load.
3. The search handles edge cases appropriately.
4. The results are paginated.

### Machine-readable (sufficient)

1. `GET /api/users/search?q=john` returns HTTP 200 with a JSON array
   containing all users whose `first_name`, `last_name`, or `email`
   contains "john" (case-insensitive).
2. `GET /api/users/search?q=john` responds within **200ms at p99**
   with 10,000 users in the database, as measured by the standard
   load test suite.
3. `GET /api/users/search?q=` (empty query) returns HTTP 400 with
   error code `INVALID_QUERY`. `GET /api/users/search` (no query
   parameter) returns HTTP 400 with error code `MISSING_PARAMETER`.
   `GET /api/users/search?q=a` (single character) returns results
   normally.
4. `GET /api/users/search?q=john` returns a maximum of **20 results
   per page**. The response includes a `next_cursor` field if more
   results exist. `GET /api/users/search?q=john&cursor={value}`
   returns the next page.

**The difference is not length — it is precision.** Each
machine-readable criterion specifies the exact HTTP method, the exact
URL, the exact parameters, the exact response format, and the exact
behavior. Each translates directly into a test assertion.

## The Test for Machine-Readability

For every criterion, ask: *Could a developer write a single test
assertion that verifies this criterion?*

- If yes → machine-readable. ✓
- If "it depends" → ambiguous. Revise.
- If no → human-readable. Rewrite as one or more machine-readable
  criteria.

## Categories of Machine-Readable Criteria

### API Contract Criteria

- Exact method, path, parameters
- Exact response status codes for each input class
- Exact response schema (JSON shape with field types)
- Exact error codes for failure cases

### Performance Criteria

- Specific percentile latency at specific load profile
- Specific throughput threshold (requests per second)
- Specific resource bounds (memory, CPU, connection pool)
- Specific timeout values

### Behavioral Criteria

- Exact behavior on empty input
- Exact behavior on maximum-size input
- Exact behavior on malformed input
- Exact behavior under concurrent access

### Side-effect Criteria

- Exact records written to which storage
- Exact events emitted with which payload
- Exact log lines produced
- Exact external API calls made

## Template

```markdown
## Acceptance Criteria (machine-readable)

### API contract
- AC-1: [METHOD path?params=values] returns [STATUS] with [exact
  schema] when [exact input condition].
- AC-2: [METHOD path?params=values] returns [STATUS] with [exact
  error code] when [exact failure condition].

### Performance
- AC-3: [Operation] completes within [Xms at pN] under [load
  profile, e.g., 100 RPS, 10K records].

### Behavior at boundaries
- AC-4: Given [boundary input — empty/max/malformed/concurrent],
  the system [exact behavior].

### Side effects
- AC-5: [Operation] writes [exact record shape] to [storage] and
  emits [event with payload] to [destination].
```

## Related

- `spec-md.md` — the SPEC.md whose Acceptance Criteria section uses
  this format
- `../checklists/pre-generation-verification.md` — the pre-generation
  gate that confirms criteria are machine-readable before generation
  begins
- `interface-spec.md` — supports the API contract criteria

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Standard 1
(Requirements as Verifiable Contracts) — the acceptance-criteria and
verification-gate half of the standard.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
