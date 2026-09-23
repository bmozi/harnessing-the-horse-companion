# Rollback Readiness Checklist

> **Chapter:** ch08 — Execution Discipline (Standard 9: Release and
> Rollback Readiness)
> **Last revised:** 2026-06-16
> **Run when:** Before deploy. Every change deployed to production
> must be reversible within minutes.

When human-authored code causes an incident, the author can be paged,
recall the design decisions, reason about the failure mode, and guide
remediation. When agent-generated code causes an incident, the session
that produced it no longer exists. The engineer who reviewed it may
remember the high-level design but is unlikely to recall the specific
implementation details at 2 AM under incident pressure.

**Rollback readiness ensures the first response to any incident is
simple, fast, and does not require deep understanding of the code that
caused the problem.**

---

## Step 1: Classify the Rollback

Pick exactly one classification. The procedure depends on what
changed.

### Clean revert (preferred)

The change modifies only application code. No database changes, no
external state changes, no configuration changes affecting data
interpretation.

- [ ] This is a clean revert (proceed to Step 2)

### Migration rollback

The change includes a reversible database migration. If reversal would lose
data or cannot restore required behavior, use the non-reversible class and
a tested containment or recovery plan instead of inventing a down script.

- [ ] This is a migration rollback (Step 2 + Step 3)
- [ ] Forward migration has been applied successfully in staging
- [ ] **Reverse migration exists and has been tested in staging**
- [ ] Order of operations is documented: revert code first or migrate
      first?

> An untested down migration is not a rollback plan — it is a prayer.

### Data-dependent rollback

The change modifies how data is written, transformed, or interpreted.
Reverting requires not only code revert but addressing data written
during the active window.

- [ ] This is a data-dependent rollback (Step 2 + Step 3 + Step 4)
- [ ] Data correction script exists for records written by the new
      code
- [ ] Validation queries to confirm the correction worked exist

### Non-reversible change

Examples: dropping a column, deleting records, sending notifications,
publishing external API changes consumers may have already used.

- [ ] This is non-reversible (Step 2 + special handling)
- [ ] Full pipeline track selected (`deployment-safety-checklist.md`)
- [ ] Extended monitoring window agreed (≥ 1 hour, on-call
      confirmed)
- [ ] Risk consciously accepted in writing — not discovered during
      the incident

> The team must accept this risk **consciously**, not discover it
> during the incident.

---

## Step 2: Document the Procedure

The deployment plan includes a "Rollback" section.

- [ ] The rollback section names the **exact commands** to reverse
      the change
- [ ] For clean reverts: the `git revert` command and the deployment
      trigger are specified
- [ ] For migration rollbacks: the down migration script and the
      order of operations are specified
- [ ] For data-dependent rollbacks: the data correction scripts and
      their validation queries are specified

## Step 3: Test the Rollback (if not clean revert)

- [ ] Rollback procedure executed against a staging environment
      *that has had the forward change applied*
- [ ] Down migration runs without error
- [ ] Data correction scripts produce the expected results
- [ ] Reverted application behaves correctly after rollback complete

## Step 4: Assign the Owner

- [ ] **Rollback owner is named** (not implicit — a specific person)
- [ ] The owner is the engineer **on call** at deploy time, with
      access to deployment infrastructure
- [ ] The owner **reviews the rollback procedure before deployment
      proceeds**
- [ ] **If the owner does not understand the procedure, the
      deployment does not proceed.**

---

## Mid-Build Rollback (for the generation process itself)

Rollback readiness applies during generation too. When the agent hits
a BLOCKING gate failure mid-generation:

- [ ] **First failure on an issue:** fix in place. Most lint/type
      errors are trivial.
- [ ] **Second failure on the same issue:** step back. Re-read the
      spec. The approach may be wrong; fixing the symptom without
      addressing the cause produces another failure downstream.
- [ ] **Third failure:** roll back to the last known-good state.
      Revert the file. Document the failure pattern in IMPL_NOTES.md
      and try an alternative approach.
- [ ] **Persistent failure across approaches:** **escalate.** Create
      ESCALATION.md (see `../prompts/escalation-protocol.md`). Stop
      generating code that repeatedly fails gates — that is the
      definition of thrashing.

> Three failures on the same issue is a signal, not a coincidence.

---

## Common Failure Modes

- **The "We'll Figure It Out" Rollback.** Deployment plan says
  "rollback: revert the deployment." Nobody has tested what that
  means when there is a database migration. At 2 AM during the
  incident, the team discovers that reverting breaks the application
  because the schema has been modified and the old code expects the
  old schema. Rollback takes three hours instead of three minutes.
- **The Orphaned Migration.** A migration is deployed as part of a
  feature. The feature is rolled back because of a bug. The migration
  is not rolled back because "it didn't cause the bug." The database
  now has a schema no running code uses. Six months later, another
  migration conflicts. The team spends a day understanding why the
  database has a column no code references.
- **The Irreversible Surprise.** Agent-generated component sends
  webhook notifications to an external system. Component deployed,
  processes several records, sends notifications. Bug discovered,
  code rolled back. But notifications have already been sent. The
  external system has already acted on them. The rollback reversed
  the code but could not reverse the side effects. **Changes with
  external side effects must be classified as non-reversible** and
  receive the corresponding level of scrutiny.

## Related

- `integration-verification-checklist.md` — Q4 of the five
  architectural questions references this checklist
- `deployment-safety-checklist.md` — the pipeline track selection
  depends on this classification
- `../prompts/escalation-protocol.md` — what to do when mid-build
  rollback escalates to a human

## Provenance

Adapted from Chapter 8 of *Harnessing the Horse*, Standard 9. The
three-element rollback protocol (procedure documented, rollback
tested, owner identified) was refined through Merlin Software Factory
operations.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
