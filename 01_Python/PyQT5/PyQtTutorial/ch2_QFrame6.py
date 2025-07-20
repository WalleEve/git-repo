import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QTabWidget, QComboBox, QDateEdit, QFormLayout
from PyQt5.QtCore import QDate

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window size
        self.setWindowTitle('Account and Personal Details Form')
        self.setGeometry(100, 100, 700, 800)  # Size: 700x800

        # Create main layout
        layout = QVBoxLayout()

        # Create the tab widget
        tab_widget = QTabWidget()

        # Tab 1: Account Details
        tab1 = QWidget()
        tab1_layout = QFormLayout()

        tab1_layout.addRow('Bank:', QLineEdit())  # Bank field
        tab1_layout.addRow('Customer Name:', QLineEdit())  # Customer Name field
        tab1_layout.addRow('Account Number:', QLineEdit())  # Account Number field
        tab1_layout.addRow('IFSC:', QLineEdit())  # IFSC field
        tab1_layout.addRow('ATM Card No:', QLineEdit())  # ATM Card No field
        tab1_layout.addRow('CVV:', QLineEdit())  # CVV field

        # Add a submit button
        submit_button1 = QPushButton('Submit')
        tab1_layout.addWidget(submit_button1)

        tab1.setLayout(tab1_layout)
        
        # Tab 2: UPI Details
        tab2 = QWidget()
        tab2_layout = QFormLayout()

        tab2_layout.addRow('UPI ID:', QLineEdit())  # UPI ID field
        tab2_layout.addRow('Name:', QLineEdit())  # Name field
        tab2_layout.addRow('Reg. Phone:', QLineEdit())  # Registered Phone field

        # Linked Bank dropdown (ComboBox)
        linked_bank = QComboBox()
        linked_bank.addItems(['SBI', 'ICICI', 'HDFC', 'BOI', 'AXIS'])
        tab2_layout.addRow('Linked Bank:', linked_bank)

        # Add a submit button
        submit_button2 = QPushButton('Submit')
        tab2_layout.addWidget(submit_button2)

        tab2.setLayout(tab2_layout)

        # Tab 3: Personal Details
        tab3 = QWidget()
        tab3_layout = QFormLayout()

        tab3_layout.addRow('Name:', QLineEdit())  # Name field
        tab3_layout.addRow('Aadhar Number:', QLineEdit())  # Aadhar Number field
        tab3_layout.addRow('Passport Number:', QLineEdit())  # Passport Number field

        # Expiry Date fields (for Passport and DL)
        tab3_layout.addRow('Expire Date (Passport):', QDateEdit())
        tab3_layout.addRow('PAN Number:', QLineEdit())  # PAN Number field
        tab3_layout.addRow('DL Number:', QLineEdit())  # DL Number field
        tab3_layout.addRow('Expire Date (DL):', QDateEdit())

        # Add a submit button
        submit_button3 = QPushButton('Submit')
        tab3_layout.addWidget(submit_button3)

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

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
