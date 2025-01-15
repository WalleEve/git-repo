# UNITILY PROGRAMS 

# Class for all Utility Programs 

# Import Modules 

import os   
import sys  
import datetime
from os.path import exists # for check_if_file_exists() method
from pathlib import Path  # for check_if_this_is_a_file() method 



class MyUtility():


	""" Utility Programs for Daily Use """

	def __init__(self):
		self.pwd = os.getcwd()



	def check_if_file_exists(self, file_name, file_path=None):
		""" 
		When processing files, we’ll often want to check if a file exists before doing something 
		else with it such as reading from the file or writing to it.
		To do it, you can use the exists() function from the os.path 
		module or is_file() method from the Path class in the pathlib module.
		"""
		if file_path == None:
			file_path = self.pwd

		#print(file_path)
		full_path = file_path + '\\' + file_name 
		#print(full_path)
		file_exists = exists(full_path)
		#print(file_exists)
		if file_exists:
			return file_exists 
		else:
			return f"Sorry File {file_name} does not Exits in the Path: {full_path}"

	def check_if_this_is_a_file(self, file_name, file_path = None):
		if file_path == None:
			file_path = self.pwd
		full_path = file_path + '\\' + file_name
		path = Path(full_path)
		status = path.is_file()
		if status == path.is_file():
			return "File"  
		elif status == path.is_dir():
			return "Directory"
		else:
			return f"Sorry Given name {file_name} does not Exits in the Path: {full_path}"

		

def main():
	myut = MyUtility()

	file_status = myut.check_if_file_exists('TestRun2.py')
	if file_status == True:
		print("File Exits")
	else:
		print(file_status)

	search_status = myut.check_if_this_is_a_file('PythonDemoProjects')
	if search_status == 'File':
		print("This is a File")
	elif search_status == 'Directory':
		print("This is a Directory")
	else:
		print(search_status)

if __name__ == "__main__":
	main()



