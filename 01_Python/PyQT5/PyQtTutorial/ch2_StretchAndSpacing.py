# 5. Adding Stretch and Spacing
# You can add stretching or spacing in layouts to adjust the widget positions. This is often useful for creating custom layouts where you need flexible space.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stretch and Spacing Example')

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add buttons to the layout
        layout.addWidget(QPushButton('Button 1'))
        layout.addStretch()  # Add a stretchable space
        layout.addWidget(QPushButton('Button 2'))

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
