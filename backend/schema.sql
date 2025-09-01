CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    education TEXT,
    skills JSON,
    projects JSON,
    work JSON,
    links JSON
);
-- Indexes
CREATE INDEX idx_name ON profiles (name);
CREATE INDEX idx_email ON profiles (email);