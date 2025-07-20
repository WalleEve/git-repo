# account_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QDialog, QHBoxLayout, 
    QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt

# Simulated account data
account_data = {
    "username": "admin_user",
    "account_type": "Admin",
    "status": "Active"
}

class AccountTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Account Details
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # Username
        self.username_label = QLabel(f"Username: {account_data['username']}")
        self.username_update_button = QPushButton("Update Username")
        self.username_update_button.clicked.connect(self.update_username)
        frame1_layout.addRow(self.username_label, self.username_update_button)

        # Account Type
        self.account_type_label = QLabel(f"Account Type: {account_data['account_type']}")
        self.account_type_update_button = QPushButton("Change Account Type")
        self.account_type_update_button.clicked.connect(self.change_account_type)
        frame1_layout.addRow(self.account_type_label, self.account_type_update_button)

        # Account Status
        self.account_status_label = QLabel(f"Account Status: {account_data['status']}")
        self.account_status_update_button = QPushButton("Change Status")
        self.account_status_update_button.clicked.connect(self.change_status)
        frame1_layout.addRow(self.account_status_label, self.account_status_update_button)

        frame1.setLayout(frame1_layout)

        # Add frame to the main layout
        layout.addWidget(frame1)
        self.setLayout(layout)

    def update_username(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Username")
        dialog_layout = QFormLayout()

        self.new_username_input = QLineEdit()
        self.new_username_input.setPlaceholderText("Enter new username")

        self.update_username_button = QPushButton("Update")
        self.update_username_button.clicked.connect(self.validate_username)

        dialog_layout.addRow("New Username:", self.new_username_input)
        dialog_layout.addRow(self.update_username_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def validate_username(self):
        new_username = self.new_username_input.text()

        if new_username:
            account_data["username"] = new_username
            self.username_label.setText(f"Username: {new_username}")
            QMessageBox.information(self, "Success", "Username updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "Username cannot be empty!")

    def change_account_type(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Change Account Type")
        dialog_layout = QFormLayout()

        self.account_type_combo = QComboBox()
        self.account_type_combo.addItem("Admin")
        self.account_type_combo.addItem("User")
        self.account_type_combo.addItem("Guest")

        self.change_account_type_button = QPushButton("Change")
        self.change_account_type_button.clicked.connect(self.update_account_type)

        dialog_layout.addRow("Select Account Type:", self.account_type_combo)
        dialog_layout.addRow(self.change_account_type_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def update_account_type(self):
        selected_type = self.account_type_combo.currentText()

        account_data["account_type"] = selected_type
        self.account_type_label.setText(f"Account Type: {selected_type}")
        QMessageBox.information(self, "Success", "Account type updated successfully!")

    def change_status(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Change Account Status")
        dialog_layout = QFormLayout()

        self.status_combo = QComboBox()
        self.status_combo.addItem("Active")
        self.status_combo.addItem("Inactive")
        self.status_combo.addItem("Suspended")

        self.change_status_button = QPushButton("Change Status")
        self.change_status_button.clicked.connect(self.update_status)

        dialog_layout.addRow("Select Status:", self.status_combo)
        dialog_layout.addRow(self.change_status_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def update_status(self):
        selected_status = self.status_combo.currentText()

        account_data["status"] = selected_status
        self.account_status_label.setText(f"Account Status: {selected_status}")
        QMessageBox.information(self, "Success", "Account status updated successfully!")
