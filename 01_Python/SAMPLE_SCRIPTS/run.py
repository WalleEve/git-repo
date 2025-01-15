
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
# calc function scope ends here 



















