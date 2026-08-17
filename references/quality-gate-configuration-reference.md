# Quality Gate Configuration Reference

The single-table reference for the four-tier quality gate
classification introduced in Standard 6 (Chapter 7) and
applied to deployment in Standard 9 (Chapter 8). Use this
appendix when configuring a CI pipeline, when reviewing an
existing pipeline's configuration, or when classifying a new
quality check the team wants to introduce.

The classification matters because not every check justifies
halting a deployment, but every check that *does* justify it
must be impossible to skip. Treating gates as equal produces
one of two pathologies: either every warning blocks (creating
friction that incentivizes engineers to bypass the gates
entirely) or every warning is advisory (creating noise that
habituates engineers to ignoring the gates entirely). The
four tiers exist to resolve that pathology.

---

## C.1 The Four-Tier Classification

| Tier | Behavior | When the gate fails | Examples |
| --- | --- | --- | --- |
| **BLOCKING** | Halts the pipeline; PR cannot merge | Resolution required before proceeding | Type check / compilation; unit tests; security scan at CRITICAL or HIGH; dependency license compliance; architecture boundary enforcement; API contract validation |
| **ADVISORY** | Pipeline proceeds; finding surfaced in PR review interface | Reviewer exercises judgment; finding can be accepted, deferred, or remediated | Code coverage delta; complexity metrics; performance regression within tolerance band; documentation coverage; security scan at MEDIUM or LOW |
| **INFORMATIONAL** | Logged to dashboard; no per-PR action required | Tracked for trend analysis; feeds the project metrics dashboard | LOC delta; dependency inventory; build duration; test execution time; AI-generation metadata; deployment frequency |
| **ASYNC** | Runs in background; does not block generation or review; must resolve before merge | PR held in "pending ASYNC" state; findings reviewed before final approval | Full integration test suite; performance benchmarks; full dependency vulnerability scan (transitive); license compliance (transitive); SAST deep analysis |

**Why four tiers, not three or two.** A two-tier system collapses ADVISORY and INFORMATIONAL into one bucket — losing the distinction between "needs reviewer judgment this PR" and "logged for trend tracking, no action required." A three-tier system (BLOCKING/ADVISORY/ASYNC) misses the INFORMATIONAL category that the SPACE framework's Activity dimension and the DORA metrics dashboards depend on. The four-tier system also recognizes ASYNC as distinct from ADVISORY: ASYNC checks must pass before merge but execute too slowly to block the synchronous pipeline. Production systems without an ASYNC tier typically run these expensive checks post-merge on `main`, accepting risk for pipeline speed; holding the PR in a pending-ASYNC state closes that gap. See Chapter 7 for the empirical framing.

---

## C.2 Gate Classification by Standard

This table cross-references each of the Twelve Standards to
the gate tier(s) it implies. Use it as the starting checklist
when configuring a new project's CI pipeline.

| Standard | Chapter | Implied gates | Tier |
| --- | --- | --- | --- |
| Std 1 — Requirements as Verifiable Contracts | 5 and 7 | SPEC.md exists; all six required sections present and non-empty; acceptance criteria are binary and machine-readable; the structured generation contract traces its requirements and constraints to the durable artifacts; pre- and post-generation gates completed | BLOCKING (existence, structural completeness, traceability, both gates) |
| Std 2 — Scope Definition and Session Boundaries | 5 | DESIGN.md exists; task scope under 400 LOC; one session per task; cyclomatic complexity within bounds | BLOCKING (existence, session-per-task); ADVISORY (complexity) |
| Std 3 — Blast Radius Analysis | 5 | Blast radius template completed at SPEC time; verified at review; review effort classification determined and matched | BLOCKING (template exists at both points) |
| Std 4 — Interface-First Design | 6 | Interface spec exists for every cross-module contract | BLOCKING (existence) |
| Std 5 — Dependency Discipline | 6 | Dependency manifest complete; every external dependency declared before the agent references it | BLOCKING (declaration before reference); ADVISORY (manifest completeness) |
| Std 6 — Automated Quality Gates and Governed Exceptions | 7 | The audit prompt in §C.3 verifies that CI respects the four-tier classification; ESCALATION.md exists whenever an override or thrashing trigger invokes the exception path | BLOCKING (configuration; exception record when triggered) |
| Std 7 — Falsification Review | 7 | REVIEW.md exists; three questions answered; eight failure dimensions enumerated (human mode); adversarial review run in a fresh instance with findings documented in REVIEW.md (agent mode, changes on the Full pipeline track) | BLOCKING (existence and structural completeness; agent mode for the Full track) |
| Std 8 — Integration Verification | 8 | Contract verification passes; cross-component tests pass; system-level smoke test passes; refactoring pass complete; five architectural questions answered yes | BLOCKING (the first three); ADVISORY (refactoring pass); BLOCKING (the five questions) |
| Std 9 — Release and Rollback Readiness | 8 | All blocking gates (above) pass; pipeline track explicitly assigned; post-merge monitoring thresholds configured; rollback classification determined; rollback procedure documented; rollback tested (for migration/data-dependent classifications); rollback owner identified | BLOCKING |
| Std 10 — Architectural Stewardship and Debt Governance | 9 | Architecture fitness functions pass; impact boundary assessment completed for any boundary-crossing change; IMPL_NOTES.md tech debt register present and structured by severity tier (must-fix-before-merge / should-fix-soon / can-defer); zero must-fix-before-merge items unresolved; Ousterhout's four simplicity tests (deep module, YAGNI, comprehension, delete) passed | BLOCKING (fitness functions, boundary assessment, zero must-fix-before-merge); ADVISORY (simplicity, others) |
| Std 11 — The Knowledge Loop | 10 | Pattern library entries reference applicable patterns; mutation testing run on critical paths; property-based tests defined for functions with complex input domains; AGENTS.md / CLAUDE.md updated within last 30 days and with session-specific learnings; file under the 300-line ceiling with regular pruning (200 lines is the target — see the tool-configuration reference); module-scoped context files where total exceeds threshold; commit references the context-file update | ADVISORY |
| Std 12 — Continuous Improvement of the Standards | 10 | Retrospective conducted on incidents; standards updated based on data (false-negative, false-positive, missing-coverage, friction signals) | INFORMATIONAL (per-PR); ADVISORY (per-retrospective) |
| **DN6 — Provenance Capture** | 10 | Commit message footer includes SPEC reference, session ID, model identifier, reviewer name | BLOCKING (footer format) |

The "implied gates" column is descriptive — many of these
gates require team-specific implementation (a linter rule, a
custom script, a CI step). The classification is the claim
that matters: which tier each implementation belongs to.

---

## C.3 The Quality Gate Configuration Review Prompt

Use this prompt to audit a project's CI configuration against
the requirements above. This is the canonical printing;
The complete prompt library's §A.2 points here.

```markdown
## Quality Gate Configuration Review

Review the project's quality gate configuration against these
requirements:

### Blocking Gates (must be present and enforced)
- [ ] Compilation / type-check passes with zero errors
- [ ] All unit tests pass (zero failures, zero skipped without
      documented reason)
- [ ] Security scan: zero CRITICAL, zero HIGH findings
- [ ] License scan: all dependencies in approved license list
- [ ] Architecture boundaries: no prohibited cross-module
      imports
- [ ] API contract: generated OpenAPI matches implementation

### Advisory Gates (must be present, findings surfaced in PR)
- [ ] Code coverage: delta reported, threshold violations
      highlighted
- [ ] Complexity: functions exceeding [threshold] flagged
- [ ] Performance: benchmark regressions above [tolerance]
      flagged
- [ ] Documentation: public APIs missing doc comments listed

### Informational Gates (logged to dashboard)
- [ ] LOC delta tracked
- [ ] Dependency inventory updated
- [ ] Test execution time recorded
- [ ] AI-generation metadata captured

### Async Gates (results required before merge; synchronous pipeline does not block)
- [ ] Full integration / e2e test suite scheduled
- [ ] Performance regression benchmark vs. baseline scheduled
- [ ] SAST deep analysis scheduled
- [ ] License compliance + dependency vulnerability deep scan
      scheduled
- [ ] PR held in "pending ASYNC" state until results return;
      failure blocks merge

### Enforcement
- [ ] Blocking gates are configured as required status checks
      in branch protection
- [ ] Blocking gates CANNOT be bypassed by administrators
      without a documented override
- [ ] Advisory gate results appear in the PR review interface
      (not buried in CI logs)
- [ ] Informational gate data feeds the project metrics
      dashboard
- [ ] Async gate results block merge on failure; the PR
      pending-ASYNC state is visible to reviewers

Identify any gaps and recommend specific configurations to
close them.
```

---

## C.4 Pipeline Track Assignment

Standard 9 distinguishes three pipeline tracks that match
gate intensity to change risk. The table below is the
authoritative classification.

| Track | Used for | Gates that run | Review |
| --- | --- | --- | --- |
| **Hotfix** | Typo fixes, configuration value updates, single-file formatting changes under 50 LOC | Lint + type check + targeted test suite | Reviewer confirms change does what it claims and nothing more |
| **Standard** | New endpoints, UI components, business logic changes, test additions (default track for agent-generated code) | Full BLOCKING gate suite + REVIEW.md + cross-component integration tests | Full disprove-only review (Std 7, human mode) |
| **Full** | Database migrations, authentication changes, payment processing, infrastructure modifications, cross-module changes, cross-boundary changes | Standard track + architectural review against five questions + extended integration testing + performance baseline comparison + security review with dependency audit | Standard track review + designated second reviewer + adversarial validation (Std 7, agent mode) |

**Track classification is explicit.** It must be documented
in the PR description or task metadata. A change that is
classified on the wrong track — a database migration on the
hotfix track, a typo fix on the full track — is caught
during review and reclassified. Track classification is a
judgment call, and judgment calls benefit from transparency.

**Gaming defense.** When the engineer (or the agent) assigns
the track, peer-review of the track assignment is required.
Automatic escalation rules also apply: any change that
touches files in `auth/`, `payments/`, `migrations/`, or
similar high-blast-radius directories triggers the Full
track regardless of the assigned track.

---

## C.5 Post-Merge Monitoring Thresholds

Deployment safety does not end at merge. The post-deploy
observation window typically runs 15–30 minutes calibrated to
traffic patterns. Four monitoring conditions trigger
automated or alerted responses:

| Condition | Threshold | Response |
| --- | --- | --- |
| Error rate exceeds baseline | 2× baseline within 15 minutes | **Automatic rollback** (no human decision required) |
| P95 latency exceeds baseline | 1.5× baseline within 15 minutes | Alert raised; **manual rollback decision** |
| New error types appear | Any error type not present pre-deploy | Alert raised; **investigation required** |
| Health check failures on critical endpoint | Any failure | **Automatic rollback** |

The thresholds are protective, not punitive. Tighter
monitoring compensates for the comprehension gap that
characterizes agent-generated code (the original author has
no memory of the session). Relaxation must be driven by
data, not by optimism.

---

The single-page reference above is the operational form. For
the chapter discussion of *why* each tier behaves the way it
does, see Chapter 7 (gate classification) and Chapter 8
(deployment). For the in-prompt audit, use §C.3 above. For
the CI/CD workflow that implements the classification, see
the tool-configuration reference.

The `checklists/deployment-safety-checklist.md` file in the
companion repository is the
per-deployment checklist that complements this
configuration-level reference; the configuration determines
which gates exist, and the checklist determines which gates
must be confirmed for a specific deployment.
