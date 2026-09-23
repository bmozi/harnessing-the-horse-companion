# Disprove-Only Review Prompt

> **Chapter:** ch07 — Generation, Verification, and Review (Standard
> 7: Falsification Review, human disprove-only mode)
> **Last revised:** 2026-09-10
> **Model assumed:** Frontier model
> **Inspired by:** Cloudflare's "disprove correctness" review practice
> **Use this for:** Reviewing AI-generated code. Your task is NOT to
> confirm correctness. Your task is to find how this code FAILS.

A specification gives review explicit claims to test. Read the changed
code, tests, and relevant surrounding paths to understand those claims.
Falsification directs that work; it does not replace comprehension.
Split or defer changes that exceed available review capacity.

---

```markdown
## Disprove-Only Review

You are reviewing AI-generated code. Your task is NOT to confirm
correctness. Your task is to find how this code FAILS.

### Input
- SPEC.md: [path to specification]
- DESIGN.md: [path to design document]
- Generated code: [path to code under review]
- MUST-NOT list from the generation prompt: [list]

### Question 1: Automated Gate Status
Confirm all blocking gates pass. List any advisory findings.

### Question 2: Specification Compliance
For each requirement in SPEC.md:
- [ ] Trace the requirement to its implementation
- [ ] Identify the test(s) that verify it
- [ ] Flag any requirement with no implementation or no test

### Question 3: Specification Violations (THE CRITICAL SECTION)
Search for:
- [ ] MUST-NOT list violations: does the code do anything the prompt
      explicitly prohibited?
- [ ] Unauthorized side effects: network calls, file I/O, state
      mutations not in the spec
- [ ] Scope creep: functionality not described in the specification
- [ ] Hidden assumptions: hardcoded values, environment-specific
      behavior, magic numbers
- [ ] Error handling gaps: null, empty, maximum, malformed, concurrent
      inputs
- [ ] Security surface: new endpoints, new input parsing, new
      privilege paths
- [ ] Resource management: unclosed connections, unbounded allocations,
      missing timeouts
- [ ] Concurrency issues: race conditions, deadlock potential, shared
      mutable state

### Output
State which code and surrounding paths you inspected, the evidence checked,
and any unresolved gaps. An unresolved material gap prevents approval.
For each finding:
1. File and line number
2. Classification: CRITICAL / MAJOR / MINOR
3. The failure scenario: under what conditions does this fail?
4. Suggested remediation

If no findings, state: "Attempted to disprove correctness across [N]
dimensions. No failures identified. This is not a guarantee of
correctness."
```

---

## Areas of Critique

- **Reviewer effort on Question 3.** A disprove-only review that
  checks three items from the list and stops is not a review. The
  reviewer should articulate which failure dimensions they examined
  and why they believe the remaining dimensions are not applicable.
- **Specification quality dependency.** Disprove-only review is only
  as powerful as the specification it reviews against. A vague
  specification produces a vague review — by design. It forces
  specification quality problems to the surface, where they can be
  addressed.
- **False confidence from empty findings.** "No failures identified"
  is not "correct." It means: given the dimensions examined and the
  effort applied, no failure was found. The code may still be wrong in
  ways the reviewer did not think to check. This epistemic humility is
  the point of the disprove-only framing.

## Common Failure Modes

- **The Confirmation-Bias Relapse.** The reviewer starts with the
  disprove-only prompt but, after finding the code reads cleanly,
  reverts to confirmation mode: "Well-structured, good variable names,
  clean separation of concerns — LGTM." None of those observations
  answer the three questions.
- **The Dimension Skip.** "This code doesn't do anything concurrent."
  Agents frequently introduce concurrency the specification did not
  contemplate. Every dimension gets checked, even if the check is
  "not applicable because [specific reason]."
- **The Silent Assumption.** Identifying a hidden assumption but not
  flagging it because it happens to be true in the current environment.
  Assumptions that are true today and wrong tomorrow are the most
  expensive bugs in software.

## Related

- `structured-prompt.md` — the prompt that generated the code under
  review
- `quality-gate-config-review.md` — Question 1's gates are configured
  here
- `adversarial-validation.md` — escalation path for high-risk changes

## Provenance

Adapted from Chapter 7 of *Harnessing the Horse*, Standard 7
(Falsification Review, human disprove-only mode).
Inspired by Cloudflare's review practice; refined through Merlin
Software Factory deployment cycles.

The Merlin Enhancement: a project-level *review dimension registry* —
seeded with the eight standard dimensions and extended with
project-specific dimensions discovered through production incidents.
When an incident is traced to a dimension not in the registry, the
postmortem adds the dimension. The registry grows over time, ensuring
the team's review practice incorporates its own history.

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
