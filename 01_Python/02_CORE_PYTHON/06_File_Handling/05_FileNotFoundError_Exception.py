# Handling the FileNotFoundError Exception 

filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contects = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file {} does not exist.".format(filename)
	print(msg)


