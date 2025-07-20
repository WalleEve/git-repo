import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QTabWidget, QComboBox, QDateEdit, QFormLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QDate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window size
        self.setWindowTitle('Account and Personal Details Form')
        self.setGeometry(100, 100, 700, 800)  # Size: 700x800

        # Initialize SQLite database
        self.db = sqlite3.connect('details.db')
        self.cursor = self.db.cursor()

        # Create tables if they don't exist
        self.create_tables()

        # Create main layout
        layout = QVBoxLayout()

        # Create the tab widget
        tab_widget = QTabWidget()

        # Tab 1: Account Details
        tab1 = QWidget()
        tab1_layout = QFormLayout()

        # Account Details Form Fields
        self.bank_input = QLineEdit()
        self.customer_name_input = QLineEdit()
        self.account_number_input = QLineEdit()
        self.ifsc_input = QLineEdit()
        self.atm_card_no_input = QLineEdit()
        self.cvv_input = QLineEdit()

        tab1_layout.addRow('Bank:', self.bank_input)
        tab1_layout.addRow('Customer Name:', self.customer_name_input)
        tab1_layout.addRow('Account Number:', self.account_number_input)
        tab1_layout.addRow('IFSC:', self.ifsc_input)
        tab1_layout.addRow('ATM Card No:', self.atm_card_no_input)
        tab1_layout.addRow('CVV:', self.cvv_input)

        # Add Submit button
        submit_button1 = QPushButton('Submit')
        submit_button1.clicked.connect(self.submit_account_details)
        tab1_layout.addWidget(submit_button1)

        # Create Account Details Grid
        self.account_grid = QTableWidget()
        self.account_grid.setColumnCount(7)
        self.account_grid.setHorizontalHeaderLabels(
            ['ID', 'Bank', 'Customer Name', 'Account Number', 'IFSC', 'ATM Card No', 'CVV'])
        self.populate_account_grid()
        tab1_layout.addWidget(self.account_grid)

        tab1.setLayout(tab1_layout)

        # Tab 2: UPI Details
        tab2 = QWidget()
        tab2_layout = QFormLayout()

        # UPI Details Form Fields
        self.upi_id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()

        # Linked Bank dropdown (ComboBox)
        self.linked_bank_input = QComboBox()
        self.linked_bank_input.addItems(['SBI', 'ICICI', 'HDFC', 'BOI', 'AXIS'])

        tab2_layout.addRow('UPI ID:', self.upi_id_input)
        tab2_layout.addRow('Name:', self.name_input)
        tab2_layout.addRow('Reg. Phone:', self.phone_input)
        tab2_layout.addRow('Linked Bank:', self.linked_bank_input)

        # Add Submit button
        submit_button2 = QPushButton('Submit')
        submit_button2.clicked.connect(self.submit_upi_details)
        tab2_layout.addWidget(submit_button2)

        # Create UPI Details Grid
        self.upi_grid = QTableWidget()
        self.upi_grid.setColumnCount(5)
        self.upi_grid.setHorizontalHeaderLabels(['ID', 'UPI ID', 'Name', 'Phone', 'Linked Bank'])
        self.populate_upi_grid()
        tab2_layout.addWidget(self.upi_grid)

        tab2.setLayout(tab2_layout)

        # Tab 3: Personal Details
        tab3 = QWidget()
        tab3_layout = QFormLayout()

        # Personal Details Form Fields
        self.p_name_input = QLineEdit()
        self.aadhar_input = QLineEdit()
        self.passport_input = QLineEdit()
        self.passport_expiry_input = QDateEdit()
        self.pan_input = QLineEdit()
        self.dl_input = QLineEdit()
        self.dl_expiry_input = QDateEdit()

        tab3_layout.addRow('Name:', self.p_name_input)
        tab3_layout.addRow('Aadhar Number:', self.aadhar_input)
        tab3_layout.addRow('Passport Number:', self.passport_input)
        tab3_layout.addRow('Expire Date (Passport):', self.passport_expiry_input)
        tab3_layout.addRow('PAN Number:', self.pan_input)
        tab3_layout.addRow('DL Number:', self.dl_input)
        tab3_layout.addRow('Expire Date (DL):', self.dl_expiry_input)

        # Add Submit button
        submit_button3 = QPushButton('Submit')
        submit_button3.clicked.connect(self.submit_personal_details)
        tab3_layout.addWidget(submit_button3)

        # Create Personal Details Grid
        self.personal_grid = QTableWidget()
        self.personal_grid.setColumnCount(8)
        self.personal_grid.setHorizontalHeaderLabels(
            ['ID', 'Name', 'Aadhar', 'Passport No', 'Expiry Date (Passport)', 'PAN', 'DL No', 'Expiry Date (DL)'])
        self.populate_personal_grid()
        tab3_layout.addWidget(self.personal_grid)

        tab3.setLayout(tab3_layout)

        # Add tabs to the tab widget
        tab_widget.addTab(tab1, "Account Details")
        tab_widget.addTab(tab2, "UPI Details")
        tab_widget.addTab(tab3, "Personal Details")

        # Create outer frame
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: #FFCCCC; border: 2px solid #888888;")
        
        # Set layout and add tab widget to the frame
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(tab_widget)
        frame.setLayout(frame_layout)

        # Add frame to the main layout
        layout.addWidget(frame)

        # Set the main layout for the window
        self.setLayout(layout)

    def create_tables(self):
        """Create tables in the database if they don't exist."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS account_details (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               bank TEXT NOT NULL,
                               customer_name TEXT NOT NULL,
                               account_number TEXT NOT NULL,
                               ifsc TEXT NOT NULL,
                               atm_card_no TEXT NOT NULL,
                               cvv TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS upi_details (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               upi_id TEXT NOT NULL,
                               name TEXT NOT NULL,
                               phone TEXT NOT NULL,
                               linked_bank TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personal_details (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT NOT NULL,
                               aadhar_number TEXT NOT NULL,
                               passport_number TEXT NOT NULL,
                               passport_expiry DATE NOT NULL,
                               pan_number TEXT NOT NULL,
                               dl_number TEXT NOT NULL,
                               dl_expiry DATE NOT NULL)''')

        self.db.commit()

    def submit_account_details(self):
        """Insert account details into the database."""
        data = (
            self.bank_input.text(),
            self.customer_name_input.text(),
            self.account_number_input.text(),
            self.ifsc_input.text(),
            self.atm_card_no_input.text(),
            self.cvv_input.text()
        )
        self.cursor.execute('INSERT INTO account_details (bank, customer_name, account_number, ifsc, atm_card_no, cvv) VALUES (?, ?, ?, ?, ?, ?)', data)
        self.db.commit()
        self.populate_account_grid()

    def submit_upi_details(self):
        """Insert UPI details into the database."""
        data = (
            self.upi_id_input.text(),
            self.name_input.text(),
            self.phone_input.text(),
            self.linked_bank_input.currentText()
        )
        self.cursor.execute('INSERT INTO upi_details (upi_id, name, phone, linked_bank) VALUES (?, ?, ?, ?)', data)
        self.db.commit()
        self.populate_upi_grid()

    def submit_personal_details(self):
        """Insert personal details into the database."""
        data = (
            self.p_name_input.text(),
            self.aadhar_input.text(),
            self.passport_input.text(),
            self.passport_expiry_input.date().toString('yyyy-MM-dd'),
            self.pan_input.text(),
            self.dl_input.text(),
            self.dl_expiry_input.date().toString('yyyy-MM-dd')
        )
        self.cursor.execute('INSERT INTO personal_details (name, aadhar_number, passport_number, passport_expiry, pan_number, dl_number, dl_expiry) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
        self.db.commit()
        self.populate_personal_grid()

    def populate_account_grid(self):
        """Populate the account details grid."""
        self.cursor.execute('SELECT * FROM account_details')
        records = self.cursor.fetchall()
        self.account_grid.setRowCount(0)
        for row_number, row_data in enumerate(records):
            self.account_grid.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.account_grid.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def populate_upi_grid(self):
        """Populate the UPI details grid."""
        self.cursor.execute('SELECT * FROM upi_details')
        records = self.cursor.fetchall()
        self.upi_grid.setRowCount(0)
        for row_number, row_data in enumerate(records):
            self.upi_grid.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.upi_grid.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def populate_personal_grid(self):
        """Populate the personal details grid."""
        self.cursor.execute('SELECT * FROM personal_details')
        records = self.cursor.fetchall()
        self.personal_grid.setRowCount(0)
        for row_number, row_data in enumerate(records):
            self.personal_grid.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.personal_grid.setItem(row_number, column_number, QTableWidgetItem(str(data)))


# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
