import tkinter as tk
from tkinter import ttk

def login():
    # main window
    root = tk.Tk()
    # Title of the main window
    root.title("Login")

    # Set Geomerty
    root.geometry("300x400")

    # Disable of resizing
    root.resizable(0, 0)


    login_frame = tk.Frame(root, height=30, width=290, bg="darkgray", bd=0, relief="raise")
    login_frame.place(x=5, y=5)

    login_title = tk.Label(login_frame, text="My Locker", width=31, height=2, font = ("Arial", 12), bg="darkgray")
    login_title.grid(padx = 2)



    root.mainloop()


if __name__ == "__main__":
    login()
