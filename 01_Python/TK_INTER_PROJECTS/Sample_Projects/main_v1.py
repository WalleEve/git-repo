import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
from datetime import datetime

# Function to connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres"
            port = 5432
        )
        return conn
    except Exception as e:
        messagebox.showerror("Error", f"Database connection error: {e}")
        return None

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.state('zoomed')
        self.root.title("Kirana Store Management")

        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        menubar.add_command(label="SALES", command=self.show_sales_frame)
        menubar.add_command(label="STOCK", command=self.show_stock_frame)
        menubar.add_command(label="REPORT", command=self.show_report_frame)
        menubar.add_command(label="ADMIN", command=self.admin_login)

        # Main container for frames
        self.container = tk.Frame(self.root)
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Create Frames
        self.sales_frame = self.create_sales_frame()
        self.stock_frame = self.create_stock_frame()
        self.report_frame = self.create_report_frame()
        self.admin_menu_frame, self.admin_content_frame = self.create_admin_frames()

        self.show_sales_frame()  # Show the Sales frame by default

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
        self.show_admin_option("Sales Report")

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
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password, last_login FROM admin_login WHERE user_name=%s", (username,))
            result = cursor.fetchone()
            if result:
                stored_password, last_login = result
                print(stored_password)
                if password == stored_password:
                    cursor.execute("UPDATE admin_login SET last_login=%s WHERE user_name=%s",
                                   (datetime.now(), username))
                    conn.commit()
                    messagebox.showinfo("Login", "Admin login successful!")
                    self.login_window.destroy()
                    self.show_admin_frame()
                else:
                    messagebox.showerror("Error", "Invalid Password!")
            else:
                messagebox.showerror("Error", "Invalid Username!")
            cursor.close()
            conn.close()
        else:
            messagebox.showerror("Error", "Could not connect to the database.")

    def create_sales_frame(self):
        frame = tk.Frame(self.root, bg="#ADD8E6")
        header = tk.Frame(frame, bg="#4682B4")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Sales Section", font=("Arial", 24), bg="#4682B4", fg="white").place(relx=0.35, rely=0.2)
        return frame

    def create_stock_frame(self):
        frame = tk.Frame(self.root, bg="#90EE90")
        header = tk.Frame(frame, bg="#3CB371")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Stock Section", font=("Arial", 24), bg="#3CB371", fg="white").place(relx=0.35, rely=0.2)

        # Search Box
        search_frame = tk.Frame(frame, bg="#90EE90")
        search_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

        tk.Label(search_frame, text="Item Search:", font=("Arial", 14), bg="#90EE90").place(relx=0.05, rely=0.3)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.place(relx=0.2, rely=0.3, relwidth=0.5)
        tk.Button(search_frame, text="Search", command=self.search_stock_item).place(relx=0.75, rely=0.3)

        # Treeview for Stock Details
        tree_frame = tk.Frame(frame, bg="#FFFFFF")
        tree_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        columns = ("sr_no", "item_name", "brand", "date_of_entry", "unit_price", "unit_type", "total_stock", "current_stock")
        self.stock_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        for col in columns:
            self.stock_tree.heading(col, text=col.replace('_', ' ').title())
            self.stock_tree.column(col, width=100, anchor='center')

        self.stock_tree.place(relx=0, rely=0, relwidth=1, relheight=1)
        return frame

    def create_report_frame(self):
        frame = tk.Frame(self.root, bg="#FFD700")
        header = tk.Frame(frame, bg="#FFA500")
        header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        tk.Label(header, text="Report Section", font=("Arial", 24), bg="#FFA500", fg="white").place(relx=0.35, rely=0.2)
        return frame

    def create_admin_frames(self):
        menu_frame = tk.Frame(self.root, bg="#F0E68C")
        content_frame = tk.Frame(self.root, bg="#FAFAD2")

        admin_options = [
            ("Sales Report", lambda: self.show_admin_option("Sales Report")),
            ("Stock Report", lambda: self.show_admin_option("Stock Report")),
            ("User Management", lambda: self.show_admin_option("User Management")),
            ("Stock Entry & Update", lambda: self.show_admin_option("Stock Entry & Update")),
            ("Password Management", lambda: self.show_admin_option("Password Management"))
        ]

        for i, (text, command) in enumerate(admin_options):
            tk.Button(menu_frame, text=text, font=("Arial", 12), width=20, command=command).place(relx=0.05, rely=0.1 + i*0.15)

        return menu_frame, content_frame

    def show_admin_option(self, option):
        """Display content based on selected admin option."""
        for widget in self.admin_content_frame.winfo_children():
            widget.destroy()

        tk.Label(self.admin_content_frame, text=f"{option}", font=("Arial", 24), bg="#FAFAD2").place(relx=0.3, rely=0.1)

    def search_stock_item(self):
        """Search stock items from the database."""
        search_query = self.search_entry.get()
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM stock WHERE item_name LIKE %s"
            cursor.execute(query, (f"%{search_query}%",))
            results = cursor.fetchall()

            # Clear previous tree content
            for row in self.stock_tree.get_children():
                self.stock_tree.delete(row)

            # Insert fetched data into Treeview
            for row in results:
                self.stock_tree.insert('', tk.END, values=row)

            cursor.close()
            conn.close()
        else:
            messagebox.showerror("Error", "Could not connect to the database.")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
