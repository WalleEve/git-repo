from PyQt5.QtWidget import QWidget, QLable, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from db.db import authenticate_user, get_user_role
from ui.registration_window import registration_window
from ui.user_window import UserWindow
from ui.admin_window import AdminWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Window")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f4f5;")
        self.create_login_ui()

    def create_login_ui(self):
        self.label_user = QLabel("Username: ", self)
        self.label_user.setFont(QFont("Arial", 10))
        self.label_user.move(50, 50)

        self.input_user = QLineEdit(self)
        self.label_user.move(150, 60)
        self.input_user.setPlaceholderText('Enter username')

        self.label_password = QLabel('Password:', self)
        self.label_password.setFont(QFont('Arial', 10))
        self.label_password.move(50, 100)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.move(150, 100)
        self.input_password.setPlaceholderText('Enter password')

        # Login and Registration buttons (same size)
        self.button_login = QPushButton('Login', self)
        self.button_login.setFixedSize(120, 40)
        self.button_login.move(150, 160)
        self.button_login.clicked.connect(self.login)

        self.button_register = QPushButton('Register', self)
        self.button_register.setFixedSize(120, 40)
        self.button_register.move(150, 210)
        self.button_register.clicked.connect(self.register)


    def login(self):
        username = self.input_user.text()
        password = self.input_password.text()

        if authenticate_user(username, password):
            role = get_user_role(username)
            if role == 'admin':
                self.admin_window = AdminWindow()
                self.admin_window.show()
            else:
                self.user_window = UserWindow()
                self.user_window.show()
            self.showMinimized() # Minimize the parent window
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect Username or password!")

    def register(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

        
