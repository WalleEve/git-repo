# Storing Data 
# The JSON JavaScript Object Notation formats was originally Developed from JavaScript.
# However, it has since become a common format used by amy languages, inclusing Python.

# USINF json.dump() and json.load()

# The json.dump() function takes two arguments: a pices of data to store and a file object it can use to store the data.

import json 

numbers = [2, 3, 4, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)


# Now we will write a program that uses json.load() to read the list back into memory.

import json 

filename = 'numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)


