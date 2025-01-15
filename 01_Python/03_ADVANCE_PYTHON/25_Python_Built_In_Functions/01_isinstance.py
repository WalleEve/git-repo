# isinstance()
"""
    The isinstance() function in Python is a built-in function used to check if an 
    object is an instance of a specified class. It takes two arguments - The object to 
    be checked and the calss or type as a second argument. It returns 'True' if the 
    object is an instance of the specified class, and 'False' otherwise.

"""

# Parameter Values:
# object    : The object to be checked 
# classinfo : A class, type, or tuple of classes and types to be check against.

# Example 1: 
""" 
    The instance() function checked if an object is an instance of a specified class ir any of its subclasses.
"""
class Dog:
    breed = 'Poodle'

my_dog = Dog()
result = isinstance(my_dog, Dog)

print(result)


# Example 2:
"""
    It can also accept a tupel of classes to check if the object is an instance of any of the specifed classes.
"""
class Car:
    brand = "Toyota"

class Bicycle:
    type = "Mountain"

my_vehicle = Car()
result = isinstance(my_vehicle, (Car, Bicycle))
print(result) # True 

# Example 3:
"""
    The isinstance() function is commonly used for type checking in Python 
    to validate input parameters or determine the type if objects in a program.
"""
def process_data(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Data must be a list or tuple")
    
    for item in data:
        print(f"Processing: {item}")

#l = [1, 4, 5, 3, 8]
s = "2345678"
process_data(s)


