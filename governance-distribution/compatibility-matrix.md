# Compatibility Matrix

| Surface | Portable core | Client adapter | Authoritative backstop |
|---|---|---|---|
| Reusable workflow | `skills/*/SKILL.md` | Client-specific invocation and discovery | PR checklist and required checks |
| MCP tools | `mcp.json` when a real server exists | Client connection and authentication settings | Gateway policy and tool audit logs |
| Always-on repository guidance | Not standardized by Agent Plugins v1 | Kiro steering, `AGENTS.md`, `CLAUDE.md`, Cursor rules | CI and branch protection |
| File- or topic-conditional context | Client extension | Kiro or Cursor adapter rules | File-scoped linters and policy checks |
| Team specialization | Additional skills and adapter content | Team-owned additive projection | Baseline gates cannot be disabled |

“Same content” is an authorship goal, not a runtime guarantee. Every client has its own precedence, context limits, activation behavior, and permissions. Validate those semantics during rollout.

