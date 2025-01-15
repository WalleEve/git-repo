# Remove a Directory
# The rmdir() function in the OS module removed the specified directory
# either with an absolute or relative path.
# Note that for a directory to be removed, it should be empty.

import os

os.rmdir("D:\\RoadMap\\Python\\24_OS_MODULE\\TestDirectory")

# However we can npt remove the current working directory.
# To Remove it, we must changes the current working directory.

print(os.getcwd())
cur_dir = os.getcwd
os.rmdir(cur_dir)
os.chdir("..")
# os.rmdir(cur_dir)
