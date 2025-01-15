#############################################################################################################################################
"""Version 1.2"""
#############################################################################################################################################

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QMessageBox, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
import psycopg2
from cryptography.fernet import Fernet
from database.db_handler import create_table, save_image_to_db, retrieve_all_images_from_db
from utils.encryption import encrypt_data, decrypt_data
from psycopg2 import Error
from config.settings import DB_CONFIG, ENCRYPTION_KEY




class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Store and Retrieve")
        self.setGeometry(100, 100, 800, 500)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)

        # Top buttons layout
        top_buttons_layout = QHBoxLayout()
        self.select_button = QPushButton('Select Image')
        self.save_button = QPushButton('Save to Database')
        top_buttons_layout.addWidget(self.select_button)
        top_buttons_layout.addWidget(self.save_button)

        # Bottom buttons layout
        bottom_buttons_layout = QHBoxLayout()
        self.load_button = QPushButton('Load Images')
        self.prev_button = QPushButton('Previous')
        self.next_button = QPushButton('Next')
        self.play_button = QPushButton('Play')
        self.pause_button = QPushButton('Pause')
        bottom_buttons_layout.addWidget(self.load_button)
        bottom_buttons_layout.addWidget(self.prev_button)
        bottom_buttons_layout.addWidget(self.next_button)
        bottom_buttons_layout.addWidget(self.play_button)
        bottom_buttons_layout.addWidget(self.pause_button)

        # Main image and preview frames
        image_frame_layout = QHBoxLayout()
        self.left_preview_label = QLabel()
        self.main_image_label = QLabel()
        self.right_preview_label = QLabel()

        # Set size and styling for labels
        for label in (self.left_preview_label, self.main_image_label, self.right_preview_label):
            label.setStyleSheet("background-color: black; border: 2px solid gray;")
            label.setAlignment(Qt.AlignCenter)

        # Configure main image frame with stretch ratios
        self.main_image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_image_label.setStyleSheet("background-color: black; border: 2px solid yellow;")

        # Add labels to layout with stretch factors for 30:70:30 ratio
        image_frame_layout.addWidget(self.left_preview_label, 3)  # 30%
        image_frame_layout.addWidget(self.main_image_label, 7)   # 70%
        image_frame_layout.addWidget(self.right_preview_label, 3)  # 30%

        main_layout.addLayout(top_buttons_layout)
        main_layout.addLayout(image_frame_layout)
        main_layout.addLayout(bottom_buttons_layout)

        # Connect buttons to actions
        self.select_button.clicked.connect(self.select_image)
        self.save_button.clicked.connect(self.save_to_db)
        self.load_button.clicked.connect(self.load_images)
        self.prev_button.clicked.connect(self.show_previous_image)
        self.next_button.clicked.connect(self.show_next_image)
        self.play_button.clicked.connect(self.start_slideshow)
        self.pause_button.clicked.connect(self.pause_slideshow)

        self.images = []
        self.current_index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next_image)

    def select_image(self):
        file_dialog = QFileDialog()
        self.selected_image_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.selected_image_path:
            pixmap = QPixmap(self.selected_image_path)
            self.main_image_label.setPixmap(pixmap)

    def save_to_db(self):
        if not self.selected_image_path:
            QMessageBox.warning(self, "Warning", "No image selected!")
            return

        try:
            with open(self.selected_image_path, 'rb') as file:
                image_data = file.read()

            encrypted_data = self.encrypt_data(image_data)
            conn = psycopg2.connect(**DB_CONFIG)
            cur = conn.cursor()
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
            QMessageBox.information(self, "Success", "Image saved to database successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save image: {e}")

    def load_images(self):
        self.images.clear()
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            cur = conn.cursor()
            select_query = "SELECT image_data FROM images ORDER BY id ASC"
            cur.execute(select_query)
            records = cur.fetchall()
            cur.close()
            conn.close()

            for record in records:
                encrypted_data = record[0]
                if isinstance(encrypted_data, memoryview):
                    encrypted_data = encrypted_data.tobytes()
                decrypted_data = self.decrypt_data(encrypted_data)
                self.images.append(decrypted_data)

            if self.images:
                self.current_index = 0
                self.show_image()
            else:
                QMessageBox.information(self, "Info", "No images found in the database.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load images: {e}")

    def show_image(self):
        if not self.images:
            return

        pixmap = QPixmap()
        pixmap.loadFromData(self.images[self.current_index])
        self.main_image_label.setPixmap(pixmap)

        if self.current_index > 0:
            prev_pixmap = QPixmap()
            prev_pixmap.loadFromData(self.images[self.current_index - 1])
            self.left_preview_label.setPixmap(prev_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.left_preview_label.clear()

        if self.current_index < len(self.images) - 1:
            next_pixmap = QPixmap()
            next_pixmap.loadFromData(self.images[self.current_index + 1])
            self.right_preview_label.setPixmap(next_pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.right_preview_label.clear()

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()

    def show_next_image(self):
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
            self.show_image()

    def start_slideshow(self):
        self.timer.start(5000)

    def pause_slideshow(self):
        self.timer.stop()

    def encrypt_data(self, data):
        cipher = Fernet(ENCRYPTION_KEY)
        return cipher.encrypt(data)

    def decrypt_data(self, encrypted_data):
        cipher = Fernet(ENCRYPTION_KEY)
        return cipher.decrypt(encrypted_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec_())
