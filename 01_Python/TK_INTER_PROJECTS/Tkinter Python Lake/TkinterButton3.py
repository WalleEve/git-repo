from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Random Widget")

def random_value():
    import random
    random1 = random.random()
    messagebox.showinfo("Random Value is: ", random1)

labelframe = LabelFrame(master, fg="red", font=14, text="Random value generator")
labelframe.pack(side=BOTTOM)

button = Button(labelframe, text="Click here", fg="blue", command=random_value)
button.pack(side=BOTTOM)

label = Label(labelframe, text="Click on button to generate random value")
label.pack(side=BOTTOM)

master.mainloop()
