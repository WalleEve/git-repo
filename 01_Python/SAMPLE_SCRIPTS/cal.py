# module / function / package 

# function :
# block of executable code with business logic 

# module:
# module contain number of similar or related functions 


# calculator 
# math 
def addition(*args):
	adds = 0
	for i in  args:
		 adds +=i
	return adds

def sub(*args):
	sub_=args[0]
	for i in range(1, len(args)):
		sub_ -=args[i]

	return sub_

def mul(*args):
	mul_=args[0]
	for i in range(1, len(args)):
		mul_ -=args[i]
	return mul_

#print(__name__)

if __name__ == '__main__':	
	result = addition(10, 30)
	print(result)
