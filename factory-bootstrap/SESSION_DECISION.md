# Session Decision Record

Use this record as the final business decision for one governed delivery
session. It is separate from `REVIEW.md`: a reviewer recommends; the named
decision owner chooses **SHIP**, **REVISE**, or **STOP**.

**Decision date:**
**Repository / branch:**
**Work Order owner:**
**Work Order ID + version:**

## Outcome

- [ ] **SHIP** — execute the release as defined.
- [ ] **REVISE** — correct required issues and rerun the loop.
- [ ] **STOP** — do not proceed with this path until the governing constraint changes.

**Decision owner:** ____________________

## Evidence and remaining risk

- Evidence requirements met:
  1. ______________________________
  2. ______________________________
- MUST-NOT list respected?
  - [ ] Yes
  - [ ] No — list gaps:
    ______________________________
- Independent review completed by:
  ______________________________
- Any deliberately skipped artifact, reason, accepting owner, and remaining risk:
  ______________________________

## Reversibility and learning

- Known uncertainty that remains:
  ______________________________
- What must trigger **STOP** if conditions change:
  ______________________________
- Who owns redesign or reversal:
  ______________________________
- Return date for revisit:
  ______________________________
- One requirement or control changed by this run:
  ______________________________
- Required evidence for the next session:
  ______________________________

## Sign-off

- Decision owner:
- Witness:
- Readable artifact links:
  - REVIEW: ____________________
  - Metrics: ____________________
