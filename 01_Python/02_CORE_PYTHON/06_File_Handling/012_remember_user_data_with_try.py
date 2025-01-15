# Write Json Data with Try Except Block 

import json 

# load the username, if it has been stored previously.
# otherwise promp for the username and store it.

filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)

except FileNotFoundError:
	username = input("What is your name? ")
	json.dump(username, filename)
	print("We'll remember you when you come back, {} !".format(username))
else:
	print("Welcome Back, {} !".format(username))



# Refactoring 1
# if we could improve the code by breaking it up into a series of functions that have specific job.
# This process is called refactoring.

def greet_user():
	""" Greet the user by Name"""

	filename = 'username.json'

	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)

	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back {} !".format(username))
	else:
		print("Welcome back {} !".format(username))


# Refactoring 2

def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)

	except FileNotFoundError:
		return None 
	else:
		return username


def geet_user():
	""" Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome Back, {} !".format(username))

	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back {} !".format(username))






