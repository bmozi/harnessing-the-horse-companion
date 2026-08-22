# Agent-Generated Code Security Review Checklist

> **Chapter:** ch17 — Security in the Agentic Era (Sections 17.1
> through 17.6)
> **Last revised:** 2026-06-16
> **Run when:** Reviewing any agent-generated code that will reach
> production. Run alongside the disprove-only review
> ([`../prompts/disprove-only-review.md`](../prompts/disprove-only-review.md)).

The **generation trifecta** names the three security failure modes
intrinsic to agent-generated code: **hallucinated dependencies**,
**reproduced vulnerabilities**, and **secret leakage** (Section 17.3;
the controls live where the Twelve Standards already put them —
Dependency Discipline (Standard 5), Automated Quality Gates
(Standard 6), and Architectural Stewardship (Standard 10)). The
term is the book's own — deliberately distinct from Simon Willison's
"lethal trifecta" (2025), which names a runtime combination of agent
capabilities: private data access, exposure to untrusted content,
and external communication. Willison's trifecta is about what a
deployed agent can be tricked into doing; the generation trifecta is
about what a code-generating agent leaves behind in your repository
(see §17.2, "One Problem, Two Trifectas").

Chapter 17 extends the generation trifecta into **six vectors**
(Section 17.6), each with specific review criteria. The checklist
below is the complete security-review surface for agent-generated
code.

---

## Dependency Verification

- [ ] Every import refers to a package in the dependency manifest
- [ ] No new dependencies were added without justification in
      `IMPL_NOTES.md`
- [ ] All dependencies have been scanned for known vulnerabilities
      (npm audit, pip-audit, govulncheck)
- [ ] No dependencies with fewer than 1,000 weekly downloads
      (configurable threshold) without security-team approval
- [ ] **Slopsquatting defense:** every import has been verified
      against the lockfile, not against the agent's memory of what
      "should exist"

> **Why this matters:** "Slopsquatting" (Thompson, 2024) is the
> attack where an attacker registers package names that AI agents
> have hallucinated. The defense is structural — agent additions to
> the dependency manifest require explicit approval.

## Vulnerability Scan

- [ ] No SQL queries constructed with string concatenation
- [ ] No user input rendered without sanitization
- [ ] No deserialization of untrusted data
- [ ] No hardcoded credentials, API keys, or secrets
- [ ] No overly permissive CORS, CSP, or security header
      configurations

## Authentication and Authorization

- [ ] All new endpoints require authentication unless explicitly
      public
- [ ] Authorization checks are present for all resource access
- [ ] No privilege escalation paths introduced
- [ ] No tool definitions that accept unconstrained input types
      (e.g., `any` in TypeScript, `interface{}` in Go without
      validation)

## Prompt Injection Propagation

- [ ] Agent-generated code that **constructs prompts from user
      data** wraps the user data in structured containers (XML
      tags, JSON fields, explicit `DATA START / DATA END` markers)
- [ ] The system prompt explicitly instructs the model to treat
      contained data as data, never as instructions
- [ ] Every instance where user data enters an agent's context has
      been checked
- [ ] No code paths where unsanitized user content becomes part of
      a system prompt or tool argument

> See [`../prompts/prompt-injection-defense.md`](../prompts/prompt-injection-defense.md)
> for the four-layer defense pattern.

## Excessive Tool Authorization

- [ ] Every new tool definition implements the principle of least
      privilege (see
      [`../patterns/scoped-authorization-token.md`](../patterns/scoped-authorization-token.md))
- [ ] No tool accepts `any` / unbounded type as a parameter
- [ ] Input validation is enforced inside the tool, not delegated
      to the agent
- [ ] Output sanitization is enforced inside the tool
- [ ] Tool's scope constraints are explicit and tested

## Memory Store Integrity

- [ ] Agent-generated code that **writes to persistent memory
      stores** (learning databases, knowledge graphs, vector
      stores) validates content before writing
- [ ] No learnings that reference unknown packages without
      verification
- [ ] No learnings that include external URLs without allowlisting
- [ ] No learnings that propose modifications to security behavior
- [ ] High-impact learnings (security-critical code paths, auth,
      credentials) require human approval before insertion

---

## Memory Poisoning Defensive Postures

For systems with persistent agent memory (graph stores, vector
databases, learning repositories):

- [ ] **Memory verification:** Learnings are verified before
      loading into future sessions. Decay semantics in place
      (older learnings weighted lower). Verification semantics in
      place (learnings producing better outcomes are reinforced).
- [ ] **Memory provenance tracking:** Every learning traces to
      its source Work Order, agent session ID, and source data.
      Forensic trail from suspicious output → memory entry →
      source data is reconstructible.
- [ ] **Human review of encoded learnings:** Security-critical
      learnings require human approval before insertion. Graduated
      autonomy applied to the learning pipeline.
- [ ] **Memory isolation:** Different agent contexts have
      isolated memory stores. Billing-context agent does not load
      learnings from UI-component agent. Bounded-context
      discipline (Appendix B) applies to memory as directly as to
      code.

## MCP Server Supply-Chain Defense

For systems consuming MCP servers from external sources:

- [ ] **First-party MCP servers only** for production workloads —
      every MCP server is built and maintained by the organization,
      with known source code, known deployment, known credential
      scope
- [ ] **Per-server credential isolation** — each MCP server
      receives only the credentials it needs for its specific
      integrations
- [ ] **Transport-level authentication** — every MCP connection
      requires authentication (e.g., Entra ID JWT for internal,
      API key for partners, reject unauthenticated)
- [ ] **Tool-call auditing** — every tool call (parameters and
      result) is logged with session correlation and authorization
      scope

## OWASP Agentic AI Top 10 Mapping

This checklist mitigates the OWASP Agentic AI Top 10 (2025):

| Risk | Where covered |
| --- | --- |
| ASI01 — Agent Goal Hijack | Prompt injection propagation + memory store integrity |
| ASI02 — Tool Misuse | Excessive tool authorization + MCP supply-chain defense |
| ASI03 — Identity & Privilege Abuse | Authentication and authorization |
| ASI04 — Agent Provenance / Traceability | (Provenance discipline lives in `../spec-templates/impl-notes-md.md`) |
| ASI05 — Cross-Agent Data Leakage | Memory isolation |
| ASI06 — Prompt Injection | Prompt injection propagation (and the dedicated prompt-injection-defense prompt) |
| ASI07 — Resource Exhaustion | (See `iteration-caps.md`) |
| ASI08 — Inadequate Guardrails | All categories above |
| ASI09 — Error Handling | (See chapter prose) |
| ASI10 — Unmonitored Behavior | Tool-call auditing |

## Related

- [`../prompts/prompt-injection-defense.md`](../prompts/prompt-injection-defense.md)
  — the four-layer defense embedded in agent prompts
- [`../prompts/disprove-only-review.md`](../prompts/disprove-only-review.md)
  — the broader review this security pass complements
- [`../code-examples/claude-settings/`](../code-examples/claude-settings/)
  — the structural guardrails at the agent-runtime level (allow/
  deny lists, principle of least privilege)
- [`../patterns/scoped-authorization-token.md`](../patterns/scoped-authorization-token.md)
  — the pattern that prevents excessive tool authorization
- [`self-improvement-safety-rails.md`](self-improvement-safety-rails.md)
  — the four rails for systems with memory-write capability

## Provenance

Adapted from Chapter 17 of *Harnessing the Horse*, Sections 17.1
through 17.6. The generation trifecta, its extension to six vectors,
and the security review checklist are the book's extension of
Standard 10.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
