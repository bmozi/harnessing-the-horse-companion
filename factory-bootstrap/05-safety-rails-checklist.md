# Safety Rails Checklist

Read Chapter 16 and Chapter 17 before using this checklist. Application checks
harden the normal proposal path; approval authority, repository permissions,
and protected verification must remain outside the process that proposes work.

## Autonomy Boundary

- [ ] The factory can propose work.
- [ ] The normal application path refuses to persist or execute proposed work without human approval.
- [ ] The calling process cannot mint, forge, or rewrite the approval record.
- [ ] Approval policy is enforced outside agent-writable configuration (for example, protected workflow state plus repository permissions).
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
- [ ] Agent credentials cannot modify these checks; protected CI verifies them independently.
- [ ] Maintainer override authority is named, least-privileged, and auditable.

## Human Review Questions

- What can this proposal touch?
- What must it not touch?
- What evidence says it improves the factory?
- What evidence would falsify it?
- What is the rollback path?
