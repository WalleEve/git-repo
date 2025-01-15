# select function a module 
from sys import argv

# passing file name using argv 
script, filename = argv

file = open(filename, 'r+')

print(file.read())

line1 = input("enter new line: ")

file.write("\n")
file.write(line1)
 
file = open(filename, 'r+')
print(file.read())




