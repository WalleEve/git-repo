# NUMPY 
# NumPy (Numerical Python)  is an open source Python library.

# Installing NumPy 
# pip install numpy 

# import NumPy 

import os 
os.system('cls') # this is to clear the old texts from the cmd line window.

import numpy as np 

a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)


# Difference Between LIST and ARRAY
"""
Numpy gives us an enormous range of fast and efficient ways of creating
arrays and manipulting numerical data inside them. While a  Python list can 
contain different data types within a single list, all of the elements in a 
NumPy array should be homogeneous. The mathematical operations that 
are ment of be performed on arrays would be extremely inefficient if the 
arrays weren't homogeneous. 

NumPy arrays are faster and more compact than Python list. 
An array consume less memory and is convenient to use.
NumPy uses much less memory to store data and it provides 
a mechanism of specifying the data types. 
This allows the code to be optimized even further. 
"""

# What is an Array 
"""
An Array is a central data structure of the NumPy library.
An array is a grid of values and it contains information about the raw data, 
how to locate an element, and how to interpret an element. It has a grid of elements that can 
be indexed in various ways. 
The elements are all of the same type, referred to as the array dtype. 

An array can be indexed by a tuple of nonnegative integers,
by boolean, by another array, or by integers.
The rank of the array is the number of dimensions.
The shape of the array is a tuple of integers giving the size of 
the array along each dimension.

One way we can initialize NumPy array is from Python lists, using nested 
list if two-or higher dimensional data 
"""

a = np.array([1, 2, 3, 4, 5, 6])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# we can access the elements in the array using square brackes.
# When we are accessing elements, remember that 
# indexing in NumPy starts at 0 

print(a[0]) # [1, 2, 3, 4]


# Attributes of an array 
"""
An array is usually a fixed-size container of items of the same type of size.
The number of dimensions and items in an array is defined by its shape. 
The shape of an array is a tuple of non-negative integers that specify the size of 
each dimension. 

In NumPy, dimensions are called axes. 
2D array looks like:
[[0., 0., 0.],
 [1., 1., 1.]]

our array has 2 axes. The first axis has length of 2 and 
the second axis has a length of 3. 


Just like in other Python container objects, the content of an array can be 
accessed and modified by indexing or slicing the array. 
Unlike the typical container objects, different arrays cab share the same data,
so changes made on one array might be visible in another. 

Array attributes reflect information intrinsic to the array itself. 
if we need to get, or even set properties of an array without creating a new array, 
we can often access an array through its attributes. 
"""

  

# CREATE A BASIC ARRAY 
# To create a NumPy array, we can use the function np.array().

import numpy as np 
a = np.array([1, 2, 3])
print(a)

# Beside creating an array from a sequence of elements, 
# we can easily create an array filled with 0's.

a = np.zeros(2)
print(a)


# Or an array filled with 1's 

a = np.ones(3)
print(a)

# Or even an empty array!
"""
The function empty creates an array whose initial content is random and 
depends on the state of the memory. The reason to use empty over zeros 
(or something similar) is speed - Just we need to make sure to fill every 
element afterwards!
"""

# Create an empty array with 2 elements 

ea = np.empty(2)
print(ea) 
print(type(ea))

# We can create an array with a range of elements 

a = np.arange(4)
print(a)


# An array that contains a range of evenly spaced intervals.
# To do this, we will specify the first number , last number and the step size.

a = np.arange(2, 9, 2)
print(a)


# We can use the np.linespace() to create an array with values that are 
# spaced linearly in a specified interval.

a = np.linspace(0, 10, num=5)
print(a)

a = np.linspace(0, 10, num=7)
print(a)



# Specifying our Data type:

# While the default data type is floating point(np.float64),
# we can explicitly specify which data type want using the dtype keyword.

x = np.ones(4, dtype=np.int64)
print(x)

