// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

import assert from 'node:assert/strict';
import test from 'node:test';

import {
  createContactWebhookHandler,
  type Database,
  type DatabaseTransaction,
  type DomainContact,
  type HubSpotWebhookEvent,
} from './handler';

function createMemoryDatabase() {
  const idempotency = new Set<string>();
  const contacts = new Map<string, DomainContact>();
  const outbox: Array<{ aggregateId: string; eventType: string; payload: DomainContact; topic: string }> = [];

  const tx: DatabaseTransaction = {
    idempotencyKeys: {
      async findUnique({ where }) {
        return idempotency.has(where.key) ? { key: where.key } : null;
      },
      async create({ data }) {
        idempotency.add(data.key);
      },
    },
    contacts: {
      async upsert({ where, create, update }) {
        const value = contacts.has(where.externalId) ? update : create;
        contacts.set(where.externalId, value);
        return value;
      },
    },
    outbox: {
      async create({ data }) {
        outbox.push(data);
      },
    },
  };

  const db: Database = {
    async transaction(fn) {
      return fn(tx);
    },
  };

  return { db, idempotency, contacts, outbox };
}

const event: HubSpotWebhookEvent = {
  eventId: 'evt-1',
  subscriptionType: 'contact.updated',
  objectId: 'contact-1',
  occurredAt: 1_700_000_000,
};

function transformToDomain(input: HubSpotWebhookEvent): DomainContact {
  return {
    externalId: input.objectId,
    email: 'reader@example.com',
    firstName: 'Example',
    lastName: 'Reader',
    source: 'webhook',
  };
}

test('business state and notification intent are written in one transaction', async () => {
  const memory = createMemoryDatabase();
  const handle = createContactWebhookHandler({ db: memory.db, transformToDomain });

  await handle(event);

  assert.equal(memory.contacts.size, 1);
  assert.equal(memory.outbox.length, 1);
  assert.equal(memory.outbox[0]?.aggregateId, 'contact-1');
  assert.equal(memory.idempotency.has('evt-1'), true);
});

test('a repeated webhook is idempotent', async () => {
  const memory = createMemoryDatabase();
  const handle = createContactWebhookHandler({ db: memory.db, transformToDomain });

  await handle(event);
  await handle(event);

  assert.equal(memory.contacts.size, 1);
  assert.equal(memory.outbox.length, 1);
});
