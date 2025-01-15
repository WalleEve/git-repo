# Write to a File 
# Writing to an Empty File 

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love Programming!")


# Writing Multitple Lines 

filename = 'programming1.txt'

with open(filename,'w') as file_object:
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")
	
	
# Note: it will write these two lines in a single line as sqished together.	

# we can incluse newline in our write() statement makes each string appear in its own line 


filename = 'programming2.txt'

with open(filename, 'w') as file_object:
	file_object.write("I Love Programming. \n")
	file_object.write("I love creating new games. \n")
	

	
	
