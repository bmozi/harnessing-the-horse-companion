// tools/schedule-appointment.ts — MCP tool definition
//
// Demonstrates the three-layer pattern for any MCP tool that
// modifies state:
//   1. Scope check
//   2. Validate
//   3. Dry-run gate (default behavior is a dry run)
//
// Maps to the Harness disciplines: scope check (Scope), validation
// (Prove), dry-run default (Enforce), audit log (Communicate).
//
// Adapted from Chapter 13 of *Harnessing the Horse* by John Briggs.
// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

// MCP type sketches — adapt to your actual MCP server's types.
export interface MCPToolDefinition {
  name: string;
  description: string;
  inputSchema: unknown;
  handler(input: ScheduleInput, context: MCPContext): Promise<ScheduleResponse>;
}

export interface MCPContext {
  agentId: string;
  requireScope(scope: string): void;   // throws if scope not granted
}

export interface ScheduleInput {
  customerId: string;
  serviceType: 'initial' | 'quarterly' | 'callback';
  preferredDate: string;
  timeWindow: 'morning' | 'afternoon';
  confirm?: boolean;
}

export type ScheduleResponse =
  | { dryRun: true; wouldCreate: AppointmentPreview; confirmRequired: true }
  | { created: true; appointmentId: string }
  | { error: 'no_availability'; alternatives: { date: string; window: string }[] };

export interface AppointmentPreview {
  appointment: { customer: string; date: string; window: string; service: string };
  estimatedDuration: string;
  technicianAssignment: string;
}

export interface ScheduleAppointmentDependencies {
  lookupCustomer(id: string): Promise<{ name: string }>;
  checkAvailability(
    date: string,
    window: string,
  ): Promise<{ open: boolean; nextOpen: { date: string; window: string }[] }>;
  createAppointment(input: ScheduleInput): Promise<{ id: string }>;
  auditLog(event: string, details: object): Promise<void>;
}

export function createScheduleAppointmentTool(
  dependencies: ScheduleAppointmentDependencies,
): MCPToolDefinition {
  const { lookupCustomer, checkAvailability, createAppointment, auditLog } = dependencies;

  return {
    name: 'schedule_service_appointment',
    description: 'Schedule an example service appointment for a customer.',
    inputSchema: {
      type: 'object',
      properties: {
        customerId: { type: 'string', description: 'Example service customer ID' },
        serviceType: { type: 'string', enum: ['initial', 'quarterly', 'callback'] },
        preferredDate: { type: 'string', format: 'date' },
        timeWindow: { type: 'string', enum: ['morning', 'afternoon'] },
        confirm: {
          type: 'boolean',
          default: false,
          description: 'Set true to execute. Default: dry-run preview.',
        },
      },
      required: ['customerId', 'serviceType', 'preferredDate', 'timeWindow'],
    },

    async handler(input, context) {
      // 1. Scope check — reject if token lacks scheduling permission
      context.requireScope('appointments:write');

      // 2. Validate — check customer exists, date is available
      const customer = await lookupCustomer(input.customerId);
      const availability = await checkAvailability(input.preferredDate, input.timeWindow);
      if (!availability.open) {
        return { error: 'no_availability', alternatives: availability.nextOpen };
      }

      // 3. Dry-run default — return what WOULD happen without executing
      if (!input.confirm) {
        return {
          dryRun: true,
          wouldCreate: {
            appointment: {
              customer: customer.name,
              date: input.preferredDate,
              window: input.timeWindow,
              service: input.serviceType,
            },
            estimatedDuration: '45 minutes',
            technicianAssignment: 'auto (route-optimized)',
          },
          confirmRequired: true,
        };
      }

      // 4. Execute — only reached when confirm: true
      const appointment = await createAppointment(input);
      await auditLog('appointment.created', { by: context.agentId, ...appointment });
      return { created: true, appointmentId: appointment.id };
    },
  };
}
