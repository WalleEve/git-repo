# Layout for Arranging Widgets 
# Introduction to Layouts 
# Instead of positioning widgets manually, yse layouts to manage the organization of widgets in the window 

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Layoyts Example")
		self.setGeometry(100, 100, 600, 400)
		
		# Create central widget 
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)
		
		# Create layouts 
		vbox = QVBoxLayout() # vertical layout 
		hbox = QHBoxLayout() # Horizontal layout 
		
		# Add widgets to layouts 
		vbox.addWidget(QLabel("Label 1"))
		vbox.addWidget(QLabel("Label 2"))
		
		hbox.addWidget(QPushButton("Button 1"))
		hbox.addWidget(QPushButton("Button 2"))
		
		vbox.addLayout(hbox) # add horizontal layout to vertical layout
		
		# set the layout for the central widget 
		central_widget.setLayout(vbox)
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv) # create the application 
	window = MainWindow() # Create instance of main window 
	window.show() # Display the window 
	sys.exit(app.exec_()) # Execute the app 
	
# Key Concepts 
# QVBoxLayout: Vertical layout Manager 
# QHBoxLayout: Horizontal Layout Manager
# addWidget(): Adds widgets to the layout 
# setLayout(): Assign the layout to a widget 

