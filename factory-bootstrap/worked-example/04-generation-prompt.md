# Generation Contract: Per-Channel Reminder Preferences

## Task

Implement the approved SPEC and DESIGN for per-channel reminder preferences.

## Functional Requirements

- Implement AC-1 through AC-7 exactly as written in `02-spec.md`.
- Use the expand-migrate-contract sequence in `03-design.md`.
- Keep the preference and audit writes atomic.

## Constraints

- Read the current domain, API, repository, migration, and test files before
  proposing edits.
- Reuse existing validation and transaction utilities.
- Preserve the module boundaries in `00-project-context.md`.
- Produce the smallest coherent change for the approved phase only.

## MUST-NOT List

Repeat every MUST-NOT item from `02-spec.md` here. Treat an inability to prove an
item as `VERIFY`, not as permission to proceed.

## Output Format

Before editing, report:

1. files inspected;
2. proposed files changed;
3. acceptance criterion to test mapping;
4. assumptions and `VERIFY` items;
5. dependency delta.

After editing, report exact commands run, results, remaining limitations, and
the proposed `IMPL_NOTES` entries. Do not push, merge, publish, or remove the
legacy field.

## Review Criteria

The implementation is not complete until every acceptance criterion has
evidence, every MUST-NOT item is checked, migration rollback remains possible,
and skipped integration evidence is explicit.
