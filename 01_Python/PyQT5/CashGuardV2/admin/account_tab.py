# Admin Tab: Account Tab
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QTabWidget, QFormLayout, QMainWindow, QDateEdit, QComboBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QCalendarWidget, QTextEdit, QDialog, QGridLayout
)
from PyQt5.QtCore import Qt, QDate
from models.account_data import account_data

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