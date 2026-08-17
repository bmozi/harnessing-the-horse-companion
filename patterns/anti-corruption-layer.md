# Anti-Corruption Layer (ACL)

> **Chapter:** ch11 — Integration Patterns (Section 11.1)
> **Last revised:** 2026-06-16

## Origin

Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart
of Software* (Addison-Wesley, 2003, ISBN 978-0321125217), Part IV
"Strategic Design."

## Intent

A mechanism for **protecting a bounded context from contamination**
when integrating with external systems whose models do not align with
the internal domain.

The ACL sits between two bounded contexts. It exposes the internal
context's shape inward and translates to and from the external
context's shape outward. It is composed of **adapters** (translating
at the wire level), **translators** (translating semantic shapes), and
**facades** (presenting a clean interface to the internal context).

The ACL is itself a bounded context — its language is the
translation, distinct from both upstream and downstream systems.

## Application in Agentic Development

In agentic development, the ACL takes on a **second audience**. The
traditional audience is human developers who need the domain model
insulated from vendor pollution. The new audience is **AI agents that
need domain-consistent interfaces to generate correct code**.

Without an ACL, the agent uses whatever vocabulary appears in its
context — typically the external system's API documentation. Vendor
field names leak into the domain model. Vendor data-model assumptions
shape the agent's implementation decisions. The domain model degrades
exactly as Evans predicted — but at the rate AI agents produce code,
not the rate humans do.

### Three categories of corruption the ACL prevents

Observed in the Fieldstone CRM Hub engagement before the ACL was
established:

- **Naming corruption.** A HubSpot custom property was created with a
  typo: `intengration_id` instead of `integration_id`. The typo could
  not be corrected without breaking dependent integrations. Without
  an ACL, every internal service that referenced the field had to
  know about the typo. The ACL translates `integration_id` (domain
  name) → `intengration_id` (vendor name) at the boundary. Internal
  code never sees the typo.
- **Dual-naming corruption.** The same conceptual field —
  `customer_id` — had two HubSpot names: `fieldstone_customer_id` and
  `fieldstoneos_customer_id`, created by different services at different
  times. New agent sessions couldn't determine which to use. The ACL
  exposes one canonical name and maps it to the winner, marking the
  alternative as a legacy alias.
- **Semantic corruption.** HubSpot's lifecycle stage vocabulary
  (`subscriber`, `lead`, `marketingqualifiedlead`) differs from the
  domain's (`new_lead`, `qualified`, `scheduled`, `active_customer`,
  `churned`). Similar but not identical. The ACL maps between them —
  and the mapping is **data** (table rows), not code, editable by
  operations teams without engineering changes.

## Why the ACL Matters More for Agents Than for Humans

A human developer who integrates with HubSpot will, over time, learn
that `intengration_id` is a typo, that `fieldstoneos_customer_id` is
legacy, and that HubSpot's lifecycle stages don't map one-to-one to
the domain. The developer builds this knowledge through experience
and carries it forward.

**An AI agent cannot do this.** Each session starts fresh. Without
the ACL, every agent session must be told about every piece of vendor
corruption — and if any corruption is omitted from the context, the
agent will generate code that propagates it.

The ACL eliminates this entire class of context requirements. The
agent generates code against the domain model. The ACL handles the
translation. **The domain model is the agent's API, and the ACL is
the mechanism that makes the domain model trustworthy.**

## Implementation

See [`../code-examples/anti-corruption-layer/`](../code-examples/anti-corruption-layer/)
— TypeScript port/adapter example from the Fieldstone CRM Hub showing:

- `CRMPort` interface defined in domain terms
- `HubSpotAdapter` implementing the port with vendor wire-format
  translation
- `InMemoryCRMAdapter` for deterministic agent-generated tests

Agent-generated business logic imports the port, never the adapter.
The adapter is a containment boundary for vendor specificity.

## Pitfalls

- **The ACL that isn't.** Calling a thin wrapper an "ACL" without
  actually translating semantic differences. Field renaming alone is
  not enough — the translation must handle semantic mismatches, dual
  names, and vocabulary differences.
- **The ACL that contains business logic.** The ACL translates; it
  does not decide. Business rules belong inside the hexagon, not
  inside the adapter.
- **The ACL that the agent learns to bypass.** If the agent has the
  vendor SDK in its training data and the ACL is incomplete, the
  agent may import vendor types directly to "fix" a missing
  translation. The fix is to complete the ACL, not to lecture the
  agent.

## Related

- [`hexagonal-architecture.md`](hexagonal-architecture.md) — the
  containing pattern; the ACL is the form a Secondary Adapter takes
  when integrating with a vendor whose model misaligns
- [`../spec-templates/interface-spec.md`](../spec-templates/interface-spec.md)
  — defines the port contract the ACL implements
- [`../code-examples/anti-corruption-layer/`](../code-examples/anti-corruption-layer/)
  — runnable TypeScript example

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
