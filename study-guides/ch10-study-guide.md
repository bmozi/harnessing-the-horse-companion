# Chapter 10: Compounding Practices — Study Guide

Student and self-study material moved from Chapter 10 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain the three cadences of the Knowledge Loop — capture, lifecycle, close the loop — and the failure mode that appears when each is unguarded.
2. Apply the five capture categories to session outcomes and write context-file entries that transfer knowledge without cross-session contamination.
3. Apply the context-file lifecycle — creation, evolution, pruning, decomposition — to repair an overgrown artifact.
4. Construct a blameless retrospective, structured by the Harness Framework, whose output is a systemic change rather than an assignment of blame.
5. Evaluate a team against the five-level maturity model and construct a 30-day plan to the next level.
6. Execute the complete session loop on a real task, producing the full artifact chain and self-assessing it against the seven-item Definition of Done.

## Key Terms

- **Close-the-loop discipline** — Part of Standard 11: every session ends with an update to AGENTS.md, the prompt library, an ADR, or another mechanism that makes the next session smarter; the most commonly skipped step in the session loop.
- **Definition of Done (DN1–DN7)** — The seven binary completion criteria for an agentic-development change; the operational checklist that turns "done" from a judgment call into a verifiable state.
- **Context file** — `AGENTS.md` or `CLAUDE.md`: the project-root document capturing conventions, constraints, and architecture boundaries; at this tier, the primary vehicle for knowledge capture, managed through creation, evolution, pruning, and decomposition.
- **AGENTS.md** — The project-root context file for non-Claude tools; the destination of DN7's loop-closure update.
- **Regeneration rate** — The percentage of agent-generated changes that require more than one generation cycle before passing review; the loop's leading health metric.
- **Honest journal** — The weekly five-minute reflection — what AI saved, what it cost, what to try differently — that sustains personal calibration; private by default.
- **ADR (Architecture Decision Record)** — At this tier, the Tier 1 destination for captured decisions and the documentation vehicle for changes to the standards themselves.

## Review Questions

1. Name the three cadences of the Knowledge Loop and the failure mode that appears when each is absent.
2. Distinguish knowledge from context as the chapter uses the terms. Why must the first flow between sessions while the second must not?
3. What are the four components of closing the loop, which Definition of Done item encodes the practice, and why is it the most commonly skipped?
4. State the four triggers for updating a standard under Standard 12, with the correct response to each.
5. What are the three things Merlin's improvement plane structurally cannot do, and why does the chapter argue those constraints are what make autonomous improvement safe?

## Discussion Questions

1. The chapter's countermeasure for skipped loop closure is visibility — freshness metrics, a DN7 checkbox, review prompts. Any such metric can be satisfied with empty updates. How does a team keep a compounding practice honest without turning it into compliance theater, and what would you measure to tell the difference?
2. Standard 12 declares every standard in this book a hypothesis. Choose the standard whose supporting evidence you find weakest and design the measurement — metric, baseline, duration, decision rule — that would validate or refute it for a team you know.
3. The honest journal is private by default because honesty requires safety, yet Standard 12's retrospectives need exactly that data. Where should the line sit between personal calibration data and organizational metrics, and who should get to move it?

## Exercises

**Exercise 10.1 (Core) — Repair an overgrown context file.** *(~90 min)* Artifact brief: a 700-line AGENTS.md, three years old, containing (among other things) a convention that was reversed by ADR-014 but never removed, two near-duplicate retry-policy entries with different class names, a warning about a race condition in a module deleted last year, aspirational architecture never built, and current, essential entries about idempotency, connection limits, and module boundaries mixed throughout. Using the lifecycle discipline of §10.1, produce the pruning plan: what is deleted (and why deletion is safe), what is merged, what survives, and how the remainder decomposes into a root file plus module files.
*Deliverable:* The pruning decision log and the proposed root-file outline with its module-file boundaries.
*Assessment:* Judged against §10.1's three pruning questions and the companion repository's `spec-templates/agents-md-template.md`: every deletion cites which question it fails; the contradiction is resolved by removal rather than appended correction; the decomposition boundary follows bounded contexts, not directory structure.

**Exercise 10.2 (Core) — Capture knowledge without contamination.** *(~1 h)* Session-outcome brief: this week's sessions produced (a) a straightforward CRUD endpoint following existing patterns; (b) the discovery that combining a migration and application code in one session caused an integration failure; (c) a new `RetryPolicy` class now used for external calls; (d) a function named `fetchUserProfile` in the profile module; (e) the discovery that production caps the connection pool at 20; (f) a convention change to an `ApiResponse<T>` wrapper adopted mid-sprint. Decide which outcomes warrant a context-file update, and write the exact entry for each that does.
*Deliverable:* The update decisions with rationale, plus the written entries.
*Assessment:* Judged against §10.1's five capture categories and the knowledge-versus-context distinction: (a) correctly produces no update; (d) is recognized as session-specific context that must be abstracted or omitted, not recorded as-is; each written entry is general, prescriptive, and consumable by a session with no memory of this week.

**Exercise 10.3 (Core) — Write the blameless retrospective.** *(~2 h)* Incident brief: an agent-generated pricing change shipped with a rounding error that undercharged customers for six hours. The specification never mentioned rounding; the tests passed because they asserted the code's own output; the reviewer approved under deadline pressure; in the incident meeting, a director asked "who merged this?" Write the retrospective using the Harness Framework structure from §10.2 — Scope, Prove, Enforce, Communicate — and produce the systemic fix. Then rewrite the director's question as the question a generative culture would ask.
*Deliverable:* The four-section retrospective document with a concrete systemic change (a standard update, gate, or context-file entry), plus the reframed question.
*Assessment:* Judged against §10.2 and the just-culture sidebar: the Enforce section proposes a change to the system — never a reminder to be more careful; the weak-test finding (asserting the code's own output) is identified under Prove; the fix is specific enough to implement this sprint.

**Exercise 10.4 (Core) — Assess maturity and plan the next 30 days.** *(~2 h)* Assess a team against the five-level maturity model — your own team, or this described one: specs are written for large features only; review happens but thoroughness depends on who reviews; AGENTS.md exists and was last updated four months ago; CI runs tests and lint; nobody tracks regeneration rate or drift. Assign the level with evidence per key indicator, then write the 30-day plan to the next level using §10.3's adoption path as the skeleton, adapted to the gaps you found.
*Deliverable:* The assessment (level, indicator-by-indicator evidence) and the week-by-week plan.
*Assessment:* Judged against §10.3's key indicators and the companion repository's `exercises/maturity-assessment.md`: the level assignment cites indicators, not vibes; the plan sequences foundations before measurement (no Level 4 practices proposed for a Level 2 team); each week ends with a verifiable state.

**Exercise 10.5 (Challenge) — Run the full session loop, end to end.** *(~4 h+)* Choose a real, small task in a codebase you have access to — a bounded feature or fix an agent session can complete within Standard 2's limits. Using an agent tool of your choice, execute the entire loop: SPEC.md (Standard 1), blast radius estimate (Standard 3), DESIGN.md with interface contracts (Standard 4), a structured generation prompt (Standard 1), generation with IMPL_NOTES.md maintained throughout, gates as available in your environment (Standard 6), both falsification modes — a fresh-instance adversarial pass and your own disprove-only review recorded in REVIEW.md (Standard 7) — blast radius verification, and the close-the-loop update to the context file (Standard 11). Then self-assess: for each of DN1–DN7, cite the evidence that the criterion is met or record honestly that it is not. *Paper variant (no AI tool):* execute the identical loop with yourself as the generation stage — write the code by hand between the same artifacts, and have a peer run the disprove-only review in place of the adversarial agent.
*Deliverable:* The complete artifact chain (SPEC.md, blast radius template, DESIGN.md, generation prompt, IMPL_NOTES.md, REVIEW.md, context-file diff) plus the DN1–DN7 self-assessment with evidence per item.
*Assessment:* Judged against the companion repository's `checklists/definition-of-done.md` with the templates in `spec-templates/` as structural references. Grading is binary at each gate: each DN item passes on cited evidence or fails; a self-assessment that marks an unmet item as honestly unmet, with the reason, outscores one that claims seven passes without evidence. The falsification section of REVIEW.md must contain at least one real finding or an enumerated account of the dimensions checked.

