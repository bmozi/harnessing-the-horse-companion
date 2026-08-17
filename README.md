# Harnessing the Horse — Companion Repository

Reader-facing, downloadable materials for *Harnessing the Horse* (John
Briggs, 2026): a book on agentic engineering — how senior practitioners
ship production software with AI agents as collaborators rather than
autocomplete.

This is the **public companion repository** for the book. The book stands
alone; this repository exists so readers can copy the templates, prompts,
checklists, examples, and quick references without retyping them.

> **Book:** *Harnessing the Horse: Engineering Discipline for Agentic
> Development*
>
> Match your Kindle, paperback, or hardcover to the correct companion in
> [`EDITION-MAP.md`](EDITION-MAP.md), and check [`ERRATA.md`](ERRATA.md)
> for confirmed corrections.

## Start Here

New to the companion? Follow [`START-HERE.md`](START-HERE.md) for a
30-minute orientation, one complete governed agent session, or a practical
software-factory bootstrap path.

For a stable classroom or team baseline, use the
[`v2.0.0` release](https://github.com/bmozi/harnessing-the-horse-companion/releases/tag/v2.0.0).
Match it to your book format in [`EDITION-MAP.md`](EDITION-MAP.md), and
check [`ERRATA.md`](ERRATA.md) for confirmed corrections.
The printable
[`Reader Quick Start`](output/pdf/Harnessing-the-Horse-Reader-Quick-Start-v2.0.0.pdf)
turns the core path into a six-page handout.

## What's here

| Directory | What it contains |
| --- | --- |
| `spec-templates/` | Specification and pipeline-artifact templates referenced across Parts II and III — fill-in scaffolds for discovery, planning, agent-scope, context files (CLAUDE.md / AGENTS.md), ADR, and migration documents. |
| `patterns/` | Named pattern reference cards (Ch11 integration patterns, Ch13 agent infrastructure patterns) with original citations and agentic-development application notes. |
| `prompts/` | Prompt library — reusable system, review, and harness prompts plus a machine-readable manifest. |
| `prompt-evals/` | Small, inspectable fixtures that test the expected behavior of representative prompts. |
| `checklists/` | Human-facing review checklists across the lifecycle — pre-generation, architectural stewardship, pre-merge / pre-deploy, closing the loop, and migration phase gates. |
| `factory-bootstrap/` | Minimum viable software factory workbook plus a completed fictional golden path from intake through learning. |
| `code-examples/` | Runnable, tested MIT-licensed code from Part III patterns — `.claude/settings.json`, Anti-Corruption Layer / Hexagonal port-adapter, Transactional Outbox (SQL + TypeScript), MCP tool pattern. |
| [`diagrams/`](diagrams/) | Architecture diagrams used in the book — four baseline diagrams (Ch4) and a guided set of conceptual, overview, teaching-panel, and print-friendly Merlin Software Factory views (Ch16). |
| `exercises/` | Hands-on exercises — Case Study Analysis Framework, Maturity Assessment. Student-facing material from the instructor package, suitable for self-study or classroom use. |
| `study-guides/` | Chapter-by-chapter learning objectives, key terms, review and discussion questions, and all 91 exercises with deliverable and assessment criteria. |
| `academic/` | Competency and curriculum mapping for academic adoption. |
| `governance-distribution/` | Worked example of a portable Agent Plugins core, client-specific governance adapters, additive team extensions, and agent-independent CI enforcement. |
| `references/` | Searchable and print-friendly references — the [Twelve Standards](references/twelve-standards-quick-reference.md), [pattern quick reference](references/pattern-quick-reference.md), [complete session loop](references/complete-session-loop.md), and [glossary](references/glossary.md). |

Each directory has its own `README.md` explaining what's inside and
how it maps to the book.

For a complete chapter-by-chapter asset map, see [`INDEX.md`](INDEX.md).
For the change log, see [`CHANGELOG.md`](CHANGELOG.md). For the
contribution policy, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## How to use this repo

You do not need the book to use the materials. Each asset is annotated
with the chapter it appears in, so if you're reading along, you can clone
this repo and follow the examples in your own editor.

```bash
git clone https://github.com/bmozi/harnessing-the-horse-companion.git
cd harnessing-the-horse-companion
npm ci
npm run check
```

The final two commands are optional for readers and recommended for anyone
adapting the runnable examples or contributing changes. They typecheck and
test the examples and validate the companion's local links, prompt metadata,
licenses, versions, and public architecture boundary.

If you're using these as part of a course or in your own team, fork the
repo and customize it within the applicable license terms, retaining
the required notices and attribution.

## License

This repository is **dual-licensed**:

- **Executable source code** in `code-examples/` and the workflow under
  `governance-distribution/enforcement/` — **MIT License**. Use, fork, adapt,
  integrate into your own projects, including commercial work.
  See [`LICENSE-CODE`](LICENSE-CODE).
- **Written content** in `spec-templates/`, `prompts/`, `checklists/`,
  `factory-bootstrap/`, `exercises/`, `study-guides/`, `academic/`,
  `governance-distribution/` except its enforcement workflow, `diagrams/`, `references/`
  (templates, prompts, checklists, exercises, diagrams, references,
  prose) — **Creative
  Commons BY-NC-SA 4.0**. Free for
  non-commercial use with attribution; share-alike for derivatives.
  Commercial use — including paid courses, paid SaaS products bundling
  these artifacts, AI-training-data licensing — requires separate
  written permission from the author. See
  [`LICENSE-CONTENT`](LICENSE-CONTENT).

[`LICENSE`](LICENSE) is the dispatcher — it explains the split and
points to the two specific licenses. Why the dual setup is in the file
itself.

The plain-language [`COMMERCIAL-USE.md`](COMMERCIAL-USE.md) guide answers
common reuse questions; the license files remain authoritative.

## Errata and contributions

Spot something broken? Use the structured
[errata](https://github.com/bmozi/harnessing-the-horse-companion/issues/new?template=errata.yml)
or [broken-resource](https://github.com/bmozi/harnessing-the-horse-companion/issues/new?template=broken-resource.yml)
form. Pull requests are welcome for
typos, code fixes, and additional examples — but please open an issue
first for anything substantive so we can discuss scope.

Report suspected vulnerabilities privately as described in
[`SECURITY.md`](SECURITY.md). Citation metadata is available in
[`CITATION.cff`](CITATION.cff).

## About the book

*Harnessing the Horse* is a practitioner book on engineering discipline
for agentic development: standards, architecture, verification, security,
measurement, and team adoption for production AI-generated code.

— John Briggs
