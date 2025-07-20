from PyQt5 import QtWidgets
from database import verify_login  # Import verification function

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        self.resize(300, 150)
        
        self.username_label = QtWidgets.QLabel("Username:")
        self.username_input = QtWidgets.QLineEdit()
        
        self.password_label = QtWidgets.QLabel("Password:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if verify_login(username, password):
            QtWidgets.QMessageBox.information(self, "Success", "Login successful!")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
