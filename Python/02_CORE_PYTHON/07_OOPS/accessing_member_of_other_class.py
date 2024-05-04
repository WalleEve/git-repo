# accessing member of once class from another class

class Employer:
	def __init__(self, empno, ename, job, salary):
		self.empno = empno
		self.ename = ename 
		self.job = job
		self.salary = salary

	def employer_details(self):
		print(f"Employer ID: {self.empno}")
		print(f"Employer Name: {self.ename.upper()}")
		print(f"Employer Designation: {self.job.upper()}")
		print(f"Employer Salary: {self.salary}")
	

class Manager:
	def sal_hike(emp):
		emp.salary = emp.salary + 10000
		emp.employer_details()


e = Employer(7339, 'sayed mahfuze', 'developer', 80000)
Manager.sal_hike(e)
