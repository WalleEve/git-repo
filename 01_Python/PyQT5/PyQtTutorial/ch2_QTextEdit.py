# 3. QTextEdit (Multiline Text Box)
# QTextEdit is a widget that allows for multiline text input.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit Example')

        # Create layout
        layout = QVBoxLayout()

        # Add a label
        layout.addWidget(QLabel('Enter Address:'))

        # Add QTextEdit (multiline text box)
        address_textbox = QTextEdit()
        address_textbox.setPlaceholderText("Write your address here...")
        layout.addWidget(address_textbox)

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
