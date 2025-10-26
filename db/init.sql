-- db/init.sql
CREATE TABLE IF NOT EXISTS customers (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
email TEXT UNIQUE,
created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_customers_created_at ON customers (created_at);
CREATE INDEX IF NOT EXISTS idx_customers_name ON customers (name);
