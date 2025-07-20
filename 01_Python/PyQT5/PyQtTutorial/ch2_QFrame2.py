# Example 2: QFrame with Different Border Styles
# In this example, we'll demonstrate different border styles and shadow effects for the frame:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFrame Border Styles')

        # Create the main layout
        layout = QVBoxLayout()

        # Frame 1 with Raised Border
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Box)  # Box-shaped border
        frame1.setFrameShadow(QFrame.Raised)  # Raised shadow
        frame1.setStyleSheet("QFrame { border: 2px solid blue; }")
        frame1_layout = QVBoxLayout()
        frame1_layout.addWidget(QLabel("Frame 1: Raised Border"))
        frame1.setLayout(frame1_layout)
        
        # Frame 2 with Sunken Border
        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Box)  # Box-shaped border
        frame2.setFrameShadow(QFrame.Sunken)  # Sunken shadow
        frame2.setStyleSheet("QFrame { border: 2px solid green; }")
        frame2_layout = QVBoxLayout()
        frame2_layout.addWidget(QLabel("Frame 2: Sunken Border"))
        frame2.setLayout(frame2_layout)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)

        # Set the main layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
