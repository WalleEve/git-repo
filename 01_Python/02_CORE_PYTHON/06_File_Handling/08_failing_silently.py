# Failing Silently 

def count_words(filename):
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()

	except FileNotFoundError:
		#msg = "Sorry, the file {} does not exist!".format(filename)
		#print("\n{}".format(msg))
		pass  # we are using this pass, not to show eny error message if the file is not found.
	else:
		words = contents.split()
		num_count = len(words)
		print("The file {} has about {} words.".format(filename, num_count))


file_names = ['alice.txt', 'alice_wanterland.txt', 'little_women.txt', 'Heidi.txt', 'Japanese_Girls.txt'] # in this list 'little_women.txt' file is exist
for filename in file_names:
	count_words(filename)


