# admin_tab.py
from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox,  QDialog, QFormLayout, QLineEdit, QPushButton, QMessageBox

class AdminTab(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.setGeometry(100, 100, 300, 200)
        self.db_manager = db_manager
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.otp_input = QLineEdit()

        self.get_otp_button = QPushButton("Login")
        self.login_button = QPushButton("Submit")

        self.get_otp_button.clicked.connect(self.get_otp)
        self.login_button.clicked.connect(self.login)

        layout.addRow("Username:", self.username_input)
        layout.addRow("Password:", self.password_input)
        layout.addRow(self.get_otp_button)
        layout.addRow("OTP:", self.otp_input)
        layout.addRow(self.login_button)

        self.setLayout(layout)

    def get_otp(self):
        QMessageBox.information(self, "OTP", "OTP has been sent to your registered contact.")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        otp = self.otp_input.text()
        if username == "admin" and password == "admin123" and otp == "123456":
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials or OTP.")

