# Portable Governance Distribution

This worked example shows how to author engineering governance once while delivering it through several coding-agent clients. It is a reference architecture, not a claim that every client natively interprets every other client's files.

The design has four layers:

1. **Portable core:** an Agent Plugins v1 package containing a manifest and Agent Skill. The specification's portable component types are skills and MCP configuration.
2. **Client adapters:** small mappings into each client's native instruction mechanism: Kiro steering, Codex `AGENTS.md`, Claude `CLAUDE.md`, and Cursor rules.
3. **Repository policy:** project-specific instructions and team extensions add context without weakening the baseline.
4. **Authoritative enforcement:** CI, branch protection, and repository controls enforce outcomes regardless of which agent—or human—created the change.

This distinction is the governance guarantee. Portable packaging reduces duplicate authorship. Adapters acknowledge real client differences. CI supplies agent-independent enforcement.

## What this example demonstrates

```text
portable-plugin/                 shared workflows and optional MCP
        |
        +--> adapters/kiro/      contextual steering
        +--> adapters/codex/     layered AGENTS.md guidance
        +--> adapters/claude/    CLAUDE.md project instructions
        +--> adapters/cursor/    project rules
        |
        +--> enforcement/        agent-independent quality gate
```

Use `portable-plugin/` as the versioned source for reusable workflows. Treat each adapter as a maintained projection of the same policy intent, with compatibility tests or review checks to detect drift. Do not market the Kiro adapter itself as universal.

The `team-extension-template/` demonstrates the additive rule: a team may strengthen the baseline or add domain detail, but it may not disable security review, evidence requirements, or blocking gates.

## Source boundaries

- [Agent Plugins v1 specification](https://agent-plugins.org/specification) — working-draft package contract, fixed component locations, and extension namespaces.
- [Agent Plugins project](https://agent-plugins.org/) — governance and current steering committee.
- [Codex `AGENTS.md` documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) — root-to-leaf instruction discovery and override behavior.

Agent and client behavior changes. Revalidate each adapter against current vendor documentation before organizational rollout. The CI layer should remain authoritative even when an adapter is unavailable or outdated.

## Adoption sequence

1. Fork and rename the portable package.
2. Replace the example policy with the organization's approved baseline.
3. Add only the adapters used in the pilot.
4. Wire the same non-negotiable controls into CI.
5. Pilot with a small group and measure first-pass CI, rework, escaped findings, and developer experience.
6. Version changes through review; test that adapters still express the same policy intent.

