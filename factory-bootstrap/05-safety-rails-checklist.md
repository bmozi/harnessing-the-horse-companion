# Safety Rails Checklist

Read Chapter 16 and Chapter 17 before using this checklist. Do not add autonomous improvement until these controls exist outside the improvement surface.

## Autonomy Boundary

- [ ] The factory can propose work.
- [ ] The factory cannot persist or execute proposed work without human approval.
- [ ] The human approval requirement is not a runtime configuration flag.
- [ ] The approval record includes approver, timestamp, Work Order ID, and scope.

## Forbidden Surface

List files or systems the factory must not modify or propose modifications to:

- Safety policy:
- Permission policy:
- CI gate definitions:
- Secrets and credentials:
- Deployment controls:
- Evaluation criteria:

## Proposal Limits

- [ ] Daily proposal cap:
- [ ] Per-repository proposal cap:
- [ ] Token or cost budget:
- [ ] Failure threshold that pauses proposal generation:

## Self-Reference Detection

- [ ] Proposals are scanned for references to the improvement system itself.
- [ ] Proposals are scanned for references to safety, permission, gate, and evaluation files.
- [ ] Blocked proposals are logged for human review.
- [ ] There is no agent-accessible path to weaken these checks.

## Human Review Questions

- What can this proposal touch?
- What must it not touch?
- What evidence says it improves the factory?
- What evidence would falsify it?
- What is the rollback path?
