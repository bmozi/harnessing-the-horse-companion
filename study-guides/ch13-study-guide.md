# Chapter 13: Designing AI-Agent Infrastructure — Study Guide

Student and self-study material moved from Chapter 13 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why AI agents constitute a third consumer category and what that implies for response verbosity, error detail, discovery, and batch design.
2. Construct a capability-partitioned MCP tool set applying domain naming, dry-run-default on write tools, and per-tool RBAC with scoped tokens.
3. Apply composite-key idempotency stores and CAS-guarded commits to serialize local work, then design reconciliation for ambiguous non-idempotent downstream outcomes.
4. Design observability for agent-driven systems keyed on session correlation, so every operation traces from agent intent to system effect.
5. Evaluate the single-agent versus multi-agent orchestration decision for a given scale, and identify handoff fidelity as the governing constraint.
6. Analyze whether a deployment topology requires per-task execution isolation, and select the appropriate isolation phase if it does.

## Key Terms

- **MCP (Model Context Protocol)** — Open standard (Anthropic, 2024) for connecting LLM agents to external tools and data sources.
- **Dry-Run-Default on Write Tools** — Design pattern requiring agent-facing write tools to preview before execution by default. The preview is evidence for review, not approval by itself; explicit authorization and an execution gate remain necessary.
- **Scoped Authorization Token** — Least privilege (Saltzer & Schroeder, 1975) applied at the session level: each agent session's token specifies which tools it may invoke.
- **CAS-Guarded Distributed Commit** — Pattern combining an atomic local ownership guard with durable checkpoints. Known outcomes can be retried safely; a lost response from a non-idempotent provider requires idempotency, reconciliation, or human disposition.
- **Agent gateway** — An infrastructure layer that mediates agent traffic behind a governed protocol; the term covers two distinct layers — agent-to-tool gateways (the Solo.io/Istio layer in Section 13.6's landscape note) and agent-to-LLM gateways that route, audit, and fail over model backends.
- **Express Arc** — A single primary agent owning the entire delivery sequence without handoffs; quality gates fire as inline self-checks.
- **Software Factory** — A continuous, instrumented loop turning external signals into reviewed, secured, shipped, monitored code; this book's contribution is the agentic variant.
- **Idempotency** — The property that processing the same request multiple times produces the same result as processing it once.

## Review Questions

1. What four benefits does the capability partition provide that a monolithic "god server" does not?
2. What must a write tool do under dry-run-default, when is an exception justified, and which risks remain because a preview is neither authorization nor proof that execution will match it?
3. Why does the chapter argue that agents should compose multi-step flows from individual tools — and what is the one situation where wrapping the orchestration is the correct choice?
4. What five things must agent-consumed infrastructure log, and why is session correlation rather than log volume the design center of agent observability?
5. In the Fieldstone server, what changed when sparse tool descriptions were expanded, what were the reported figures, and what is their stated evidentiary status?

## Discussion Questions

1. The orchestration section concludes that both single-agent and multi-agent architectures work — and fail — for the same reason. A team of eight is choosing today, under vendor marketing pressure from heavily funded multi-agent platforms and a tool landscape that shifts quarterly. What evidence from the team's own operation should drive the decision, and what observed signal should trigger revisiting it?
2. Dry-run-default doubles the invocations, latency, and token cost of every write. Human confirmation dialogs teach us that mandatory confirmation degrades into reflexive clicking. What stops an agent from developing the equivalent — always sending `confirm: true` immediately — and does that failure mode argue for relaxing the pattern or hardening it?
3. Ruthless consistency is cheap on a greenfield API and expensive on an existing estate with three naming conventions and two error formats. When agents become consumers of your current APIs, do you retrofit the estate, wrap it in an agent-facing BFF, or accept the per-session error rate? What does each choice cost, and who pays it?

## Exercises

**Exercise 13.1 (Core) — Design an MCP tool set for a described domain.** A veterinary clinic chain operates four business capabilities: appointment scheduling, patient records (pets and owners), prescription management, and billing. Regulatory constraints: prescriptions may only be created by tools invoked under a veterinarian-authorized scope; billing adjustments over a threshold require human approval. Design the agent-facing infrastructure. *(~2 h)*
*Deliverable:* A partition map (which servers exist and why the split follows capability, not vendor) plus a tool catalog for one server: per tool, its domain-oriented name, description, input schema sketch, required scope, and dry-run behavior.
*Assessment:* Judged against the Section 13.1–13.2 patterns and the companion repository's `examples/mcp-tool-definition.ts`: every write tool dry-run-default, every tool scope-checked, no CRUD-named or orchestration-endpoint tools, and the prescription constraint enforced structurally rather than by description text.

**Exercise 13.2 (Core) — Write selection-grade tool descriptions.** Take five tools from your Exercise 13.1 catalog and write full descriptions including parameter semantics, business rules, and cross-tool relationships, following the `check_availability` example in Section 13.6. Then write three realistic but ambiguous task statements (for example, "get Bella ready for her follow-up") and predict, with reasoning, which tool an agent would select for each and where selection could still fail. *(~2 h)*
*Deliverable:* The five descriptions plus the three-task selection analysis.
*Assessment:* Peer or instructor review against Section 13.6's finding: a description passes if a reader who has never seen the server can state what the tool accepts, what it validates, and which tool to call first.

**Exercise 13.3 (Core) — Contain ambiguity in a multi-step workflow.** An agent-operated workflow performs four steps across two vendors, neither of which supports idempotency keys: reserve inventory, charge a card, create a shipment, send a confirmation. Design the local retry machinery and the operational handling for a lost provider response. *(~2 h)*
*Deliverable:* The composite-key store schema, CAS-guarded state machine (including an `INDETERMINATE` state), checkpoint ordering, correlation identifiers and reconciliation queries, and the manual disposition rule when the provider cannot be queried.
*Assessment:* Judged against Section 13.3 and the CAS-Guarded Distributed Commit card in `references/pattern-quick-reference.md` §8: a reviewer must be able to trace a crash before a call, a known response, and a response lost after provider acceptance. Any design that automatically retries the ambiguous charge or claims exactly-once execution across the vendors fails.

**Exercise 13.4 (Challenge) — Write the orchestration ADR twice.** Write an architecture decision record choosing single-agent or multi-agent orchestration for each of two organizations: (a) a six-person team shipping roughly twenty work orders a week, and (b) a platform business processing two thousand work orders a day across many tenants. Each ADR must state the decision, the alternatives, the consequences, and — critically — the measured signals (handoff failure rate, per-work-order cost, wall-clock throughput) that would trigger reversal. *(~4 h+)*
*Deliverable:* Two ADRs with an "Agent Implications" section each.
*Assessment:* ADR discipline per Standard 10 (Chapter 9), graded on whether the two decisions differ for reasons traceable to Section 13.7's scale and handoff-fidelity arguments rather than to taste, and on whether the reversal triggers are observable quantities.
