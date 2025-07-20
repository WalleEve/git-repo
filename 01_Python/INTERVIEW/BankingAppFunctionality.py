# Project Structure (Modular Design)

# Core Classes:

#     Account (Base class)

#     SavingsAccount, LoanAccount, FDAccount (inherit from Account)

#     Transaction (for tracking CR/DR/history)

#     Admin (for viewing reports, analytics)

# Database Tables:

#     accounts (id, name, type, balance, created_at)

#     transactions (id, account_id, type, amount, timestamp, remarks)

#     loans (id, account_id, principal, interest, due_date)

#     fds (id, account_id, amount, rate, duration, start_date)


#  Core Technologies

#     Language: Python 3

#     Database: SQLite (via sqlite3 module)

#     Concepts: Object-Oriented Programming (OOP), Inheritance, Encapsulation, CRUD operations