# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:34:56 2019

@author: Migration
"""

# Quadric Equation:
"""
The standard formula of a quadric equation is:
    a(x)2 + bx + c = 0, where  # (x)square
    a, b and c are real numbers and
    a ≠ 0
    
    
    
Example: Solve 5x2 + 6x + 1 = 0
Coefficients are:a = 5, b = 6, c = 1
Quadratic Formula:x = −b ± √(b2 − 4ac) / 2a
Put in a, b and c:x = −6 ± √(62 − 4×5×1) 2×5
Solve:x = −6 ± √(36 − 20) 10
 x = −6 ± √(16) 10
 x = −6 ± 4 10
 x = −0.2 or −1

"""



import math

def quadric(a, b, c):
    if a ==0:
        exit
    else:
        n1 = -b
        n2 = (b ** 2)
        n3 = (4 * a * c)
        n4 = (2 * a)
        sqrtn2n3 =abs( n2 - n3 )
        print("sqrtn2n3: ", abs(sqrtn2n3) )
        sqrtres = math.sqrt(sqrtn2n3)
        
        x1 =( n1 + (sqrtres* -1)) / n4
    
        x2 =( n1 - (sqrtres* -1)) / n4
        return x1, x2
    """
        resultX1 = ( a * (x1 ** 2) ) +( b * x1 ) + c
        resultX2 = a * (x2 ** 2) + b * x2 + c
    
    if resultX1 == 0 and resultX2 == 0:
        return x1, x2
    elif resultX1 == 0:  
        return x1
    elif resultX2 == 0:
        return x2"""
        
     

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

print("Value of Quadric X is: ", quadric(a, b, c))


# 

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

d = (b ** 2) - (4 * a * c)

sol1 = (-b - math.sqrt(d)) / (2 * a)
sol2 = (-b + math.sqrt(d)) / (2 * a)

print(f"The solutions are {sol1} and  {sol2}")
print("THE solutions are {0} and {1}".format(sol1, sol2))

 


 