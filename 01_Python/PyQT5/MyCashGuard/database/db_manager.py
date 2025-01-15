### database/db_manager.py
# Module to handle database operations

import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with open("D:\\Code\\git-repo\\01_Python\\PyQT5\\MyCashGuard\\database\\schema.sql", "r") as f:  #D:\Code\git-repo\01_Python\PyQT5\MyCashGuard\database\schema.sql
            self.connection.executescript(f.read())

    def add_expense(self, date, description, amount, payment_option):
        query = "INSERT INTO expenses (date, description, amount, payment_option) VALUES (?, ?, ?, ?)"
        self.connection.execute(query, (date, description, amount, payment_option))
        self.connection.commit()

    def get_expenses(self):
        query = "SELECT date, description, amount, payment_option FROM expenses"
        cursor = self.connection.execute(query)
        return [{"date": row[0], "description": row[1], "amount": row[2], "payment_option": row[3]} for row in cursor]
        
    def add_savings(self, date, description, target_amount, current_amount):
        query = "INSERT INTO savings (date, description, target_amount, current_amount) VALUES (?, ?, ?, ?)"
        self.connection.execute(query, (date, description, target_amount, current_amount))
        self.connection.commit()

    def get_savings(self):
        query = "SELECT date, description, target_amount, current_amount FROM savings"
        cursor = self.connection.execute(query)
        return [
            {
                "date": row[0],
                "description": row[1],
                "target": row[2],
                "current": row[3],
            }
            for row in cursor
        ]