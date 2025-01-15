# High Order Function 
# Function which accepts other function as input.

def f(a, b):
	return a + b

def f1(f, x):
	z = f
	return z * x

res = f1(f(3, 5), 10)
print(res)


# filter()
# it always accepts 2 paramters 
# first paramter will be the function
# second parameter can be list or tuple or string
# result will be be return value of the function

# syntax
# filter(<function name>, parameter)

def get_even(n):
	if n%2 == 0:
		return 1
	else:
		return 0
	


def get_odd(n):
	if n%2 != 0:
		return 1
	else:
		return 0



l = [2, 3, 5, 8, 7, 9]

res = filter(get_even, l)
print(list(res))
res2 = filter(get_odd, l)
print(list(res2))



a = ['1234567890', '983295902', 'a12345678' ]

def get_phone(n):
	if n.isnumeric():
		if len(n) == 10:
			return 1
	else:
		return 0


phone = filter(get_phone, a)
print(list(phone))



# using labda 

l = [2, 3, 5, 8, 7, 9]

even = list(filter(lambda x:x%2==0, l))
print(even)
even2 = list(filter(lambda x: 1 if x%2==0 else 0, l))
print(even2)

odd = list(filter(lambda x:x%2!=0, l))
print(f'ODD: {odd}')


phone = list(filter(lambda x: x if x.isnumeric() and len(x)==10 else 0 , a ))
print(f'Phone: {phone}')

a = lambda x: x if x.isnumeric()else 0

print(a('10a'))

b = lambda x: x if len(x) ==10 else 0

print(b(a('1000000000')))


# map()
l = [1, 2, 3, 4, 5]

def double(n):
	return n*2


dlist = list(map(double, l))
print(dlist)


dlist2 = list(map(lambda x: x*2, l))
print(f"dlist2: {dlist2}")


l1 = [1, 2, 3, 4, 5, 6]
l2 = [13, 13, 13, 13, 13, 13]

mtable = list(map(lambda x,y: x*y, l1, l2))
print(f"mtable: {mtable}")

l1 = [1, 2, 3, 4, 5, 6]
l2 = [13, 13, 13, 13, 13]

mtable = list(map(lambda x,y: x*y, l1, l2))
print(f"mtable: {mtable}")



account= ['1012040001', '1010002', '1012040003', '0004']

def check_acc(ac):
	print(f'IS NUMERIC: {ac.isnumeric()}')
	print(f'Length: {len(ac)}')
	print(f'Branch {ac[0:3]}')
	if ac.isnumeric() and len(ac) == 10 and ac[0:3]=='101':
		return ac
	else:
		return 'Not a Valid Account Number'+str(ac)


vac = check_acc('1012040001')	
print(vac)
# reduce()





