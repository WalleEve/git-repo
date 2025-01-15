# Sample Function for Unit Test.

# Test Pass
def get_formatted_name(first, last):
	""" Generate a neatly formatted full name"""
	full_name = first + ' '+last
	return full_name.title()    

# Test Fail
def get_formatted_name(first, middle, last):
	""" Generate a neatly formatted full name"""
	full_name = first +' '+middle +' ' +last
	return full_name.title()    


# Responding To A Failed Test 

def get_formatted_name(first, last, middle=''):
	""" Generate a Neatly formated Full Name."""
	if middle:
		full_name = first +' '+middle +' ' +last
	else:
		full_name = first + ' '+last
	return full_name.title()    


if __name__ == "__main__":
	first_name = input('Enter your first name: ')
	last_name = input('Enter your last name: ')
	get_formatted_name(first_name, last_name)