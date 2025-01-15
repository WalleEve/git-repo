# Widgets and Layouts 

# Add Widgets 
# Widgets are UI elements like button, labels, input fields, etc.

import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("PyQt5 Widget Example")
		self.setGeometry(100, 100, 600, 400)
		
		# Adding a label 
		
		self.label = QLabel("Hello, PyQt5!", self)
		self.label.move(50, 50) # set position
		
		# Adding a button 
		self.button = QPushButton("Click Me", self)
		self.button.move(50, 100)
		self.button.clicked.connect(self.on_button_click) # Button click event

		self.button2 = QPushButton("Unclick Me", self)
		self.button2.move(200, 100)
		self.button2.clicked.connect(self.on_button_unclick)
		
	def on_button_click(self):
		self.label.setText("Button Clicked!")
		
	def on_button_unclick(self):
		self.label.setText("Button UnClicked!")
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv) # create the application 
	window = MainWindow() # Create instance of main window 
	window.show() # Display the window 
	sys.exit(app.exec_()) # Execute the app 



# Key Concepts 
# QLabel: Display text or an image. 
# QPushButton: A clickable button. 
# move(x, y): Positioning widgets in the window. 