# Chapter 2: The Agentic Development Landscape — Study Guide

Student and self-study material moved from Chapter 2 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Distinguish the three generations of AI coding tools and the review discipline each demands.
2. Classify current agentic tools into the architectural tiers of Section 2.2 and explain why the tiers outlast the products that exemplify them.
3. Define an agentic system by its three properties — autonomy in execution, tool use, and multi-step reasoning with state — and distinguish workflows from agents.
4. Apply the five operations of context engineering (select, compress, order, isolate, format) to the design of a project context file.
5. Analyze Kiro's requirements → design → tasks pipeline as vendor validation of spec-to-code, distinguishing spec artifacts from the governance discipline that evaluates them.
6. Evaluate the single-agent default against the five orchestration patterns, using the SWE-bench evidence and Stripe's published enterprise practice.

## Key Terms

- **Context engineering** — The discipline of curating tokens across multi-turn, multi-tool, multi-session work; the successor to prompt engineering once an organization moves past single-turn AI interaction.
- **Context file** — AGENTS.md or CLAUDE.md: the project-root document that captures the conventions, constraints, and architecture boundaries every agent session needs to know.
- **MCP (Model Context Protocol)** — The open standard for connecting LLM agents to external tools and data sources, originally released by Anthropic in 2024.
- **Kiro** — AWS's spec-driven agentic IDE, which turns a prompt into requirements.md (in EARS notation), design.md, and tasks.md before implementation begins; vendor validation of the industry's move from prompt-to-code to spec-to-code.
- **Spec-driven development** — The workflow in which reviewable specification artifacts, with human approval between phases, precede any code generation.
- **Stripe Minions** — Stripe's internal coding-agent system: 1,300+ pull requests per week under constraint-first architecture and mandatory human review, the best publicly documented enterprise convergence on the book's standards.
- **Agent gateway** — An infrastructure layer mediating all agent-to-tool or agent-to-LLM communication, providing circuit breaking, rate limiting, audit logging, and policy enforcement.
- **Software Factory** — A continuous, instrumented loop that turns external signals into reviewed, secured, shipped, monitored code; agents operate as first-class workers within it.
- **Adoption gap** — The observation that the productivity gap between disciplined-AI and undisciplined-AI teams is widening faster than organizations can adopt the discipline.
- **Calibration delta** — The gap between felt speedup and measured speedup; the personal-level manifestation of the METR finding.

## Review Questions

1. What structural changes did Generation 1 (autocomplete) adoption not require, and why does that make its lessons non-transferable to Generation 3?
2. Name the three properties that distinguish an agentic system from an assistant, and restate Anthropic's workflow-versus-agent distinction in your own words.
3. List the five operations of context engineering. Why does the chapter call Select the highest-leverage operation?
4. Describe Kiro's three artifacts, where human approval sits between them, and the four questions Section 2.7 says the Harness Framework asks that an artifact cannot ask about itself.
5. Stripe's Minions merge over 1,300 pull requests per week with zero human-written code. Which controls in Stripe's published account bound the agents' blast radius, and what does mandatory human review add on top of them?

## Discussion Questions

1. The August 2026 sidebar is designed to go stale — the chapter says so. Which claims in this chapter would you bet still hold in 2031, and what makes a claim durable: the architecture, the economics, or the shape of the workflow itself?
2. Developer trust in AI output fell from roughly 42% to 29% while use became nearly universal. Is it professionally defensible to rely daily on a tool you distrust — or is the distrust itself the discipline working as intended?
3. Both Merlin's architectural history and the SWE-bench dissection point toward a single-agent default, yet multi-agent architectures dominate conference talks and vendor marketing. What pressures push teams toward orchestration complexity, and who bears the cost when it underperforms?

## Exercises

**Exercise 2.1 (Core) — Re-audit the landscape sidebar and rule on the tier taxonomy.** *(~2 h)* The "Landscape as of August 2026" sidebar in Section 2.2 quarantines the perishable facts, and its going stale is the lesson. Research current figures, as of your course date, for at least six of the sidebar's bullet items; where your sources disagree — vendor press release against independent reporting, for instance — you must pick one number and defend the pick. Then rule on Section 2.2's architectural-tier taxonomy itself: for each tier, issue a verdict — still standing, boundary redrawn, or retired — supported by at least one product that moved, died, or emerged since the sidebar's date.
*Deliverable:* A revised sidebar in the same format, retitled for the current quarter, with a source-conflict note for every adjudicated figure, plus a ~400-word taxonomy ruling.
*Assessment:* Every figure carries a source and a date; at least one source conflict is adjudicated with stated reasoning rather than averaged away; every tier verdict cites product evidence. A ruling that keeps all tiers without evidence fails, and so does one that redraws them without it. Web research only; no agentic tool required.

**Exercise 2.2 (Core) — Map the Kiro pipeline onto the Harness.** *(~90 min)* For each element of Kiro's published workflow — requirements.md with EARS notation, design.md, tasks.md, steering files, hooks, and the phase-approval points — identify (a) the corresponding pipeline artifact or mechanism in the companion pipeline-artifact and quality-gate references and (b) the Harness discipline it serves. Then mark which of Section 2.7's four governance questions each element leaves unanswered.
*Deliverable:* A mapping table plus a gap analysis of one page or less.
*Assessment:* The mapping keeps artifacts and governance distinct, per Section 2.7 and Chapter 4; the gap analysis identifies at least two questions the artifacts cannot answer about themselves. No AI tool required.

**Exercise 2.3 (Core) — Write a context file.** *(~2 h)* For a codebase you know well, write a CLAUDE.md or AGENTS.md of under 200 lines following the vendor guidance in Section 2.11: include build commands, conventions, architectural constraints, and known gotchas; exclude anything an agent can infer by reading the code and any self-evident practice. Apply the five operations of Section 2.5 as your design checklist.
*Deliverable:* The context file.
*Assessment:* The Minimum Viable Context File criteria (Chapter 4 and the companion tool-configuration reference): length bound respected, exclusion rules followed, and at least one constraint that would have prevented a real past mistake in that codebase. No AI tool required to write it; optionally verify it by running one agent session.

**Exercise 2.4 (Challenge) — The orchestration decision memo.** *(~2 h)* Three incoming work orders: (a) a one-file bug fix with an existing failing test; (b) a greenfield feature adding one new module behind an interface; (c) a rename touching two hundred files across module boundaries. For each, choose the single-agent default or one of the five orchestration patterns from Section 2.8, specify iteration bounds, and define the escalation path when the loop fails to converge.
*Deliverable:* A decision memo of two pages or less covering all three scenarios.
*Assessment:* The memo engages the single-agent default evidence (Section 2.8); every loop is bounded with an escalation path consistent with Standard 6 (Chapter 7); pattern choices are justified by the structure of the work, not by novelty. Paper variant: the memo requires no tool execution.
