# Python Functions:

"""
Functions are the most important of an application.
A function can be defined as the orizinal block or reusable code 
Which can be called whenever required.

Python allows us to divide a large program into the basic building blocks known
as function. The function contains the set of programming statements enclosed 
by {}. A function can be called multiple times to provide reusability and 
modularity to the python program.

Python provide us various inbuilt functions like range(), or print. Although, 
the user can create its functions which can be called user-defined functions.
"""

# Creating a Function:
"""
In Python, we can use def keyword to define the function.
syntax:
    def my_function():
        function_suite
        return <expression>
The function block is started with the colon(:)  and all the same leave block 
statements remains at the same indentation.

A function can accept any number of parameters that must be the same in the 
definition and function calling.

"""

# Function calling:
"""
In Python, a function must be defined before the function calling otherwise the 
Python interpreter gives an error. Once the function is defined, we can call it 
from  another function or the python prompt. To call the function, use the 
function name followed by the parentheses.

A simple function that prints the message "Hello World":
    
"""

def hello_world():
    print("Hello World")
    

hello_world()

# Paramenters in Function:
"""
The information into the functions can be passed as the parameters. 
The parameteres are spefied in the parentheses. We can give any number of 
parameters, but we have to separate them with a comma.

"""

# Define a function:
def func(name):
    print("Hi", name)
    
# Calling the function:
func("Eva")


# Python function to calculate the sum of two variables

# Define the function
def sum(a, b):
    return(a + b)
    
# taking values from the user:
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
total = sum(num1, num2)
print(total)


# Call by reference in Python:\
"""
In python, all the functions are called by reference, i.e., all the chnages 
made to the reference inside the function revert back to the original value
referred by the reference.
however, there is an exception in the case of mutable objects since the changes
made to the mutable objects like string do not revert to the original string 
rather, a new string object is made, and therefore the two different objects 
are printed.

"""

# Example 1 Passing Immutable Object(List)

# defining the function
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("List inside function= ", list1)
          
# Define the list
list1 = [10, 30, 40, 50]

# calling the function

change_list(list1)
print("List outside function=", list1);

# Example 2 Passing Mutable Object(String)

def change_string(strng):
    strng = strng + " Hows you"
    print("Printing the string inside function: ", strng)

# Define:
string1 = "Hi I am there"

# calling the function:
change_string(string1)
print("Printing the String Outside the function: ", string1)


# Types of arguments:
"""
There may be several types of argumnets which can be passed at calling.

1. Required arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments

"""

# Required Arguments:
"""
We can provide the arguments at the time of function calling.
As far as the required arguments are concerned, these are the 
arguments whcih are required to be passed at the time of function
calling with the exact match of their positions in the function call 
and function definations. If either of the arguments is not provided
in the function call, or the position of the arguments is changed, 
then the python interpreter will show the error.

"""

# Example:

# The argument name is the required argument to the function func

def func(name):
    message = "Hi "+name
    return message

name = input("Enter the name:")
print(func(name))


# Example2:

# The function simple_interest accepts three arguments and returns the simple interest accordingly

def simple_interest(p, r, t):
    return (p* t* r) / 100


p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in yesrs: "))
print("Simple Interesst: ", simple_interest(p, r, t))


# Example 3:

# The function calculate and returns the sum of two arguments a and b

def calculate(a, b):
    return a+b

calculate (10)  # This causes an error : TypeError: calculate() missing 1 required positional argument: 'b'
calculate(10, 60)

# Keyword Arguments:

"""
Python allows us to call the function with the keyword arguments. This kind of 
function call will enable us to pass the arguments in the random order.

The name of the arguments is treated as the keywords and matched in the function
calling and definion. If the same match is found, the values of the arguments 
are copied in the function defination.

"""

# Example 1:

# Function func is called withe name and message as the keyword argument

def func(name, message):
    print("Printing the message with ", name, " and ", message)

func(name='John', message= ' Hello') # name andmessage is copied with the values John and Hello respectively


# Example 2: Providing the values in Different order at the calling

# The function simple_interest(p, r, t) is called with the keyword arguments the order of arguments doesn't matter in this case.

def simple_interest( p, t, r):
    return (p* t* r)/100

print("Simple Interest: ", simple_interest(t= 10, r = 10, p= 1900))

# If we provide the different name of arguments at the time of function call, an error will be thrown.


