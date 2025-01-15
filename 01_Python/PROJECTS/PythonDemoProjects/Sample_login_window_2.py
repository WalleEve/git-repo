import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("350x200")

        # Connect to SQLite Database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Username Label and Entry
        tk.Label(root, text="Username: ").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password Label and Entry
        tk.Label(root, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, pady=10)

        # Register Button
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.grid(row=3, column=1, pady=10)

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                username TEXT PRIMARY KEY,
                                password TEXT)''')
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = self.cursor.fetchone()

        if user:
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return

        hashed_password = self.hash_password(password)

        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            messagebox.showinfo("Registration Successful", "You have been registered successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different one.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
