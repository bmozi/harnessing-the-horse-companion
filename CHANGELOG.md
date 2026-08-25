# Changelog

All notable public changes to the *Harnessing the Horse* companion
repository are recorded here.

## [Unreleased]

### Added

- Added a book-to-toolkit practice map and a four-book progression so readers
  can see what to practice in the repository, what judgment remains in the
  book, and when one governed session becomes a factory-scale problem.

### Changed

- Positioned the unchanged published companion as an AI coding-agent
  production-readiness toolkit with an explicit request-to-decision journey.
- Clarified that the repository delivers a complete bounded first result while
  the book remains the source of the integrated reasoning, tradeoffs, case
  evidence, and judgment required for responsible application.
- Relettered the platform-modernization design study and its companion
  references from Appendix D to Appendix B so the current two-appendix reader
  edition runs consecutively from A to B.

## [2.1.0] — 2026-08-16

### Added

- Amazon purchase link for the Kindle edition.
- A completed Four-Risk Evidence Contract in the fictional golden path,
  demonstrating how evidence can authorize a reversible phase while keeping a
  later migration gate blocked.

### Changed

- Expanded DESIGN.md from a descriptive skeleton into an agent execution
  contract connecting acceptance criteria, invariants, architecture,
  operational safety, verification, rollback, implementation latitude, and
  human decisions.
- Rebuilt the Cagan four-risk supplement as a risk-to-evidence decision
  instrument with evidence grades, falsifiers, precommitted thresholds,
  engineering constraints, named owners, and generation-gate dispositions.

## [2.0.0] — 2026-08-16

### Added

- A 30-minute [`START-HERE.md`](START-HERE.md) path and a complete,
  fictional software-factory worked example from intake through learning.
- A machine-readable prompt manifest and representative evaluation fixtures
  for structured generation, falsification review, and escalation.
- Runnable TypeScript examples with strict typechecking and five automated
  tests, plus continuous integration for code and content integrity.
- Edition mapping, maintained errata, security reporting, citation metadata,
  commercial-use guidance, and structured issue forms.
- Searchable glossary, twelve-pattern quick reference, and complete
  session-loop reference with its two print-ready diagrams, moved online
  from the print manuscript without removing reader access.
- Twenty chapter Study Guides plus the Appendix D design-study guide,
  preserving all 91 exercises, deliverables, assessments, formal learning
  objectives, key terms, and review/discussion questions outside the
  practitioner manuscript.
- Complete prompt, pipeline-artifact, quality-gate, tool-configuration,
  and competency references moved from the print appendices.
- A portable governance-distribution worked example separating the Agent
  Plugins core, client adapters, additive team extensions, and CI enforcement.
- A sanitized, teaching-oriented software-factory architecture set that
  explains lifecycle, gates, memory, and human judgment without exposing
  private implementation topology or operational inventories.

### Changed

- Consolidated the framework from fourteen to twelve standards while
  preserving every control: structured generation is now Standard 1's
  generation practice, and escalation and override handling are the
  governed-exception half of Standard 6.
- Renamed the canonical standards reference to
  `references/twelve-standards-quick-reference.md` and aligned the
  competency map, prompts, checklists, diagrams, and index.
- Corrected ASYNC gate semantics: checks may run outside the synchronous
  PR pipeline, but their results are required before merge and failures
  block approval.
- Clarified the context-file lifecycle: target fewer than 200 root-file
  lines through pruning and decompose into module-scoped files when a
  monolith grows past roughly 300 lines.
- Reworked the code examples around injected dependencies so their important
  behavior can be tested without live third-party services.

## [1.0.0-kdp-launch] — 2026-08-01

Public companion release for *Harnessing the Horse: Engineering
Discipline for Agentic Development*.

### Added

- Complete chapter-by-chapter asset index in `INDEX.md`.
- Specification and pipeline-artifact templates in `spec-templates/`,
  including SPEC, DESIGN, implementation notes, review, ADR,
  interface, blast-radius, escalation, migration, and task templates.
- Prompt library in `prompts/`, including structured generation,
  adversarial validation, disprove-only review, quality-gate review,
  blast-radius analysis, prompt-injection defense, escalation, and
  verification-marker prompts.
- Lifecycle checklists in `checklists/` for pre-generation,
  post-generation, integration verification, rollback readiness,
  deployment safety, security review, metrics, architecture drift,
  simplicity review, definition of done, iteration caps, migration
  gates, and self-improvement safety rails.
- Pattern reference cards in `patterns/` for anti-corruption layers,
  hexagonal architecture, transactional outbox, event sourcing,
  CAS-guarded distributed commit, scoped authorization tokens,
  dry-run-default tools, and Express Arc.
- MIT-licensed code examples in `code-examples/` for Claude Code
  settings, anti-corruption layer / hexagonal port-adapter structure,
  transactional outbox, and MCP tool design.
- Compatibility example paths in `examples/` for book references that
  point directly to compact snippets.
- Diagram sources and exports in `diagrams/`, including baseline
  architecture diagrams and Merlin Software Factory visuals.
- Reader exercises in `exercises/`, including maturity assessment,
  30-day transformation roadmap, expertise traps, quarterly self-A/B
  test, and case-study analysis materials.
- Single-page references in `references/`, including the Fourteen
  Standards quick reference and pattern catalog.
- Dual-license structure:
  - executable code under MIT via `LICENSE-CODE`
  - written companion content under CC BY-NC-SA 4.0 via
    `LICENSE-CONTENT`
  - top-level `LICENSE` dispatcher explaining the split.

### Release Notes

- This public release is intended to support the Kindle and paperback
  launch of the book.
- The repository history was intentionally squashed for a clean public
  reader experience; this changelog records the public release state,
  not private drafting history.
