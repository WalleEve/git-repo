class BankAccount:
    def __init__(self, account_id, name, email, balance=0):
        self.account_id = account_id
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        # Logic to update DB and self.balance
        pass

    def withdraw(self, amount):
        # Logic to update DB and self.balance
        pass

    def get_balance(self):
        # Fetch from DB
        pass

    def get_transaction_history(self):
        # Return list of transactions
        pass
