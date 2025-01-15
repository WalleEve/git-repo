import tkinter as tk
from tkinter import messagebox
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

# Database setup (for demonstration)
def setup_database():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    # Create employee table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emp (
            ename TEXT,
            job TEXT,
            sal REAL,
            hiredate TEXT,
            deptno INTEGER,
            comm REAL
        )
    ''')
    # Insert some sample data
    cursor.execute("INSERT INTO emp VALUES ('John', 'Manager', 5000, '2019-05-21', 10, 200)")
    cursor.execute("INSERT INTO emp VALUES ('Alice', 'Clerk', 2000, '2018-07-14', 20, 150)")
    conn.commit()
    conn.close()

setup_database()

# Function to send email
def send_email(email, code):
    try:
        sender_email = "your-email@gmail.com"
        sender_password = "your-password"
        subject = "Verification Code"
        message = f"Your verification code is {code}"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Tkinter App
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        
        # Username and Password fields
        tk.Label(root, text="Username").grid(row=0, column=0)
        tk.Label(root, text="Password").grid(row=1, column=0)
        self.username_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root, show="*")
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        # Login and Signup buttons
        tk.Button(root, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(root, text="Signup").grid(row=2, column=1)
        
        # Forget Password button
        tk.Button(root, text="Forget Password", command=self.forget_password).grid(row=3, columnspan=2)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Dummy login check
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login successful")
            self.show_employee_details()
        else:
            messagebox.showerror("Login", "Invalid credentials")

    def forget_password(self):
        forget_window = tk.Toplevel(self.root)
        forget_window.title("Forget Password")
        
        tk.Label(forget_window, text="Username").grid(row=0, column=0)
        tk.Label(forget_window, text="Email").grid(row=1, column=0)
        username_entry = tk.Entry(forget_window)
        email_entry = tk.Entry(forget_window)
        username_entry.grid(row=0, column=1)
        email_entry.grid(row=1, column=1)

        verification_code = random.randint(1000, 9999)
        
        def send_verification():
            email = email_entry.get()
            send_email(email, verification_code)
            messagebox.showinfo("Verification", f"Verification code sent to {email}")
            verify_code()

        tk.Button(forget_window, text="Send Code", command=send_verification).grid(row=2, columnspan=2)

        def verify_code():
            verification_window = tk.Toplevel(forget_window)
            verification_window.title("Enter Verification Code")
            
            tk.Label(verification_window, text="Enter Code").grid(row=0, column=0)
            code_entry = tk.Entry(verification_window)
            code_entry.grid(row=0, column=1)

            def check_code():
                entered_code = int(code_entry.get())
                if entered_code == verification_code:
                    messagebox.showinfo("Success", "Code Verified! You can now reset your password.")
                    # Code to reset password here
                else:
                    messagebox.showerror("Error", "Invalid Code")
                    
            tk.Button(verification_window, text="Verify", command=check_code).grid(row=1, columnspan=2)

    def show_employee_details(self):
        # New window to show employee details
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Employee Details")
        
        conn = sqlite3.connect('employees.db')
        cursor = conn.cursor()
        cursor.execute("SELECT ename, job, sal, hiredate, deptno, comm FROM emp WHERE hiredate < '2020-01-01'")
        rows = cursor.fetchall()
        conn.close()

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                tk.Label(employee_window, text=value).grid(row=i, column=j)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
