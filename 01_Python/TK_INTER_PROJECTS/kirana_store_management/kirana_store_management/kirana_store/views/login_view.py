import tkinter as tk
from kirana_store.controllers.login_controller import login
from kirana_store.views.product_view import open_product_management_window

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
        print(username.get(), password.get())
        if login(username.get(), password.get()):            
            root.destroy()  # Close the login window
            open_product_management_window()  # Open the product management window

    tk.Button(root, text="Login", command=handle_login).grid(row=2, columnspan=2)
    root.mainloop()
