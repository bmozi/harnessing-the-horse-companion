# Cagan Four-Risk Assessment Template

> **Chapter:** ch05 — Discovery and Planning (Section 5.1, "Assessing
> the Risk Before Writing the Spec: Cagan's Four Risks")
> **Last revised:** 2026-06-16
> **Use this for:** Complex features — those that cross multiple module
> boundaries, introduce new user-facing capabilities, or change data
> models. Supplements the SPEC.md.

Adapted from Marty Cagan's product discovery framework:
*Inspired: How to Create Tech Products Customers Love*, 2nd ed.,
Wiley, 2018.

If any risk category scores high and is unmitigated, the feature should
not proceed to generation. Return to discovery and resolve the risk
first. The cheapest time to kill a bad idea is before anyone writes
code for it.

---

```markdown
# Cagan Four-Risk Assessment: [feature name]

## Value Risk
**Question:** Will users actually find this valuable? What evidence
supports this?

**Assessment:** [Low / Medium / High]

**Evidence:**
- [What evidence do we have that users want this?]
- [Customer interviews, support tickets, usage data, ...]

**Mitigation (if Medium or High):**
- [How will we validate value before committing to full implementation?]

**Red flag:** Building features based on assumptions rather than
evidence.

## Usability Risk
**Question:** Can users figure out how to use this? Does it follow
established UX conventions?

**Assessment:** [Low / Medium / High]

**Evidence:**
- [Existing UX patterns this follows or breaks]
- [Prototype testing, user research]

**Mitigation (if Medium or High):**
- [How will we test usability before locking in the design?]

**Red flag:** The technical solution works but users cannot navigate
it.

## Feasibility Risk
**Question:** Can we build this with the current architecture,
dependencies, and timeline?

**Assessment:** [Low / Medium / High]

**Evidence:**
- [What technical spike or proof-of-concept has been done?]
- [Architectural constraints, existing patterns]

**Mitigation (if Medium or High):**
- [What spike or POC will validate feasibility before full build?]

**Red flag:** Committing to a solution before validating architectural
support.

## Business Viability Risk
**Question:** Does this align with business strategy, compliance
requirements, and operational constraints?

**Assessment:** [Low / Medium / High]

**Evidence:**
- [Stakeholder alignment, compliance review, operational readiness]
- [Legal, finance, support, ops considered]

**Mitigation (if Medium or High):**
- [What sign-offs are needed before proceeding?]

**Red flag:** Building something the business cannot legally deploy or
operationally support.

## Decision

- [ ] All four risks Low → proceed to generation
- [ ] One or more Medium/High with documented mitigation → proceed with
      mitigation tracked
- [ ] Unmitigated High → return to discovery
```

---

## Related

- `spec-md.md` — the SPEC.md this assessment supplements

## Provenance

Adapted from Chapter 5 of *Harnessing the Horse*. The four risks come
from Marty Cagan, *Inspired: How to Create Tech Products Customers
Love*, 2nd ed., Wiley, 2018. The template is the book's adaptation for
agentic development.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
