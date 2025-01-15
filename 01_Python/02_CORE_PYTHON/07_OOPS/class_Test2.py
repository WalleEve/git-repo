class Test:
	def __init__(self):
		print("no-param Constructor ")

	def __init__(self, name):
		print("Param constructor")


t1 = Test() # This object creation will raise error because python do not accept function overloading so it will consider last constructor for initialization and we should provide value for name 
			# TypeError: __init__() missing 1 required positional argument: 'name'
			
t2 = Test("sayed")

