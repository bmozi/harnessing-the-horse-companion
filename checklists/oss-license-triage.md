# OSS License-Class Triage

> **Chapter:** ch12 — Migration at Scale with AI Agents (Section
> 12.3, "Build vs. Buy in the Agentic Era")
> **Last revised:** 2026-06-16
> **Run when:** Before accepting any AI-recommended open-source
> dependency.

AI agents accelerate build velocity so dramatically that the
build-versus-buy calculus shifts. When an AI agent can generate a
working component in a day, the build option becomes competitive —
but only if the generated component meets quality standards and does
not introduce licensing, security, or maintenance risks that the
vendor solution would have handled.

**The governance challenge:** AI agents, when asked to find a
solution, recommend open-source packages based on **capability
match**, not on licensing terms, maintenance status, or supply chain
risk.

An agent may recommend:

- A package with an **AGPL license** (imposes copyleft obligations on
  the consuming application)
- A package **maintained by a single developer** who has not pushed
  a commit in eighteen months
- A package with **known vulnerabilities** that the agent's training
  data predates

When an AI agent recommends a dependency, **the license class must
be evaluated before the dependency is accepted**. This evaluation is
part of the pre-generation gate (see
[`pre-generation-verification.md`](pre-generation-verification.md))
for any task that involves dependency selection.

**The agent's recommendation is a starting point for evaluation, not
a decision.**

---

## The Five License Classes

### Permissive (MIT, BSD, Apache 2.0)

✅ **Generally safe.**

The obligation is **attribution**, which is low-cost. Compatible
with commercial use, modification, and distribution.

- [ ] Verified license file is present and matches a permissive
      license
- [ ] Attribution mechanism in place (NOTICE file, third-party
      licenses page, etc.)

### Weak Copyleft (LGPL, MPL)

⚠️ **Acceptable as a dependency, requires review if modified.**

Modifications to the library itself must be open-sourced, but the
consuming application is not affected.

- [ ] Library is used as a **dependency**, not forked or modified
- [ ] No engineer is planning to modify the library source
- [ ] If modifications are planned → escalate for engineering
      review

### Strong Copyleft (GPL, AGPL)

🛑 **Requires legal review. Often blocking.**

The consuming application may be subject to copyleft obligations.
**AGPL is particularly aggressive** — even network interaction
(SaaS) can trigger the obligation.

- [ ] License has been reviewed by legal counsel for this
      application's business model
- [ ] If AGPL → confirmed that SaaS-trigger does not apply OR the
      copyleft obligation is acceptable
- [ ] In many enterprise contexts: **strong copyleft is a blocking
      finding.**

### Source-Available (ELv2, BSL, SSPL)

⚠️ **Not OSI-approved. Requires legal AND business review.**

These are **not open-source licenses** by OSI definition. They impose
commercial restrictions that may conflict with the consuming
application's business model.

- [ ] Legal review of the specific license terms
- [ ] Business review: does the license conflict with our
      product's commercial model?
- [ ] Risk assessment of license change: vendors using these
      licenses (Elastic, MongoDB, Redis) have changed terms; what
      is the migration cost if this happens to us?

### No License

🛑 **BLOCKING.**

Code with no license file is, by default, **all-rights-reserved**.
An agent that recommends unlicensed code is recommending code that
**cannot legally be used**.

- [ ] Do **not** adopt
- [ ] If the package genuinely has no license, contact the
      maintainer and request one
- [ ] Document the rejection in IMPL_NOTES.md so future agent
      sessions don't re-propose it

---

## The Triage Worksheet

For each AI-recommended dependency, complete:

```markdown
## Dependency Triage: [package-name@version]

**Source:** [npm / PyPI / Maven / etc.]
**Recommended by:** [agent session ID, or "human evaluation"]
**Capability sought:** [what the package provides]

### License classification
- License: [exact name from the LICENSE file]
- Class: [Permissive / Weak copyleft / Strong copyleft / Source-available / No license]
- Verdict: [Accept / Accept with review / Reject]

### Maintenance check
- Last commit: [date]
- Open issues: [count, especially security-tagged]
- Maintainer count: [N]
- CVE history: [list any in last 24 months]

### Risk assessment
- License risk: [low / medium / high — and why]
- Maintenance risk: [low / medium / high — and why]
- Supply chain risk: [low / medium / high — and why]

### Decision
- [ ] Accept
- [ ] Reject (with reason)
- [ ] Escalate (license / security / legal review needed)

### If accepted
- [ ] Added to dependency manifest with exact version pin
- [ ] Attribution in NOTICE / third-party licenses page
- [ ] License class noted in IMPL_NOTES.md for future agent context
```

## Why This Belongs in the Pre-Generation Gate

By the time you discover a license conflict at code-review time, the
agent has already generated code that depends on the package. Removal
requires regenerating against an alternative — and the alternative
may not exist or may impose its own constraints.

Catching license issues **before** generation begins:

- Prevents wasted generation cycles
- Avoids "we've already shipped this, let's just keep it" pressure
- Keeps the dependency manifest clean
- Documents the rejection so future agent sessions have the
  context

## Related

- [`pre-generation-verification.md`](pre-generation-verification.md)
  — Check 3 (Dependency Check) should run this triage
- `../spec-templates/impl-notes-md.md` — record rejected packages in
  the IMPL_NOTES.md so future sessions inherit the context
- `migration-phase-gate.md` — when migration introduces new
  dependencies, run triage as part of the phase pre-conditions

## Provenance

Adapted from Chapter 12 of *Harnessing the Horse*, Section 12.3.
The five-class taxonomy was developed in the Fieldstone CRM Hub
engagement during evaluation of 22 open-source alternatives to a
custom-built solution.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
