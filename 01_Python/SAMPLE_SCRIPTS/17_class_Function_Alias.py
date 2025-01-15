# Function Aliasing 

name = 'uma sanker palai' # garbage 

my_name = name 

print(my_name)

print(type(name))
print(type(my_name))

print('name refered object location: ',id(name))
print('my_name refered object location: ', id(my_name) )

print(name is my_name)

del name 

#print(name)
print(my_name)
# Map
# Filter 
# Reduce (functools)

import functools as fn

print(dir(fn)) # 

# Function Alias 

a = [1, 2, 3, 4]

b = a 
 
del a 

c = b

#print(b)
#print(c)

messag = 'Hello'

#print(type(messag))

def messag():
	print('Hi')
	

#print(type(messag)) # 
#print(id(messag))


my_message = messag

#print(type(my_message)) 
#print(id(my_message)) 

#messag()
#my_message()

del messag

# messag() # NameError: name 'messag' is not defined
#my_message()



def fname(mname):
	print(f'Hi {mname}, How are you')
	return mname.title()  # 


#title_name = fname('uma sanker')
#print(f'Title Name: {title_name}')

alias_name = fname

aname = alias_name('uma sanker')
print(aname)



# Function can return mutiuple values
# Function can accept function
# Function can return function 


def cal(a):
	return a * a



def my_app(fun):
	x = int(input('Enter First Number: '))
	y = int(input('Enter Second Number: '))
	result = fun(x, y)
	print(result)

#my_app(cal) # fun = cal


a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))

def my_app(fun, x, y):
	result = fun(x)
	return result


result = my_app(cal, a, b) # 
print(result)
















































