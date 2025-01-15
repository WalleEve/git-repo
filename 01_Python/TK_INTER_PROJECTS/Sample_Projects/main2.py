import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")  # Start with a window size
        self.root.state('zoomed')  # Maximize window
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
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)

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
        self.sales_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_stock_frame(self):
        self.hide_all_frames()
        self.stock_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_report_frame(self):
        self.hide_all_frames()
        self.report_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_admin_frame(self):
        self.hide_all_frames()
        self.admin_menu_frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.admin_content_frame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
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
        header = tk.Frame(frame, bg="#4682B4")  # Darker blue header
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Sales Section", font=("Arial", 24), bg="#4682B4", fg="white").place(relx=0.35, rely=0.2)
        content_frame = tk.Frame(frame, bg="#ADD8E6")
        content_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        return frame

    def create_stock_frame(self):
        frame = tk.Frame(self.root, bg="#90EE90")  # Light Green Background
        header = tk.Frame(frame, bg="#3CB371")  # Darker green header
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Stock Section", font=("Arial", 24), bg="#3CB371", fg="white").place(relx=0.35, rely=0.2)
        content_frame = tk.Frame(frame, bg="#90EE90")
        content_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        return frame

    def create_report_frame(self):
        frame = tk.Frame(self.root, bg="#FFD700")  # Gold Background
        header = tk.Frame(frame, bg="#FFA500")  # Darker gold header
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Report Section", font=("Arial", 24), bg="#FFA500", fg="white").place(relx=0.35, rely=0.2)

        # Search Section
        search_frame = tk.Frame(frame, bg="#FFD700")
        search_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

        tk.Label(search_frame, text="Item Search:", font=("Arial", 14), bg="#FFD700").place(relx=0.05, rely=0.3)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.place(relx=0.2, rely=0.3, relwidth=0.5)
        tk.Button(search_frame, text="Search", command=self.search_item).place(relx=0.75, rely=0.3)

        # Text Box for Report
        text_frame = tk.Frame(frame, bg="#FFFACD")
        text_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
        self.report_text = tk.Text(text_frame, font=("Arial", 12), bg="#FFFACD")
        self.report_text.place(relx=0, rely=0, relwidth=1, relheight=1)

        return frame

    def create_admin_frames(self):
        menu_frame = tk.Frame(self.root, bg="#F0E68C")  # Light Yellow Background for Menu
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
            tk.Button(menu_frame, text=text, font=("Arial", 12), width=20, command=command).place(relx=0.05, rely=0.05 + i * 0.1)

        return menu_frame, content_frame

    def show_admin_option(self, option):
        """Display the selected admin option in the content frame."""
        for widget in self.admin_content_frame.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.admin_content_frame, bg="#CD5C5C", height=60)  # Light Red header for Admin
        header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header_frame, text=option, font=("Arial", 18), bg="#CD5C5C", fg="white").place(relx=0.25, rely=0.2)

        content_frame = tk.Frame(self.admin_content_frame, bg="#FFE4E1")  # Misty rose background for content
        content_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        # Placeholder content for now
        tk.Label(content_frame, text=f"Content for {option}", font=("Arial", 14), bg="#FFE4E1").place(relx=0.25, rely=0.1)

    def search_item(self):
        """Search for the item and display in report."""
        search_query = self.search_entry.get()
        # Sample data for illustration
        sample_data = [
            [1, "Item A", "Brand X", "2023-08-01", 20.5, "kg", 100, 75],
            [2, "Item B", "Brand Y", "2023-08-15", 15.75, "ltr", 200, 160],
        ]

        # Clear previous content
        self.report_text.delete(1.0, tk.END)

        # Insert the grid headers
        self.report_text.insert(tk.END, f"{'Sr No':<8}{'Item Name':<15}{'Brand':<15}{'Date of Entry':<15}{'Unit Price':<12}{'Unit Type':<10}{'Total Stock':<12}{'Current Stock'}\n")
        self.report_text.insert(tk.END, "-" * 100 + "\n")

        # Display filtered data
        for row in sample_data:
            if search_query.lower() in row[1].lower():  # Simple search filter
                self.report_text.insert(tk.END, f"{row[0]:<8}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<12}{row[5]:<10}{row[6]:<12}{row[7]}\n")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
