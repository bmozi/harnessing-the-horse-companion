# Anti-Corruption Layer + Hexagonal Architecture (TypeScript)

> **Chapter:** ch11 — Integration Patterns (Sections 11.1 and 11.2)
> **Patterns:** [Anti-Corruption Layer](../../patterns/anti-corruption-layer.md), [Hexagonal Architecture](../../patterns/hexagonal-architecture.md)

> These artifacts are companion materials for *Harnessing the Horse*.
> The book provides the design rationale, failure modes, and
> case-study context that make these patterns concrete in practice.
> **TypeScript source files in this directory are licensed under the
> MIT License** ([see `../../LICENSE-CODE`](../../LICENSE-CODE)) —
> use, fork, and integrate into commercial work freely.

## Files

| File | What it is |
| --- | --- |
| [`crm.port.ts`](crm.port.ts) | The `CRMPort` interface defined in **domain terms**. The contract agents code against. |
| [`hubspot.adapter.ts`](hubspot.adapter.ts) | `HubSpotAdapter` — implements `CRMPort` by translating to/from HubSpot wire-format. The vendor-specific translation is **contained** in this file. |
| [`test.adapter.ts`](test.adapter.ts) | `InMemoryCRMAdapter` — deterministic in-memory implementation for tests. Lets generated business logic be testable in isolation. |

## The structural property

When an agent generates a new workflow that creates contacts, it
imports `CRMPort` and codes against `DomainContact`. The agent
**never sees**:

- HubSpot's `firstname` vs. the domain's `firstName`
- HubSpot's `lead_source` custom property name
- HubSpot's `intengration_id` typo
- HubSpot's lifecycle stage vocabulary

**The adapter is a containment boundary for vendor specificity.**

If you swap HubSpot for Salesforce, the business logic does not
change — only a new `SalesforceAdapter` implementing `CRMPort` is
required.

## Trying it

Run `npm ci && npm test` from the repository root to compile the port and
adapters and execute their contract-focused test. The example below shows the
same in-memory adapter in direct use.

```typescript
import { InMemoryCRMAdapter } from './test.adapter';

const crm = new InMemoryCRMAdapter();
await crm.createContact({
  firstName: 'Jane',
  lastName: 'Smith',
  email: 'jane@example.com',
  source: 'referral',
});

const found = await crm.findContact({ email: 'jane@example.com' });
console.log(found);
// → { firstName: 'Jane', lastName: 'Smith', email: 'jane@example.com', source: 'referral' }
```

The same code works against `HubSpotAdapter` in production. **No
business-logic change. No mocks. No coupling.**

## Related

- [`../../patterns/anti-corruption-layer.md`](../../patterns/anti-corruption-layer.md)
- [`../../patterns/hexagonal-architecture.md`](../../patterns/hexagonal-architecture.md)
- [`../../spec-templates/interface-spec.md`](../../spec-templates/interface-spec.md)
  — the template you would have written before generating the port

## Provenance

Adapted from Chapter 11 of *Harnessing the Horse* by John Briggs.

TypeScript source: © 2026 John Briggs, MIT licensed
(see [`../../LICENSE-CODE`](../../LICENSE-CODE)).
This README: CC BY-NC-SA 4.0
(see [`../../LICENSE-CONTENT`](../../LICENSE-CONTENT)).
