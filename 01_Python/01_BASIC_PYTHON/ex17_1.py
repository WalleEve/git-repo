# copy text from one file to another

from sys import argv
from os.path import exists 

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print(f"The input file length is {len(indata)} bytes long")

print(f"Does the out file exists ? {exists(to_file)}")
print("Ready, Hit RETURN to continue, CRTL-C to abort.")

input()

out_file = open(to_file, 'w')
outfile.write(indata)

print("Alright all done")


out_file.close()
in_file.close()



