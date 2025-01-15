from sys import argv 

script, fileName = argv
text = open(fileName)

print(text.read())

