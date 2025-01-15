# Styling and Customization 
# Styling with CSS (Qt Style Sheets)
# We can use Qt Style sheets (CSS like syntax) to style our PyQt5 application.



import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Styling Example")
		
		button = QPushButton("Styled Button", self)
		button.setStyleSheet("""
			QPushButton{
				background-color: #4CAF50;
				color: white;
				border-radius: 5px;
				padding: 10px;
			}
			QPushButton:hover{
				background-color: #45a049;
			}
		""")
		
		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

# Key Concepts 
# QTableWidget: Display data in a table.
# setItem(row, col, QTableWidgetItem): Sets an itme in the table 

