# Subagent Challenge Clauses

> **Chapter:** ch07 — Generation, Verification, and Review (Section
> 7.3, challenge clauses in generation prompts)
> **Last revised:** 2026-06-16
> **Use this for:** Embedding inside any generation prompt to change
> the agent's incentive structure — from "minimize visible uncertainty"
> to "surface uncertainty explicitly."

These clauses do not replace independent adversarial review, but they
reduce the surface area the review agent must cover. They make the
agent's output more honest and the review more efficient.

Add the relevant clauses to your `structured-prompt.md` template under
a "Challenge clauses" subsection or near the MUST-NOT list.

---

## The Clauses

### Decision Justification

```
For every design decision, state the alternative you considered and
why you rejected it.
```

Forces the agent to make tradeoffs visible. Without this, the agent
presents the chosen path as if it were the only path.

### Error Path Coverage

```
For every error handling path, describe the condition under which this
path executes and whether you have test coverage for it.
```

Surfaces error paths that were written but not tested — the most
common gap in AI-generated code.

### Uncertainty Logging

```
If you are uncertain about any aspect of the implementation, state the
uncertainty explicitly in an IMPL_NOTES.md entry rather than making a
best guess.
```

Redirects the agent from a confident-sounding guess to a logged
uncertainty the reviewer can investigate.

### Assumption Markers

```
Flag any assumption about the runtime environment, input format, or
external service behavior with a comment beginning `// ASSUMPTION:`
that the reviewer can search for.
```

Makes assumptions grep-able. Pair with the verification stance markers
(`verified` / `ASSUMPTION` / `VERIFY`) in
`verification-stance-markers.md`.

---

## Why These Work

The clauses change the agent's incentive structure. Without them, the
agent is rewarded (by the implicit objective of producing
complete-looking code) for minimizing visible uncertainty. With them,
the agent is explicitly instructed to surface uncertainty.

Result: the output is more honest, the review is more efficient, and
the failure modes that adversarial validation would otherwise have to
find are surfaced by the generator itself.

## Related

- `structured-prompt.md` — the prompt these clauses embed inside
- `adversarial-validation.md` — what runs against the output; these
  clauses reduce its work
- `verification-stance-markers.md` — the marker scheme this references

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 7
(Falsification Review, agent adversarial mode), Section 7.3.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
