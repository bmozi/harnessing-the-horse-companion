# Escalation Assessment Prompt

> **Compatibility path:** The book references
> `prompts/escalation-assessment.md`. The canonical companion asset is
> [`escalation-protocol.md`](escalation-protocol.md), which includes the
> full escalation protocol, authority levels, and prompt below.

Use this assessment before any quality-gate override is considered.

```markdown
## Escalation Assessment

A quality gate has failed. Complete this assessment before any override is considered.

### Gate Failure Details
- Gate name: [which gate failed]
- Classification: [BLOCKING / ADVISORY]
- Finding: [specific finding with file:line reference]
- Severity: [CRITICAL / HIGH / MEDIUM / LOW]

### Root Cause
- Is this a false positive? [yes/no, with evidence]
- Is this a genuine issue? [yes/no, with description]
- Is this a tooling limitation? [yes/no, with explanation]

### Thrashing Check
- How long has the engineer been working on this issue? [duration]
- How many fix iterations have been attempted? [count]
- Is the issue converging toward resolution? [yes/no, with evidence]
- If duration >= 30 minutes OR iterations >= 3:
  STOP. Document and escalate to human. Do not iterate further.

### Override Assessment
- Authority level required: [1 / 2 / 3 / 4-no-override]
- Business justification: [specific, not general]
- Risk assessment: [severity if the finding is real and ships to production]
- Mitigation: [what controls reduce the risk until remediation]
- Remediation plan: [ticket number, owner, deadline]
- Blast radius if the finding is real: [reference Standard 3 analysis]

### Decision
- [ ] Fix the issue (no override needed)
- [ ] Override with documentation (Level 1-3, with all required artifacts)
- [ ] Escalate to human (issue exceeds agent capability)
```

See also:

- [`escalation-protocol.md`](escalation-protocol.md)
- [`quality-gate-config-review.md`](quality-gate-config-review.md)
- [`blast-radius-analysis.md`](blast-radius-analysis.md)

