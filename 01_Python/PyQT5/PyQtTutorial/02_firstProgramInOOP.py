# Creating a Qt Program in an object-oriented way:



import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		# Set the window title 
		self.setWindowTitle("Hellow World")

		# show the window 
		self.show()




if __name__ == "__main__":
	app = QApplication(sys.argv)

	# create the main window 
	window = MainWindow()

	# start tee event loop
	sys.exit(app.exec())


