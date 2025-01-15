# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:22:28 2019

@author: Migration
"""

# Calculate the area of a Triangle

# if a, b, c are the 3 sides of a Triangle then
# s = (a + b + c)/ 2 s: Side
# area = √(s(s-a)*(s-b)*(s-c)) s: Side
# Area = ½ bh  b: Base, h: Height

import math
def area_triangle(a, b, c):
    
    side =( a + b + c ) / 2
    #area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    area = math.sqrt(side * (side - a) * (side - b) * (side - c)) 
    return area



def triangle_height(a, b, c):
    side = (a + b + c) / 2
    
    area = math.sqrt( side * (side - a) * (side - b) * (side - c))
    base = 0
    if a > base:
        base  = a
    if b > base:
        base = b
    if c > base:
        base = c
    
    
    hight = 2 * (area / base)

    return hight
    
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

print("Area of a Triangle is: ", area_triangle(a, b, c))
print("Height of a Triangle is: ", triangle_height(a, b, c))