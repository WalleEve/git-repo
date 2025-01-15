# Toplevel
"""
The Toplevel widged provides a separate for other widgets, such as Frame.
"""
from tkinter import *
root = Tk()
#root.open_readfile('optionDB')
root.title("Toplevel")

Label (root, text="This is the main (default) Toplevel").pack(pady=10)

t1 = Toplevel(root)
Label(t1, text = "This is a child of root").pack(padx=10, pady=10)

t2 = Toplevel(root)
Label (t2, text = "This is a trasient window of root").pack(padx=10, pady=10)
t2.transient(root)

t3 = Toplevel(root, borderwidth=5, bg='blue')
Label(t3, text ="No wm decorations", bg='blue', fg='white').pack(padx=10, pady=10)
t3.overrideredirect(1)
t3.geometry("200x70+150+150")

root.mainloop()
