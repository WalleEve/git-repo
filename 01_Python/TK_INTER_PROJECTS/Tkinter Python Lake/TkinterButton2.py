# The tkinter Button generated the Random number through Random.random() method.

from tkinter import *
master = Tk()
master.title("Random Number")

def random_number():
    import random
    random1 = random.random()
    print(random1)

button = Button(master, text="Generate Random Number", command=random_number).pack()

master.mainloop()
