# Variable Length Argument 
# Note: After variable length argument,if we are taking any other arguments then we 
# should provide values as keyword arguments.
#  +, -, *, /
import os 

os.system('cls')
"""
def calc(ope, *args):
	result = 0

	if ope == '+' or ope.lower() =='add':
		for i in args:
			result = result + i;

	elif ope == '-' or ope.lower() =='sub':	
		result = args[0]
		for i in range(1, len(args)):  			
			result = result -  args[i] 
			
	elif ope == '*' or ope.lower() == 'mul':
		result = args[0]
		for i in range(1, len(args)):
			result = result * args[i]

	elif ope == '/' or ope.lower() == 'div':
		result = args[0]
		for i in range(1, len(args)):
			result = result / args[i]
	else:
		return 'Please Enter the valid option!'
	return result 


print("Calculation")
print("Please enter one Option")
print("For Addition: + or add ")
print("For Subtraction: - or sub")
print("For Multiplication: * or mul")
print("For Division: / or div")

ope = input("Please choose one operator: ")

result = calc(ope, 9, 5)
print(result)

"""

def calc(*args, ope):
	result = 0

	if ope == '+' or ope.lower() =='add':
		for i in args:
			result = result + i;

	elif ope == '-' or ope.lower() =='sub':	
		result = args[0]
		for i in range(1, len(args)):  			
			result = result -  args[i] 
			
	elif ope == '*' or ope.lower() == 'mul':
		result = args[0]
		for i in range(1, len(args)):
			result = result * args[i]

	elif ope == '/' or ope.lower() == 'div':
		result = args[0]
		for i in range(1, len(args)):
			result = result / args[i]
	else:
		return 'Please Enter the valid option!'
	return result 


print("Calculation")
print("Please enter one Option")
print("For Addition: + or add ")
print("For Subtraction: - or sub")
print("For Multiplication: * or mul")
print("For Division: / or div")

oper = input("Please choose one operator: ")

result = calc(9, 5, ope = oper)
print(result)


# VARIBALE LENGTH KEYWORD ARGUMENT 


