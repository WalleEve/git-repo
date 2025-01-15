import sys
import psycopg2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow, QVBoxLayout, QAction, QMenu
)
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QFont

# Database Connection
def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
			database="PyQt5_DB",
			user="postgres",
			password="postgres",
			port= 5432
        )
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Main Login Window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Window')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f0f4f5;")
        self.create_login_ui()

    def create_login_ui(self):
        # Create labels and fields
        self.label_user = QLabel('Username:', self)
        self.label_user.setFont(QFont('Arial', 10))
        self.label_user.move(50, 60)

        self.input_user = QLineEdit(self)
        self.input_user.move(150, 60)
        self.input_user.setPlaceholderText('Enter username')
        self.input_user.setStyleSheet("padding: 5px; border-radius: 5px;")

        self.label_password = QLabel('Password:', self)
        self.label_password.setFont(QFont('Arial', 10))
        self.label_password.move(50, 100)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.move(150, 100)
        self.input_password.setPlaceholderText('Enter password')
        self.input_password.setStyleSheet("padding: 5px; border-radius: 5px;")

        # Create login button
        self.button_login = QPushButton('Login', self)
        self.button_login.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 10px;")
        self.button_login.move(150, 160)
        self.button_login.clicked.connect(self.login)

        # Create registration and account recovery
        self.button_register = QPushButton('Register', self)
        self.button_register.setStyleSheet("background-color: #008CBA; color: white; padding: 10px; border-radius: 10px;")
        self.button_register.move(150, 200)
        self.button_register.clicked.connect(self.register)

        self.button_recover = QPushButton('Forgot Password?', self)
        self.button_recover.setStyleSheet("color: #555; border: none; background-color: none;")
        self.button_recover.move(150, 240)
        self.button_recover.clicked.connect(self.recover_password)

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
            self.showMinimized()  # Minimize login window
        else:
            QMessageBox.warning(self, "Failed", "Incorrect username or password!")

    def register(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def recover_password(self):
        QMessageBox.information(self, "Recovery", "Password recovery is not implemented yet.")

# Function to authenticate user from the database
def authenticate_user(username, password):
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_name = %s AND password = %s", (username, password))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error during authentication: {e}")
            return False
        finally:
            connection.close()
    return False

# Function to get user role
def get_user_role(username):
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT category FROM users WHERE user_name = %s", (username,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return result[0]
        except Exception as e:
            print(f"Error during role fetching: {e}")
        finally:
            connection.close()
    return "user"  # Default to user role

# User Window
class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Dashboard")
        self.setGeometry(100, 100, 600, 400)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        sales_menu = menubar.addMenu('Sales')
        stocks_menu = menubar.addMenu('Stocks')

# Admin Window
class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        sales_details = menubar.addMenu('Sales Details')
        stock_details = menubar.addMenu('Stock Details')
        stock_entry = menubar.addMenu('Stock Entry')
        user_mgmt = menubar.addMenu('User Management')
        report = menubar.addMenu('Reports')
        help_menu = menubar.addMenu('Help')

# Registration Window
class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Registration")
        self.setGeometry(200, 200, 400, 300)

        # Add registration form fields (similar to login form)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
