# Admin Tab: User Tab
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QTabWidget, QFormLayout, QMainWindow, QDateEdit, QComboBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QCalendarWidget, QTextEdit, QDialog, QGridLayout
)
from PyQt5.QtCore import Qt, QDate
from models import user_data

class UserTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Phone and Email Update
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # Phone Update
        self.phone_label = QLabel(f"Registered Phone: ******{user_data['phone'][-4:]}")
        self.phone_update_button = QPushButton("Update Phone")
        self.phone_update_button.clicked.connect(self.update_phone)
        frame1_layout.addRow(self.phone_label, self.phone_update_button)

        # Email Update
        self.email_label = QLabel(f"Registered Email: ****{user_data['email'][-4:]}")
        self.email_update_button = QPushButton("Update Email")
        self.email_update_button.clicked.connect(self.update_email)
        frame1_layout.addRow(self.email_label, self.email_update_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Password Reset
        frame2 = QWidget()
        frame2_layout = QFormLayout()

        self.old_password_input = QLineEdit()
        self.old_password_input.setPlaceholderText("Enter old password")
        self.old_password_input.setEchoMode(QLineEdit.Password)

        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("Enter new password")
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.reset_button = QPushButton("Reset Password")
        self.reset_button.clicked.connect(self.reset_password)

        frame2_layout.addRow("Old Password:", self.old_password_input)
        frame2_layout.addRow("New Password:", self.new_password_input)
        frame2_layout.addRow("Confirm Password:", self.confirm_password_input)
        frame2_layout.addRow(self.reset_button)

        frame2.setLayout(frame2_layout)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        self.setLayout(layout)

    def update_phone(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Phone")
        dialog_layout = QFormLayout()

        self.old_phone_input = QLineEdit()
        self.old_phone_input.setPlaceholderText("Enter old phone number")

        self.new_phone_input = QLineEdit()
        self.new_phone_input.setPlaceholderText("Enter new phone number")

        self.update_phone_button = QPushButton("Update")
        self.update_phone_button.clicked.connect(lambda: self.validate_phone(dialog))

        dialog_layout.addRow("Old Phone:", self.old_phone_input)
        dialog_layout.addRow("New Phone:", self.new_phone_input)
        dialog_layout.addRow(self.update_phone_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def validate_phone(self, dialog):
        old_phone = self.old_phone_input.text()
        new_phone = self.new_phone_input.text()

        if old_phone == user_data["phone"]:
            user_data["phone"] = new_phone
            self.phone_label.setText(f"Registered Phone: ******{new_phone[-4:]}")
            QMessageBox.information(self, "Success", "Phone number updated successfully!")
            dialog.close()
        else:
            QMessageBox.warning(self, "Error", "Old phone number does not match!")

    def update_email(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Email")
        dialog_layout = QFormLayout()

        self.old_email_input = QLineEdit()
        self.old_email_input.setPlaceholderText("Enter old email")

        self.new_email_input = QLineEdit()
        self.new_email_input.setPlaceholderText("Enter new email")

        self.update_email_button = QPushButton("Update")
        self.update_email_button.clicked.connect(lambda: self.validate_email(dialog))

        dialog_layout.addRow("Old Email:", self.old_email_input)
        dialog_layout.addRow("New Email:", self.new_email_input)
        dialog_layout.addRow(self.update_email_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def validate_email(self, dialog):
        old_email = self.old_email_input.text()
        new_email = self.new_email_input.text()

        if old_email == user_data["email"]:
            user_data["email"] = new_email
            self.email_label.setText(f"Registered Email: ****{new_email[-4:]}")
            QMessageBox.information(self, "Success", "Email updated successfully!")
            dialog.close()
        else:
            QMessageBox.warning(self, "Error", "Old email does not match!")

    def reset_password(self):
        old_password = self.old_password_input.text()
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if old_password == user_data["password"]:
            if new_password == confirm_password:
                user_data["password"] = new_password
                QMessageBox.information(self, "Success", "Password reset successfully!")
            else:
                QMessageBox.warning(self, "Error", "New passwords do not match!")
        else:
            QMessageBox.warning(self, "Error", "Old password is incorrect!")