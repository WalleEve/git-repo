import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QTabWidget, QSplitter, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Details Form Application')
        self.setGeometry(100, 100, 700, 800)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the tab widget
        tab_widget = QTabWidget()

        # Tab 1: Bank Details
        tab1 = QWidget()
        tab1_layout = QHBoxLayout()

        # Split the tab into Entry Frame (70%) and CRUD Frame (30%)
        splitter1 = QSplitter(Qt.Horizontal)

        # Entry Frame for Bank Details
        entry_frame1 = self.create_entry_frame_bank()
        # CRUD Frame for Bank Details (Data table)
        crud_frame1 = self.create_crud_frame_bank()

        # Add frames to the splitter
        splitter1.addWidget(entry_frame1)
        splitter1.addWidget(crud_frame1)

        # Add splitter to the tab layout
        tab1_layout.addWidget(splitter1)
        tab1.setLayout(tab1_layout)

        # Tab 2: UPI Details
        tab2 = QWidget()
        tab2_layout = QHBoxLayout()

        # Split the tab into Entry Frame (70%) and CRUD Frame (30%)
        splitter2 = QSplitter(Qt.Horizontal)

        # Entry Frame for UPI Details
        entry_frame2 = self.create_entry_frame_upi()
        # CRUD Frame for UPI Details (Data table)
        crud_frame2 = self.create_crud_frame_upi()

        # Add frames to the splitter
        splitter2.addWidget(entry_frame2)
        splitter2.addWidget(crud_frame2)

        # Add splitter to the tab layout
        tab2_layout.addWidget(splitter2)
        tab2.setLayout(tab2_layout)

        # Tab 3: Personal Details
        tab3 = QWidget()
        tab3_layout = QHBoxLayout()

        # Split the tab into Entry Frame (70%) and CRUD Frame (30%)
        splitter3 = QSplitter(Qt.Horizontal)

        # Entry Frame for Personal Details
        entry_frame3 = self.create_entry_frame_personal()
        # CRUD Frame for Personal Details (Data table)
        crud_frame3 = self.create_crud_frame_personal()

        # Add frames to the splitter
        splitter3.addWidget(entry_frame3)
        splitter3.addWidget(crud_frame3)

        # Add splitter to the tab layout
        tab3_layout.addWidget(splitter3)
        tab3.setLayout(tab3_layout)

        # Tab 4: User Details
        tab4 = QWidget()
        tab4_layout = QHBoxLayout()

        # Split the tab into Entry Frame (70%) and CRUD Frame (30%)
        splitter4 = QSplitter(Qt.Horizontal)

        # Entry Frame for User Details
        entry_frame4 = self.create_entry_frame_user()
        # CRUD Frame for User Details (Data table)
        crud_frame4 = self.create_crud_frame_user()

        # Add frames to the splitter
        splitter4.addWidget(entry_frame4)
        splitter4.addWidget(crud_frame4)

        # Add splitter to the tab layout
        tab4_layout.addWidget(splitter4)
        tab4.setLayout(tab4_layout)

        # Add all tabs to the tab widget
        tab_widget.addTab(tab1, "Bank Details")
        tab_widget.addTab(tab2, "UPI Details")
        tab_widget.addTab(tab3, "Personal Details")
        tab_widget.addTab(tab4, "User Details")

        # Add tab widget to the main layout
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def create_entry_frame_bank(self):
        """Create entry frame for Bank Details."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: lightgray;")

        layout = QFormLayout()

        layout.addRow("Bank Name:", QLineEdit())
        layout.addRow("Account Number:", QLineEdit())
        layout.addRow("IFSC:", QLineEdit())
        layout.addRow("ATM Card Number:", QLineEdit())
        layout.addRow("CVV:", QLineEdit())

        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)

        frame.setLayout(layout)
        return frame

    def create_crud_frame_bank(self):
        """Create CRUD frame for Bank Details (Display in Table)."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()

        # Create a table to display data
        self.bank_table = QTableWidget()
        self.bank_table.setColumnCount(5)
        self.bank_table.setHorizontalHeaderLabels(["Bank Name", "Account No", "IFSC", "ATM Card", "CVV"])

        layout.addWidget(self.bank_table)

        frame.setLayout(layout)
        return frame

    def create_entry_frame_upi(self):
        """Create entry frame for UPI Details."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: lightgray;")

        layout = QFormLayout()

        layout.addRow("UPI ID:", QLineEdit())
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Phone:", QLineEdit())

        linked_bank_combobox = QComboBox()
        linked_bank_combobox.addItems(["SBI", "ICICI", "HDFC", "BOI", "AXIS"])
        layout.addRow("Linked Bank:", linked_bank_combobox)

        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)

        frame.setLayout(layout)
        return frame

    def create_crud_frame_upi(self):
        """Create CRUD frame for UPI Details (Display in Table)."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()

        # Create a table to display data
        self.upi_table = QTableWidget()
        self.upi_table.setColumnCount(4)
        self.upi_table.setHorizontalHeaderLabels(["UPI ID", "Name", "Phone", "Linked Bank"])

        layout.addWidget(self.upi_table)

        frame.setLayout(layout)
        return frame

    def create_entry_frame_personal(self):
        """Create entry frame for Personal Details."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: lightgray;")

        layout = QFormLayout()

        layout.addRow("Name:", QLineEdit())
        layout.addRow("Aadhar Number:", QLineEdit())
        layout.addRow("Passport Number:", QLineEdit())
        layout.addRow("PAN Number:", QLineEdit())
        layout.addRow("DL Number:", QLineEdit())

        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)

        frame.setLayout(layout)
        return frame

    def create_crud_frame_personal(self):
        """Create CRUD frame for Personal Details (Display in Table)."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()

        # Create a table to display data
        self.personal_table = QTableWidget()
        self.personal_table.setColumnCount(6)
        self.personal_table.setHorizontalHeaderLabels(["Name", "Aadhar No", "Passport No", "PAN No", "DL No"])

        layout.addWidget(self.personal_table)

        frame.setLayout(layout)
        return frame

    def create_entry_frame_user(self):
        """Create entry frame for User Details."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: lightgray;")

        layout = QFormLayout()

        layout.addRow("Username:", QLineEdit())
        layout.addRow("Password:", QLineEdit())
        layout.addRow("Email:", QLineEdit())

        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)

        frame.setLayout(layout)
        return frame

    def create_crud_frame_user(self):
        """Create CRUD frame for User Details (Display in Table)."""
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()

        # Create a table to display data
        self.user_table = QTableWidget()
        self.user_table.setColumnCount(3)
        self.user_table.setHorizontalHeaderLabels(["Username", "Email", "Password"])

        layout.addWidget(self.user_table)

        frame.setLayout(layout)
        return frame


# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
