// adapters/hubspot.adapter.ts — vendor-specific translation
//
// Implements CRMPort by translating between the DOMAIN model
// (DomainContact in domain terms) and HubSpot wire-format. This
// adapter is where vendor specificity is CONTAINED. The hexagon
// (business logic) never sees HubSpot field names, typos, or
// quirks.
//
// Adapted from Chapter 11 of *Harnessing the Horse* by John Briggs.
// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

import type { CRMPort, DomainContact, ContactQuery, ContactResult } from './crm.port';

// Pretend this is whatever HTTP client your project uses.
interface HttpClient {
  post(path: string, body: unknown): Promise<{ id: string }>;
  get(path: string): Promise<unknown>;
  patch(path: string, body: unknown): Promise<unknown>;
}

export class HubSpotAdapter implements CRMPort {
  constructor(private client: HttpClient) {}

  async createContact(contact: DomainContact): Promise<ContactResult> {
    // Translate domain model to HubSpot wire-format.
    // HubSpot lowercases field names and uses custom property names
    // like `lead_source` that differ from the domain vocabulary.
    const hubspotPayload = {
      properties: {
        firstname: contact.firstName,     // HubSpot uses lowercase
        lastname: contact.lastName,
        email: contact.email,
        phone: contact.phone ?? '',
        lead_source: contact.source,      // HubSpot custom property
      },
    };
    const response = await this.client.post('/crm/v3/objects/contacts', hubspotPayload);
    return { id: response.id, success: true };
  }

  async findContact(criteria: ContactQuery): Promise<DomainContact | null> {
    // Translate query criteria into HubSpot search format.
    // Returns DOMAIN type, not HubSpot type.
    if (criteria.email) {
      const result = await this.client.get(`/crm/v3/objects/contacts/search?email=${encodeURIComponent(criteria.email)}`);
      if (!result) return null;
      return this.toDomain(result);
    }
    return null;
  }

  async updateContact(id: string, patch: Partial<DomainContact>): Promise<ContactResult> {
    const hubspotPatch = this.translatePatch(patch);
    await this.client.patch(`/crm/v3/objects/contacts/${id}`, { properties: hubspotPatch });
    return { id, success: true };
  }

  private toDomain(hubspotContact: unknown): DomainContact {
    // Convert HubSpot's payload shape into a DomainContact.
    // This is where naming corruption (e.g., intengration_id),
    // dual-naming (fieldstone_customer_id vs fieldstoneos_customer_id),
    // and semantic mismatches (lifecycle stage vocabulary) are
    // resolved.
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
