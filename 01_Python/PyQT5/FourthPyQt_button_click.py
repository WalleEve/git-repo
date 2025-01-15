# Signals and Slots (Event Handling)
# Signals and slots allow communication between objects (e.g., handling button click, text changes, etc.)

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget 


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Signals and Slots Example")
		
		self.button = QPushButton("Click Me", self)
		self.button.clicked.connect(self.on_button_click)
		
	def on_button_click(self):
		print("Button was clicked!")
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
	
# Key Concepts 
# clicked: A single emitted when a button is clicked. 
# connect(): Connects the signal to the slot (event handler)
# Slot(on_button_click): The method that handles the signal.

