# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:46:11 2019

@author: Migration
"""


# With User Input
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

result = num1 + num2
print(result)

# Without result variable:
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("Result: ", num1 + num2)

# Without User Input:

num1 = 10 
num2 = 20
print("Addition of num1 and num2 is: ", num1 + num2)


# Class:

class Addition():

    
    def addition(self, num1, num2):
        return num1 + num2
    
    def add_abs(self, num1, num2):
        if num1 < 0:
            num1 = num1 * (-1)
        if num2 < 0:
            num2 = num2 * (-1)
        result = num1 + num2
        return result


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

adds = Addition()

result = adds.add_abs(num1, num2)
print(f"Addition of Assolute {num1} and {num2}: ", result)


        
    



