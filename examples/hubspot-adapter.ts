// Compatibility path for the book's `examples/hubspot-adapter.ts`.
// Canonical source: ../code-examples/anti-corruption-layer/hubspot.adapter.ts

import type { CRMPort, DomainContact, ContactQuery, ContactResult } from './hexagonal-crm-port';

interface HttpClient {
  post(path: string, body: unknown): Promise<{ id: string }>;
  get(path: string): Promise<unknown>;
  patch(path: string, body: unknown): Promise<unknown>;
}

export class HubSpotAdapter implements CRMPort {
  constructor(private client: HttpClient) {}

  async createContact(contact: DomainContact): Promise<ContactResult> {
    const hubspotPayload = {
      properties: {
        firstname: contact.firstName,
        lastname: contact.lastName,
        email: contact.email,
        phone: contact.phone ?? '',
        lead_source: contact.source,
      },
    };
    const response = await this.client.post('/crm/v3/objects/contacts', hubspotPayload);
    return { id: response.id, success: true };
  }

  async findContact(criteria: ContactQuery): Promise<DomainContact | null> {
    if (!criteria.email) return null;
    const result = await this.client.get(`/crm/v3/objects/contacts/search?email=${encodeURIComponent(criteria.email)}`);
    if (!result) return null;
    return this.toDomain(result);
  }

  async updateContact(id: string, patch: Partial<DomainContact>): Promise<ContactResult> {
    const hubspotPatch = this.translatePatch(patch);
    await this.client.patch(`/crm/v3/objects/contacts/${id}`, { properties: hubspotPatch });
    return { id, success: true };
  }

  private toDomain(hubspotContact: unknown): DomainContact {
    const props = (hubspotContact as { properties: Record<string, string> }).properties;
    return {
      firstName: props.firstname,
      lastName: props.lastname,
      email: props.email,
      phone: props.phone || undefined,
      source: (props.lead_source as DomainContact['source']) ?? 'web',
    };
  }

  private translatePatch(patch: Partial<DomainContact>): Record<string, string> {
    const out: Record<string, string> = {};
    if (patch.firstName !== undefined) out.firstname = patch.firstName;
    if (patch.lastName !== undefined) out.lastname = patch.lastName;
    if (patch.email !== undefined) out.email = patch.email;
    if (patch.phone !== undefined) out.phone = patch.phone;
    if (patch.source !== undefined) out.lead_source = patch.source;
    return out;
  }
}

