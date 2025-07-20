# Example with setSpacing and setContentsMargins:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spacing and Margins Example')

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add buttons to the layout
        layout.addWidget(QPushButton('Button 1'))
        layout.addWidget(QPushButton('Button 2'))
        
        # Set spacing and margins
        layout.setSpacing(10)  # Space between widgets
        layout.setContentsMargins(20, 20, 20, 20)  # Margins around the layout

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

