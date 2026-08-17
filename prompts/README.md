# Prompt Library

System prompts, review prompts, and harness prompts adapted from
Chapter 7 of *Harnessing the Horse* — the heart of the book — plus
companions from Chapters 5 and 17.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and case-study
> context that make these prompts effective rather than merely
> plausible. Written content in this directory is licensed under
> CC BY-NC-SA 4.0 ([see `../LICENSE-CONTENT`](../LICENSE-CONTENT)).

These are starting points. Adapt them to your model, your codebase,
and your team's conventions. The book argues against treating prompts
as magic incantations; treat these as *templates* and tune them
against your actual measured outcomes.

## Prompts

| File | Chapter | Purpose |
| --- | --- | --- |
| [`complete-prompt-library.md`](complete-prompt-library.md) | cross-book | Full compact prompt library moved from the print appendices; use the smaller files below when you want one workflow at a time |
| [`structured-prompt.md`](structured-prompt.md) | ch07 — Std 1 | The generation prompt: Task, Functional Requirements, Constraints (Interface, Dependencies, Patterns, Security, Performance), MUST-NOT List, Output Format, Review Criteria |
| [`quality-gate-config-review.md`](quality-gate-config-review.md) | ch07 — Std 6 | Audit a project's CI gate configuration against the four-tier classification (Blocking / Advisory / Informational / Async) |
| [`disprove-only-review.md`](disprove-only-review.md) | ch07 — Std 7 (human mode) | The standard review prompt. Your task is NOT to confirm correctness — your task is to find how this code FAILS. |
| [`adversarial-validation.md`](adversarial-validation.md) | ch07 — Std 7 (agent mode) | Escalation prompt for high-risk changes. Fresh agent instance, zero shared context, destructive mandate. Includes Security Audit and Verification Stance Audit. |
| [`blast-radius-analysis.md`](blast-radius-analysis.md) | ch05 — Std 3 (review-time) | Review-time blast-radius quantification across direct / dependency / data / external impact; produces a Contained / Moderate / Broad / Critical classification for review prioritization |
| [`escalation-protocol.md`](escalation-protocol.md) | ch07 — Std 6 | What happens when a quality gate fails: four-tier authority model, thrashing prevention rule (30 min / 3 iterations), ESCALATION.md format |
| [`subagent-challenge-clauses.md`](subagent-challenge-clauses.md) | ch07 — §7.3 | Four clauses to embed inside generation prompts that change the agent's incentive structure from "minimize visible uncertainty" to "surface uncertainty explicitly" |
| [`verification-stance-markers.md`](verification-stance-markers.md) | ch07 — §7.3 | The `verified` / `ASSUMPTION` / `VERIFY` marker convention. Eliminates the worst failure mode of AI-generated documentation: the confidently-stated falsehood. |
| [`prompt-injection-defense.md`](prompt-injection-defense.md) | ch17 — §17.2 | Four-layer prompt-injection defense embedded in any agent that processes external data: privilege minimization, input-output separation (XML/JSON containers), output validation (tool manifest allowlist), human-in-the-loop for high-risk operations. Maps to OWASP Agentic Top 10 ASI06. |

## The flow

```
         Generation                Review                  Escalation
      ─────────────────         ───────────────         ─────────────────
   structured-prompt.md  ──►  disprove-only-review.md  ──►  adversarial-validation.md
            │                          │                          │
            │ embeds                   │ also runs                 │ also runs
            ▼                          ▼                          ▼
   subagent-challenge-clauses.md  quality-gate-config-review.md  verification-stance-markers.md
            │                          │                          │
            │ uses                     │ failures trigger         │ used by
            ▼                          ▼                          ▼
   verification-stance-markers.md  escalation-protocol.md       (same)
                                       │
                                       │ informed by
                                       ▼
                                  blast-radius-analysis.md
```

## Provenance

Each prompt file carries a header block with:
- Chapter and standard reference
- Last revised date
- Model assumed (frontier-class, e.g. Claude Sonnet 4.6+)

When you adapt one, change `Last revised` and add a `# Adapted from:`
line so attribution stays intact downstream.

## Coverage note

This directory contains the complete compact library plus the reusable
prompt assets the book treats as portable: generation, review, escalation, blast-radius analysis,
verification stance, and prompt-injection defense. Case-study-specific
prompts are represented through the general templates and the
case-study walkthroughs in `../exercises/`.
