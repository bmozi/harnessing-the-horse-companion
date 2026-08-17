# Minimum Viable Software Factory Bootstrap

This kit is intentionally not self-contained. It assumes you have read the book sections that teach the judgment behind each artifact:

- Chapter 16: the Merlin Software Factory reference case
- Chapter 19: crawl, walk, run adoption sequencing
- Companion `references/complete-session-loop.md`
- Companion quality-gate configuration reference
- Companion tool-configuration reference
- Chapter 18: measurement and baselines

The files here are scaffolds. They tell you what to fill out; the book explains how to decide what belongs in each field and which risks each field controls.

If you want to see the artifacts working together before filling in your own,
start with the completed, fictional [`worked-example/`](worked-example/).

## What You Are Building

A minimum viable software factory is one governed delivery loop:

1. A context layer that tells agents how this project works.
2. A Work Order layer that scopes non-trivial changes before generation.
3. A gate layer that enforces the checks humans skip under pressure.
4. A learning layer that records what happened and improves the next run.

Do not start with multi-agent orchestration, autonomous improvement, or self-modifying prompts. Those are run-stage practices. Start with one active repository, one pilot task, one manual session loop, and one honest metrics baseline.

## Files

| File | Use it for | Read first |
| --- | --- | --- |
| `01-context-file-checklist.md` | Project context and permission setup | Chapter 19, companion tool-configuration reference |
| `02-work-order-template.md` | Intake artifact for the first pilot task | Chapter 16, companion pipeline-artifact reference |
| `03-quality-gates-starter.yml` | CI skeleton after gate classification | Chapter 7, companion quality-gate configuration reference |
| `04-session-loop-runbook.md` | Manual execution of the first full loop | Companion Complete Session Loop |
| `05-safety-rails-checklist.md` | Autonomy and self-improvement constraints | Chapter 16, Chapter 17 |
| `06-metrics-baseline.md` | Baseline and first-30-days measurement | Chapter 18 |
| `07-factory-readiness-review.md` | Decision to expand beyond the first repo | Chapter 19 |
| `worked-example/` | One complete fictional delivery path from project context through metrics and learning | Read after the session-loop reference |

## Completion Rule

The kit is complete only when every filled artifact points back to a book section or local project fact. If an answer relies on "seems reasonable," stop and find the relevant section, source, test result, or repository evidence.
