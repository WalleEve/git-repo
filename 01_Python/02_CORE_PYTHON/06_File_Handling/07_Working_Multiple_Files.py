# Working with Multiple Files 
def count_words(filename):
	""" Count the approximate number of words in a file"""

	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()

	except FileNotFoundError:
		msg = "Sorry, the file {} does not exist!".format(filename)
		print("\n{}".format(msg))

	else:
		# count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file {} has about {} words.".format(filename, num_words))


filename = 'alice.txt'
count_words(filename)


file_names = ['alice.txt', 'alice_wanterland.txt', 'Heidi.txt', 'Japanese_Girls.txt']

for filename in file_names:
	count_words(filename)