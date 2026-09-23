# Glossary and Acronym Reference

Terms and acronyms used across the book, consolidated for
quick reference. Terms coined or named by the book are marked
with **(this book)** and link to the chapter that introduces
them as the canonical reference. Established terms cite the
original authoritative source.

This searchable online reference replaces the former print glossary.

---

## Glossary

**Acceleration arc (this book)** — Documented three-phase
throughput progression in the author's own practice,
measured in LOC/day (a volume metric, not a value metric).
The conservative post-learning-curve attribution is ~4.3x;
the raw endpoint comparison is larger but confounded by
model improvement and the author's learning curve, which
the data cannot separate. Presented as hypothesis, not
proof. See Chapter 1 for the full methodology and caveats.

**Adapter** — In Hexagonal Architecture, the implementation
of a port for a specific external technology (HubSpot
adapter, PostgreSQL adapter, in-memory test adapter). The
adapter is the containment boundary for vendor specificity.
See companion pattern quick reference §2.

**Adoption gap (this book)** — The observation that the
development capacity can increase faster than organizations
can absorb it through review, stakeholder alignment,
operational change, and shared practice. The DORA 2025 "AI is
an amplifier" finding (Chapter 2) is the empirical expression
of this gap at the individual-vs-organizational boundary;
Chapter 15 illustrates it through the interval between an
initial platform foundation and a planned launch window,
while explicitly acknowledging that engineering hardening
continued; Chapter 20 extends it to team adoption, where the
practice had not yet become a shared capability.
See Chapters 2, 15, 20.

**ADR (Architecture Decision Record)** — A short document
capturing the context, decision, alternatives, and
consequences of a significant architectural choice (Michael
Nygard, 2011). In the agentic era, ADRs gain a new audience:
AI agents that need to understand the constraints their
generated code must respect. Augmented in this book with an
"Agent Implications" section. See Chapter 9.

**ADVISORY gate** — Quality gate whose findings are surfaced
for human judgment but do not halt the pipeline. Used for
issues requiring judgment (coverage delta, complexity metrics,
performance regression within tolerance band). One of four
tiers in the four-tier gate classification. See Chapter 7 and the
companion quality-gate configuration reference.

**Adversarial validation** — The agent mode of Standard 7,
Falsification Review (Chapter 7). A fresh-instance agent
attacks the generated code, looking for failure modes the
generating session may have missed. Removing the generation
conversation reduces one source of assumption carryover; it does
not remove shared model biases or errors in the specification.
Verify candidate findings and treat silence as limited evidence.

**Agent gateway** — An infrastructure layer that mediates
all agent-to-LLM communication, providing circuit breaker
failover across providers, audit logging, and traffic
routing. Reference implementation in the Merlin Software
Factory (Chapter 16) supports five LLM backends with
automatic selection.

**Agent Implications (this book)** — The ADR section, absent
from the traditional format, that states explicitly how the
decision constrains future agent-generated code: which
modules agents must use, what they must not introduce, and
the test that verifies compliance. A useful Agent
Implications section is specific, actionable, and testable —
one that restates the rationale without constraints fails.
See Chapter 9.

**Agentic era (DORA 2026)** — DORA's named inflection point:
"The software engineering industry has entered the agentic era.
This era represents the critical evolution from reactive
artificial intelligence tools to autonomous systems capable of
independently executing complex, multiple-step workflows"
(DORA, *ROI of AI-assisted Software Development*, Google Cloud,
2026). The framing this book adopts for the period its
standards address. See Chapter 1.

**AGENTS.md** — A project-root context file analogous to
CLAUDE.md, intended for use with non-Claude AI tools.
Either filename works; choose one and stay consistent
across the repository. See Chapter 4 and the companion tool-configuration reference.

**AI Capabilities Model (DORA 2025)** — The seven foundational
practices DORA identified as amplifying AI's positive impact on
organizational performance: clear AI policy, healthy data
ecosystem, quality internal platform, user-centric focus, plus
three additional capabilities. Introduced in DORA, *State of
AI-assisted Software Development*, Google Cloud, 2025.
Value Stream Management is named as the force multiplier that
converts individual gains into organizational outcomes. See
Chapters 1 and 2.

**AI is an amplifier (DORA 2025)** — DORA's central finding:
"AI's primary role in software development is that of an
amplifier. It magnifies the strengths of high-performing
organizations and the dysfunctions of struggling ones"
(DORA, *State of AI-assisted Software Development*, Google
Cloud, 2025). Reframed in DORA 2026 as "garbage in, garbage out
refers to the context provided to the agent" — the structural
case for context engineering as the input-quality discipline of
agentic development. See Chapter 1, Chapter 7.

**Anti-Corruption Layer (ACL)** — A translation boundary
that prevents an external system's data model from leaking
into the domain (Eric Evans, *Domain-Driven Design*, 2003).
In agentic development, the ACL eliminates the need for
each agent session to re-learn vendor quirks. See Appendix
E §1.

**Architecture-as-code** — Architectural constraints
expressed as enforceable rules in CI/CD (import-linter,
ArchUnit, ESLint architectural rules), not as
documentation. The mechanism that prevents architectural
drift at the speed of generation. See Chapter 9, Standard 10.

**ASYNC gate** — Quality gate that runs in the background
without blocking generation or review, but must resolve
before merge. Used for checks that are valuable but too
expensive to run synchronously (full integration test suite,
performance benchmarks, dependency vulnerability scans).
See Chapter 7 and the companion quality-gate configuration reference.

**Backend for Frontend (BFF)** — Pattern that tailors a
backend interface to a particular consumer class rather than
forcing one general-purpose backend to compromise for all of
them (Sam Newman, 2015; *Building Microservices*, 2nd ed.,
O'Reilly, 2021). AI agents are the next consumer class it
fits: agent-optimized backends differ in response verbosity,
error detail, runtime discovery, and batch operations. See
Chapter 13.

**Blast radius** — The set of components, modules, services,
and users that could be affected if a change contains a
defect. Distinct from *scope* (what the change intends to
modify). Standard 3 (Chapter 5) requires explicit blast
radius estimation across five dimensions at SPEC time and
verification of the estimate at review time.

**BLOCKING gate** — Quality gate whose failure halts the
pipeline; the PR cannot merge until the gate passes. Used
for invariants whose violation produces production
incidents (type errors, failing tests, critical security
findings, architecture boundary violations). See Appendix
C.

**Bounded context** — A boundary within which a particular
domain model applies (Eric Evans, *Domain-Driven Design*,
2003). In agentic development, bounded contexts are
structural requirements, not organizational tools — they
constrain the vocabulary the agent uses, preventing
semantic confusion at context boundaries. See Appendix B.

**Bounded iteration** — A hard ceiling on automated fix
loops: after a fixed number of attempts against a failing
gate, the agent stops and escalates instead of thrashing at
API prices. Stripe caps its CI retry loop at two rounds;
Merlin, from its own production data, settled on the same
bound. Formalized with escalation as part of Standard 6. See
Chapter 2, Chapter 7, Chapter 16.

**Calibration delta (this book)** — The gap between *felt*
speedup and *measured* speedup. The personal-level
manifestation of the METR finding (19% slower while
feeling 20% faster). Tracked via the quarterly self-A/B
test and the honest journal. See Chapter 18.

**Canary release** — Progressive delivery pattern: deploy to
a small percentage of traffic (typically 1–5%) and monitor
before progressively expanding (named in James Governor's
"Progressive Delivery" series, RedMonk, 2018). For
agent-generated code, the highest-leverage safety net: the
small initial population surfaces failure modes no test
caught, with bounded customer impact. See Chapter 8.

**Capable of more (thesis) (this book)** — Distinguishes
"AI makes developers faster at known tasks" (sometimes
true) from "AI makes developers capable of previously
impossible tasks" (consistently true when discipline is
present). See Chapter 15.

**CAS-Guarded Distributed Commit (this book)** — Pattern applying Maurice
Herlihy's compare-and-swap primitive (1991) to distributed workflow
coordination. Combines an atomic local state-machine guard with durable
per-step checkpoints. Known outcomes can be retried safely; lost responses from
non-idempotent providers require provider idempotency, reconciliation, or human
disposition. The composed goal is an effectively-once business outcome, not an
exactly-once claim across an uncontrolled provider. See Chapter 15, companion
pattern quick reference §8.

**Centrifuge** — Rate-fairness pattern (Segment, 2018):
per-source virtual queues with isolated token-bucket rate
budgets in front of a shared, rate-limited downstream, so
one source's quota exhaustion cannot starve the others.
Pairs with the Circuit Breaker at the publisher boundary;
the Fieldstone CRM Hub uses it to allocate HubSpot's
per-account API quota across its integration sources. See
Chapter 11 §11.4, Chapters 12 and 14, companion pattern quick reference §4.

**Circuit Breaker** — Resilience pattern (Michael Nygard,
*Release It!*, 2007) that stops calling a failing service
and fails fast, periodically probing for recovery. Applied
to LLM provider routing in agent gateways. See companion pattern quick reference §4.

**CLAUDE.md** — A project-root context file loaded
automatically by Claude Code. Same purpose as AGENTS.md
for other tools. See Chapter 4 and the companion tool-configuration reference.

**Close-the-loop discipline** — Part of Standard 11, the
Knowledge Loop (Chapter 10). Every session ends with an
update to AGENTS.md, the prompt library, an ADR, or another
mechanism that makes the next session smarter. The single
most commonly skipped step in the session loop; the
discipline that makes compounding real.

**Code churn** — GitClear's leading indicator of low-quality
commits: lines revised or deleted within two weeks of being
written. A line changed within fourteen days of merging was,
by definition, not correct when it merged. Churn rose from
5.5% to 7.9% across GitClear's 211-million-line dataset as
AI assistance spread (GitClear, AI Copilot Code Quality
report, 2025). See Chapter 3.

**Confused deputy problem (Hardy, 1988)** — An agent (the
deputy) acting on a user's behalf may hold permissions the
user does not have — or did not intend to delegate for this
task — and the confusion arises when the deputy uses them
for unauthorized purposes (Norm Hardy, "The Confused
Deputy," *ACM SIGOPS Operating Systems Review* 22(4), 1988).
Agentic defenses: scoped authorization tokens, dry-run
defaults on write tools, explicit escalation. See Chapter 17.

**Context contamination** — The condition in which
assumptions and framings from one part of an agent
session's reasoning influence another part, including review
of its own output. Self-review can find errors but is not an
independent check of the assumptions that produced the code.
The structural argument for fresh-instance adversarial
validation (Standard 7, agent mode). See Chapter 7.

**Context engineering** — The discipline of curating tokens
across multi-turn, multi-tool, multi-session work. Replaces
"prompt engineering" as the central skill once an
organization moves past single-turn AI interaction
(Karpathy, 2025). See Chapter 2.

**Context file** — `AGENTS.md` or `CLAUDE.md`. The
project-root document that captures conventions,
constraints, and architecture boundaries every agent
session needs to know. See Chapter 4 and the companion tool-configuration reference.

**CQRS (Command Query Responsibility Segregation)** —
Architectural pattern (Greg Young, 2010) that separates the
write path (commands producing events) from the read path
(projections optimized for queries). Frequently paired with
Event Sourcing. See Appendix B.

**Crawl-walk-run** — The adoption model of Chapter 19: three
stages with explicit entry criteria, exit criteria, and the
practices belonging at each. Crawl (context files,
guardrails, spec-before-generation) delivers most of the
safety benefit within a single sprint; walk adds the full
artifact pipeline, pipeline tracks, and architecture-as-code;
stage transitions are gated by regeneration-rate thresholds
(see *Regeneration rate*). Chapter 7 sequences Standard 1's
generation contract with Standards 6–7
along the same path. See Chapter 19.

**Cui et al. (2025)** — Field experiment of 4,867 developers
across Microsoft, Accenture, and a Fortune 100 firm,
published as "The Effects of Generative AI on High-Skilled
Work: Evidence from Three Field Experiments with Software
Developers" (Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff,
Sida Peng, and Tobias Salz, *Management Science*, 2025).
Productivity rose ~26% on average; junior developers gained
27–39%, senior developers 8–13%. See Chapter 3.

**Dark code (this book)** — Code that exists, compiles, and
possibly passes tests, but that no one understands or can
maintain. Distinct from traditional technical debt (where
someone knows what was compromised and why). Dark code is
*unexamined*. See Chapter 1, Chapter 3.

**Debt register** — A structured inventory of known
technical debt, categorized by severity and tracked to
resolution, maintained as a section of IMPL_NOTES.md. Three
tiers: must-fix-before-merge (BLOCKING), should-fix-soon
(tracked with specific remediation deadlines), and can-defer
(batched into refactoring cycles). Items move between tiers
as circumstances change. See Chapter 9 and the companion pipeline-artifact reference.

**Definition of Done (DN1–DN7)** — The seven binary
completion criteria for an agentic-development change,
introduced in Chapter 10. Each is a BLOCKING gate
where marked. The set is the operational checklist that
turns "the work is done" from a judgment call into a
verifiable state.

**DN1. Specification Complete.** SPEC.md exists with
binary acceptance criteria, a MUST-NOT list, and a scope
boundary, reviewed by the feature owner. *(BLOCKING.)*
See Chapter 10.

**DN2. Design Validated.** DESIGN.md exists with task
decomposition meeting session scope rules (each task under
400 lines, under 60 minutes of review), a clean DAG of
dependencies, and explicit interface contracts. *(BLOCKING.)*
See Chapter 10.

**DN3. Implementation Documented.** IMPL_NOTES.md captures
all design decisions, deviations from spec, scope expansion
requests, and a discovery log. Every non-obvious choice is
justified; every deviation is flagged. See Chapter 10.

**DN4. Quality Gates Passed.** All BLOCKING gates pass;
ADVISORY findings are documented in REVIEW.md; INFORMATIONAL
gate data is captured for dashboards; ASYNC gates are
scheduled and tracked. *(BLOCKING.)* See Chapter 10.

**DN5. Review Complete.** REVIEW.md exists with adversarial
review findings, all BLOCKING findings resolved, and the
reviewing engineer can explain the algorithm, failure modes,
test gaps, and architectural rationale. *(BLOCKING.)*
See Chapter 10.

**DN6. Provenance Captured.** Commit metadata links to
SPEC.md and DESIGN.md; agent session information is recorded;
the merging engineer is identified; IMPL_NOTES.md decisions
are linked to specific code locations. See Chapter 10;
cross-reference: *Provenance capture*.

**DN7. Loop Closed.** AGENTS.md (or CLAUDE.md) is updated
with any new learnings, patterns, or constraints discovered
during implementation. The single most commonly skipped DN
item; the one that converts a series of isolated sessions
into a learning system. See Chapter 10;
cross-reference: *Close-the-loop discipline* (Standard 11).

**Design by Contract (Meyer)** — The discipline of
specifying every function as a contract between caller and
implementer: preconditions, postconditions, and invariants
(Bertrand Meyer, introduced in Eiffel; *Object-Oriented
Software Construction*, 2nd ed., Prentice Hall, 1997). In
agentic development, each stated contract element is an
inference the agent no longer has to make. See Chapter 6.

**DESIGN.md** — The pipeline artifact that captures *how*
the system will satisfy the specification. Sections:
Approach, Module Boundaries, Data Model, API Contracts,
Tradeoffs, Risks. The Tradeoffs section preserves design
rationale that no other artifact captures. See the companion pipeline-artifact reference.

**Discipline dividend (this book)** — The compounding
advantage that disciplined teams accumulate over time. Each
investment in context files, specifications, and calibration
practices makes subsequent sessions more productive,
widening the gap with undisciplined teams. See Chapter 3,
Chapter 20.

**Disprove-only review** — The human mode of Standard 7,
Falsification Review (Chapter 7). The reviewer's task is not
to confirm correctness but to find how the code fails. Three
questions: automated gate status, specification compliance,
specification violations (across eight failure dimensions).

**DORA metrics** — Deployment frequency, lead time for
changes, change failure rate, mean time to restore
(Forsgren, Humble, Kim, *Accelerate*, IT Revolution, 2018).
DORA's 2024 report formally added deployment rework rate as
a fifth metric — the percentage of deployments that are
unplanned work performed to fix user-facing bugs. DORA's rework
rate is a deployment metric, distinct from this book's
*regeneration rate* (see that entry). See Chapter 3,
Chapter 18.

**Drift scan** — Periodic comparison of the actual
dependency graph against the documented architecture, with
findings classified as *violation*, *evolution*, or
*ambiguity*. See Chapter 9.

**Dry-Run-Default on Write Tools (this book)** — Design
pattern requiring every agent-facing write tool to default
to a read-only preview; actual execution requires an
explicit `confirm: true` parameter. Makes the agent's first
invocation of any write tool safe and reversible. See
Chapter 13, companion pattern quick reference §11.

**Error budget** — The gap between a Service Level Objective
and 100%, defining what a team can spend on risky changes
(Beyer et al., eds., *Site Reliability Engineering*,
O'Reilly, 2016). For agent-augmented teams, the budget
structurally constrains deployment cadence: when the
quarter's budget is spent, agent-generated deployments slow
until it recovers — a constraint governed by data rather
than negotiation. See Chapter 8.

**ESCALATION.md** — The Standard 6 artifact (Chapter 7)
documenting any quality-gate override or thrashing
escalation. Required content: gate failure details, root
cause analysis, thrashing check, override authority level
and justification, blast radius reference, remediation plan.

**Event Sourcing** — Architectural pattern (Greg Young,
2006) that persists every state change as an immutable
event; current state is a projection. Three properties
matter for agentic development: audit trail by
construction, temporal queries for migration validation,
projection-based read models for sub-second agent access.
See Appendix B and companion pattern quick reference §9.

**Expand-Migrate-Contract** — Database refactoring pattern,
also called Expand-Contract or Parallel Change (Scott Ambler
and Pramod Sadalage, *Refactoring Databases*,
Addison-Wesley, 2006), that decomposes a backward-
incompatible schema change into backward-compatible steps:
add the new element, backfill and switch behind a toggle,
then remove the old element. A rollback at any point
restores a working state without data loss. See Chapter 12.

**Express Arc (this book)** — Single primary agent owns
the entire delivery sequence (investigate → plan → tests →
implement → audit → ship) without handoffs to specialist
agents. Quality gates fire as inline self-checks. Named
in this book; emerged in the Merlin Software Factory
engagement. See Chapter 16 and companion pattern quick reference §12.

**Fail loud** — Universal principle #5 (companion prompt-library preamble;
applied as Standard 6, Chapter 7). "Completed" is wrong
if anything was skipped silently. "Tests pass" is wrong if
any were skipped. Surface uncertainty; never hide it behind
a tidy summary. The discipline that prevents the most
expensive class of AI failure: the confidently-stated wrong
answer. See the companion prompt library; Standard 6.

**Faros AI 10,000-developer telemetry (2025)** — Telemetry
analysis published by Faros AI of more than 10,000 developers
across 1,255 teams using AI coding tools, parallel to and
commenting on the DORA findings. Found 21% more tasks completed and 98% more
pull requests merged at the individual level while
organizational DORA delivery metrics (deployment frequency,
lead time, change failure rate, MTTR, rework rate) remained
flat. The empirical anchor for "AI is an amplifier." See
Chapter 1, Chapter 3 (Faros AI, "The AI Productivity
Paradox," faros.ai, 2025).

**Fitness function** — Automated test that evaluates the
architecture's adherence to its design principles (Neal
Ford, Rebecca Parsons, Patrick Kua, *Building Evolutionary
Architectures*, O'Reilly, 2017). In agentic development,
fitness functions are the continuous monitoring layer for
architectural health. See Chapter 9.

**FMEA (Failure Mode and Effects Analysis)** — Reliability
method (MIL-STD-1629A, 1980; software adaptation in Goddard,
2000) that scores each potential failure mode for Severity,
Occurrence, and Detection and ranks by their product, the
Risk Priority Number. The quantitative complement to the
five blast-radius dimensions, reserved for high-blast-radius
features and security- or safety-critical paths. See
Chapter 5.

**Four-tier gate classification** — The book's classification
of automated quality gates into four tiers: BLOCKING (halts
the pipeline on failure), ADVISORY (surfaces findings for
human judgment), INFORMATIONAL (logged for trend tracking,
no per-PR action), and ASYNC (must resolve before merge but
executes asynchronously). Introduced as Standard 6
(Chapter 7); applied to deployment by Standard 9
(Chapter 8). See the companion quality-gate configuration reference.

**Generation-review asymmetry (this book)** — The gap
between the rate at which code can be generated (thousands
of LOC/hour) and the rate at which it can be meaningfully
reviewed (bounded by human cognition). The structural
problem that motivates the book's standards. See Chapter 1.

**Generation trifecta (this book)** — The agentic-era
supply-chain attack surface comprising three
mutually-reinforcing failure modes at the generation
boundary: (1) hallucinated dependencies (the *slopsquatting*
vector — agents importing plausible package names attackers
have registered), (2) reproduced vulnerabilities from
training data (CVE-known patterns regenerated as new code),
and (3) secret leakage (credentials embedded in generated
code or echoed into model context). The structural defense
is dependency allow-listing, regenerated-code SAST, and
secret scanning at the generation boundary. Distinct from
Simon Willison's *lethal trifecta* (see that entry), which
names a different triple. See Chapter 17, where the model is
extended to six vectors adding prompt injection propagation,
excessive tool authorization, and memory store integrity.

**Goodhart's Law** — "When a measure becomes a target, it
ceases to be a good measure" (Charles Goodhart, 1975;
phrasing popularized by Marilyn Strathern). It operates with
particular speed in agentic development because activity
metrics are trivially inflatable. Defenses: read the metrics
jointly, never singly, and never use them as targets for
individuals. See Chapter 18.

**Harness Framework (this book)** — Scope, Prove, Enforce,
Communicate: the four disciplines for governing agentic
development. A specification tells the agent what to build;
the Harness Framework tells the team how to govern the work.
Specifications (SPEC.md, requirements.md, Kiro specs) are
artifacts; the Harness Framework is the governance
discipline for evaluating those artifacts and the workflow
around them. Introduced in the author's article "AI Fluency
Should Be an Engineering Standard" (August 2025); expanded
into the book's organizing framework. See Chapter 4. The
four disciplines:

**Scope (Harness discipline)** — *Define what the agent is
allowed to touch.* The discipline of constraint before
generation: functional requirements (positive space), the
MUST-NOT list (negative space), and architectural boundaries
(structural space). When Scope fails: agents modify files
the specification did not mention; imports cross module
boundaries; unauthorized dependencies appear. See Chapter 4.

**Prove (Harness discipline)** — *Validate output against the
specification, not against intuition.* The discipline of
verification after generation, grounded in Popperian
falsification: the reviewer tries to break the code, not
to confirm it. Operationalized as Falsification Review
(Standard 7), in both its human and agent modes. See
Chapter 4.

**Enforce (Harness discipline)** — *Automate the constraints
that humans forget under pressure.* The discipline of
automation over intention: quality gates (Standard 6),
structural guardrails (Chapter 4), architecture fitness
functions, and CI/CD enforcement. If a constraint is
important enough to define, it is important enough to
automate. See Chapter 4.

**Communicate (Harness discipline)** — *Make decisions
auditable, not tribal.* The discipline of documentation as
infrastructure: the four pipeline artifacts (SPEC.md,
DESIGN.md, IMPL_NOTES.md, REVIEW.md), ADRs, ESCALATION.md,
and the close-the-loop update to AGENTS.md. Persistent
decisions are the only decisions that matter when each agent
session starts with zero memory. See Chapter 4.

**Hexagonal Architecture** — Also called Ports and Adapters
(Alistair Cockburn, 2005). Application core (the hexagon)
decoupled from infrastructure via ports (interfaces) and
adapters (implementations). The pattern that makes
agent-generated business logic survive infrastructure
changes without modification. See companion pattern quick reference §2.

**Honest journal** — The Standard 11 weekly artifact
described in Chapter 18. Three sections written in five
minutes: what AI saved time on this week, what AI cost
time on this week, pattern to try differently next week.
The mechanism for sustaining personal calibration over
months.

**Horse/Harness metaphor (this book)** — The book's core
organizing metaphor. The horse is the AI's generative
capability (powerful, fast, not optional). The harness is
the engineering discipline. A horse without a harness is a
liability. A horse with a harness is transportation
infrastructure. See the entire book; title.

**Hub (CRM Hub)** — The Fieldstone engagement
documented in Chapter 14. The v1 implementation of a CRM
integration mediating layer applying Hexagonal Architecture,
Anti-Corruption Layer, and Strangler Fig at the integration
scale.

**Hyrum's Law** — "With a sufficient number of users of an
API, it does not matter what you promise in the contract:
all observable behaviors of your system will be depended on
by somebody" (Hyrum Wright, hyrumslaw.com; elaborated in
*Software Engineering at Google*, O'Reilly, 2020). The
SPEC.md acceptance criteria define which behaviors are
contractual; everything else is implementation detail. See
Chapter 6.

**Idempotency** — The property that processing the same
request multiple times produces the same result as
processing it once. Critical for agent-generated code
because AI agents underestimate the importance of
idempotency without explicit specification. See Appendix
E §3.

**IDP (Internal Developer Platform) — risk mitigator and
context provider (DORA 2026)** — DORA's named architectural
role for the IDP in agentic systems: "In the agentic era,
an IDP is no longer just a portal for infrastructure, it is
the risk mitigator and the context provider for AI agents"
(DORA, *ROI of AI-assisted Software Development*, Google
Cloud, 2026). The MCP server fleet (Chapter 13) is the
agent-facing surface of the IDP: a context provider for
business capabilities and a risk mitigator for operational
systems. See Chapter 13.

**IMPL_NOTES.md** — The pipeline artifact maintained as a
running log during generation. Captures implementation
log entries, deviations from design, discovered
constraints, the tech debt register (three severity
tiers), and agent uncertainty entries. See the companion pipeline-artifact reference.

**Indirect prompt injection** — Attack vector where the
attacker plants instructions in data the agent processes
from external sources (emails, web pages, database
records), as opposed to direct prompt injection where the
attacker controls the prompt input directly. Greshake et
al., 2023. See Chapter 17.

**INFORMATIONAL gate** — Quality gate whose result is logged
and available for dashboards but requires no per-PR action.
Tracks trends meaningful at the project level (LOC delta,
dependency inventory, build duration, deployment frequency,
AI-generation metadata). One of four tiers in the four-tier
gate classification. See Chapter 7 and the companion quality-gate configuration reference.

**Jagged technological frontier (Dell'Acqua et al., 2023)** —
The finding that AI capability is unevenly distributed
across tasks: real gains inside the frontier, degraded
output outside it, and no visible marking on the boundary
("Navigating the Jagged Technological Frontier," HBS Working
Paper 24-013, September 2023). The strongest empirical
argument for verifying output regardless of which side of
the frontier you believe you are on. See Chapter 1.

**Kiro** — AWS's spec-driven agentic IDE. Structures every
feature as a spec pipeline — requirements.md (written in
EARS notation), design.md, and tasks.md — supported by
steering files and hooks. Vendor validation that the
industry is moving from prompt-to-code to spec-to-code.
Kiro specs are artifacts; the Harness Framework is the
governance discipline for evaluating those artifacts and
the workflow around them. See Chapter 2, Chapter 4.

**Lethal trifecta (Willison, 2025)** — Simon Willison's
established term for the dangerous combination, in a single
agent, of (1) access to private data, (2) exposure to
untrusted content, and (3) the ability to communicate
externally. A different triple from this book's *generation
trifecta* (see that entry); the two are distinguished in
Chapter 17.

**License-class triage (this book)** — Governance pattern
classifying dependencies into five license classes —
permissive, weak copyleft, strong copyleft, source-available,
and no license — with dispositions from adopt-freely to
default-skip on foundational components. Evaluated before
any agent-recommended dependency is accepted, as part of
Standard 5. Emerged in the CRM Hub engagement's 22-project
build-vs-buy analysis. See Chapter 12; Chapter 14.

**MCP (Model Context Protocol)** — Open standard for
connecting LLM agents to external tools and data sources
(Anthropic, 2024). Used across Chapter 13 as the
infrastructure for the Fieldstone MCP server fleet.

**Memory poisoning** — The attack in which an adversary
manipulates an agent's persistent memory store — graph
stores, vector databases, learning repositories — to alter
the agent's future behavior. The first entry in OWASP's
agentic threat catalog (see *OWASP Agentic AI — Threats and
Mitigations*). See Chapter 17.

**METR study (2025)** — The randomized controlled trial
finding that experienced developers were 19% slower with
AI tools while reporting they felt 20% faster.
40-percentage-point perception gap. The empirical
foundation for Chapter 18's personal calibration
practices.

**Multi-person adversarial advantage (this book)** — The
structural argument that two engineers cross-reviewing
each other's AI-assisted work catches *assumption errors*
that originate in the human's mental model — errors no
agent configuration can replicate. The case for small,
high-judgment teams in the agentic era. See Chapter 20.

**MUST-NOT list** — The negative-space section of SPEC.md.
Standard 1 requires six categories: architectural
boundaries, dependency constraints, data constraints,
security constraints, performance constraints, behavioral
constraints. An empty MUST-NOT list is a reliable predictor
of scope drift.

**Mutation testing** — Testing technique that makes small
modifications to the code — `>` to `>=`, a null check
removed, a constant zeroed — and verifies that at least one
test fails; if none does, the suite has a gap. Particularly
valuable for agent-generated code, whose tests often achieve
high coverage on happy paths without verifying rejection of
invalid inputs. See Chapter 10.

**Optimization principle (this book)** — Agents optimize for
the instruction over the constraint: asked to implement a
feature, an agent implements it without unprompted regard
for the constraints that surround the instruction —
idempotency, rate budgets, failure boundaries, license
terms. Constraints must therefore arrive contextually
(fragile) or structurally (robust: the architecture makes
the wrong behavior unreachable). The behavioral premise of
the Part III patterns. See Chapter 11.

**OWASP *Agentic AI — Threats and Mitigations* (2025)** —
The OWASP GenAI Security Project's threat catalog (version
1.0, February 2025) for systems where AI agents act:
fifteen named threats, opening with Memory Poisoning, Tool
Misuse, and Privilege Compromise. Distinct from the OWASP
Top 10 for LLM Applications, which addresses applications
that embed LLMs as components; teams building agent systems
need both, with the agentic catalog taking precedence.
Mapped to defenses throughout Chapter 17.

**Pipeline tracks** — Three deployment tracks (Hotfix,
Standard, Full) defined in Chapter 4, Section 4.7,
to match gate intensity to change risk. See the companion quality-gate configuration reference.

**Port** — In Hexagonal Architecture, an interface defined
in the application's own terms (not in vendor wire
format). Adapters implement ports for specific
technologies. See companion pattern quick reference §2.

**Property-based testing** — Testing technique that defines
properties holding for all valid inputs ("for any valid
user, `serialize(deserialize(user))` equals `user`") and
exercises them across generated cases, catching the corners
of the input space that neither the agent nor the
test-writing session considered. See Chapter 10.

**Provenance capture** — DN6 (Chapter 10, Definition of Done).
Every line of agent-generated code traces to its
specification, agent session, model, and reviewer through
structured commit message metadata.

**Quality throughput (this book)** — The rate at which a
team ships production-quality changes that move the product
forward without causing regressions. Chapter 18 treats it as
a lens rather than a metric and deliberately declines to
give a formula: any single composite number smuggles in
weights every team would set differently. The discipline is
reading deployment frequency, change failure rate, and
regeneration rate jointly, refusing to celebrate any one of
them alone. See Chapter 18.

**Recursive dark code problem (this book)** — The risk
that AI companies using AI to build AI infrastructure
without engineering discipline accumulate dark code in
their own training and serving infrastructure. The Harness
Framework applies at every level of the stack: solo
practitioner, software factory, foundation model company.
The harness on the harness. See Chapter 20.

**Regeneration rate (this book)** — The percentage of
agent-generated changes that require more than one
generation cycle before passing review. A coinage of this
book, deliberately distinct from DORA's *rework rate* (a
deployment metric: the percentage of deployments that are
unplanned work performed to fix user-facing bugs — see *DORA
metrics*). Proposed starting bands: aim below 20%; investigate
40–60%; above 60% prompts a pause in expansion and inspection
of failed cycles. These are uncalibrated, not established healthy
rates or a diagnosis of specification quality. Interpret them with
task difficulty, review rigor, and consequences. See Chapters 3 and 18.

**REVIEW.md** — The pipeline artifact recording the
reviewer's evidence-backed verdict. Sections: gate status,
specification compliance (AC-by-AC), MUST-NOT compliance,
disprove-only findings, adversarial validation findings,
disposition, sign-off. See the companion pipeline-artifact reference.

**Rollback classification** — Standard 9's four-way
classification of changes, determined before merge rather
than during the incident: clean revert, migration rollback,
data-dependent rollback, and non-reversible change. Each
class dictates what the rollback plan must contain;
non-reversible changes require the Full Track and explicit
acknowledgment that rollback is unavailable. See Chapter 8;
Chapter 5 asks the same question at blast-radius time.

**Saga** — Multi-step transaction coordination pattern
(Garcia-Molina & Salem, 1987) composing forward steps with
compensating transactions. Compensating transactions are
*not* "undo" — they are forward-moving operations that
neutralize a completed step's effect. See Chapter 15,
companion pattern quick reference §7.

**Scoped Authorization Token** — Applying the Principle of
Least Privilege (Saltzer & Schroeder, 1975) at the session
level. OAuth 2.0 scope is the modern formalization. In
agentic systems, each agent session receives a token
whose scope specifies which tools it can invoke. See
Chapter 13, companion pattern quick reference §10.

**Self-A/B test (quarterly)** — The Chapter 18 personal
calibration protocol: complete one task hand-coded (no AI),
then an equivalent task with the standard agentic
workflow. Measure both. Compare perceived vs. measured
speedup. Four data points per year are enough to detect
the METR gap personally.

**Shadow AI** — AI tools and agents operating outside the
organization's engineering standards entirely — the
governance problem that sits outside every threat catalog.
Requires a structural response — approved tools as good as
the unapproved ones, instrumentation rather than policing,
standards adoptable in stages — because policy documents
alone do not change behavior. See Chapter 17.

**Slopsquatting** — Supply chain attack where attackers
register package names that AI agents hallucinate, hoping
developers will install the malicious version. Term coined
by Seth Larson (Python Software Foundation, 2024); empirical
study by Bar Lanyado at Lasso Security ("Diving deeper into
AI package hallucinations," Lasso Security blog, 2024). The
empirical foundation for the dependency allowlist discipline
(Chapters 6 and 9) and Chapter 17's generation trifecta.

**Software Factory** — A continuous, instrumented loop
that turns external signals (bug reports, feedback,
requirements) into reviewed, secured, shipped, monitored
code. Term predates this book (Greenfield et al., *Software
Factories*, Wiley, 2004); this book's contribution is the
*agentic software factory* — application of the
engineering discipline framework to a system where AI
agents are first-class workers. See Chapter 16.

**SPACE framework** — Five-dimension developer-productivity
model: Satisfaction, Performance, Activity, Communication,
Efficiency (Forsgren, Storey, Maddila, Zimmermann, Houck,
and Butler, "The SPACE of Developer Productivity," *ACM
Queue* 19(1), 2021). In agentic development, Activity is the
dimension generation distorts most — track it only as a
denominator. The DevEx framework is its operational
successor. See Chapter 18.

**Spec-driven development** — The workflow in which
reviewable specification artifacts, with human approval
between phases, precede any code generation — the industry's
move from prompt-to-code to spec-to-code. Kiro (see that
entry) is the vendor productization; this book's SPEC.md
pipeline is the tool-agnostic form, and the Harness
Framework is the governance discipline around either. See
Chapter 2, Chapter 4.

**SPEC.md** — The first pipeline artifact. Six required
sections per Standard 1: problem statement, proposed
solution, machine-readable acceptance criteria, MUST-NOT
list, out of scope, affected components. Requirements are
expressed as the acceptance criteria. A specification is an
artifact; the Harness Framework is the governance
discipline around it. See the companion pipeline-artifact reference.

**Standards 1–12 (the Twelve Standards) (this book)** —
The numbered engineering standards that compose the book's
core discipline, organized in six tiers. Canonical names:

*Tier 1 — Plan:* **1.** Requirements as Verifiable
Contracts · **2.** Scope Definition and Session Boundaries ·
**3.** Blast Radius Analysis.

*Tier 2 — Design:* **4.** Interface-First Design ·
**5.** Dependency Discipline.

*Tier 3 — Generate & Verify:* **6.** Automated Quality Gates
and Governed Exceptions · **7.** Falsification Review (one
principle, two modes: human disprove-only review and agent
adversarial validation). Standard 1's structured generation
contract is demonstrated at this tier.

*Tier 4 — Ship:* **8.** Integration Verification ·
**9.** Release and Rollback Readiness.

*Tier 5 — Steward:* **10.** Architectural Stewardship and
Debt Governance.

*Tier 6 — Compound:* **11.** The Knowledge Loop ·
**12.** Continuous Improvement of the Standards.

Chapter homes: Chapter 5 (Standards 1–3), Chapter 6
(Standards 4–5), Chapter 7 (Standards 6–7 plus Standard 1's
generation practice), Chapter 8 (Standards 8–9), Chapter 9
(Standard 10), Chapter 10 (Standards 11–12).

**Status and Evidence box (this book)** — The boxed
statement opening each case-study chapter, declaring exactly
what is deployed, what is measured, what is projected, and
what the reader cannot verify. The mechanism by which no
case in this book claims a production status it does not
have. See Chapters 14–16 and Appendix B.

**Strangler Fig** — Migration pattern (Martin Fowler, 2004)
that incrementally builds new components alongside the
legacy system and gradually routes traffic from old to
new. See Chapter 12, Chapter 14, and Appendix B.

**STRATEGIC_PIVOT.md** — Document recording a significant
architectural course correction. Larger in scope than an
ADR, smaller than the project SPEC. Records the original
design, why it failed (with measured evidence), the new
direction, and what the pivot means for new work. See
Chapter 16; companion
`spec-templates/strategic-pivot-template.md`.

**STRIDE** — Threat-classification model (Loren Kohnfelder
and Praerit Garg, Microsoft, 1999; published treatment in
Howard and Lipner, *The Security Development Lifecycle*,
2006) organizing threats by the security property each
threatens: Spoofing, Tampering, Repudiation, Information
Disclosure, Denial of Service, Elevation of Privilege.
Applied in this book as the security-side blast radius at
specification time. See Chapter 5.

**Stripe Minions** — Stripe's internal coding-agent system,
publicly described in February 2026 (Alistair Gray,
"Minions: Stripe's one-shot, end-to-end coding agents,"
stripe.dev/blog, February 2026). Generates over 1,300 pull
requests per week with approximately 70% merged without
human modification, every PR receiving mandatory human
review. Built on "Blueprints" — state machines alternating
deterministic nodes and agentic nodes — and a core principle:
"AI reliability scales with the quality of its constraints,
not just the size of the model." The most consequential
practitioner-level convergence on the book's standards.
See Chapter 1; Chapter 2.

**Subagent challenge clauses** — Four prompt clauses
(Chapter 7) that change the agent's incentive
structure from "minimize visible uncertainty" to "surface
uncertainty explicitly." Embed inside any structured
generation prompt.

**Tag-text drift (this book)** — The failure mode in which
an agent expresses one judgment in two representations —
machine-readable tags and natural-language prose — and the
two diverge. Named from the Merlin post-mortem in which the
tags said block while the prose said approve, and the
aggregation logic trusted the tags. The rule: verify
agreement between the channels at emission, or build with
only one channel. See Chapter 16.

**Task Fit Matrix** — The Chapter 7 delegation framework
classifying work as strong, conditional, or weak fit for
agent generation. Strong: scaffolding, typed refactors, glue
code, documentation, boilerplate. Weak: security-critical
logic — hand-write it, always. Conditional fits depend on
substrate (types, tests, benchmarks); a conditional fit
without its substrate is a weak fit in disguise. See
Chapter 7.

**The 70% problem** — Addy Osmani's 2024 observation: AI
coding tools rapidly produce approximately 70% of a solution
— the happy path, the obvious cases, the structural skeleton
— but the remaining 30% comprises edge cases, security
hardening, production integration, and architectural
coherence. The remaining 30% is where bugs live, where
security vulnerabilities hide, and where architectural drift
compounds into technical debt (Addy Osmani, "The 70%
Problem," 2024). The practitioner observation that the book's
generation-review asymmetry and disprove-only review respond
to. See Chapter 1, Chapter 7.

**Thrashing (this book)** — Repeated fix iterations against
the same gate failure without convergence. The operational
trigger in Standard 6 (Chapter 7): more than 30 minutes or
more than three fix iterations on a single issue without
converging means stop, document, and escalate to a human.
See the companion prompt library for the thrashing check.

**Transactional Outbox** — Pattern named by Chris Richardson
(microservices.io); concept rooted in Pat Helland, "Life
Beyond Distributed Transactions" (CIDR, 2007). Atomically
updates a database and publishes a message without using
distributed transactions. See Chapter 11, Appendix
E §5.

**Trust boundary** — A point where your code interacts with
a system you do not control (external API, database,
message queue, user input). The location where integration
tests at the boundary catch failures that unit tests with
mocks miss. See Chapter 8.

**Universal principles (seven) (this book)** — The compressed
operational discipline that opens every context file
template: (1) Think before coding (Standard 1); (2) Surgical
changes (Standard 2); (3) Read before you write (Standard
11); (4) Match the codebase's conventions (Standard 10);
(5) Fail loud (Standard 6); (6) Adversarially review your
own substantive work (Standard 7); (7) Close the loop
(Standard 11). See the companion prompt-library preamble.

**Verification stance markers (this book)** — The
`verified` / `ASSUMPTION` / `VERIFY` marker convention
for factual claims in agent-generated code and
documentation. Eliminates the worst failure mode of
AI-generated documentation: the confidently stated
falsehood. See Chapter 7.

**Work Order (Merlin)** — The unit of work in the Merlin
Software Factory: a product idea or task submitted to the
factory and carried through discovery, design, tests,
implementation, self-audit, deployment, and institutional
learning. Scoped with success criteria; Merlin's own defect
catalog is formatted as Work Orders, the discipline
operating on its own output. See Chapter 16.

---

## Acronyms

| Acronym | Expansion |
| --- | --- |
| ACL | Anti-Corruption Layer |
| ADR | Architecture Decision Record |
| ADVISORY | (gate tier) |
| API | Application Programming Interface |
| ASYNC | (gate tier) Asynchronous |
| AC | Acceptance Criterion (in SPEC.md) |
| AGENTS.md | Agents Markdown (the non-Claude equivalent of CLAUDE.md) |
| AWS | Amazon Web Services |
| BFF | Backend for Frontend |
| BLOCKING | (gate tier) |
| CAS | Compare-and-Swap |
| CDC | Change Data Capture |
| CFR | Change Failure Rate (DORA metric) |
| CI | Continuous Integration |
| CI/CD | Continuous Integration / Continuous Deployment |
| CLAUDE.md | Claude Markdown (the project-root context file for Claude Code) |
| COTS | Commercial Off-The-Shelf |
| CPU | Central Processing Unit |
| CQRS | Command Query Responsibility Segregation |
| CRM | Customer Relationship Management |
| CRUD | Create, Read, Update, Delete |
| CSP | Content Security Policy |
| CVE | Common Vulnerabilities and Exposures |
| CVSS | Common Vulnerability Scoring System |
| DAG | Directed Acyclic Graph |
| DDD | Domain-Driven Design |
| DLQ | Dead Letter Queue |
| DORA | DevOps Research and Assessment |
| EARS | Easy Approach to Requirements Syntax (used in Kiro requirements.md) |
| EIP | Enterprise Integration Patterns |
| FR | Functional Requirement (requirements expressed as acceptance criteria in SPEC.md) |
| GDPR | General Data Protection Regulation |
| HMAC | Hash-based Message Authentication Code |
| HSM | Hardware Security Module |
| HTTP | Hypertext Transfer Protocol |
| IDE | Integrated Development Environment |
| INFORMATIONAL | (gate tier) |
| JSON | JavaScript Object Notation |
| JWT | JSON Web Token |
| LOC | Lines of Code |
| LLM | Large Language Model |
| LTS | Long-Term Support |
| MCP | Model Context Protocol |
| METR | Model Evaluation & Threat Research (research organization) |
| MFA | Multi-Factor Authentication |
| MIME | Multipurpose Internet Mail Extensions |
| MN | MUST-NOT item (in SPEC.md) |
| MTTR | Mean Time to Restore (DORA metric) |
| MVP | Minimum Viable Product |
| OAuth | Open Authorization |
| ORM | Object-Relational Mapping |
| OWASP | Open Worldwide Application Security Project |
| PCI | Payment Card Industry |
| PII | Personally Identifiable Information |
| POC | Proof of Concept |
| PR | Pull Request |
| QA | Quality Assurance |
| RBAC | Role-Based Access Control |
| REST | Representational State Transfer |
| RFC | Request for Comments |
| SAST | Static Application Security Testing |
| SDK | Software Development Kit |
| SLA | Service Level Agreement |
| SOC | (in SOC 2) System and Organization Controls |
| SOLID | Single-responsibility, Open-closed, Liskov, Interface-segregation, Dependency-inversion |
| SPEC | Specification (the SPEC.md artifact) |
| SQL | Structured Query Language |
| SSO | Single Sign-On |
| TCPA | Telephone Consumer Protection Act |
| TLS | Transport Layer Security |
| TOCTOU | Time-of-Check to Time-of-Use |
| TOGAF | The Open Group Architecture Framework |
| TTL | Time to Live |
| UI/UX | User Interface / User Experience |
| UUID | Universally Unique Identifier |
| WCAG | Web Content Accessibility Guidelines |
| YAGNI | You Aren't Gonna Need It |

---

This glossary is the canonical reference for terminology
across the book. Where a term has a chapter-specific
treatment that goes beyond the definition here (e.g., the
Harness Framework in Chapter 4, the Merlin Software Factory
in Chapter 16), the chapter is authoritative. The glossary
exists for the reader who encounters a term in one chapter
and needs the definition without searching the index.
