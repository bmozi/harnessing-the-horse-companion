// adapters/test.adapter.ts — in-memory adapter for agent-generated tests
//
// Deterministic, no network calls, no vendor dependency. Lets
// agent-generated business logic be testable in isolation against
// the CRMPort contract.
//
// Adapted from Chapter 11 of *Harnessing the Horse* by John Briggs.
// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

import type { CRMPort, DomainContact, ContactQuery, ContactResult } from './crm.port';

export class InMemoryCRMAdapter implements CRMPort {
  private contacts: Map<string, DomainContact> = new Map();
  private byEmail: Map<string, string> = new Map();

  async createContact(contact: DomainContact): Promise<ContactResult> {
    const id = crypto.randomUUID();
    this.contacts.set(id, contact);
    this.byEmail.set(contact.email, id);
    return { id, success: true };
  }

  async findContact(criteria: ContactQuery): Promise<DomainContact | null> {
    if (criteria.email) {
      const id = this.byEmail.get(criteria.email);
      if (!id) return null;
      return this.contacts.get(id) ?? null;
    }
    if (criteria.externalId) {
      return this.contacts.get(criteria.externalId) ?? null;
    }
    return null;
  }

  async updateContact(id: string, patch: Partial<DomainContact>): Promise<ContactResult> {
    const existing = this.contacts.get(id);
    if (!existing) return { id, success: false, error: 'not_found' };
    this.contacts.set(id, { ...existing, ...patch });
    if (patch.email && patch.email !== existing.email) {
      this.byEmail.delete(existing.email);
      this.byEmail.set(patch.email, id);
    }
    return { id, success: true };
  }

  // Test helpers — not part of CRMPort.
  reset(): void {
    this.contacts.clear();
    this.byEmail.clear();
  }

  size(): number {
    return this.contacts.size;
  }
}
