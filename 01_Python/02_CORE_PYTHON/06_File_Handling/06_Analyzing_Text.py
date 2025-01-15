# Analyzing Text 
import os 

os.system('cls')

title = "Alice in Wanderland"
print(title.split())



filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contects = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file {} does not exist".format(filename)
	print(msg)
else:
	# Count the approximate number of words in the file
	words = contects.split()
	num_words = len(words)
	print("The file {} has about {} words".format(filename, num_words))




