from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('bank.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database tables
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        balance REAL DEFAULT 0,
        type TEXT CHECK(type IN ('savings', 'loan', 'fd')),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER,
        type TEXT CHECK(type IN ('credit', 'debit', 'interest')),
        amount REAL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(account_id) REFERENCES accounts(account_id)
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
        username TEXT PRIMARY KEY,
        password TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/account', methods=['POST'])
def create_account():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, email, type) VALUES (?, ?, ?)",
                   (data['name'], data['email'], data['type']))
    conn.commit()
    account_id = cursor.lastrowid
    conn.close()
    return jsonify({'message': 'Account created', 'account_id': account_id})

@app.route('/account/<int:account_id>', methods=['GET'])
def get_account(account_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_id=?", (account_id,))
    account = cursor.fetchone()
    cursor.execute("SELECT * FROM transactions WHERE account_id=?", (account_id,))
    transactions = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if account:
        return jsonify(dict(account, transactions=transactions))
    return jsonify({'error': 'Account not found'}), 404

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
                   (data['amount'], data['account_id']))
    cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, 'credit', ?)",
                   (data['account_id'], data['amount']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deposit successful'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (data['account_id'],))
    balance = cursor.fetchone()[0]
    if balance < data['amount']:
        return jsonify({'error': 'Insufficient balance'}), 400
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?",
                   (data['amount'], data['account_id']))
    cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, 'debit', ?)",
                   (data['account_id'], data['amount']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Withdrawal successful'})

@app.route('/apply-interest/<int:account_id>', methods=['POST'])
def apply_interest(account_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = ? AND type = 'savings'", (account_id,))
    row = cursor.fetchone()
    if not row:
        return jsonify({'error': 'Savings account not found'}), 404
    interest = row['balance'] * 0.03  # 3% annually
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
                   (interest, account_id))
    cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, 'interest', ?)",
                   (account_id, interest))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Interest applied', 'amount': interest})

@app.route('/admin/accounts', methods=['GET'])
def admin_view_accounts():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(accounts)

if __name__ == '__main__':
    app.run(debug=True)
