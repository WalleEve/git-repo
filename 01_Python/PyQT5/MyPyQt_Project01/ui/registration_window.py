from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from db.db import insert_user_info, insert_user_credentials
import random

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Registration")
        self.setGeometry(200, 200, 400, 400)
        self.create_registration_ui()

    def create_registration_ui(self):
        self.label_name = QLabel('Name: ', self)
        self.label_name.move(30, 30)
        self.input_name = QLineEdit(self)
        self.input_name.move(150, 30)

        self.label_email = QLabel('Email:', self)
        self.label_email.move(30, 70)
        self.input_email = QLineEdit(self)
        self.input_email.move(150, 70)

        self.label_phone = QLabel('Phone:', self)
        self.label_phone.move(30, 110)
        self.input_phone = QLineEdit(self)
        self.input_phone.move(150, 110)

        self.label_age = QLabel('Age:', self)
        self.label_age.move(30, 150)
        self.input_age = QLineEdit(self)
        self.input_age.move(150, 150)

        self.label_gender = QLabel('Gender:', self)
        self.label_gender.move(30, 190)
        self.input_gender = QLineEdit(self)
        self.input_gender.move(150, 190)

        self.label_address = QLabel('Address:', self)
        self.label_address.move(30, 230)
        self.input_address = QLineEdit(self)
        self.input_address.move(150, 230)

        self.label_aadhar = QLabel('Aadhar:', self)
        self.label_aadhar.move(30, 270)
        self.input_aadhar = QLineEdit(self)
        self.input_aadhar.move(150, 270)

        self.button_register = QPushButton('Submit', self)
        self.button_register.move(150, 320)
        self.button_register.clicked.connect(self.register_user)


    def register_user(self):
        name = self.input_name.text()
        email = self.input_email.text()
        phone = self.input_phone.text()
        age = self.input_age.text()
        gender = self.input_gender.text()
        address = self.input_address.text()
        aadhar_number = self.input_aadhar.text()

        if not (name and email and phone and aadhar_number):
            QMessageBox.warning(self, "Input Error", "Please fill in all mandatory fields.")
            return
        user_id = insert_user_info(name, email, phone, age, gender, address, aadhar_number)

        # Generate username and password based on name
        username = name.lower() + str(random.randint(100, 999))
        password = 'pass' + str(random.randint(1000, 9999))

        insert_user_credentials(user_id, username, password)

        QMessageBox.information(self, "Registration Successfull", f"username: {username}\nPassword: {password}")
        self.close()


    
