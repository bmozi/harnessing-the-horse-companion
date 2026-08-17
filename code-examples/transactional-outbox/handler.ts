// handler.ts — Agent-generated webhook handler with Transactional Outbox
//
// Three-step template the agent follows:
//   1. Check idempotency
//   2. Write business state
//   3. Write to outbox
// All in ONE database transaction.
//
// The architecture makes exactly-once semantics the default path.
// The agent does not need to reason about distributed transactions.
//
// Adapted from Chapter 11 of *Harnessing the Horse* by John Briggs.
// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

// Pretend these match your project's actual types and ORM.
export interface HubSpotWebhookEvent {
  eventId: string;
  subscriptionType: string;
  objectId: string;
  propertyName?: string;
  propertyValue?: string;
  occurredAt: number;
}

export interface DomainContact {
  externalId: string;
  email: string;
  firstName: string;
  lastName: string;
  source: string;
}

export interface DatabaseTransaction {
  idempotencyKeys: {
    findUnique(args: { where: { key: string } }): Promise<{ key: string } | null>;
    create(args: { data: { key: string } }): Promise<void>;
  };
  contacts: {
    upsert(args: {
      where: { externalId: string };
      create: DomainContact;
      update: DomainContact;
    }): Promise<DomainContact>;
  };
  outbox: {
    create(args: {
      data: {
        aggregateId: string;
        eventType: string;
        payload: DomainContact;
        topic: string;
      };
    }): Promise<void>;
  };
}

export interface Database {
  transaction<T>(fn: (tx: DatabaseTransaction) => Promise<T>): Promise<T>;
}

export interface ContactWebhookDependencies {
  db: Database;
  transformToDomain(event: HubSpotWebhookEvent): DomainContact;
}

// Dependency injection keeps the pattern runnable and testable without a
// specific ORM. Production code supplies the real database and translation.
export function createContactWebhookHandler({
  db,
  transformToDomain,
}: ContactWebhookDependencies): (event: HubSpotWebhookEvent) => Promise<void> {
  return async function handleContactWebhook(event: HubSpotWebhookEvent): Promise<void> {
    await db.transaction(async (tx) => {
      // 1. Idempotency check
      const exists = await tx.idempotencyKeys.findUnique({ where: { key: event.eventId } });
      if (exists) return;  // Already processed — skip
      await tx.idempotencyKeys.create({ data: { key: event.eventId } });

      // 2. Business logic — transform and persist
      const contact = transformToDomain(event);
      await tx.contacts.upsert({
        where: { externalId: contact.externalId },
        create: contact,
        update: contact,
      });

      // 3. Outbox — notification intent, same transaction
      await tx.outbox.create({
        data: {
          aggregateId: contact.externalId,
          eventType: 'contact.updated',
          payload: contact,
          topic: 'crm-events',
        },
      });
    });
    // Transaction committed — the sender gets a successful response.
    // A separate outbox publisher delivers asynchronously.
  };
}
