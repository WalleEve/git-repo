from kirana_store.models.user_model import check_user_credentials
from tkinter import messagebox

def login(username, password):
    if check_user_credentials(username, password):
        messagebox.showinfo("Login", "Login successful!")
        return True
    else:
        messagebox.showerror("Login", "Invalid credentials")
        return False
