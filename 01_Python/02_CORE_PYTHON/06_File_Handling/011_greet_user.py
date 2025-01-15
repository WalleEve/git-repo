# Now let's write a new program that geets a user whose name has already been store in 'username.josn' file 

import json 


filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, {} !".format(username))

	