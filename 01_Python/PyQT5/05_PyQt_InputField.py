# Input Fields and Forms 
# We can add text input fields for collecting user data 

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Input Form Example")
		self.setGeometry(100, 100, 600, 400)
		
		# Creating a Lable, input field and button 
		
		self.label_name = QLabel("Enter your name: ", self)
		self.label_name.move(20, 20)
		
		self.label_address = QLabel("Enter your Address: ", self)
		self.label_address.move(20, 50)
		
		self.input_field_name = QLineEdit(self)
		self.input_field_name.move(170, 20)
		
		self.input_field_add = QLineEdit(self)
		self.input_field_add.move(170, 50)
		
		
		self.button = QPushButton("Submit", self)
		self.button.move(170, 120)
		self.button.clicked.connect(self.show_name)
		
		self.display_level = QLabel(self)
		self.display_level.move(170, 150)
		
	def show_name(self):
		name = self.input_field_name.text() # get the input text 
		add = self.input_field_add.text() # get the input text
		self.display_level.setText(f"Hello {name}!, your address: {add}") # Update label with input
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
	
	
# Key Concepts:
# QLineEdit: A single-line text input field 
# text(): Retrives text from the input field.

