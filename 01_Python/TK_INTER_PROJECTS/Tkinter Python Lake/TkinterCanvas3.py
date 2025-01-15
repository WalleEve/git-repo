import tkinter as tk

root =  tk.Tk()

WIDTH = HEIGHT = 400
x1 = y1 = WIDTH / 2

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
def draw_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="green")

def del_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="white")

def move(event):
    global x1, y1
    if event.char == "a":
        del_rect()
        x1 +=10
    elif event.char =="d":
        del_rect()
        x1 -=10
    elif event.char =="w":
        del_rect()
        y1 -=10
    elif event.char =="s":
        del_rect()
        y1 +=10
    draw_rect()

root.bind("<Key>", move)

root.mainloop()
