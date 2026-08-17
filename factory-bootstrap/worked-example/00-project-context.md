# Example Notifications Service: Project Context

> Fictional completed example. Adapt the blank context templates in
> `../../spec-templates/` to your actual repository.

## Project Overview

This service stores notification preferences and schedules account reminders.
The domain layer decides eligibility. Delivery adapters send messages. Domain
code never imports an email, SMS, queue, or database SDK.

## Commands

- Install: `npm ci`
- Type check: `npm run typecheck`
- Unit tests: `npm test`
- Architecture check: `npm run check:boundaries`

These commands are illustrative project facts. An agent must verify the actual
commands in the target repository before running them.

## Boundaries

- `domain/` may depend only on domain types and ports.
- `adapters/` may implement domain ports and contain vendor translation.
- `api/` may call domain use cases but may not call delivery vendors directly.
- Preference updates and audit records must commit atomically.

## MUST-NOT Constraints

- Do not add a dependency for validation that existing project utilities cover.
- Do not change reminder scheduling or delivery retry behavior.
- Do not expose vendor field names through the public API.
- Do not log email addresses, phone numbers, tokens, or message bodies.
- Do not execute destructive database commands or publish from an agent session.

## Review Expectations

Every non-trivial change requires a SPEC, test evidence, dependency-delta check,
MUST-NOT verification, and a reviewer who did not generate the implementation.
