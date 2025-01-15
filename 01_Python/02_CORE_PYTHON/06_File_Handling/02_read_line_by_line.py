# Reading Line By Line 

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	for line in file_object:
		print(line)


# Removig the empty lines 
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())



# Making a List of Lines from a File 

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()

	for line in lines:
		print(line.rstrip())


# making all the lines into a single string value
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string +=line.rstrip()

print(pi_string)

print(len(pi_string))


# removing space from in between words 

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()


pi_string = ''

for line in lines:
	pi_string +=line.strip()


print('PI STRING: {}'.format(pi_string))
print('Length: {}'.format(len(pi_string)))


file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()


pi_string = ''

for line in lines:
	pi_string += line.rstrip()


birthdate = input('Input your birthdate, in the form mmddyy: ')
if birthdate in pi_string:
	print('Your birthday appears in the firrst million digits of pi!')
else:
	print('Your birthday does not appear in the first million digits of pi!')











