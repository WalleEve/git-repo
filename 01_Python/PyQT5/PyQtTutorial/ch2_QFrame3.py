# Example 3: Using QFrame with a Simple Shadow Effect
# In this example, we'll use a shadow effect along with the QFrame to enhance the look.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFrame Shadow Effect')

        # Create the main layout
        layout = QVBoxLayout()

        # Create frame with a shadow effect
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)  # Set the shape to styled panel
        frame.setFrameShadow(QFrame.Raised)  # Raised shadow
        frame.setStyleSheet("""
            QFrame {
                border: 2px solid black;
                border-radius: 10px;
                background-color: lightgrey;
            }
        """)

        # Add some widgets inside the frame
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(QLabel("This frame has a shadow effect"))
        frame.setLayout(frame_layout)

        # Add frame to main layout
        layout.addWidget(frame)

        # Set the main layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
