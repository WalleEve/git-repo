import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap
import psycopg2
from cryptography.fernet import Fernet
import base64

# Generate and store a key (only once, should be securely stored for later use)
# key = Fernet.generate_key()
# print(key)  # Print and save this key securely

# Replace with your securely stored encryption key
ENCRYPTION_KEY = b'oSq58WtVdx4QlGKGVkzf8hc1rifLwJW0ADYlm70wEU8='  # Fernet key must be a 32-byte URL-safe base64 encoded string

# Database configuration
DB_CONFIG = {
    'dbname': 'myDB_080631',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

class ImageApp(QWidget):
    def _init_(self):
        super()._init_()
        #self.setWindowTitle("Image Store and Retrieve")
        #self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Image Store and Retrieve')
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        # Buttons for selecting, saving, and viewing images
        self.select_button = QPushButton('Select Image')
        self.select_button.clicked.connect(self.select_image)
        self.save_button = QPushButton('Save to Database')
        self.save_button.clicked.connect(self.save_to_db)
        self.view_button = QPushButton('View Image from Database')
        self.view_button.clicked.connect(self.view_from_db)

        # Label to display selected or retrieved images
        self.image_label = QLabel()

        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.view_button)
        self.layout.addWidget(self.image_label)
        self.setLayout(self.layout)

        self.selected_image_path = None

    def select_image(self):
        file_dialog = QFileDialog()
        self.selected_image_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.selected_image_path:
            pixmap = QPixmap(self.selected_image_path)
            self.image_label.setPixmap(pixmap)

    def save_to_db(self):
        if not self.selected_image_path:
            return  # No image selected

        # Read and encrypt the image file
        with open(self.selected_image_path, 'rb') as file:
            image_data = file.read()

        encrypted_data = self.encrypt_data(image_data)

        # Connect to PostgreSQL and insert the encrypted image
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Make sure your table has been created with an image_data column to store bytea data
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS images (
            id SERIAL PRIMARY KEY,
            image_data BYTEA NOT NULL
        );
        '''
        cur.execute(create_table_query)
        conn.commit()

        insert_query = "INSERT INTO images (image_data) VALUES (%s)"
        cur.execute(insert_query, (encrypted_data,))
        conn.commit()

        cur.close()
        conn.close()

        print("Image saved to database successfully!")

    def view_from_db(self):
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Retrieve the last inserted image (for demonstration, you may want to retrieve specific records)
        select_query = "SELECT image_data FROM images ORDER BY id DESC LIMIT 1"
        cur.execute(select_query)
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            encrypted_data = result[0]
            decrypted_data = self.decrypt_data(encrypted_data)

            # Display the retrieved image
            self.show_image(decrypted_data)

    def encrypt_data(self, data):
        cipher = Fernet(ENCRYPTION_KEY)
        encrypted_data = cipher.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        cipher = Fernet(ENCRYPTION_KEY)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data

    def show_image(self, image_data):
        # Save image to a temporary file to display it
        temp_image_path = 'temp_image.png'
        with open(temp_image_path, 'wb') as file:
            file.write(image_data)

        # Display the image using QPixmap
        pixmap = QPixmap(temp_image_path)
        self.image_label.setPixmap(pixmap)

        # Optionally, delete the temporary file after display (or keep it for caching purposes)
        os.remove(temp_image_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec_())