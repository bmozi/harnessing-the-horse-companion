# Changelog

All notable public changes to the *Harnessing the Horse* companion
repository are recorded here.

## [Unreleased]

### Added

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
