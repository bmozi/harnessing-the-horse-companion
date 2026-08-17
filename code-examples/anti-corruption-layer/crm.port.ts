// ports/crm.port.ts — the contract agents code against
//
// Defines the CRM port in DOMAIN terms. Agent-generated business
// logic imports this port, never the adapter. The adapter
// translates to vendor wire-format at the boundary.
//
// Adapted from Chapter 11 of *Harnessing the Horse: Engineering
// Discipline for Agentic Development* by John Briggs.
// © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

export interface CRMPort {
  createContact(contact: DomainContact): Promise<ContactResult>;
  findContact(criteria: ContactQuery): Promise<DomainContact | null>;
  updateContact(id: string, patch: Partial<DomainContact>): Promise<ContactResult>;
}

export interface DomainContact {
  firstName: string;
  lastName: string;
  email: string;
  phone?: string;
  source: 'web' | 'phone' | 'referral';
}

export interface ContactQuery {
  email?: string;
  externalId?: string;
}

export interface ContactResult {
  id: string;
  success: boolean;
  error?: string;
}
