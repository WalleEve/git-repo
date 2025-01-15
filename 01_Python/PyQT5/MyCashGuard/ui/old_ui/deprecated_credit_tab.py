### ui/credit_tab.py
# Module for the Daily credit Tracking tab

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QMessageBox
)
from PyQt5.QtCore import QDate

class CreditTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.layout = QVBoxLayout()

