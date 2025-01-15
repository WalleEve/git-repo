import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)  # Set the geometry of the window (width=600, height=400)
        self.setWindowTitle("Login Window")
        
        # Create UI elements for login
        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)
        
        # Set layout for login form
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        # Set main widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Connect login button to login function
        self.login_button.clicked.connect(self.login)

    def login(self):
        # Dummy validation of username and password
        if self.username_input.text() == "admin" and self.password_input.text() == "password":
            self.open_child_window()

    def open_child_window(self):
        # Open the child window and minimize the login window
        self.child_window = ChildWindow()
        self.child_window.show()
        self.showMinimized()

class ChildWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle("Child Window")

        # Create two frames with different background colors
        self.frame1 = QFrame(self)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setAutoFillBackground(True)
        palette1 = self.frame1.palette()
        palette1.setColor(QPalette.Window, QColor(Qt.red))
        self.frame1.setPalette(palette1)

        self.frame2 = QFrame(self)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setAutoFillBackground(True)
        palette2 = self.frame2.palette()
        palette2.setColor(QPalette.Window, QColor(Qt.blue))
        self.frame2.setPalette(palette2)

        # Use QSplitter to split the frames in a 30:70 ratio
        #splitter = QSplitter(Qt.Horizontal)
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.frame1)
        splitter.addWidget(self.frame2)
        splitter.setSizes([180, 420])  # Set the ratio to 30:70 (approx.)

        # Set layout for the child window
        layout = QHBoxLayout()
        layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the login window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())
