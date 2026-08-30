# Small Change Session

Use this one-page scaffold only for a local, reversible change that introduces
no new dependency, external interface, data-classification change, production
rollout, or material consequence. Otherwise use the ordered
[governed-session pack](governed-session-pack/README.md).

## 1. Boundary and owner

- **Change and affected files:**
- **Owner and reviewer:**
- **Outcome we expect:**
- **Out of scope and MUST-NOT:**
- **Stop condition or reason to return to the full pack:**

## 2. Testable contract

- **Acceptance criterion 1:**
- **Acceptance criterion 2:**
- **Existing behavior that must not change:**
- **Evidence to run:**

## 3. Implementation record

- **What changed:**
- **What the generator or implementer was told:**
- **Unexpected result, uncertainty, or deviation:**

## 4. Independent challenge

- **Reviewer (not the generator):**
- **What claim did they try to disprove?**
- **Gate results and unresolved finding:**

## 5. Decision and learning

- **Final outcome:** **SHIP / REVISE / STOP**
- **Decision owner and reason:**
- **What would reverse or roll back this decision:**
- **One reusable lesson for the next session:**

Copy this file into the target repository with the change. The compact form is
proportional documentation, not a lower safety standard: a missing owner,
boundary, independent challenge, or decision means the session is incomplete.
