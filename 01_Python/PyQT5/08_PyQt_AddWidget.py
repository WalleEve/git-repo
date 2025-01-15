# Using Layouts in Depth 


import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QGridLayout 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Grid Layout Example")
		self.setGeometry(100, 100, 600, 400)
		
		central_widget = QWidget()
		self.setCentralWidget(central_widget)
		
		grid = QGridLayout()
		
		grid.addWidget(QLabel("Row 0, Col 0"), 0, 0)
		grid.addWidget(QLabel("Row 0, Col 1"), 0, 1)
		grid.addWidget(QPushButton("Button"), 1, 0, 1, 2) # Span two columns
		
		central_widget.setLayout(grid)
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
	
# Key Concepts 
# QGridLayout: Lays out widget in a grid 
# addWidget(widget, row, col, rowspan, colspan): Adds a widget to the grid 