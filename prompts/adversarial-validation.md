# Adversarial Validation Prompt

> **Chapter:** ch07 — Generation, Verification, and Review (Standard
> 8: Falsification Review, agent adversarial mode)
> **Last revised:** 2026-06-16
> **Model assumed:** Frontier model — a FRESH instance with zero shared
> context from the generation session
> **Use this for:** High-risk changes (security-sensitive code,
> payment paths, data migrations). Escalation beyond the standard
> disprove-only review.

The deepest problem with single-agent review is context contamination.
Ask the same agent that generated the code to review it, and you will
receive a confident self-assessment that confirms its own choices. This
is not a flaw in the agent's reasoning; it is a structural property of
context-dependent inference.

Adversarial validation uses a *fresh* agent instance — zero shared
context — with the explicit goal of finding failures. Not a second
opinion. A structured adversarial process designed to exploit the fact
that different agent instances, starting from different initial
contexts, will catch different classes of errors.

---

```markdown
## Adversarial Validation Review

You are a FRESH reviewer with NO prior context about this code.
Your objective is DESTRUCTION: find every way this code can fail.

### Context
- Specification: [SPEC.md contents]
- Generated code: [code under review]
- MUST-NOT list: [prohibitions from the generation prompt]

### Your Mandate
You are not evaluating whether this code is "good."
You are trying to BREAK it. For every function, ask:
1. What happens with null/nil/undefined input?
2. What happens with empty input?
3. What happens with maximum-size input?
4. What happens with malformed input?
5. What happens under concurrent access?
6. What happens when an external dependency fails?
7. What happens when an external dependency is slow?
8. What happens when disk/memory/network is exhausted?

### Security Audit
- [ ] Input validation: is every external input validated before use?
- [ ] Authentication: are all endpoints properly authenticated?
- [ ] Authorization: are permissions checked at the resource level, not
      just the route level?
- [ ] Injection: can any input reach a query/command without
      sanitization?
- [ ] Secrets: are any credentials, keys, or tokens hardcoded or
      logged?
- [ ] Dependencies: are there known CVEs in any imported package?

### Verification Stance Audit
For every factual claim in comments or documentation:
- Mark as `verified` (with source) if you can confirm it
- Mark as `ASSUMPTION` if it appears plausible but unverified
- Mark as `VERIFY` if it appears questionable or you have no basis to
  evaluate it

### Output Format
List every finding as:
- **Location:** file:line
- **Severity:** CRITICAL / MAJOR / MINOR
- **Failure scenario:** [specific conditions under which this fails]
- **Evidence:** [why you believe this is a real issue, not a false
  positive]
- **Remediation:** [specific fix]

End with a summary: X findings (Y critical, Z major, W minor).
If you find zero issues, state: "Unable to identify failures in this
review pass. This does NOT mean the code is correct — it means this
review instance did not find issues. A subsequent review with different
focus areas may."
```

---

## Operational Setup

The adversarial validation review MUST run in a fresh agent instance.
Tactical options:

- A new chat session in your AI IDE / CLI tool with no prior context
  loaded.
- A different model entirely (e.g., generation by Claude, review by
  GPT or Gemini) for orthogonal failure-mode coverage.
- A separate session that loads only the SPEC.md, the generated code,
  and the MUST-NOT list — no CLAUDE.md, no IMPL_NOTES.md, no design
  rationale.

The discipline is: zero shared context with the generation session.

## Related

- `disprove-only-review.md` — the standard review; adversarial
  validation escalates from there
- `subagent-challenge-clauses.md` — embed in generation prompt to
  reduce the surface area the adversarial reviewer must cover
- `verification-stance-markers.md` — the `verified` / `ASSUMPTION` /
  `VERIFY` scheme audited above

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 7
(Falsification Review, agent adversarial mode).

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
