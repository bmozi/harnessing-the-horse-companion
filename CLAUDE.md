# CLAUDE.md

Guidance for Claude Code sessions in this repo.

## What this is

The public companion repo for *Harnessing the Horse*. Readers can clone
it for downloadable assets that accompany the book:

- SPEC templates
- Prompt library
- Code examples (Part III + case studies)
- Diagrams
- Exercises
- Prompt evaluations

Treat everything here as reader-facing. Do not commit anything that
would not belong in a public technical-book companion repository.

## What this is NOT

- Not the manuscript. Never copy chapter prose, proposal material, or
  unpublished publishing notes into this repo. Chapter references here
  are by name/number only.
- Not a place for unredacted internal systems, customer data, or
  proprietary code. Everything here is publicly licensed under a
  **dual-license arrangement**:
  - **Source code** (`code-examples/`) → MIT (`LICENSE-CODE`)
  - **Written content** (templates, prompts, checklists,
    factory-bootstrap workbooks, exercises, diagrams, references,
    prose) → CC BY-NC-SA 4.0 (`LICENSE-CONTENT`) — non-commercial use
    with attribution; commercial use requires separate written
    permission. See `LICENSE` for the dispatcher explaining the split.
  When adding new files, classify them correctly: code → MIT;
  templates/prompts/checklists/workbooks/exercises/prose →
  CC BY-NC-SA 4.0.
- Not a forum. Discussion belongs in GitHub Issues / Discussions, not
  in committed prose.

## Source-of-truth boundary

- The book is canonical. If an asset in this repo contradicts a
  passage in the book, the book wins; fix the asset.
- Each asset names its chapter and section in a header comment or
  README entry so readers can navigate book ↔ companion.

## Conventions

- **Asset naming.** `<chapter-or-part>-<slug>.<ext>` — e.g.
  `ch07-review-harness.md`, `part-iii-spec-template.md`. This way an
  alphabetical listing tracks book order.
- **READMEs per directory.** Each top-level dir keeps a `README.md`
  listing assets, the chapter each maps to, and a one-line description.
  Update it when you add an asset.
- **License headers.** Code files include a one-line `// © 2026 John
  Briggs — MIT licensed` header so the license travels with copy-paste.
- **No proprietary identifiers.** Same confidentiality rules as the
  book: no real customer names, no internal employee names other than
  the author, no unredacted credentials, no internal codenames for
  unreleased systems.
- **Examples must run.** Code in `code-examples/` should be runnable as
  written, with a `README.md` explaining setup. If something requires
  external services (an LLM API, etc.), document the env vars and link
  to provider signup.

## Structure

```
spec-templates/    # specification + pipeline-artifact scaffolds (Part II)
prompts/           # prompt library (cross-chapter)
code-examples/     # runnable code (Part III + case studies)
factory-bootstrap/ # minimum viable software factory workbook
prompt-evals/      # compact fixtures for reusable prompt behavior
diagrams/          # architecture diagrams
exercises/         # hands-on practice problems
references/        # single-page references (Twelve Standards)
scripts/           # repository integrity checks
```

## Relationship to manuscript source

Do not move chapter text or proposal content here. Move only reusable
companion assets here: templates, code, diagrams, prompts, checklists,
exercises, and references. Chapter prose should link to the public
companion URL rather than being duplicated.
