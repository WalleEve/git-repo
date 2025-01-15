# Instance Method 
# Class method 
# Static Method 

class Test:
	""" This class the created by Sayed for demo purpose"""
	Institute = "Vitech"                              # Static Variable
	Director = "Frank Vitiello"                       # Static Variable 
	def __init__(self, name, empid, dept):                 # __init__() Constructor (special method)
		self.name = name                              # Object level Variable / instance variable 
		self.empid = empid                            # Object Level Variable / instance variable
		self.dept = dept                              # Object Level Variable / instance variable

	def empDtls(self):
		
		print("#" * 50)
		print("name of the employee: ", self.name)
		print("employee id: ", self.empid)
		print("Department: ", self.dept) 


	@classmethod
	def orgDtl(cls):
		print("Organization: ", cls.Institute)
		print("Director: ", cls.Director) 

	@staticmethod 
	def bons( salary, period):  # salary, period # Local variable 
		return (salary * (period * 0.1))


t =Test("sayed", 101, "Dev")
t.empDtls() 
t.orgDtl() 
bonus = Test.bons(10000, 8)
print(f"Bonus: {bonus}")






