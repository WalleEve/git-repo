Let's design a Kirana Store Management System using Tkinter and organize the project into directories. This system will include functionalities for login, managing products (add/update/delete), and generating reports on sales and stock. Below is a sample project structure along with specific examples for each component.

/kirana_store_management
│
├── /assets                   # Static assets (images, icons)
│   ├── store_logo.png
│
├── /config                   # Configurations
│   └── config.py             # Configuration settings (database path, etc.)
│
├── /controllers              # Business logic (handling user actions)
│   ├── login_controller.py   # Handles login validation
│   ├── product_controller.py # Handles product management (add/update/delete)
│   └── report_controller.py  # Handles report generation (sales, stock)
│
├── /models                   # Data handling (database operations)
│   ├── user_model.py         # User authentication
│   ├── product_model.py      # Product table interactions
│   └── sales_model.py        # Sales and stock interactions
│
├── /views                    # UI components
│   ├── login_view.py         # Login form UI
│   ├── product_view.py       # UI for product management
│   └── report_view.py        # UI for sales/stock reports
│
├── /utils                    # Utility functions (helper scripts)
│   ├── email_util.py         # Function for sending notifications (optional)
│   └── random_util.py        # Function to generate random codes (optional)
│
├── main.py                   # Entry point of the application
│
├── requirements.txt          # Dependencies
│
└── README.md                 # Project documentation
Example Code for the Kirana Store
/config/config.py
python
Copy code
DATABASE_PATH = 'kirana_store.db'
/models/user_model.py
python
Copy code
import sqlite3
from config.config import DATABASE_PATH

def create_user_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def check_user_credentials(username, password):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def add_user(username, password):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Call the function once to create the users table
create_user_table()
/models/product_model.py
python
Copy code
import sqlite3
from config.config import DATABASE_PATH

def create_product_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            stock INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, stock, price):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (product_name, stock, price) VALUES (?, ?, ?)', (name, stock, price))
    conn.commit()
    conn.close()

def update_product(product_id, name, stock, price):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET product_name=?, stock=?, price=? WHERE product_id=?', (name, stock, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id=?', (product_id,))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

create_product_table()
/controllers/login_controller.py
python
Copy code
from models.user_model import check_user_credentials
from tkinter import messagebox

def login(username, password):
    if check_user_credentials(username, password):
        messagebox.showinfo("Login", "Login successful!")
        return True
    else:
        messagebox.showerror("Login", "Invalid credentials")
        return False
/controllers/product_controller.py
python
Copy code
from models.product_model import add_product, update_product, delete_product, get_all_products

def add_new_product(name, stock, price):
    add_product(name, stock, price)

def update_existing_product(product_id, name, stock, price):
    update_product(product_id, name, stock, price)

def remove_product(product_id):
    delete_product(product_id)

def fetch_products():
    return get_all_products()
/views/login_view.py
python
Copy code
import tkinter as tk
from controllers.login_controller import login
from views.product_view import open_product_management_window

def create_login_window():
    root = tk.Tk()
    root.title("Kirana Store - Login")

    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)
    
    username = tk.Entry(root)
    password = tk.Entry(root, show="*")
    username.grid(row=0, column=1)
    password.grid(row=1, column=1)
    
    def handle_login():
        if login(username.get(), password.get()):
            root.destroy()  # Close the login window
            open_product_management_window()  # Open the product management window

    tk.Button(root, text="Login", command=handle_login).grid(row=2, columnspan=2)
    root.mainloop()
/views/product_view.py
python
Copy code
import tkinter as tk
from controllers.product_controller import add_new_product, fetch_products

def open_product_management_window():
    root = tk.Tk()
    root.title("Kirana Store - Product Management")

    tk.Label(root, text="Product Name").grid(row=0)
    tk.Label(root, text="Stock").grid(row=1)
    tk.Label(root, text="Price").grid(row=2)
    
    product_name = tk.Entry(root)
    stock = tk.Entry(root)
    price = tk.Entry(root)
    
    product_name.grid(row=0, column=1)
    stock.grid(row=1, column=1)
    price.grid(row=2, column=1)
    
    def handle_add_product():
        add_new_product(product_name.get(), stock.get(), price.get())
        refresh_product_list()

    tk.Button(root, text="Add Product", command=handle_add_product).grid(row=3, columnspan=2)
    
    # Display the list of products
    product_list = tk.Listbox(root)
    product_list.grid(row=4, columnspan=2)
    
    def refresh_product_list():
        product_list.delete(0, tk.END)
        for product in fetch_products():
            product_list.insert(tk.END, f"{product[1]} (Stock: {product[2]}, Price: {product[3]})")

    refresh_product_list()
    root.mainloop()
/utils/email_util.py (optional)
python
Copy code
import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, message_body):
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"

    msg = MIMEText(message_body)
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
/main.py
python
Copy code
from views.login_view import create_login_window

if __name__ == "__main__":
    create_login_window()
Workflow:
Login: Users log into the system using the credentials stored in the users table (managed in /models/user_model.py).
Product Management: After login, users can manage products (add, update, delete) using the product management window (/views/product_view.py).
Database Handling: All product-related data is handled in the products table via /models/product_model.py.
Notes:
Modular Design: Each directory has a clear responsibility—models handle database operations, controllers handle business logic, and views handle the UI.
Extensibility: This structure makes it easy to add more features, such as sales management or customer reports.
Email Feature (Optional): You can add an email utility to send stock alerts or notifications.