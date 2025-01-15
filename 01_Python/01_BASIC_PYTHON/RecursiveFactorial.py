# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 07:28:58 2019

@author: Migration
"""

# Python Recursion:
"""
Recursion is the process of defining something in terms of itself.

We know that in Python, a function can call other functions. It is even 
possible for the function to call itself. These type of construct are termed as
recursive functions.

Factorial of a number is the product of all the integers from 1 to that number.
For Ex: the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

"""
# Recursive function to find the factorial of a number

def calc_factorial(x):
    if x == 1:
        return 1

    else:
        return (x * calc_factorial(x-1))
    

num = int(input("Enter a number: "))
print(f"The factorial of {num} is", calc_factorial(num))



# Factorial:

def factorial(x):
    result = 1
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        while x < 0:
            result *= x 
            x += 1 
        while x > 0:
            result *= x
            x -=1
    return result

num = float(input("Enter a number: "))
print(f"Factorial of {num} is : {factorial(num)} \n", )