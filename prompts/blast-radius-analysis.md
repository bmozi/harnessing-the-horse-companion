# Blast Radius Analysis Prompt (Review-Time)

> **Chapter:** ch05 — Discovery and Planning (Standard 3: Blast
> Radius Analysis — the review-time verification pass)
> **Last revised:** 2026-06-16
> **Model assumed:** Frontier model
> **Use this for:** Quantifying the impact surface of a change at
> *review* time, after generation. Pairs with the SPEC-time blast
> radius template (`../spec-templates/blast-radius-template.md`).

In traditional development, engineers develop an intuitive sense of
blast radius through accumulated context. AI-generated code
invalidates this intuition because the agent has no accumulated
context beyond the current session, and the agent's changes may reach
further than the engineer realizes.

The concept draws from Cloudflare's deployment practices. A July 2019
outage caused by a bad regex in their WAF rules took down a
significant portion of the internet for 27 minutes. The root cause was
not the regex. The root cause was that a change to a single rule had
a blast radius spanning every HTTP request through Cloudflare's
network, and no one had quantified that radius before deployment.

In agentic development, blast radius analysis is about **review
prioritization** — telling the reviewer where to focus, how much
effort to invest, and what constitutes "good enough" verification.

---

```markdown
## Blast Radius Analysis

Before this change can be reviewed, complete the following impact
assessment.

### Direct Impact
- Files modified: [list]
- Lines changed: [count]
- New files: [list]
- Deleted files: [list]

### Dependency Impact
- Modules that import or reference changed code: [list with file paths]
- Services that consume changed APIs or events: [list]
- Shared types or interfaces modified: [list with consumer count]

### Data Impact
- Database tables affected (schema or query changes): [list]
- Data formats changed (serialization, API response, event payload):
  [list]
- Data migration required: [yes/no, with migration plan reference if
  yes]

### External Impact
- External APIs affected: [list with consumer count]
- Webhook payloads changed: [list with subscriber count]
- Event schemas changed: [list with consumer count]
- User-facing behavior changes: [list with affected user segments]

### Rollback Strategy
- Can this change be reverted with a single git revert? [yes/no]
- Are there irreversible side effects (data migrations, external API
  calls)? [list]
- Estimated rollback time: [duration]
- Rollback dependencies: [list of coordinated actions required]

### Review Effort Classification
Based on the above:
- [ ] **Contained** — affects only the implementing module, no
      external consumers, revert is trivial. Standard review.
- [ ] **Moderate** — affects 2-5 internal modules, no external
      consumers, revert is straightforward. Enhanced review with
      dependency verification.
- [ ] **Broad** — affects external consumers, shared infrastructure,
      or data schemas. Full review with integration testing and
      staged rollout plan.
- [ ] **Critical** — affects security boundaries, payment flows, or
      regulatory-compliance code. Full review + designated second
      reviewer + explicit sign-off.
```

---

## Areas of Critique

- **Completeness of dependency tracing.** The most common gap is
  stopping at direct dependencies and not tracing transitive ones. If
  module A changes, B depends on A, and C depends on B, the blast
  radius includes C even though C does not directly reference the
  changed code. In large codebases, tooling (dependency graph
  analyzers, architecture fitness functions) is necessary to trace
  transitive impact.
- **Data flow awareness.** Analyses that focus solely on code
  dependencies miss the data dimension. A change to an input
  validation rule may be a one-line code change but affect every
  record processed from that point forward.
- **Rollback realism.** "Revert the commit" is only valid if the
  change has no side effects that persist after revert: no database
  migrations, no external API calls with lasting effects, no event
  publications downstream consumers have already processed. If the
  change has any persistent side effect, the rollback strategy must
  address it specifically.
- **Review-effort-to-risk proportionality.** A "contained"
  classification should not be accepted uncritically. Question
  whether it is accurate. AI-generated changes are particularly prone
  to having larger blast radii than their authors realize.

## Common Failure Modes

- **The "It's Just a Refactor" Assumption.** Classifying a change as
  "contained" because "I'm just renaming a variable" or "I'm just
  moving a function to a different file." Renaming can break
  serialization contracts, configuration references, and external
  API consumers that reference the old name.
- **The Missing Data Dimension.** Listing code dependencies
  comprehensively but saying nothing about data. Data blast radius is
  often the largest dimension and the most frequently omitted.
- **The Optimistic Rollback.** "We can always revert." If the change
  includes a database migration that drops a column, reverting the
  code does not restore the column. Every rollback strategy must be
  evaluated against the specific side effects of the change.
- **The Underscoped External Impact.** Listing zero external
  consumers because "nobody uses this API externally." But does the
  OpenAPI spec say that? Has the endpoint been discovered by an
  internal tool nobody mentioned? In one CRM Hub design instance,
  blast radius analysis revealed an internal endpoint was being
  called by a vendor-built HubSpot card the platform team did not
  know existed — six months of development had missed it.

## The Merlin Enhancement

Merlin automates blast radius analysis by integrating with the
project's dependency graph and the CI/CD pipeline's change detection.
The template is auto-populated from:

- `git diff` for the direct impact
- The module dependency graph (maintained as an architecture fitness
  function) for the dependency impact
- The database migration log for the data impact
- The API contract registry (OpenAPI specs, event schemas) for the
  external impact

The auto-populated template is then reviewed by the engineer, who
validates the classification and adds any context the tooling missed.
Hybrid approach: automated data collection, human judgment on
classification.

## Related

- `../spec-templates/blast-radius-template.md` — the SPEC-time
  companion (ch05 Std 3) that estimates this *before* generation
- `escalation-protocol.md` — what to do when a blast-radius
  classification reveals risk above the team's autonomous threshold
- `../checklists/deployment-safety-checklist.md` — the classification
  determined here selects the pipeline track at deploy time

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*, Standard 3 — blast
radius is estimated at planning time and verified at review time; this
prompt is the review-time pass. Inspired by Cloudflare's
post-2019-WAF-outage deployment practices.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
