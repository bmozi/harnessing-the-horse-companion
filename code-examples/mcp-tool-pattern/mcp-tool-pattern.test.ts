// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

import assert from 'node:assert/strict';
import test from 'node:test';

import {
  createScheduleAppointmentTool,
  type MCPContext,
  type ScheduleAppointmentDependencies,
  type ScheduleInput,
} from './schedule-appointment';

function createHarness() {
  const created: ScheduleInput[] = [];
  const audits: Array<{ event: string; details: object }> = [];
  const dependencies: ScheduleAppointmentDependencies = {
    async lookupCustomer() {
      return { name: 'Example Reader' };
    },
    async checkAvailability() {
      return { open: true, nextOpen: [] };
    },
    async createAppointment(input) {
      created.push(input);
      return { id: 'appt-1' };
    },
    async auditLog(event, details) {
      audits.push({ event, details });
    },
  };
  const context: MCPContext = {
    agentId: 'agent-example',
    requireScope(scope) {
      assert.equal(scope, 'appointments:write');
    },
  };
  return { tool: createScheduleAppointmentTool(dependencies), context, created, audits };
}

const input: ScheduleInput = {
  customerId: 'customer-1',
  serviceType: 'quarterly',
  preferredDate: '2026-09-01',
  timeWindow: 'morning',
};

test('write tools default to a non-mutating preview', async () => {
  const harness = createHarness();
  const result = await harness.tool.handler(input, harness.context);

  assert.equal('dryRun' in result && result.dryRun, true);
  assert.equal(harness.created.length, 0);
  assert.equal(harness.audits.length, 0);
});

test('explicit confirmation executes and leaves an audit record', async () => {
  const harness = createHarness();
  const result = await harness.tool.handler({ ...input, confirm: true }, harness.context);

  assert.deepEqual(result, { created: true, appointmentId: 'appt-1' });
  assert.equal(harness.created.length, 1);
  assert.equal(harness.audits[0]?.event, 'appointment.created');
});
