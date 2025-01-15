# CLIENT PROGRAM AAPS
import tkinter as tk
from tkinter import ttk
import os
import time


class MyAap:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My app")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.config(bg="gray")
        self.loginFrame()
        self.root.mainloop()



    def loginFrame(self):
        global user_name
        global password
        self.user_name = ''
        self.password = ''

        self.main_frame = tk.Frame(self.root, height=150, width=400, bg="#BDFCC9")
        self.main_frame.place(x=0, y=100)
        # Label
        self.name_label = tk.Label(self.main_frame, text = "user name ", font=("Arial", 14), bg="#BDFCC9")
        self.name_label.place(x= 20, y=20)
        self.password_label = tk.Label(self.main_frame, text ="password ", font=("Arial", 14), bg="#BDFCC9")
        self.password_label.place(x=20, y=60)
        # Entry Box
        self.userentry =  tk.Entry(self.main_frame, textvariable = self.user_name, width=30, font=("Arial", 10))
        self.userentry.place(x=150, y=27)
        self.paswdentry = tk.Entry(self.main_frame, textvariable = self.password, width=30, font=("Arial", 10), show="*")
        self.paswdentry.place(x=150, y=67)



def main():
    myaap = MyAap()

if __name__ == "__main__":
    main()
