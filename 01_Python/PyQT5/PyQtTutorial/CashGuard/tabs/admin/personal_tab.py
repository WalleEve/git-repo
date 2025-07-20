# personal_tab.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QDialog, 
    QDateEdit, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import QDate

# Simulated personal data
personal_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "dob": QDate(1990, 5, 15),
    "phone": "123-456-7890"
}

class PersonalTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Personal Details
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # First Name
        self.first_name_label = QLabel(f"First Name: {personal_data['first_name']}")
        self.first_name_update_button = QPushButton("Update First Name")
        self.first_name_update_button.clicked.connect(self.update_first_name)
        frame1_layout.addRow(self.first_name_label, self.first_name_update_button)

        # Last Name
        self.last_name_label = QLabel(f"Last Name: {personal_data['last_name']}")
        self.last_name_update_button = QPushButton("Update Last Name")
        self.last_name_update_button.clicked.connect(self.update_last_name)
        frame1_layout.addRow(self.last_name_label, self.last_name_update_button)

        # Email
        self.email_label = QLabel(f"Email: {personal_data['email']}")
        self.email_update_button = QPushButton("Update Email")
        self.email_update_button.clicked.connect(self.update_email)
        frame1_layout.addRow(self.email_label, self.email_update_button)

        # Date of Birth
        self.dob_label = QLabel(f"DOB: {personal_data['dob'].toString()}")
        self.dob_update_button = QPushButton("Update DOB")
        self.dob_update_button.clicked.connect(self.update_dob)
        frame1_layout.addRow(self.dob_label, self.dob_update_button)

        # Phone
        self.phone_label = QLabel(f"Phone: {personal_data['phone']}")
        self.phone_update_button = QPushButton("Update Phone")
        self.phone_update_button.clicked.connect(self.update_phone)
        frame1_layout.addRow(self.phone_label, self.phone_update_button)

        frame1.setLayout(frame1_layout)

        # Add frame to the main layout
        layout.addWidget(frame1)
        self.setLayout(layout)

    def update_first_name(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update First Name")
        dialog_layout = QFormLayout()

        self.new_first_name_input = QLineEdit()
        self.new_first_name_input.setText(personal_data["first_name"])
        self.update_first_name_button = QPushButton("Update")
        self.update_first_name_button.clicked.connect(self.save_first_name)

        dialog_layout.addRow("New First Name:", self.new_first_name_input)
        dialog_layout.addRow(self.update_first_name_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def save_first_name(self):
        new_first_name = self.new_first_name_input.text()
        if new_first_name:
            personal_data["first_name"] = new_first_name
            self.first_name_label.setText(f"First Name: {new_first_name}")
            QMessageBox.information(self, "Success", "First name updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "First name cannot be empty!")

    def update_last_name(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Last Name")
        dialog_layout = QFormLayout()

        self.new_last_name_input = QLineEdit()
        self.new_last_name_input.setText(personal_data["last_name"])
        self.update_last_name_button = QPushButton("Update")
        self.update_last_name_button.clicked.connect(self.save_last_name)

        dialog_layout.addRow("New Last Name:", self.new_last_name_input)
        dialog_layout.addRow(self.update_last_name_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def save_last_name(self):
        new_last_name = self.new_last_name_input.text()
        if new_last_name:
            personal_data["last_name"] = new_last_name
            self.last_name_label.setText(f"Last Name: {new_last_name}")
            QMessageBox.information(self, "Success", "Last name updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "Last name cannot be empty!")

    def update_email(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Email")
        dialog_layout = QFormLayout()

        self.new_email_input = QLineEdit()
        self.new_email_input.setText(personal_data["email"])
        self.update_email_button = QPushButton("Update")
        self.update_email_button.clicked.connect(self.save_email)

        dialog_layout.addRow("New Email:", self.new_email_input)
        dialog_layout.addRow(self.update_email_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def save_email(self):
        new_email = self.new_email_input.text()
        if new_email:
            personal_data["email"] = new_email
            self.email_label.setText(f"Email: {new_email}")
            QMessageBox.information(self, "Success", "Email updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "Email cannot be empty!")

    def update_dob(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Date of Birth")
        dialog_layout = QFormLayout()

        self.dob_input = QDateEdit()
        self.dob_input.setDate(personal_data["dob"])
        self.dob_input.setDisplayFormat("yyyy-MM-dd")

        self.update_dob_button = QPushButton("Update")
        self.update_dob_button.clicked.connect(self.save_dob)

        dialog_layout.addRow("New Date of Birth:", self.dob_input)
        dialog_layout.addRow(self.update_dob_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def save_dob(self):
        new_dob = self.dob_input.date()
        if new_dob.isValid():
            personal_data["dob"] = new_dob
            self.dob_label.setText(f"DOB: {new_dob.toString()}")
            QMessageBox.information(self, "Success", "Date of Birth updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please select a valid date!")

    def update_phone(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Phone Number")
        dialog_layout = QFormLayout()

        self.new_phone_input = QLineEdit()
        self.new_phone_input.setText(personal_data["phone"])
        self.update_phone_button = QPushButton("Update")
        self.update_phone_button.clicked.connect(self.save_phone)

        dialog_layout.addRow("New Phone Number:", self.new_phone_input)
        dialog_layout.addRow(self.update_phone_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def save_phone(self):
        new_phone = self.new_phone_input.text()
        if new_phone:
            personal_data["phone"] = new_phone
            self.phone_label.setText(f"Phone: {new_phone}")
            QMessageBox.information(self, "Success", "Phone number updated successfully!")
        else:
            QMessageBox.warning(self, "Error", "Phone number cannot be empty!")
