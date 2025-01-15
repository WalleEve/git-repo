# Testing a Function 

from name_function import get_formatted_name    

print("Enter 'q' at any time to quit.")

while True:
	first = input('\nPlease give me a first name: ')
	if first.lower() =='q':
		break 
	last = input('Please give me a last mane: ')
	if last.lower() =='q':
		break 

	formatted_name = get_formatted_name(first, last)
	print("\tNeatly formatted name: {}.".format(formatted_name))
 