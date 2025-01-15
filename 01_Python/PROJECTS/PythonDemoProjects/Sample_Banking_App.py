import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Application")

        # Initial balance
        self.balance = 0

        # Labels
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}")
        self.balance_label.grid(row=0, column=1)

        # Deposit section
        tk.Label(root, text="Deposit Amount: ").grid(row=1, column=0)
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.grid(row=1, column=1)
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=1, column=2)

        # Withdraw section
        tk.Label(root, text="Withdraw Amount: ").grid(row=2, column=0)
        self.withdraw_entry = tk.Entry(root)
        self.withdraw_entry.grid(row=2, column=1)
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=2, column=2)

    def deposit(self):
        amount = self.deposit_entry.get()
        if amount.isdigit():
            self.balance += int(amount)
            self.update_balance()
            messagebox.showinfo("Success", f"${amount} deposited successfully!")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid amount")

    def withdraw(self):
        amount = self.withdraw_entry.get()
        if amount.isdigit():
            if self.balance >= int(amount):
                self.balance -= int(amount)
                self.update_balance()
                messagebox.showinfo("Success", f"${amount} withdrawn successfully!")
            else:
                messagebox.showwarning("Insufficient Funds", "You do not have enough balance.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid amount")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
