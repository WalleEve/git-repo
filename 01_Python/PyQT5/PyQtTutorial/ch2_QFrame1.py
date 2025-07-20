# QFrame can be used as a container for other widgets, and it can be styled to show different 
# kinds of borders or even a shadow effect. You can customize the appearance of QFrame widgets using its properties, such as:

# Frame Shape: Defines the border style (e.g., no border, raised, sunken).
# Frame Shadow: Defines the shadow style of the border (e.g., plain, raised, sunken).


# Example 1: Basic QFrame Container with Border

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFrame Example')

        # Create the main layout
        layout = QVBoxLayout()

        # Create a frame with a border
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)  # Set the border shape
        frame.setFrameShadow(QFrame.Raised)  # Set the shadow style

        # Add widgets inside the frame
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(QLabel("This is a label inside a frame"))
        frame_layout.addWidget(QLineEdit("This is a text input"))
        
        frame.setLayout(frame_layout)

        # Add the frame to the main layout
        layout.addWidget(frame)

        # Set the main layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())


