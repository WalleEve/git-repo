# Admin Tab: Personal Tab
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QTabWidget, QFormLayout, QMainWindow, QDateEdit, QComboBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QCalendarWidget, QTextEdit, QDialog, QGridLayout
)
from PyQt5.QtCore import Qt, QDate
from models import personal_data

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