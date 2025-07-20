# 4. Using QFormLayout (Form Layout)
# A form layout is used to display labels and input fields in a row format.


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFormLayout Example')

        # Create a form layout
        layout = QFormLayout()

        # Add widgets to the form layout
        layout.addRow(QLabel('Name:'), QLineEdit())  # Label and input field
        layout.addRow(QLabel('Email:'), QLineEdit())  # Label and input field

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
