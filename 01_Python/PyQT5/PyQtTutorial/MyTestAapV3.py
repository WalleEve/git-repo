import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QTabWidget, QFormLayout, QMainWindow, QTableWidget, QTableWidgetItem, 
    QDateEdit, QDialog, QGridLayout, QHeaderView
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

# Simulated Data Storage
user_data = {
    "phone": "1234567890",
    "email": "user@example.com",
    "password": "old_password"
}

account_data = []
personal_data = []

# Admin Tab: User Tab
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

# Admin Tab: Account Tab
class AccountTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Account Details Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.bank_input = QLineEdit()
        self.ac_no_input = QLineEdit()
        self.ifsc_input = QLineEdit()
        self.reg_mob_input = QLineEdit()
        self.reg_email_input = QLineEdit()
        self.net_banking_user_input = QLineEdit()
        self.net_banking_password_input = QLineEdit()
        self.atm_card_no_input = QLineEdit()
        self.cvv_input = QLineEdit()
        self.pin_input = QLineEdit()
        self.upi_reg_mob_input = QLineEdit()
        self.upi_id_input = QLineEdit()
        self.upi_pin_input = QLineEdit()

        self.add_button = QPushButton("Add Account")
        self.add_button.clicked.connect(self.add_account)

        frame1_layout.addRow("Name:", self.name_input)
        frame1_layout.addRow("Bank:", self.bank_input)
        frame1_layout.addRow("Account No:", self.ac_no_input)
        frame1_layout.addRow("IFSC:", self.ifsc_input)
        frame1_layout.addRow("Registered Mobile:", self.reg_mob_input)
        frame1_layout.addRow("Registered Email:", self.reg_email_input)
        frame1_layout.addRow("Net Banking User:", self.net_banking_user_input)
        frame1_layout.addRow("Net Banking Password:", self.net_banking_password_input)
        frame1_layout.addRow("ATM Card No:", self.atm_card_no_input)
        frame1_layout.addRow("CVV:", self.cvv_input)
        frame1_layout.addRow("PIN:", self.pin_input)
        frame1_layout.addRow("UPI Registered Mobile:", self.upi_reg_mob_input)
        frame1_layout.addRow("UPI ID:", self.upi_id_input)
        frame1_layout.addRow("UPI PIN:", self.upi_pin_input)
        frame1_layout.addRow(self.add_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Grid View
        self.account_table = QTableWidget()
        self.account_table.setColumnCount(14)
        self.account_table.setHorizontalHeaderLabels([
            "Name", "Bank", "Account No", "IFSC", "Reg Mob", "Reg Email", "Net Banking User",
            "Net Banking Password", "ATM Card No", "CVV", "PIN", "UPI Reg Mob", "UPI ID", "UPI PIN"
        ])
        self.account_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(self.account_table)
        self.setLayout(layout)

    def add_account(self):
        account = [
            self.name_input.text(),
            self.bank_input.text(),
            self.ac_no_input.text(),
            self.ifsc_input.text(),
            self.reg_mob_input.text(),
            self.reg_email_input.text(),
            self.net_banking_user_input.text(),
            self.net_banking_password_input.text(),
            self.atm_card_no_input.text(),
            self.cvv_input.text(),
            self.pin_input.text(),
            self.upi_reg_mob_input.text(),
            self.upi_id_input.text(),
            self.upi_pin_input.text()
        ]
        account_data.append(account)
        self.load_accounts()

    def load_accounts(self):
        self.account_table.setRowCount(len(account_data))
        for row, account in enumerate(account_data):
            for col, value in enumerate(account):
                item = QTableWidgetItem(value)
                self.account_table.setItem(row, col, item)

# Admin Tab: Personal Tab
class PersonalTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Personal Details Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.dob_input = QDateEdit()
        self.dob_input.setCalendarPopup(True)
        self.address_input = QLineEdit()
        self.pan_input = QLineEdit()
        self.aadhar_input = QLineEdit()
        self.passport_input = QLineEdit()
        self.voter_id_input = QLineEdit()

        self.add_button = QPushButton("Add Personal Details")
        self.add_button.clicked.connect(self.add_personal_details)

        frame1_layout.addRow("Account Holder Name:", self.name_input)
        frame1_layout.addRow("Date of Birth:", self.dob_input)
        frame1_layout.addRow("Address:", self.address_input)
        frame1_layout.addRow("PAN:", self.pan_input)
        frame1_layout.addRow("AADHAR:", self.aadhar_input)
        frame1_layout.addRow("PASSPORT:", self.passport_input)
        frame1_layout.addRow("Voter ID:", self.voter_id_input)
        frame1_layout.addRow(self.add_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Grid View
        self.personal_table = QTableWidget()
        self.personal_table.setColumnCount(7)
        self.personal_table.setHorizontalHeaderLabels([
            "Name", "DOB", "Address", "PAN", "AADHAR", "PASSPORT", "Voter ID"
        ])
        self.personal_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(self.personal_table)
        self.setLayout(layout)

    def add_personal_details(self):
        personal = [
            self.name_input.text(),
            self.dob_input.date().toString("yyyy-MM-dd"),
            self.address_input.text(),
            f"****{self.pan_input.text()[-4:]}",
            f"****{self.aadhar_input.text()[-4:]}",
            f"****{self.passport_input.text()[-4:]}",
            f"****{self.voter_id_input.text()[-4:]}"
        ]
        personal_data.append(personal)
        self.load_personal_details()

    def load_personal_details(self):
        self.personal_table.setRowCount(len(personal_data))
        for row, personal in enumerate(personal_data):
            for col, value in enumerate(personal):
                item = QTableWidgetItem(value)
                self.personal_table.setItem(row, col, item)

# Main Window with Admin Tab
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cash+Guard")
        self.setGeometry(100, 100, 800, 600)

        # Create a tab widget
        self.tabs = QTabWidget()

        # Add Admin Tab with sub-tabs
        self.admin_tab = QWidget()
        self.admin_tab_layout = QVBoxLayout()

        self.admin_sub_tabs = QTabWidget()
        self.admin_sub_tabs.addTab(UserTab(), "User")
        self.admin_sub_tabs.addTab(AccountTab(), "Account")
        self.admin_sub_tabs.addTab(PersonalTab(), "Personal")

        self.admin_tab_layout.addWidget(self.admin_sub_tabs)
        self.admin_tab.setLayout(self.admin_tab_layout)

        self.tabs.addTab(self.admin_tab, "Admin")
        self.setCentralWidget(self.tabs)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Modern style
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())