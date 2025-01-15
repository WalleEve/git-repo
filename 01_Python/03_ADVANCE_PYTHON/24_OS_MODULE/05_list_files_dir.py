# List files and Sub-Directories

# The listdir() function returns the list of all files and
# Directories in the specified directory.

import os

cur_dir = os.getcwd()

print(os.listdir(cur_dir))

# if we do not specify any directory, then list of files and directories in the
# current working directory will be returned.

print(os.listdir())
