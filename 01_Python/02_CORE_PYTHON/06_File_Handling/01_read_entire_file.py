# File Handling 
# Reading an Entire File 

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)


with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())


# File Path 
file_path = "C:/Users/Sayed/Desktop/RoadMap/Python/06_File_Handling/pi_digits.txt"

with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

