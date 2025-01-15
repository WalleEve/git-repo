# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:54:07 2019

@author: Migration
"""

# Square Root:
import math

num1 = int(input("Enter a number: "))

sqrt = math.sqrt(num1)
print(f"Square Root of {num1} is: ", sqrt)

# 2nd:

num1 = int(input("Enter a number: "))
print(f"Square Root of {num1} is: ", math.sqrt(num1))


# 

num = int(input("Enter a number: "))

# ** is used for exponentiation
num_sqrt = num ** 0.5
print(f"The square root of {num} is: ", num_sqrt)

# Here we have raised num to the power of 0.5 which gives us the square root

# Find the square root if real or complex numbers
# Import the complex math module

import cmath
num = int(input("Enter a number: "))
cnum_sqrt = cmath.sqrt(num)
num_sqrt = math.sqrt(num)
print(f" The square root of complex {num} is: ", cnum_sqrt)
print(f" The square root of real {num} is: ", num_sqrt)
