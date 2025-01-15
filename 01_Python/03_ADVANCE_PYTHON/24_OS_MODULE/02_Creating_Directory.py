# Creating a Directory
# We can create a new directory using the os.mkdir() function,

import os

directory_path = os.getcwd() # This will get the current Working Directory
os.mkdir(directory_path+'\\TestDirectory')

# Note: If we do not specify the whole path in the mkdir() function,
# It will create the specified directory in the current working directory or drive.

os.mkdir('TestDir2')
