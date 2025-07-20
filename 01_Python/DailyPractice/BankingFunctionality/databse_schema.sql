-- accounts table
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    balance REAL DEFAULT 0,
    type TEXT CHECK(type IN ('savings', 'loan', 'fd')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- transactions table
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    type TEXT CHECK(type IN ('credit', 'debit', 'interest')),
    amount REAL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(account_id) REFERENCES accounts(account_id)
);

-- admin table (optional)
CREATE TABLE admin (
    username TEXT PRIMARY KEY,
    password TEXT
);
