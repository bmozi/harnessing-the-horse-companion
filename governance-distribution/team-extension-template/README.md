# Team Governance Extension

Use this directory to add domain vocabulary, approved dependencies, commands, data-contract rules, and team-specific review checks.

The extension is additive:

- It may make a baseline gate stricter.
- It may add new file-scoped or domain-scoped constraints.
- It may not disable security review, falsification review, evidence reporting, or required CI.
- A conflict with the organization baseline must fail closed and be resolved by the baseline owner.

Record the baseline version this extension targets and test the combined behavior before release.

