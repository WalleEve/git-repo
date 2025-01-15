# Filter()
# Map()
# Reduce()

# Higher Order Function 



#filter(function, iterable)# string  list tuple set 

l = [3, 5, 7, 8, 1, 2, 4] # odd number: 

def odd(n):
	if n%2 != 0:
		return 1


odd_list = list(filter(odd, l))
print(odd_list)

# input: number of items 10: 10, <10



# map()
# map(function, iterable)

l = [2, 3, 4, 5, 6, 7]
v = [2, 3, 4, 5, 1]


def double(n, m):
	return n*m 

dub_list = list(map(double, l, v))

print(dub_list)



# Reduce ()
# reduce(function, iterable) 
# it always return single result 

def my_add(a, b):
	result = a + b
	print(f"{a} + {b} = {result}")
	return result


from functools import reduce
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)


from functools import reduce 

lis = [2, 4, 5, 7, 8, 9] 

st = '2345678' # 35 

[2345, ]  = result

def sums(n, m):
	result = int(n) + int(m)
	return result
list_sum = reduce(sums, lis)
print(f'Sum Of the Given List: {list_sum}')


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