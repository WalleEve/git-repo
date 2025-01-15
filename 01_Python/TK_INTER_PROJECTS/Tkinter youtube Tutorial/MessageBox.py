# Message Box / Alert Box
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")

messagebox.showinfo("Windows Title","Hello How are you")

ans = messagebox.askquestion("Answer", "Are you 18+")

if ans == "yes":
    messagebox.showinfo("Title", "Welcome")
if ans == "no":
    messagebox.showwarning("Title", "Objectionable Content")

# root.mainloop()
