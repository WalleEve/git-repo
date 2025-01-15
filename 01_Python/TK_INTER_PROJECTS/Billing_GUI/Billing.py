from tkinter import *
from tkinter import ttk

class Billing:
    """ This is a Billing GUI to DEMO purpose """

    def __init__(self, root):
        self.root = root
        self.root.title("Billing Application")
        self.root.geometry("1350x700+0+0")
        


root = Tk()
Blng = Billing(root)
root.mainloop()
