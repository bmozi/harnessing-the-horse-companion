# Claude Code Settings Reference (.claude/settings.json)

> **Chapter:** ch04 — Foundations (Section 4.2, "Structural Guardrails")
> **Last revised:** 2026-06-16
> **Use this for:** Reference implementation of structural guardrails
> for Claude Code agent sessions. Apply the principle of least privilege
> to AI agents.

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and
> case-study context that make these guardrails meaningful rather
> than ritual. **This `.jsonc` configuration is licensed under the MIT
> License** ([see `../../LICENSE-CODE`](../../LICENSE-CODE)) — drop it
> into your project's `.claude/` directory and adjust per project,
> including in commercial contexts.

## What's in this directory

| File | Purpose |
| --- | --- |
| [`settings.jsonc`](settings.jsonc) | Reference configuration with annotations explaining *why* each entry exists |
| `README.md` (this file) | How to apply, what it prevents, and how to extend |

## How to apply

1. Copy `settings.jsonc` to your project's `.claude/` directory.
2. Rename to `.claude/settings.json` and strip the `//` comments if
   your tool doesn't accept JSONC. (Claude Code accepts JSONC; some
   tools don't.)
3. Adjust the `allow` and `deny` lists for your project's specific
   needs. Document each customization with a comment explaining the
   rationale — **guardrails without rationale are guardrails that
   will be removed the first time they inconvenience someone.**
4. Treat overrides as non-negotiable. If an engineer needs an
   operation the deny list prohibits, they perform that operation
   manually, outside the agent session.

## What the deny list protects against (OWASP Agentic AI Top 10)

In December 2025, the OWASP Foundation published its first *Top 10
for Agentic Applications*. This reference configuration directly
mitigates several of these risks:

### ASI02: Tool Misuse

An agent with access to `rm -rf` can misuse it — not through malice,
but through a misinterpretation of the task that leads it to "clean
up" files it should not touch. An agent with access to `git push`
can push incomplete or broken code to a shared branch. An agent with
access to `curl | sh` can execute a malicious script injected through
prompt manipulation. **The deny list removes these tools from the
agent's reach entirely.**

### ASI03: Identity and Privilege Abuse

Without the deny list, the agent inherits the user's full shell
privileges — typically including `sudo`, package publishing, and
remote repository access. **The deny list strips these privileges**,
ensuring the agent operates as a constrained code-generation tool,
not as a fully-privileged shell user.

### ASI01: Agent Goal Hijack

Demonstrated in production by the EchoLeak vulnerability
(CVE-2025-32711, late 2025) — a zero-click prompt injection in
Microsoft 365 Copilot. Even if an attacker succeeds in hijacking the
agent's goal through a similar vector, **the deny list limits the
damage.** A hijacked agent that cannot push to remote, cannot
publish packages, and cannot execute downloaded scripts is a
substantially less dangerous agent than one that can.

## Allowed operations: read, write, verify

The allow list is intentionally narrow. It covers exactly the
operations an agent needs to **generate and validate code**:

- `read` — understand the codebase
- `inspect_git` — view git state (read-only)
- `write` / `edit` — produce code
- `test` / `lint` / `build` / `type_check` — validate output

## Operations NOT on the allow list (granted per-session if needed)

These operations may be necessary for specific tasks, but they
should be granted per-session with explicit justification, **not
blanket-allowed in the project configuration**:

- Network requests to arbitrary URLs
- Package installation
- Service restarts
- Environment variable modification
- Database access

**The default posture is deny. Exceptions are documented.**

## Common misconfigurations to avoid

- **The allow list that includes everything** (`["*"]`) — equivalent
  to running your database as root because creating a service
  account takes five minutes. The allow list exists precisely
  because trust is not a security strategy.
- **The deny list that blocks too much** — blocking all file writes
  means the agent cannot generate code. The deny list should block
  *dangerous* operations, not *productive* ones.
- **The guardrails that are routinely overridden** — guardrails that
  exist but are not enforced are worse than no guardrails at all,
  because they create a false sense of protection that discourages
  the adoption of compensating controls. Combine with the
  escalation protocol (see `../../prompts/escalation-protocol.md`).
- **Allowing `git push` because "it saves time"** — the single most
  common and most consequential misconfiguration. Allowing the
  agent to push collapses the separation between generation and
  integration. **The agent generates. The human publishes.**

## Other tools, same principle

In Cursor: `.cursor/rules` (the equivalent settings file).
In GitHub Copilot Workspace: workspace configuration.
**The tool varies. The principle does not.**

## Provenance

Adapted from Chapter 4 of *Harnessing the Horse*, Section 4.2. The
principle of least privilege is from Saltzer & Schroeder, "The
Protection of Information in Computer Systems," *Proceedings of the
IEEE*, 1975. The OWASP Agentic AI Top 10 (2025) provides the modern
threat catalog.

The configuration in `settings.jsonc` is © 2026 John Briggs, MIT
licensed (see [`../../LICENSE-CODE`](../../LICENSE-CODE)). The
written README is CC BY-NC-SA 4.0 (see
[`../../LICENSE-CONTENT`](../../LICENSE-CONTENT)).
