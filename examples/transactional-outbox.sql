-- Compatibility path for the book's `examples/transactional-outbox.sql`.
-- Canonical source: ../code-examples/transactional-outbox/schema.sql

CREATE TABLE outbox (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregate_id  TEXT NOT NULL,
  event_type    TEXT NOT NULL,
  payload       JSONB NOT NULL,
  topic         TEXT NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT now(),
  published_at  TIMESTAMPTZ NULL
);

CREATE INDEX outbox_unpublished_idx ON outbox (created_at)
  WHERE published_at IS NULL;

CREATE TABLE idempotency_keys (
  key           TEXT PRIMARY KEY,
  created_at    TIMESTAMPTZ DEFAULT now()
);

