// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

import assert from 'node:assert/strict';
import test from 'node:test';

import { InMemoryCRMAdapter } from './test.adapter';

test('the in-memory adapter honors the domain port without vendor types', async () => {
  const crm = new InMemoryCRMAdapter();
  const created = await crm.createContact({
    firstName: 'Jane',
    lastName: 'Smith',
    email: 'jane@example.com',
    source: 'referral',
  });

  assert.equal(created.success, true);
  assert.equal(crm.size(), 1);
  assert.deepEqual(await crm.findContact({ email: 'jane@example.com' }), {
    firstName: 'Jane',
    lastName: 'Smith',
    email: 'jane@example.com',
    source: 'referral',
  });

  const updated = await crm.updateContact(created.id, {
    email: 'jane.smith@example.com',
  });
  assert.equal(updated.success, true);
  assert.equal(await crm.findContact({ email: 'jane@example.com' }), null);
  assert.equal(
    (await crm.findContact({ email: 'jane.smith@example.com' }))?.firstName,
    'Jane',
  );
});
