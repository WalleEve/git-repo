from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit,
                             QComboBox, QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class AdminTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Admin Payment Details")

        # Password Authentication
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.otp_label = QLabel("OTP:")
        self.otp_input = QLineEdit()

        # Payment Details Section
        self.payment_merchant_label = QLabel("Payment Merchant:")
        self.payment_merchant_combo = QComboBox()
        self.payment_merchant_combo.addItems(["GPay", "PhonePay", "AmazonPay"])
        self.upi_id_label = QLabel("UPI ID:")
        self.upi_id_input = QLineEdit()
        self.linked_mobile_label = QLabel("Linked Mobile Number:")
        self.linked_mobile_input = QLineEdit()

        # Bank Account Details Section
        self.bank_name_label = QLabel("Bank Name:")
        self.bank_name_input = QLineEdit()
        self.account_number_label = QLabel("Account Number:")
        self.account_number_input = QLineEdit()
        self.account_holder_name_label = QLabel("Account Holder Name:")
        self.account_holder_name_input = QLineEdit()
        self.ifsc_code_label = QLabel("IFSC Code:")
        self.ifsc_code_input = QLineEdit()
        self.atm_card_number_label = QLabel("ATM Card Number:")
        self.atm_card_number_input = QLineEdit()
        self.cvv_label = QLabel("CVV:")
        self.cvv_input = QLineEdit()
        self.internet_banking_label = QLabel("Internet Banking:")
        self.internet_banking_combo = QComboBox()
        self.internet_banking_combo.addItems(["Yes", "No"])
        self.user_id_label = QLabel("User ID:")
        self.user_id_input = QLineEdit()
        self.internet_banking_password_label = QLabel("Password:")
        self.internet_banking_password_input = QLineEdit()
        self.internet_banking_password_input.setEchoMode(QLineEdit.Password)
        self.bank_linked_mobile_label = QLabel("Linked Mobile Number:")
        self.bank_linked_mobile_input = QLineEdit()

        # Personal ID Details Section
        self.id_number_label = QLabel("ID Number:")
        self.id_number_input = QLineEdit()
        self.id_name_label = QLabel("Name:")
        self.id_name_input = QLineEdit()
        self.dob_label = QLabel("Date of Birth:")
        self.dob_input = QLineEdit()
        self.id_type_label = QLabel("ID Type:")
        self.id_type_combo = QComboBox()
        self.id_type_combo.addItems(["PAN", "AADHAR", "DL"])

        # Buttons
        self.submit_button = QPushButton("Submit")

        # Layout
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.username_label, 0, 0)
        grid_layout.addWidget(self.username_input, 0, 1)
        grid_layout.addWidget(self.password_label, 1, 0)
        grid_layout.addWidget(self.password_input, 1, 1)
        grid_layout.addWidget(self.otp_label, 2, 0)
        grid_layout.addWidget(self.otp_input, 2, 1)

        # Payment Details Layout
        payment_layout = QVBoxLayout()
        payment_layout.addWidget(QLabel("Payment Details"))
        payment_layout.addWidget(self.payment_merchant_label)
        payment_layout.addWidget(self.payment_merchant_combo)
        payment_layout.addWidget(self.upi_id_label)
        payment_layout.addWidget(self.upi_id_input)
        payment_layout.addWidget(self.linked_mobile_label)
        payment_layout.addWidget(self.linked_mobile_input)

        # Bank Account Details Layout
        bank_layout = QVBoxLayout()
        bank_layout.addWidget(QLabel("Bank Account Details"))
        bank_layout.addWidget(self.bank_name_label)
        bank_layout.addWidget(self.bank_name_input)
        bank_layout.addWidget(self.account_number_label)
        bank_layout.addWidget(self.account_number_input)
        bank_layout.addWidget(self.account_holder_name_label)
        bank_layout.addWidget(self.account_holder_name_input)
        bank_layout.addWidget(self.ifsc_code_label)
        bank_layout.addWidget(self.ifsc_code_input)
        bank_layout.addWidget(self.atm_card_number_label)
        bank_layout.addWidget(self.atm_card_number_input)
        bank_layout.addWidget(self.cvv_label)
        bank_layout.addWidget(self.cvv_input)
        bank_layout.addWidget(self.internet_banking_label)
        bank_layout.addWidget(self.internet_banking_combo)
        bank_layout.addWidget(self.user_id_label)
        bank_layout.addWidget(self.user_id_input)
        bank_layout.addWidget(self.internet_banking_password_label)
        bank_layout.addWidget(self.internet_banking_password_input)
        bank_layout.addWidget(self.bank_linked_mobile_label)
        bank_layout.addWidget(self.bank_linked_mobile_input)

        # Personal ID Details Layout
        id_layout = QVBoxLayout()
        id_layout.addWidget(QLabel("Personal ID Details"))
        id_layout.addWidget(self.id_number_label)
        id_layout.addWidget(self.id_number_input)
        id_layout.addWidget(self.id_name_label)
        id_layout.addWidget(self.id_name_input)
        id_layout.addWidget(self.dob_label)
        id_layout.addWidget(self.dob_input)
        id_layout.addWidget(self.id_type_label)
        id_layout.addWidget(self.id_type_combo)

        # Main Layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(payment_layout)
        main_layout.addLayout(bank_layout)
        main_layout.addLayout(id_layout)

        # Button Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)

        # Final Layout
        vbox = QVBoxLayout()
        vbox.addLayout(main_layout)
        vbox.addLayout(button_layout)
        self.setLayout(vbox)

        # Connect Submit Button
        self.submit_button.clicked.connect(self.submit_details)

    def submit_details(self):
        # Implement logic to validate user input,
        # send data to database, and handle success/failure
        print("Submit button clicked!")
        # Example:
        username = self.username_input.text()
        password = self.password_input.text()
        # ... other data collection
        # ... database interaction
        # ... success/failure handling

if __name__ == '__main__':
    app = QApplication([])
    window = AdminTab()
    window.show()
    app.exec_()

