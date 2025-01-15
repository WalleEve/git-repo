# Functions Alias  

# Function can return a Function 


def wish(name):

	def inner(name):
		if name =='uma':
			print('Hi {} How are you!'.format(name))
		else:
			print('Hi {} Good Morning!'.format(name)) 
	# Inner Function Scope End
	inner(name)
# wish Function Scope


wish('sadhan')
#inner('uma') # NameError: name 'inner' is not defined




# Functions Alias  

# Function can return a Function 


def wish(name):

	def inner(name):
		if name =='uma':
			print('Hi {} How are you!'.format(name))
		else:
			print('Hi {} Good Morning!'.format(name))
			
	print('iNNER: ', type(inner))
	print('iNNER: ', id(inner))
	return inner


func_inner = wish('uma') 

print(type(func_inner))
print(id(func_inner))

func_inner('sADHAN')




def calc():
	# Inner Function Declarion Section!
	def addition(a, b):
		return a + b
	print('addition: ', type(addition))
	print('addition', id(addition))

	def subtraction(a, b):
		return a - b
		
	def multiplication(a, b):
		return a * b 

	def division(a, b):
		return a / b

	print('This is Calculation Function')
	return addition, subtraction, multiplication, division

func_retrun_val = calc()
print(func_retrun_val)

first_object = func_retrun_val[0]
print(first_object)

print('first_object: ', type(first_object))
print('first_object', id(first_object))

result = first_object(5, 7)
print('Result: ', result)




















