-- schema.sql — Transactional Outbox table (PostgreSQL)
--
-- The outbox table is written in the SAME database transaction as
-- the business state. A separate publisher process reads the
-- outbox and delivers to the message bus. This means an
-- agent-generated handler does not need to reason about
-- distributed transactions or dual-write failure modes.
--
-- Adapted from Chapter 11 of *Harnessing the Horse: Engineering
-- Discipline for Agentic Development* by John Briggs.
-- © 2026 John Briggs — MIT licensed (see ../../LICENSE-CODE)

CREATE TABLE outbox (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregate_id  TEXT NOT NULL,             -- e.g., contact ID
  event_type    TEXT NOT NULL,             -- e.g., 'contact.created'
  payload       JSONB NOT NULL,            -- the event body
  topic         TEXT NOT NULL,             -- target: 'crm-events', 'billing-events'
  created_at    TIMESTAMPTZ DEFAULT now(),
  published_at  TIMESTAMPTZ NULL           -- NULL until the publisher delivers it
);

-- Index for the publisher to find unpublished rows efficiently.
CREATE INDEX outbox_unpublished_idx ON outbox (created_at)
  WHERE published_at IS NULL;

-- Idempotency keys table — companion to the outbox for inbound
-- webhook deduplication.
CREATE TABLE idempotency_keys (
  key           TEXT PRIMARY KEY,
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- Retention: published rows can be archived/deleted after N days.
-- Configure via your scheduler:
--   DELETE FROM outbox WHERE published_at IS NOT NULL
--     AND published_at < now() - INTERVAL '30 days';
