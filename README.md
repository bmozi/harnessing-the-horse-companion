# Harnessing the Horse — Companion Repository

## AI Coding Agent Production-Readiness Toolkit

Take one AI-assisted software change from a vague request to an evidence-backed
**SHIP**, **REVISE**, or **STOP** decision. The repository supplies copyable
specifications, scope controls, prompts, quality gates, review checks, and a
worked fictional delivery loop. It helps a reader practice the mechanics; it
does not certify that a change or organization is production-ready.

This is the reader-facing, downloadable companion for *Harnessing the Horse*
(John Briggs, 2026), a book about how senior practitioners ship production
software with AI agents as collaborators rather than autocomplete.

### The book-and-toolkit contract

The book stands alone. The toolkit extends it without reproducing it:

- **The toolkit provides the moves:** reusable artifacts, runnable examples,
  and one bounded path readers can practice immediately.
- **The book provides the judgment:** why the moves exist, how they fit
  together, which tradeoffs and failure modes matter, how the case evidence
  changes the guidance, and how a team earns greater autonomy.
- **The complete practice requires both:** copying a checklist is not the same
  as knowing when its evidence is sufficient or when the responsible decision
  is to stop.

> **Book:** *Harnessing the Horse: Engineering Discipline for Agentic
> Development*
>
> **[Read on Kindle](https://www.amazon.com/dp/B0HCR9KHMB)**
>
> Match your Kindle, paperback, or hardcover to the correct companion in
> [`EDITION-MAP.md`](EDITION-MAP.md), and check [`ERRATA.md`](ERRATA.md)
> for confirmed corrections.

## Start Here

New to the companion? Follow [`START-HERE.md`](START-HERE.md) for a
30-minute orientation or one complete production-readiness journey:

`REQUEST → SPECIFY → BOUND → BUILD → CHALLENGE → PROVE → SHIP / REVISE / STOP`

The journey produces a useful first result. The book supplies the integrated
engineering system needed to repeat and adapt it responsibly.

For a stable classroom or team baseline, use the
[`v2.1.1` release](https://github.com/bmozi/harnessing-the-horse-companion/releases/tag/v2.1.1).
Match it to your book format in [`EDITION-MAP.md`](EDITION-MAP.md), and
check [`ERRATA.md`](ERRATA.md) for confirmed corrections.
The printable
[`Reader Quick Start`](output/pdf/Harnessing-the-Horse-Reader-Quick-Start-v2.1.1.pdf)
turns the core path into a six-page handout.

## What's here

| Directory | What it contains |
| --- | --- |
| `spec-templates/` | Specification and pipeline-artifact templates referenced across Parts II and III — fill-in scaffolds for discovery, planning, agent-scope, context files (CLAUDE.md / AGENTS.md), ADR, and migration documents. |
| `patterns/` | Named pattern reference cards (Ch11 integration patterns, Ch13 agent infrastructure patterns) with original citations and agentic-development application notes. |
| `prompts/` | Prompt library — reusable system, review, and harness prompts plus a machine-readable manifest. |
| `prompt-evals/` | Small, inspectable fixtures that test the expected behavior of representative prompts. |
| `checklists/` | Human-facing review checklists across the lifecycle — pre-generation, architectural stewardship, pre-merge / pre-deploy, closing the loop, and migration phase gates. |
| `factory-bootstrap/` | Minimum governed delivery loop workbook plus a completed fictional golden path from intake through learning; the Book 2 production-readiness path, not a complete multi-team production factory. The published path remains unchanged. |
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
Use the [`BOOK-TO-TOOLKIT-MAP.md`](BOOK-TO-TOOLKIT-MAP.md) to pair each
practice step with the book reasoning needed to complete it. See
[`SERIES-PROGRESSION.md`](SERIES-PROGRESSION.md) for the role of all four books
and the handoff from one governed change to an accountable software factory.
For the change log, see [`CHANGELOG.md`](CHANGELOG.md). For the
contribution policy, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## How to use this repo

You can inspect or run an individual asset without the book. To apply the
materials as a coherent production practice, pair them with the relevant book
chapters. Each asset identifies its chapter so the reasoning and the reusable
artifact stay connected.

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

When one team's governed delivery loop becomes a multi-team production-system
problem, continue with *The Accountable AI Software Factory* and its
[runnable laboratory](https://github.com/bmozi/accountable-ai-software-factory-companion).

— John Briggs
