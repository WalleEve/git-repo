import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window size
        self.setWindowTitle('Window with Frames')
        self.setGeometry(100, 100, 700, 800)  # Size: 700x800

        # Create main layout
        layout = QVBoxLayout()

        # Create frame 1 with a red background and black border
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.StyledPanel)  # Set frame shape
        frame1.setFrameShadow(QFrame.Raised)  # Set shadow effect
        frame1.setStyleSheet("""
            background-color: #FFCCCC;
            border: 5px solid black;
        """)  # Set background color to red and black border

        # Create frame 2 with a blue background and black border
        frame2 = QFrame()
        frame2.setFrameShape(QFrame.StyledPanel)  # Set frame shape
        frame2.setFrameShadow(QFrame.Raised)  # Set shadow effect
        frame2.setStyleSheet("""
            background-color: #ADD8E6;
            border: 5px solid black;
        """)  # Set background color to blue and black border

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
