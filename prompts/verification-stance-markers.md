# Verification Stance Markers: verified / ASSUMPTION / VERIFY

> **Chapter:** ch07 — Generation, Verification, and Review (Section
> 7.3, "The Verification Stance")
> **Last revised:** 2026-06-16
> **Use this for:** A three-tier marker convention for factual claims
> in AI-generated code and documentation. Eliminates the worst failure
> mode of AI-generated documentation: the confidently-stated falsehood.

When an agent writes "HubSpot guarantees exactly-once delivery of
webhook events" without a verification marker, a reviewer may accept it
as fact. When the marker reads `[ASSUMPTION: HubSpot delivers webhooks
exactly once — their docs say "at least once" which may be different]`,
the reviewer knows to investigate.

---

## The Three Markers

### `verified`

The claim has been checked against a primary source — vendor API
documentation, a test result, a runtime observation, a database query.
The marker includes the source.

```
[verified: HubSpot API docs, 2026-06-01]
[verified: integration test, test_webhook_dedup.go:47]
[verified: production logs 2026-05-15, request_id 0x4f3a2b1c]
```

### `ASSUMPTION`

The claim is based on the agent's inference, a partial reading of the
documentation, or a pattern match against training data. It has not
been independently verified. The marker flags it for human review.

```
[ASSUMPTION: HubSpot webhook eventId is unique per event —
verify against docs]

[ASSUMPTION: this Postgres column has a unique constraint —
check pg_indexes before relying on it]
```

### `VERIFY`

The claim could not be verified from available context and requires
human investigation before the code is trusted in production. The
marker is a direct request for action.

```
[VERIFY: FieldRoutes sandbox returns same HTTP status codes as
production — could not confirm from available documentation]

[VERIFY: this rate limit applies per-account or per-API-key —
docs are ambiguous]
```

---

## How to Use

1. **In the generation prompt**, instruct the agent to apply markers
   to every factual claim. See `subagent-challenge-clauses.md` for the
   prompt clause.
2. **In the review**, audit the markers (`disprove-only-review.md`
   Question 3 and `adversarial-validation.md` Verification Stance
   Audit cover this).
3. **In production code**, `ASSUMPTION` and `VERIFY` markers should
   not survive merge to main unless explicitly documented as known
   fragilities. Grep for them in CI as a gate.

## Why This Discipline Matters

The three-tier stance eliminates the worst failure mode of AI-generated
documentation: the confidently-stated falsehood. It is infectious in
the best sense — once a team adopts it, they start applying it to
human-written documentation too. Every architecture document benefits
from the discipline of marking which claims are verified and which are
assumptions.

## Related

- `subagent-challenge-clauses.md` — the prompt clause that instructs
  agents to use these markers
- `disprove-only-review.md` — review prompt that audits marker usage
- `adversarial-validation.md` — adversarial review with explicit
  Verification Stance Audit

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 7
(Falsification Review, agent adversarial mode), Section 7.3.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
