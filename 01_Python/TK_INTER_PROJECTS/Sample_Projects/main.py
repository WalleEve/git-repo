import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Kirana Store Management")

        # Create Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Add menu items
        menubar.add_command(label="SALES", command=self.show_sales_frame)
        menubar.add_command(label="STOCK", command=self.show_stock_frame)
        menubar.add_command(label="REPORT", command=self.show_report_frame)
        menubar.add_command(label="ADMIN", command=self.admin_login)

        # Frames for different sections with colors and size matching the window
        self.sales_frame = self.create_sales_frame()
        self.stock_frame = self.create_stock_frame()
        self.report_frame = self.create_report_frame()
        self.admin_frame = self.create_admin_frame()

        # Show the default frame (Sales)
        self.show_sales_frame()

    def hide_all_frames(self):
        """Hide all frames."""
        self.sales_frame.pack_forget()
        self.stock_frame.pack_forget()
        self.report_frame.pack_forget()
        self.admin_frame.pack_forget()

    def show_sales_frame(self):
        self.hide_all_frames()
        self.sales_frame.pack(fill="both", expand=1)

    def show_stock_frame(self):
        self.hide_all_frames()
        self.stock_frame.pack(fill="both", expand=1)

    def show_report_frame(self):
        self.hide_all_frames()
        self.report_frame.pack(fill="both", expand=1)

    def show_admin_frame(self):
        self.hide_all_frames()
        self.admin_frame.pack(fill="both", expand=1)

    def admin_login(self):
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Admin Login")
        self.login_window.geometry("300x150")

        tk.Label(self.login_window, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_window, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_window, text="Login", command=self.check_admin_login).grid(row=2, column=0, columnspan=2)

    def check_admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy credentials
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login", "Admin login successful!")
            self.login_window.destroy()
            self.show_admin_frame()
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

    # Creating Frames for each section

    def create_sales_frame(self):
        frame = tk.Frame(self.root, bg="#ADD8E6")  # Light Blue Background
        tk.Label(frame, text="Sales Section", font=("Arial", 24), bg="#ADD8E6").pack(pady=20)
        return frame

    def create_stock_frame(self):
        frame = tk.Frame(self.root, bg="#90EE90")  # Light Green Background
        tk.Label(frame, text="Stock Section", font=("Arial", 24), bg="#90EE90").pack(pady=20)
        return frame

    def create_report_frame(self):
        frame = tk.Frame(self.root, bg="#FFD700")  # Gold Background
        tk.Label(frame, text="Report Section", font=("Arial", 24), bg="#FFD700").pack(pady=20)
        return frame

    def create_admin_frame(self):
        frame = tk.Frame(self.root, bg="#FFB6C1")  # Light Pink Background
        tk.Label(frame, text="Admin Section", font=("Arial", 24), bg="#FFB6C1").pack(pady=20)

        # Admin options
        admin_options = [
            "Sales Report",
            "Stock Report",
            "User Management",
            "Stock Entry & Update",
            "Password Management"
        ]

        for option in admin_options:
            tk.Button(frame, text=option, font=("Arial", 16), width=30).pack(pady=10)

        return frame

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
