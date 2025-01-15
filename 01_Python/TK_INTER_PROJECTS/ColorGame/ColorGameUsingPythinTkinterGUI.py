# Color Game Using Pythin Tkinter GUI 

"""--------------------------------------------------
| We are going to build a color game in Tkinter pyhton. 
| In this game, different color names will be displayed 
| with different text colors. Here in this game, the role 
| of a player is to enter the correct color of the word 
| which is display on the screen. Each tome when the 
| player enters the correct color the scor will be 
| incremented by one. And the game duration will be 60 
| seconds.
-------------------------------------------------------"""




# Import Modules 
from tkinter import * 
import tkinter.font as font 
import random 

# Variables
colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60 
score = 0 
displayed_word_color = "" 

# This function will be called when start button is clicked 

# Function startGame 
def startGame():
	print("call startGame")
	global displayed_word_color 

	if timer == 60 : 
		startCountDown()
		displayed_word_color = random.choice(colors).lower()
		display_words.config(text = random.choice(colors), fg = displayed_word_color)
		color_entry.bind('<Return>', displayNextWord)


# This function is to reset the game
# Function resetGame 
def resetGame():
	print("call resetGame")

	global timer, score, displayed_word_color 
	timer = 60 
	score = 0 
	displayed_word_color = ''
	game_score.config(text = "Your Score: " + str(score))
	display_words.config(text = "")
	time_left.config(text = "Game Ends in: -")
	color_entry.delete(0, END)

def startCountDown():
	global timer 
	if (timer >= 0):
		time_left.config(text = "Game Ends in : " + str(timer) + "s")
		timer -= 1 
		time_left.after(1000, startCountDown)
		if timer == -1:
			time_left.config(text = " Game Over !!!")


# This function to display random words 
def displayNextWord(event):
	global displayed_word_color
	global score 
	if timer > 0:
		if displayed_word_color == color_entry.get().lower():
			score += 1

		color_entry.delete(0, END)
		display_word_color = random.choice(colors).lower()
		display_words.config(text = random.choice(colors), fg = display_word_color)



# Main Program 
root = Tk()
root.title("Color Game")
root.geometry("500x200")

app_font = font.Font(family = "Helvetica", size = 12)

game_desp = "Game Description: Enter the color of the words displayd below."
myFont = font.Font(family = "Helvetica")

# Lable:
game_description = Label(root, text = game_desp, font = app_font, fg="grey")
game_description.pack()

game_score = Label(root, text = "Your Score: " + str(score) , font = (font.Font(size=16)), fg = "green")
game_score.pack()

display_words = Label(root, font = (font.Font(size=28)), pady = 10)
display_words.pack() 

time_left = Label(root, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "orange")
time_left.pack() 

# Entry:
color_entry = Entry(root, width = 30)
color_entry.pack(pady = 10)

# Frame:
btn_frame = Frame(root, width = 80, height = 40, bg = "red")
btn_frame.pack(side = BOTTOM)

# Button:
start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "pink", bd = 0, padx = 20, pady = 20, command = startGame)
start_button.grid(row=0, column=0)

reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 0, padx = 20, pady = 20, command = resetGame )
reset_button.grid(row = 0, column = 1)





root.geometry("600x300")
root.mainloop()







