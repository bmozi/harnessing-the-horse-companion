# AGENTS.md Context File Template

> **Chapter:** ch04 — Foundations (Section 4.1, "The Context File")
> **Last revised:** 2026-07-02
> **Use this for:** The minimum viable project-root context file, in the
> vendor-neutral filename. Drop into your repository as `AGENTS.md`.
> Either filename works — `AGENTS.md` is the tool-agnostic convention
> a growing number of agents read by default, while `CLAUDE.md` is the
> filename Claude Code loads automatically (see
> [`claude-md-template.md`](claude-md-template.md) for that variant).
> The content and the upkeep discipline are identical; only the filename
> determines which tools pick it up without configuration. Roughly 800 tokens, five
> sections.

A context file that tries to document everything documents nothing
effectively. Attention quality degrades long before the context
window fills (the "lost in the middle" effect — Liu et al., 2024).
Keep this file *short, selective, and current*. Move domain-specific
details into module-level context files; move task-specific details
into the session prompt.

This template is the project-root layer (Level 1). It tells the agent:
**what kind of project this is, how we write code, what to avoid, and
where the architectural boundaries are.**

---

```markdown
# AGENTS.md

## Operating Principles

1. **Think before coding.** State assumptions explicitly. If the task is
   ambiguous, ask rather than guess. Push back when a simpler approach
   exists. Stop when confused — name what's unclear instead of guessing
   forward.
2. **Surgical changes.** Touch only what the task requires. Don't
   "improve" adjacent code, comments, or formatting. Don't refactor what
   isn't broken. Match the surrounding style.
3. **Read before you write.** Before adding code, read the immediate
   callers, exports, and shared utilities. "Looks orthogonal" is
   dangerous. If you can't explain why something is structured the way
   it is, you're not ready to change it.
4. **Match the codebase's conventions, even if you disagree.**
   Conformance beats taste inside someone else's codebase. If a
   convention seems harmful, surface it once. Don't fork silently.
5. **Fail loud.** "Completed" is wrong if anything was skipped silently.
   "Tests pass" is wrong if any were skipped. Surface uncertainty;
   never hide it behind a tidy summary.
6. **Adversarially review your own substantive work before presenting
   it.** Try to break your own output; surface the strongest objections.
   If a sincere attempt finds none, say so.
7. **Close the loop.** Every session ends with an update — to this file,
   a refined prompt, a new ADR, or a retrospective entry — that helps
   the next session do better.


## Project Overview
[Project name] is a [brief description: what it does, who it serves, what
stage it is at]. The primary language is [language/version]. The project
follows [architectural pattern] as described in [reference].

Key technologies: [list with versions]
Package manager: [tool and lockfile location]
Build command: [exact command]
Test command: [exact command]
Lint command: [exact command]

## Conventions
- Error handling: [describe the pattern — e.g., "Return errors as the
  last value; never panic outside of main"]
- Naming: [describe conventions — e.g., "PascalCase for exported types,
  camelCase for local variables, snake_case for database columns"]
- File organization: [describe where things go — e.g., "Domain logic in
  internal/domain/, adapters in internal/adapters/, handlers in
  internal/handlers/"]
- Testing: [describe the testing philosophy — e.g., "Unit tests alongside
  source files as *_test.go; integration tests in test/integration/"]
- Dependencies: [policy — e.g., "No new dependencies without documented
  rationale in IMPL_NOTES.md. Prefer stdlib over third-party."]

## Constraints
- MUST-NOT modify the database schema without an approved migration plan
- MUST-NOT add routes outside the /api/v2/ prefix
- MUST-NOT import from internal/legacy/ (deprecated; scheduled for removal)
- MUST-NOT use global mutable state
- MUST-NOT introduce new environment variables without updating
  deploy/env.example
- [Add project-specific prohibitions]

## Architecture Boundaries
- The domain layer (internal/domain/) MUST NOT import from adapter or
  handler packages
- The adapter layer (internal/adapters/) may import from domain but
  MUST NOT import from handlers
- External vendor SDKs are wrapped in adapter implementations; domain
  code never references vendor types directly
- See diagrams/system-context.mmd and diagrams/component.mmd for
  visual reference
```

---

## The Three-Level Context Hierarchy

This template is **Level 1: Project Context**. Two more layers compose
to form the agent's complete understanding:

- **Level 1: Project Context** — `AGENTS.md` at repository root.
  Project-wide conventions, constraints, architecture boundaries. Every
  session in the repo receives this automatically (or via explicit
  configuration — see Failure Modes below). Answers: *"What kind of
  project is this, and what are the universal rules?"*
- **Level 2: Module Context** — `AGENTS.md` in subdirectories. Domain-
  specific guidance (e.g., `services/payment/AGENTS.md`: "All monetary
  values as integer cents, never floating-point. PCI compliance requires
  raw card numbers never appear in logs."). Supplements Level 1.
  Answers: *"What is special about this part of the project?"*
- **Level 3: Session Context** — the prompt itself, plus the SPEC.md /
  DESIGN.md for the task. Ephemeral, session-scoped. Answers: *"What am
  I building right now?"*

## Living Constraint Pattern

The most effective context files evolve into living architecture
documents. Compare:

- **Static constraint:** `MUST-NOT import from internal/legacy/`
- **Living constraint:** `MUST-NOT import from internal/legacy/ — this
  package contains the pre-2025 monolith's data access layer. It uses
  raw SQL with string concatenation (injection risk) and returns
  untyped map[string]interface{} values. We are migrating to the
  repository pattern in internal/domain/repo/. ADR-007 documents the
  migration plan. Target completion: Q3 2026.`

The second gives the agent not just the rule but the *reason*. An
agent that understands *why* a package is prohibited can propose a
correct alternative at the boundary rather than silently importing
the prohibited package because it seemed like the fastest path.

## Maintaining Both Filenames

If your team uses tools that read different filenames, keep one file
as the source of truth and make the other a symlink or a one-line
pointer ("See AGENTS.md"). Two independently edited context files
drift apart, and a drifted context file actively misleads the agent
that loads the stale copy.

## Failure Modes

- **Too long** — irrelevant or stale material can obscure important rules;
  there is no universal 2,000-token failure threshold. Keep root guidance
  focused, scope detail by module, and test retrieval of critical constraints.
- **Too short** — "This is a Go project using PostgreSQL" is barely
  better than nothing. The Conventions and Constraints sections carry
  the weight.
- **Never updated** — a context file describing six-month-old
  architecture actively misleads. Update on every PR that touches
  conventions, boundaries, or constraints.
- **Exists but is not loaded** — loading behavior varies by tool:
  many agents read `AGENTS.md` by default, Claude Code loads
  `CLAUDE.md`, Cursor loads `.cursorrules`, and some tools need the
  file referenced in configuration. Test by asking a new session:
  *"What are the project's architecture boundaries?"* If the agent
  can't answer from the file, it isn't being loaded.

## Related

- `claude-md-template.md` — the same template under the filename
  Claude Code loads automatically
- `spec-md.md` — Level 3 task context that the agent receives per session
- `../checklists/pre-generation-verification.md` — verifies the agent
  loaded the context before generating

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.1, and the
companion tool-configuration reference.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
