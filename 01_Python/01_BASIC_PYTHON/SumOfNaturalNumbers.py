# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:48:47 2019

@author: Migration
"""
# Find the Sum of Natural Numbers

def sum_narutal(num):
    result = 0
    if num <0:
        return ("Not a Natural Number")
    elif num == 0:
        return 0
    else:
        for i in range(1, num + 1):
            result += i
    return result


num = int(input("Enter a number: "))
print("The sum is: ", sum_narutal(num))



#

num = int(input("Enter a Natural Number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is",sum)
    
    
    
# 

def sum_netural2(num):
    if num < 0:
        return "Enter a Positive Number !"
    else:
        result = num * (num +1)/ 2 
        return result
        
num = int(input("Enter a Natural Number: "))
print("The sum is: ", sum_netural2(num))



    
    
    
    