# Calculator:
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x100")

# Function to Evaluate the Value/Expression
def evaluate(event):
    value =  ExpEntry.get()
    ansLabel.config(text="Answer: " + str(eval(value)))


# Lebel for Expression Entry Box:
ExpLabel = Label(root, text="Enter your expression")
ExpLabel.pack()
# Expression Entry Box
ExpEntry = Entry(root)
ExpEntry.bind("<Return>", evaluate)
ExpEntry.pack()

# Label for Answer:
ansLabel = Label(root)
ansLabel.pack()

root.mainloop()
