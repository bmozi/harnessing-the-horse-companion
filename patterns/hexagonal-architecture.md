# Hexagonal Architecture (Ports and Adapters)

> **Chapter:** ch11 — Integration Patterns (Section 11.2)
> **Last revised:** 2026-06-16

## Origin

Alistair Cockburn, "Hexagonal Architecture" (Portland Pattern
Repository wiki, 2005; book-length treatment with Juan Manuel
Garrido de Paz, 2024). Also called **Ports and Adapters**.

Referenced in AWS prescriptive guidance and at
hexagonalarchitecture.org.

## Intent

Allow an application to be **equally driven by users, programs,
automated tests, or batch scripts**, and to be developed and tested
in isolation from its eventual runtime devices and databases.

- The **hexagon** is the application core — the business logic.
- A **port** is an entry or exit point defined in the application's
  own terms.
- An **adapter** is an implementation of a port for a specific
  external technology.
- **Primary adapters** drive the application (a REST controller
  invoking a port).
- **Secondary adapters** are driven by the application (a database
  client implementing a persistence port).

## Application in Agentic Development

Hexagonal Architecture provides a structural answer to two problems
that plague AI-generated integrations.

### The vendor swap problem

Agent-generated code that depends directly on a vendor's API creates
a coupling that resists migration. If the code references HubSpot's
`crm/v3/objects/contacts` endpoint throughout the business logic,
swapping to Salesforce requires rewriting the business logic — not
because the logic changed, but because the dependency was baked in.

Hexagonal Architecture solves this by defining the port in the
application's terms. The port says "create a contact with these
properties." The HubSpot adapter translates that to
`POST /crm/v3/objects/contacts`. A Salesforce adapter translates it
to a different API. **The hexagon does not change.**

This is the load-bearing design choice in the Fieldstone CRM Hub: the
CRM port is named generically (`CRMPort`, not `HubSpotPort`), defined
by what the Hub needs, not by what HubSpot offers.

### The testability problem

Agent-generated code must be testable in isolation. If the generated
code calls HubSpot's API directly, unit tests require either mocking
the entire HTTP layer (fragile) or running against HubSpot's sandbox
(slow, rate-limited, non-deterministic).

With hexagonal architecture, the generated code calls the port. The
unit test provides a test adapter — an in-memory implementation that
returns predictable responses. The agent can generate both the
implementation and the tests against the port, and both will work
without requiring access to the external system.

## The Four Adapter Categories

In a hexagonal system that AI agents both produce code for and
consume as a tool, four categories of adapters emerge:

1. **Human-facing primary adapters** — REST APIs, web UIs, CLI tools.
   Entry points for human users. Well-understood.
2. **Agent-facing primary adapters** — MCP servers, tool APIs,
   structured prompt interfaces. Entry points for AI agents acting
   as consumers. Strongly typed, well-documented, explicit error
   contracts. See Chapter 13 for design discipline.
3. **System-facing secondary adapters** — Database clients, message
   bus publishers, external API clients. Implement the ports the
   application uses to interact with infrastructure.
4. **Vendor-facing secondary adapters** — The ACL-implementing
   adapters (see [`anti-corruption-layer.md`](anti-corruption-layer.md))
   that translate between the domain model and vendor-specific APIs.

## The Discipline

**Agent-generated code targets ports, never adapters.**

- An agent generating business logic should not know whether the
  persistence layer is PostgreSQL or DynamoDB.
- An agent generating a workflow should not know whether the message
  bus is Azure Service Bus or Apache Kafka.

The port defines the contract. The adapter implements the contract
for a specific technology. **This separation means agent-generated
business logic survives infrastructure changes without
modification.**

## Implementation

See [`../code-examples/anti-corruption-layer/`](../code-examples/anti-corruption-layer/)
— the worked example combines Hexagonal Architecture and the
Anti-Corruption Layer pattern. The `CRMPort` interface is the
hexagonal port; the `HubSpotAdapter` is the ACL-implementing
secondary adapter; the `InMemoryCRMAdapter` is the test adapter that
makes the generated business logic testable in isolation.

## Pitfalls

- **The leaky port.** A port that exposes vendor-specific types in
  its interface defeats the purpose. If `CRMPort.createContact`
  returns a `HubSpotContact`, the hexagon is coupled to HubSpot.
  Use domain types only.
- **The port that has no adapter.** A port without a working
  implementation is a port that doesn't actually verify the
  abstraction works. Always implement at least the InMemory test
  adapter as you define the port.
- **The "we'll add a port later" fallacy.** Once business logic
  imports a vendor SDK directly, every future agent session has the
  vendor SDK in its training context and will reproduce the
  coupling. The port must exist from the first commit that touches
  the vendor.
- **The adapter that grows business logic.** Adapters translate.
  When an adapter starts making business decisions ("if the contact
  exists, update it; otherwise create it"), the logic has migrated
  out of the hexagon. Move it back.

## Related

- [`anti-corruption-layer.md`](anti-corruption-layer.md) — the most
  common form a vendor-facing secondary adapter takes
- [`../spec-templates/interface-spec.md`](../spec-templates/interface-spec.md)
  — the template for defining the port contract
- [`../code-examples/anti-corruption-layer/`](../code-examples/anti-corruption-layer/)
  — runnable example

© 2026 John Briggs. Licensed under CC BY-NC-SA 4.0 (see LICENSE-CONTENT). Commercial use requires separate written permission.
