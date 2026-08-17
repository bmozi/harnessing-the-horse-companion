// Compatibility path for the book's `examples/hexagonal-crm-port.ts`.
// Canonical source: ../code-examples/anti-corruption-layer/crm.port.ts

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

