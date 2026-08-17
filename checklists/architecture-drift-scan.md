# Architecture Drift Scan Checklist

> **Chapter:** ch09 — Architectural Stewardship (Standard 10; the
> drift scan); companion complete prompt library §A.18
> **Last revised:** 2026-07-03
> **Run when:** Periodically (quarterly at minimum) and before
> merging any change with a boundary-adjacent blast radius. Compares
> the actual dependency graph against the documented architecture.

The impact boundary assessment (`impact-boundary-assessment.md`)
asks five questions about *one change*. The drift scan asks a
different question about *the whole system*: does the code, as it
exists today, still match the architecture as documented? Drift
accumulates through individually reasonable, individually approved
changes; this scan is how the cumulative pattern gets evaluated as a
whole.

Every finding from the checks below is classified as **Violation**
(must resolve), **Evolution** (documentation needs updating), or
**Ambiguity** (architecture needs more precision) — see the
classification section at the end.

---

## The Five Checks

### 1. Module-Boundary Conformance

- [ ] Does every import in the codebase respect the **module
      boundaries** defined in the architecture documentation?
- [ ] Are there imports reaching into another module's **internal
      packages** rather than its public interface?
- [ ] Have any **layer crossings** appeared (e.g., the API layer
      calling the database directly, bypassing the service layer)?

### 2. Dependency-Direction Rules

- [ ] Do all dependencies point in the **documented direction**
      (e.g., domain never imports adapters or handlers; adapters may
      import domain)?
- [ ] Are there any **circular dependencies** between modules?
- [ ] Do any modules reference **vendor types directly** where the
      architecture requires an adapter or anti-corruption layer?

### 3. New-Dependency Detection

- [ ] Does the current dependency manifest contain any external
      dependency **not present at the last scan** and not declared
      through the Standard 5 process?
- [ ] Have any **new inter-module dependencies** appeared since the
      last scan that no impact boundary assessment approved?
- [ ] Are all allowlist **exceptions still justified**, or has an
      approved exception quietly become the norm?

### 4. Fitness-Function Coverage of New Modules

- [ ] Is every module added since the last scan **covered by the
      architecture fitness functions** (import-linter, ArchUnit,
      ESLint architectural rules, or equivalent)?
- [ ] Do the fitness-function rules still **match the documented
      boundaries**, or have rules been loosened without a
      corresponding architecture decision?
- [ ] Would a **seeded boundary violation** in each new module
      actually fail the build? (Spot-check at least one.)

### 5. ADR-Index Cross-Check

- [ ] Does every structural change found by checks 1–4 trace to an
      **ADR in the index**?
- [ ] Are any indexed ADRs **contradicted by the current code**
      (decision says X, dependency graph shows Y)?
- [ ] Do superseded ADRs still have **live code depending on the
      superseded decision**?

---

## Classify Every Finding

| Class | Meaning | Disposition |
| --- | --- | --- |
| **Violation** | Code clearly violates the documented architecture. | **Must resolve** — fix the code, or record a deliberate decision (ADR) and update the architecture. |
| **Evolution** | The architecture has legitimately evolved; the documentation has not. | Update the diagrams, boundary docs, and fitness-function rules. Documentation gaps left unaddressed become drift. |
| **Ambiguity** | The documentation is unclear about whether the dependency is allowed. | Add precision — more granular boundary definitions, more explicit rules — then re-classify. |

A scan that produces zero findings on a system under active
agent-assisted development is more likely a shallow scan than a
clean system. Record the scan date, the findings, and their
dispositions; the trend across scans is the health metric.

## Related

- `impact-boundary-assessment.md` — the per-change five-question
  gate this scan complements (change-time vs. system-time)
- `../diagrams/baseline-architecture-diagrams.md` — the documented
  architecture the actual dependency graph is compared against
- `../spec-templates/adr-template.md` — where deliberate departures
  from the documented architecture are recorded
- `simplicity-review.md` — the companion ch09 review for
  agent-generated structural excess

## Provenance

Adapted from Chapter 9 of *Harnessing the Horse* (Standard 10 —
Architectural Stewardship and Debt Governance). The three-class
finding taxonomy (Violation / Evolution / Ambiguity) is the book's
drift scan classification; the scan prompt is printed in the companion
complete prompt library §A.18.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
