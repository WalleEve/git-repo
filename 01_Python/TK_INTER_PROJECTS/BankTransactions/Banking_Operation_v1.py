# Banking Operation
import sys
class Customer:
	bankname = "ISL Bank"
	bnkaddress = "Ameerpet Hyderabad 500016"

	def __init__(self, name, amount = 0.0):
		self.name = name
		self.amount = amount


	def withdraw(self, amt):
		if amt > self.amount:
			print("Insufficent Balance...")
			sys.exit()
		self.amount = self.amount - amt
		print("Balance after withdraw: ", self.amount)

	def deposit(self, amt):
		self.amount = self.amount + amt
		print("Balance after deposit: ", self.amount)



print("Welcome to ", Customer.bankname)
print(Customer.bnkaddress)

print()

cust = input("Please enter your name: ")
c = Customer(cust)

while True:
	print("Please choose option:\n d - Deposit\n w - Withdraw\n e - Exit ")
	flag = input("> ")

	if flag.lower() == "e":
		print("Thank you for Banking with us")
		sys.exit()

	elif flag.lower() == "d":
		amount = float(input("Please enter amount: "))
		c.deposit(amount)

	elif flag.lower() == "w":
		amount = float(input("Please enter amount: "))
		c.withdraw(amount)
	else:
		print("Please choose valid option !")
