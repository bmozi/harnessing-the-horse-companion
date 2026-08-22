# Tool Configuration Reference

The three configuration artifacts that turn the engineering
standards from advisory documentation into enforced
infrastructure: the agent permission policy
(`.claude/settings.json`), the project context file
(`AGENTS.md` / `CLAUDE.md`), and the CI/CD integration that
makes the quality gates blocking. Each is shown in full,
with annotations explaining why each entry exists.

The companion repository carries the
same configuration with full per-line annotation
(`code-examples/claude-settings/settings.jsonc`); this
appendix gives you the configurations in the form you can
copy and adapt for your project.

---

## F.1 `.claude/settings.json` — Agent Permission Policy

The reference structural guardrails for Claude Code agent
sessions, applying the Principle of Least Privilege (Saltzer
& Schroeder, 1975) to AI agents. In other tools, the
equivalent file exists under a different name (in Cursor,
`.cursorrules` and its successor `.cursor/rules/`; workspace
configuration in Copilot Workspace).
**The tool varies. The principle does not.**

The permission strings below are illustrative pseudocode —
permission syntax differs by tool and version, so consult
your tool's current documentation for the exact schema.

```jsonc
// .claude/settings.json
{
  "permissions": {
    "allow": [
      // READ operations — the agent needs to understand the
      // codebase
      "read",           // Read any file in the project
      "inspect_git",    // View git status, log, diff —
                        //   read-only git

      // WRITE operations — the agent needs to produce code
      "write",          // Create or modify files
      "edit",           // Edit existing files (some tools
                        //   distinguish write from edit)

      // VERIFY operations — the agent needs to validate its
      // output
      "test",           // Run the project's test suite
      "lint",           // Run linters and static analysis
      "build",          // Compile or bundle the project
      "type_check"      // Run type-checking (tsc, mypy, etc.)
    ],

    "deny": [
      // DESTRUCTIVE operations — the agent must not destroy
      // state
      "rm -rf",         // Recursive force-delete. No
                        //   legitimate agentic use case.
      "git clean -fdx", // Deletes untracked files.
                        //   Irreversible in the wrong context.

      // PUBLICATION operations — the agent must not publish
      // artifacts
      "git push",       // Pushing is a human decision. The
                        //   agent generates; the human
                        //   publishes.
      "git merge",      // Merging is a human decision.
                        //   Separates generation from
                        //   integration.
      "npm publish",    // Publishing a package is irreversible.
      "docker push",    // Publishing an image is irreversible.
      "twine upload",   // Publishing to PyPI is irreversible.

      // EXECUTION-FROM-UNTRUSTED-SOURCE operations
      "curl | sh",      // Downloading and executing arbitrary
      "curl | bash",    //   scripts from the internet is the
      "wget | sh",      //   canonical supply chain attack
      "wget | bash",    //   vector.

      // PRIVILEGE ESCALATION operations
      "sudo",           // The agent should never need root.
      "chmod 777",      // World-writable permissions are never
                        //   correct.
      "chown"           // Ownership changes require human
                        //   judgment.
    ]
  }
}
```

**Allow list rationale.** Read, write, verify. Nothing more.
The agent reads to understand, writes to produce, runs the
project's verification suite to validate its own output.

**Deny list rationale.** Three categories:
**destructive** (`rm -rf`, `git clean -fdx`) — operations the
agent has no legitimate need for; **publication** (`git push`,
`npm publish`) — operations that collapse the separation
between generation and integration; **untrusted execution**
(`curl | sh`) — the canonical supply chain attack vector.
Allowing `git push` is the single most common and most
consequential misconfiguration. The agent generates; the
human publishes.

**Operations NOT on the allow list** (granted per-session
if needed): network requests to arbitrary URLs, package
installation, service restarts, environment variable
modification, database access. These may be necessary for
specific tasks, but should be granted per-session with
explicit justification, not blanket-allowed in the project
configuration.

---

## F.2 `AGENTS.md` (or `CLAUDE.md`) — Project Context File

The minimum viable project-root context file. Stored at the
repository root. Claude Code loads `CLAUDE.md`
automatically; non-Claude tools load `AGENTS.md` by
convention. Either filename works; choose one and stay
consistent across the repository.

The file is four sections. Anything beyond four sections
risks the "lost in the middle" problem (Liu et al., 2024) —
attention quality degrades for content placed in the middle
of long contexts. Aim for under 200 lines; 300 lines with
regular pruning is the enforceable ceiling — the Standard 11
gate (see the quality-gate configuration reference) flags a file that exceeds it.

```markdown
# AGENTS.md (or CLAUDE.md)

## Project Overview
[Project name] is a [brief description: what it does, who it
serves, what stage it is at]. The primary language is
[language/version]. The project follows [architectural
pattern] as described in [reference].

Key technologies: [list with versions]
Package manager: [tool and lockfile location]
Build command: [exact command]
Test command: [exact command]
Lint command: [exact command]

## Conventions
- Error handling: [describe the pattern — e.g., "Return errors
  as the last value; never panic outside of main"]
- Naming: [describe conventions — e.g., "PascalCase for
  exported types, camelCase for local variables, snake_case
  for database columns"]
- File organization: [describe where things go — e.g., "Domain
  logic in internal/domain/, adapters in internal/adapters/,
  handlers in internal/handlers/"]
- Testing: [describe the testing philosophy — e.g., "Unit
  tests alongside source files as *_test.go; integration
  tests in test/integration/"]
- Dependencies: [policy — e.g., "No new dependencies without
  documented rationale in IMPL_NOTES.md. Prefer stdlib over
  third-party."]

## Constraints
- MUST-NOT modify the database schema without an approved
  migration plan
- MUST-NOT add routes outside the /api/v2/ prefix
- MUST-NOT import from internal/legacy/ (deprecated;
  scheduled for removal — see ADR-007 for the migration
  plan; target completion Q3 2026)
- MUST-NOT use global mutable state
- MUST-NOT introduce new environment variables without
  updating deploy/env.example
- [Add project-specific prohibitions]

## Architecture Boundaries
- The domain layer (internal/domain/) MUST NOT import from
  adapter or handler packages
- The adapter layer (internal/adapters/) may import from
  domain but MUST NOT import from handlers
- External vendor SDKs are wrapped in adapter implementations;
  domain code never references vendor types directly
- See diagrams/system-context.mmd and diagrams/component.mmd
  for visual reference
```

**Update cadence.** Every PR that changes project
conventions, architecture boundaries, or constraints should
include a corresponding update to this file. Living
constraints (those that include the *why*, not just the
rule) outperform static constraints because they let the
agent reason about edge cases at the boundary.

---

## F.3 CI/CD Integration

The quality gates from Standard 9 (Chapter 8) must run as
*blocking* checks in CI, not as advisory documentation.
Below is a sample GitHub Actions workflow that enforces
the four-tier gate classification. Adapt to your CI system
(GitLab, CircleCI, Jenkins, etc.) — the gate structure is
universal; the syntax varies.

```yaml
# .github/workflows/quality-gates.yml
name: Quality Gates

on:
  pull_request:
    branches: [main]

jobs:
  blocking-gates:
    name: Blocking Gates (must pass to merge)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - name: Setup toolchain
        # tool versions pinned in your project's manifest
        run: ./scripts/setup-ci.sh

      # ─── BLOCKING gates: failure halts merge ───────────────
      - name: Type check
        run: pnpm type-check        # zero errors tolerated

      - name: Unit tests
        run: pnpm test:unit         # 100% pass; no skipped
                                    # tests without documented
                                    # reason

      - name: Security scan
        run: pnpm security:scan     # zero CRITICAL, zero HIGH
                                    # findings

      - name: Dependency license compliance
        run: pnpm license:check     # all deps on approved
                                    # license list

      - name: Architecture boundaries
        run: pnpm arch:check        # CI-enforced architecture
                                    # rules (no prohibited
                                    # cross-module imports)

      - name: API contract validation
        run: pnpm contract:check    # generated OpenAPI matches
                                    # implementation signatures

  advisory-gates:
    name: Advisory Gates (findings surfaced, not blocking)
    runs-on: ubuntu-latest
    continue-on-error: true        # findings surface but do
                                    # not fail the PR
    steps:
      - uses: actions/checkout@v7
      - name: Coverage delta
        run: pnpm coverage:delta    # delta reported; threshold
                                    # violations highlighted

      - name: Complexity metrics
        run: pnpm complexity:check  # functions exceeding
                                    # threshold flagged

      - name: Performance regression
        run: pnpm bench:regression  # benchmarks above tolerance
                                    # flagged

      - name: Documentation coverage
        run: pnpm docs:check        # public APIs missing
                                    # doc comments listed

  informational-gates:
    name: Informational Gates (logged for trend tracking)
    runs-on: ubuntu-latest
    continue-on-error: true        # never blocks; data feeds
                                    # the metrics dashboard
    steps:
      - uses: actions/checkout@v7
      - name: LOC delta
        run: pnpm metrics:loc-delta      # logged to dashboard

      - name: Dependency inventory
        run: pnpm metrics:deps           # inventory snapshot

      - name: Test execution time
        run: pnpm metrics:test-time      # trend tracking

      - name: AI-generation metadata
        run: pnpm metrics:ai-provenance  # session/model data
                                          # for attribution

  async-gates:
    name: Async Gates (resolve before merge but run async)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - name: Full integration tests
        run: pnpm test:integration

      - name: Full dependency vulnerability scan
        run: pnpm audit --recursive

      - name: Performance benchmarks
        run: pnpm bench:full
```

**Branch protection settings.** In the repository settings,
the `blocking-gates` job above must be configured as a
*required status check* on the protected branch (typically
`main`). Without this, the CI's BLOCKING gates are
advisory only — anyone with write access can merge over
them. The Standard 6 escalation protocol governs the
narrow cases when an override is justified; those
overrides are logged in `ESCALATION.md`.

**Provenance commits.** A separate workflow tags
agent-generated commits with session metadata. The commit
message footer should include:

```
Session: claude-code-<YYYY-MM-DDTHH:MM:SSZ>
Model: <model-id>
Reviewer: <name>
Spec: <path or link to SPEC.md>
```

The provenance metadata enables the attribution discipline
described in Chapter 18 — separating agent-generated from
human-generated changes in metric dashboards is the
prerequisite for honest measurement.

---

The three artifacts above — `.claude/settings.json`,
`AGENTS.md`, and the CI/CD workflow — compose the
*structural* layer of the engineering discipline. The
context file tells the agent what to do; the permission
policy constrains what it *can* do; the CI/CD pipeline
verifies the result. Each layer compensates for the
others' weaknesses. The context file's compliance is
statistical (~70%, author's estimate from practice). Hooks
are deterministic when invoked but can be bypassed locally;
protected CI and repository permissions supply independent
merge enforcement. Defense in depth is the design.

For the companion repository's annotated version of
`.claude/settings.json` with OWASP Agentic Top 10 mapping,
see `code-examples/claude-settings/`. For prompt-injection
defense at the agent-prompt layer (a complementary
configuration not shown here), see Chapter 17 and
companion `prompts/prompt-injection-defense.md`.
