import sys 

import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox 
from PyQt5.QtCore import QDateTime 

# Database Connection 
def create_connection():
	try:
		connection = psycopg2.connect(
			host="localhost",
			database="PyQt5_DB",
			user="postgres",
			password="postgres",
			port= 5432
		)
		return connection 
	except Exception as e:
		print(f"Error connection to PostgreSQL: {e}")
		return None 

# Main Window (login WIndow)
class LoginWindow(QWidget):
	def __init__(self):
		super().__init__()
		
		# Window properties 
		self.setWindowTitle("Login WIndow")
		self.setGeometry(100, 100, 300, 200)
		
		# create labels 
		self.label_user = QLabel("Username: ", self)
		self.label_user.move(20, 30)
		
		self.label_password = QLabel('Password: ', self)
		self.label_password.move(20, 70)
		
		# Create input fields 
		self.input_user = QLineEdit(self)
		self.input_user.move(100, 30)
		self.input_user.setPlaceholderText("Enter username")
		
		self.input_password = QLineEdit(self)
		self.input_password.move(100, 70)
		self.input_password.setEchoMode(QLineEdit.Password)
		self.input_password.setPlaceholderText("Enter password")
		
		# Create Buttons 
		self.button_login = QPushButton('Login', self)
		self.button_login.move(100, 120)
		self.button_login.clicked.connect(self.login)
		
	def login(self):
		username = self.input_user.text()
		password = self.input_password.text()
		
		# Call the authenticate function 
		if authenticate_user(username, password):
			self.update_last_login(username)
			QMessageBox.information(self, "Success", "Login Successfull!")
			self.input_user.clear()
			self.input_password.clear()
		else:
			QMessageBox.warning(self, "Failed", "Incorrect username or password!")
	
	# update last_login after sucessfull login 
	def update_last_login(self, username):
		connection = create_connection()
		if connection is not None:
			try:
				cursor = connection.cursor()
				current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
				cursor.execute(
				"UPDATE users SET last_login = %s WHERE user_name = %s", (current_time, username) 
				)
				connection.commit()
				cursor.close()
			except Exception as e:
				QMessageBox.warning(self, "Error", f"Failed to update last_login: {e}")
			finally:
				connection.close()
				
def authenticate_user(username, password):
	connection = create_connection()
	if connection is not None:
		try:
			cursor = connection.cursor()
			cursor.execute(
			"SELECT * FROM users WHERE user_name = %s and password = %s", (username, password)
			)
			result = cursor.fetchone()
			cursor.close()
			
			if result:
				return True
			else:
				return False 
		except Exception as e:
			print(f"Error during authentication: {e}")
			return False 
		finally:
			connection.close()
			
		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = LoginWindow()
	window.show()
	sys.exit(app.exec_())
