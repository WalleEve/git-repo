# Exceptions 
"""
Python uses special object called exceptions to manage errors that arise during a program's execution.

"""

# Handling the ZeroDivisionError Exception 

try:
	print(5/0)
except ZeroDivisionError:
	print("We can not divide by Zero!")
	
    

# Using Exceptions TO Prevent Crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to Quit.")


while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\Second Number: ")
    if second_number == 'q':
        break 
    answer = int(first_number) / int(second_number)
    print("Division of {} and {} is: {}".format(first_number, second_number, answer))
    
    
# The Else Block 

print("\nGive me two numbers, and I'll divide them.")
print("Enter 'q' to Quit.")

while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break
	second_number = input("Second Number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("We can not divide by Zero!")
	else:
		print("Division of {} with {} is: {}".format(first_number, second_number, answer))

	
    



