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

        # Create container for frames
        self.container = tk.Frame(self.root)
        self.container.place(x=0, y=0, width=500, height=600)

        # Frames for different sections
        self.sales_frame = self.create_sales_frame()
        self.stock_frame = self.create_stock_frame()
        self.report_frame = self.create_report_frame()
        self.admin_menu_frame, self.admin_content_frame = self.create_admin_frames()

        # Show the default frame (Sales)
        self.show_sales_frame()

    def hide_all_frames(self):
        """Hide all frames."""
        self.sales_frame.place_forget()
        self.stock_frame.place_forget()
        self.report_frame.place_forget()
        self.admin_menu_frame.place_forget()
        self.admin_content_frame.place_forget()

    def show_sales_frame(self):
        self.hide_all_frames()
        self.sales_frame.place(x=0, y=0, width=500, height=600)

    def show_stock_frame(self):
        self.hide_all_frames()
        self.stock_frame.place(x=0, y=0, width=500, height=600)

    def show_report_frame(self):
        self.hide_all_frames()
        self.report_frame.place(x=0, y=0, width=500, height=600)

    def show_admin_frame(self):
        self.hide_all_frames()
        self.admin_menu_frame.place(x=0, y=0, width=150, height=600)
        self.admin_content_frame.place(x=150, y=0, width=350, height=600)
        self.show_admin_option("Sales Report")  # Default view

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
        header = tk.Frame(frame, bg="#4682B4", height=60, width=500)  # Darker blue header
        header.place(x=0, y=0)
        tk.Label(header, text="Sales Section", font=("Arial", 24), bg="#4682B4", fg="white").place(x=150, y=10)
        content_frame = tk.Frame(frame, bg="#ADD8E6")
        content_frame.place(x=0, y=60, width=500, height=540)
        # Add your sales widgets here in content_frame
        return frame

    def create_stock_frame(self):
        frame = tk.Frame(self.root, bg="#90EE90")  # Light Green Background
        header = tk.Frame(frame, bg="#3CB371", height=60, width=500)  # Darker green header
        header.place(x=0, y=0)
        tk.Label(header, text="Stock Section", font=("Arial", 24), bg="#3CB371", fg="white").place(x=150, y=10)
        content_frame = tk.Frame(frame, bg="#90EE90")
        content_frame.place(x=0, y=60, width=500, height=540)
        # Add your stock widgets here in content_frame
        return frame

    def create_report_frame(self):
        frame = tk.Frame(self.root, bg="#FFD700")  # Gold Background
        header = tk.Frame(frame, bg="#FFA500", height=60, width=500)  # Darker gold header
        header.place(x=0, y=0)
        tk.Label(header, text="Report Section", font=("Arial", 24), bg="#FFA500", fg="white").place(x=150, y=10)
        content_frame = tk.Frame(frame, bg="#FFD700")
        content_frame.place(x=0, y=60, width=500, height=540)
        # Add your report widgets here in content_frame
        return frame

    def create_admin_frames(self):
        menu_frame = tk.Frame(self.root, bg="#F0E68C", width=150)  # Light Yellow Background for Menu
        content_frame = tk.Frame(self.root, bg="#FAFAD2")  # Light goldenrod for Content

        # Create admin menu options on the left
        admin_options = [
            ("Sales Report", lambda: self.show_admin_option("Sales Report")),
            ("Stock Report", lambda: self.show_admin_option("Stock Report")),
            ("User Management", lambda: self.show_admin_option("User Management")),
            ("Stock Entry & Update", lambda: self.show_admin_option("Stock Entry & Update")),
            ("Password Management", lambda: self.show_admin_option("Password Management"))
        ]

        for i, (text, command) in enumerate(admin_options):
            tk.Button(menu_frame, text=text, font=("Arial", 12), width=20, command=command).place(x=10, y=20 + i * 40)

        return menu_frame, content_frame

    def show_admin_option(self, option):
        """Display the selected admin option in the content frame."""
        for widget in self.admin_content_frame.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.admin_content_frame, bg="#CD5C5C", height=60)  # Light Red header for Admin
        header_frame.place(x=0, y=0, width=350)
        tk.Label(header_frame, text=option, font=("Arial", 18), bg="#CD5C5C", fg="white").place(x=70, y=10)

        content_frame = tk.Frame(self.admin_content_frame, bg="#FFE4E1")  # Misty rose background for content
        content_frame.place(x=0, y=60, width=350, height=540)

        # Placeholder content for now
        tk.Label(content_frame, text=f"Content for {option}", font=("Arial", 14), bg="#FFE4E1").place(x=70, y=50)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
