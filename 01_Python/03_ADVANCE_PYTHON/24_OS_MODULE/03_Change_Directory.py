# Changing the Current Working Directory

# We must forst changes the current working directory to a newly
# created one before doing any operations in it.
# This is done by using the cdir() function.

import os

os.chdir("D:\\RoadMap\\Python\\24_OS_MODULE\\TestDirectory")

print(os.getcwd())

# In Order ti set the current directory to the parent directory use
# ".." as the argument in the chdir() function

os.chdir("..")
print(os.getcwd())
