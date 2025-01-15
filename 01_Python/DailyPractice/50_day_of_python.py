# Day1 
# Write a function called divide_or_square that takes one argument (anumber)
# and returns the square root of the number if it is divisible by 5,
# returns its remainder if it is not divisible by 5. 
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root. 
import math 


def divide_or_square(ln_number):
    if ln_number % 5 == 0:
        return math.sqrt(ln_number)
    else:
        return ln_number%5

input_number = int(input("Enter a number: "))   
result = divide_or_square(input_number)

print('Result %.2f'%result)


# Day2
# Write a function called convert_add that takes a list of strings as an 
# argument and converts it to integers and sums the list.
# ['1', '3', '5'] should be converted to [1, 3, 5] and summed to 9 

import functools as fn

def convert_add(list_in):
    list_integer = []
    for i in list_in:
        list_integer.append(int(i))
    return list_integer, fn.reduce(lambda x, y: x + y, list_integer)

in_list = ['1', '3', '5']
list_int, list_sum = convert_add(in_list)

print(f"integer list: {list_int} and sum the list elements is: {list_sum}")
    

# Day3 Register Check 
# Write a function called register_check that checks how many students 
# are in school. The function takes a dictionary as a parameter. If the 
# student is in school, the dictionary says "Yes". If the student is not in 
# school, the discionary says "No". Your function should return the number 
# students in school. Use the dictionary below.
# register = {'Michael': "Yes", 'John': "No", 'Peter': "Yes", 'Mary': "Yes"}
# Function should return 3 


def register_check(dic_in):
    student_cnt = 0

    for key, value in dic_in.items():
        if value == 'Yes':
            student_cnt += 1
    return student_cnt

register = {'Michael': "Yes", 'John': "No", 'Peter': "Yes", 'Mary': "Yes"}
student_count = register_check(register)
print(f"The total number of students: {student_count}")

# Day 4: Only Floats 
# Write a function called only_floats, which takes two parameters a and b 
# and return 2 if both arguments are floats, return 1 if only 
# one argument is a float, and returns 0 if neither argument is a float.
# If you pass (12.1, 23) as an srgument, function should return a 1.

def only_floats(a_in, b_in):
    if isinstance(a_in, int) and isinstance(b_in, int):
        return 0
    elif isinstance(a_in, float) and isinstance(b_in, float):
        return 2
    else:
        return 1

a = 12.20
b = 23.2 

print(type(a))
print(type(b))
print(type(float(a)))
print(type(float(b)))

result = only_floats(a, b)
print(f"Result: {result}")
     

