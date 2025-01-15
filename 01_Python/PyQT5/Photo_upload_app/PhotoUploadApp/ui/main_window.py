#############################################################################################################################################
"""Version 1.0"""
#############################################################################################################################################

import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from database.db_handler import create_table, save_image_to_db, retrieve_all_images_from_db
from utils.encryption import encrypt_data, decrypt_data
import psycopg2
from psycopg2 import Error
from config.settings import DB_CONFIG

# from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
# from PyQt5.QtGui import QPixmap, QPalette, QColor
# from PyQt5.QtCore import Qt, QTimer
# from database.db_handler import create_table, save_image_to_db, retrieve_all_images_from_db
# from utils.encryption import encrypt_data, decrypt_data
# import os

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Store and Retrieve")
        self.setGeometry(100, 100, 600, 500)
        self.set_background_color()
        self.init_ui()
        create_table()
        self.images = []
        self.current_index = -1
        self.timer = QTimer()
        self.timer.setInterval(5000)  # 5 seconds
        self.timer.timeout.connect(self.show_next_image)

    def set_background_color(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        self.setPalette(palette)

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # First row: Select and Save buttons
        first_row = QHBoxLayout()
        self.select_button = QPushButton('Select Images')
        self.select_button.clicked.connect(self.select_images)
        self.save_button = QPushButton('Save to Database')
        self.save_button.clicked.connect(self.save_to_db)
        first_row.addWidget(self.select_button)
        first_row.addWidget(self.save_button)

        # Second row: Load, Previous, Next, Play, and Pause buttons
        second_row = QHBoxLayout()
        self.view_button = QPushButton('Load Images from Database')
        self.view_button.clicked.connect(self.load_images_from_db)
        self.previous_button = QPushButton('Previous')
        self.previous_button.clicked.connect(self.show_previous_image)
        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.show_next_image)
        self.play_button = QPushButton('Play')
        self.play_button.clicked.connect(self.start_slideshow)
        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.stop_slideshow)
        
        second_row.addWidget(self.view_button)
        second_row.addWidget(self.previous_button)
        second_row.addWidget(self.next_button)
        second_row.addWidget(self.play_button)
        second_row.addWidget(self.pause_button)

        # Image display label with fixed size and styled border
        self.image_label = QLabel()
        self.image_label.setFixedSize(300, 300)
        self.image_label.setStyleSheet("border: 2px solid #4CAF50;")  # Green border
        self.image_label.setAlignment(Qt.AlignCenter)

        # Add layouts to main layout
        main_layout.addLayout(first_row)
        main_layout.addLayout(second_row)
        main_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Disable navigation and play buttons initially
        self.next_button.setEnabled(False)
        self.previous_button.setEnabled(False)
        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(False)

        self.selected_image_paths = []

    def select_images(self):
        file_dialog = QFileDialog()
        self.selected_image_paths, _ = file_dialog.getOpenFileNames(self, "Select Images", "", "Images (*.png *.jpg *.jpeg)")
        if self.selected_image_paths:
            pixmap = QPixmap(self.selected_image_paths[0])
            self.display_image(pixmap)

    def display_image(self, pixmap):
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)

    def save_to_db(self):
        if not self.selected_image_paths:
            QMessageBox.warning(self, "Warning", "No images selected!")
            return

        try:
            for image_path in self.selected_image_paths:
                with open(image_path, 'rb') as file:
                    image_data = file.read()
                
                encrypted_data = encrypt_data(image_data)
                if save_image_to_db(encrypted_data):
                    print(f"Image {image_path} saved successfully!")
                else:
                    QMessageBox.critical(self, "Error", f"Failed to save image: {image_path}")
            
            QMessageBox.information(self, "Success", "All selected images saved to database successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def load_images_from_db(self):
        self.images = retrieve_all_images_from_db()
        if self.images:
            self.current_index = 0
            self.show_image(self.current_index)
            self.update_navigation_buttons()
        else:
            QMessageBox.information(self, "Info", "No images found in the database.")

    def show_image(self, index):
        encrypted_data = self.images[index]
        decrypted_data = decrypt_data(encrypted_data)
        
        temp_image_path = 'temp_image.png'
        with open(temp_image_path, 'wb') as file:
            file.write(decrypted_data)

        pixmap = QPixmap(temp_image_path)
        self.display_image(pixmap)
        os.remove(temp_image_path)

    def show_next_image(self):
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
        else:
            self.current_index = 0  # Loop back to the first image
        self.show_image(self.current_index)
        self.update_navigation_buttons()

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
        else:
            self.current_index = len(self.images) - 1  # Loop back to the last image
        self.show_image(self.current_index)
        self.update_navigation_buttons()

    def start_slideshow(self):
        self.timer.start()
        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(True)

    def stop_slideshow(self):
        self.timer.stop()
        self.play_button.setEnabled(True)
        self.pause_button.setEnabled(False)

    def update_navigation_buttons(self):
        has_images = len(self.images) > 1
        self.previous_button.setEnabled(has_images)
        self.next_button.setEnabled(has_images)
        self.play_button.setEnabled(has_images)
        self.pause_button.setEnabled(False)
