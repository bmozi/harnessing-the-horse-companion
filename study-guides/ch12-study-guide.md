# Chapter 12: Migration at Scale with AI Agents — Study Guide

Student and self-study material moved from Chapter 12 so the book's main reading path remains practitioner-focused.

> Instructor solutions, answer keys, and grading rubrics are distributed separately to verified instructors.

## Learning Objectives

1. Explain why migration phases are sequenced by learning value and blast radius rather than by what agents can generate in parallel.
2. Construct a strangler-fig migration plan with per-phase acceptance criteria, rollback procedures, and phase-gate checklists.
3. Decompose a backward-incompatible schema change into Expand-Migrate-Contract steps, each independently deployable and reversible.
4. Apply the three migration-specific governance requirements — shrinking credential surface, sync loop detection, and review time budgeted as a percentage — to agent-generated migration code.
5. Evaluate an agent-recommended dependency using license-class triage, and the underlying build decision using Wardley-map differentiation reasoning.
6. Analyze whether Event Sourcing and CQRS, with event versioning specified from day one, are justified foundations for a multi-year coexistence.

## Key Terms

- **Strangler Fig** — Migration pattern (Fowler, 2004) that incrementally builds new components alongside the legacy system and gradually routes traffic from old to new.
- **Event Sourcing** — Architectural pattern (Young, 2006) that persists every state change as an immutable event, deriving current state by replay.
- **CQRS (Command Query Responsibility Segregation)** — Splitting a system into a command side that processes writes and a query side that serves reads, each free to use different models and storage.
- **Saga** — Multi-step transaction coordination pattern (Garcia-Molina & Salem, 1987) composing forward steps with compensating transactions.
- **Bounded context** — A boundary within which a particular domain model applies (Evans, 2003); in agentic development, a structural requirement that constrains the vocabulary an agent session uses.
- **Blast radius** — The set of components, services, and users that could be affected if a change contains a defect; the sequencing criterion for migration phases.
- **ADR (Architecture Decision Record)** — A short document capturing the context, decision, alternatives, and consequences of a significant architectural choice.

## Review Questions

1. What three risks does agent-generated migration code introduce beyond greenfield development, and what governance requirement answers each?
2. Name the three steps of Expand-Migrate-Contract and explain why a rollback at any point in the sequence restores a working state without data loss.
3. Why must acceptable divergence thresholds be set per entity type per phase rather than as one global number?
4. What are the five license classes in the triage pattern, and which of them are flagged for default-skip on foundational components?
5. When an agent generates a multi-phase data migration governed by the Saga pattern, which three artifacts must it produce per phase, and what is lost if any one is missing?

## Discussion Questions

1. The chapter requires that migration timelines budget review time as a percentage of total time, never as a compressible buffer — but a regulatory deadline does not move. When generation is finished and review is behind schedule, something gives: scope, the deadline, review depth, or headcount. Who should decide, and what makes that decision defensible afterward?
2. Wardley-map logic says buy commodities even when agents make building cheap. Is there any commodity — authentication, email delivery, payments — where the calculus genuinely flips as build cost approaches zero, or does the provider's accumulated operational hardening always dominate? Argue a specific component both ways.
3. Event sourcing purchases audit trails and temporal validation at the price of versioning discipline sustained for years. Under what organizational conditions — turnover, tooling maturity, team size — is that trade a bad one even for a multi-year migration?

## Exercises

**Exercise 12.1 (Core) — Plan a strangler-fig migration and defend the sequencing.** A monolithic order-management system serves five consumers: the customer storefront, a warehouse picking app, a nightly finance export to the ERP, transactional email, and a reporting dashboard. All five read one shared database; the storefront and warehouse app also write to it. The payment provider's current API sunsets in nine months — a hard external deadline affecting only the storefront's checkout path. Plan the migration to a service-based target. *(~4 h+)*
*Deliverable:* A migration plan artifact containing the phase sequence, per-phase acceptance criteria and rollback procedure, a credential plan (created and decommissioned per phase), plus a one-page defense of your sequencing in terms of learning value and blast radius — including why you did or did not put the deadline-critical path first.
*Assessment:* Judged against the migration phase gate checklist (Section 12.2; companion repository `examples/migration-phase-gate.md`) and Standard 3 (Blast Radius Analysis). Pass requires an explicit rollback path for every phase and a sequencing rationale that references what each phase teaches the next.

**Exercise 12.2 (Core) — Audit and repair an agent's schema decomposition.** An agent asked to rename `user_email` to `email_address` and split `full_name` into `first_name` and `last_name` — across a table with four consuming services owned by two other teams, two of which deploy monthly, plus a nightly finance export that reads `full_name` directly — produced this plan: PR1 adds the three new columns and an insert trigger that dual-writes them for new rows; PR2 backfills the whole table in one transaction and switches all four services to read the new columns; PR3 switches writes to the new columns and drops the trigger; PR4 drops `user_email` and `full_name` one sprint later. Find every step that is backward-incompatible, lossy, or unsafe to pause after, then produce the corrected Expand-Migrate-Contract decomposition. *(~2 h)*
*Deliverable:* A flaw log — per flaw, the step, the concrete failure a reviewer could trigger, and the Expand-Migrate-Contract rule it violates — plus the corrected decomposition: per PR, the schema DDL, the application changes, the backfill or dual-write mechanics, and a note stating what happens if the sequence pauses indefinitely after this PR.
*Assessment:* Section 12.1's discipline: no individual step backward-incompatible, the migrate step chunked/idempotent/resumable, and every pause-note describing a state safe to hold indefinitely. Reviewed as Standard 2 task decomposition; pass requires catching the two unrecoverable flaws — the calendar-gated drop of `full_name` while slow-deploying consumers and the finance export still read it (irreversible once mis-split names can no longer be re-derived from the source), and the read-switch of services the author's team does not deploy.

**Exercise 12.3 (Core) — Run a license-class triage.** Take the dependency manifest of a real project you have access to (or, paper variant, a provided list of ten packages spanning at least three license classes) and triage every direct dependency. *(~2 h)*
*Deliverable:* A triage table: package, license, license class, evidence link (the actual LICENSE file or SPDX identifier, not a package-registry summary), and disposition (adopt / review / skip) with one sentence of reasoning.
*Assessment:* Section 12.3's five classes applied per Standard 5 (Dependency Discipline). Pass requires primary-source evidence for every classification and at least one dependency where the registry metadata and the repository license disagree or require investigation.

**Exercise 12.4 (Challenge) — Design divergence detection, then defeat it.** For the coexistence period of the migration you planned in Exercise 12.1, design the divergence-detection instrumentation: shadow-read sampling rate and coverage, reconciliation job schedule and comparison logic, and per-entity-type thresholds with escalation triggers. Then attack your own design: identify two divergence classes it would miss (consider rarely-read entities, timing windows, and semantic mappings that are wrong only for edge-case values) and either fix the design or document why the residual risk is acceptable. *(~4 h+)*
*Deliverable:* The detection design plus an adversarial appendix listing the misses and their disposition.
*Assessment:* Standard 7 (Falsification Review) applied to your own artifact: the adversarial appendix is graded on whether the misses are real (a reviewer can construct the divergent record) rather than hypothetical.

