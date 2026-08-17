# Context File Checklist

Read Chapter 19 and the companion tool-configuration reference before using this checklist. This file deliberately does not explain why each section matters.

## Target Repository

- Repository:
- Primary language and version:
- Package manager:
- Build command:
- Test command:
- Lint command:
- Type-check command:
- Secret-scan command:

## Context File

- [ ] `AGENTS.md` or `CLAUDE.md` exists at the project root.
- [ ] Project overview names what the system does and who it serves.
- [ ] Key technologies and versions are listed.
- [ ] Build, test, lint, and type-check commands are exact.
- [ ] Conventions are explicit: errors, naming, file organization, tests, dependencies.
- [ ] Constraints include project-specific MUST-NOT items.
- [ ] Architecture boundaries are written as import or module rules where possible.
- [ ] The file is short enough to be reliably read by agents.
- [ ] There is an owner responsible for pruning and updating it.

## Agent Permission Policy

- [ ] Read source and documentation.
- [ ] Edit source and tests.
- [ ] Run tests, lint, build, type check, and inspect git state.
- [ ] Block destructive deletes.
- [ ] Block push, merge, and publish by default.
- [ ] Block untrusted network script execution.
- [ ] Require per-session approval for package installation, database access, service restarts, and environment changes.

## First Update Trigger

Record the first condition that will require this context file to change:

- New project convention:
- New forbidden pattern:
- New architecture boundary:
- New recurring agent failure:
