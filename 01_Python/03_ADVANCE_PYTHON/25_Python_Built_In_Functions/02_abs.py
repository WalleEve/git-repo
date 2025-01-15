# abs()
"""
    The abs() function in Python is a built-in functions that returns the absolute
    value of a number. It can be used with both integers and floating-point
    numbers, and it always returns a positive value.
"""

# Parameter Values 
#   x : A numeric value or object for which the absolute value is computed.

# Return Values:
#   The abs() function can return an int, float, or complex number.

# Example 1:
"""
    The abs() function can also be used with complex numbers to return
    their magnitude.
"""
print(abs(3+4j)) # Output: 5.0

# Example 2:
"""
    Return the absolute value of a number. The argument my be an integer 
    or a float-point number.
"""

print(abs(-10)) # output 10 

# Example 3:
"""
    If a custom class defines the __abs__() method, bas() can be called an object of the calss
"""

class CustomClass:
    def __abs__(self):
        return 100
    
obj = CustomClass()
print(abs(obj)) # output: 100