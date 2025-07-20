# Example 4: Nested QFrame for Better Structuring
# You can also nest QFrame widgets inside one another to create better-structured layouts.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nested QFrame Example')

        # Main layout
        layout = QVBoxLayout()

        # Outer Frame
        outer_frame = QFrame()
        outer_frame.setFrameShape(QFrame.Box)
        outer_frame.setFrameShadow(QFrame.Raised)
        
        # Inner Frame
        inner_frame = QFrame()
        inner_frame.setFrameShape(QFrame.Panel)
        inner_frame.setFrameShadow(QFrame.Sunken)

        # Add widgets inside the inner frame
        inner_layout = QVBoxLayout()
        inner_layout.addWidget(QLabel("Name:"))
        inner_layout.addWidget(QLineEdit())
        inner_frame.setLayout(inner_layout)

        # Add inner frame to the outer frame
        outer_layout = QVBoxLayout()
        outer_layout.addWidget(inner_frame)
        outer_frame.setLayout(outer_layout)

        # Add the outer frame to the main layout
        layout.addWidget(outer_frame)

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
