# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 08:09:48 2022

@author: Sayed
"""

#Python Quiz 

class Test:
    def __init__(self, __id):
        self.__id = 101 
        # print(self.__id)
        
test = Test(102)
print(test.__id) # AttributeError: 'Test' object has no attribute '__id'

# Private Keyword
# The private members of a class are only accessible within the class. In Python,
# a private member can be defined by using a prefix __ (double underscore).

#------------------------------------------------------------------------------


List = ['Python', 'Developers']
result = [i for i in List if len(i)>6]
print(*result) # Developers
print(*List)

d = {'color': 'green', 'points':5}
print(d)
print(*d)

# * will unpack the list / dictionary and print the element.

#------------------------------------------------------------------------------

# Exception Handling:
# Exception 
An exception is an abnormal condition, that occurs 
during the execution of a program and disrupts the 
normal flow of program. 
When ever an exception occurs, the program stops 
the execution and the further code is not executed. 

Following are some of the common built-in exceptions 
that occurs during the program execution 

ZeroDivisionError: Occurs when a number is divided by zero 
NameError: Occurs when a name is not found 
ModuleNotFoundError: Occurs when the imported modules is not found 
IndexError: Occurs when the index of a sequence is out of range 

a, b = 10, 0 
devision = a/b 
print(devision)
print("Program after ZeroDivisionError Exception")

# output 
Traceback (most recent call last):

  File "C:\Users\Sayed\AppData\Local\Temp\ipykernel_21528\2829225665.py", line 2, in <module>
    devision = a/b

ZeroDivisionError: division by zero

# Exception Handling 
If we do not handle the exception, the program 
stops the execution and thus the further code 
is not executed 
Python provides a way to handel such exceptions 
so that the program can be executed without any 
disruption 

Python used try...except block/clause to handel the exception 

# try...except 
The code which can raise an exception should be placed inside 
the try clause, and the code that handel the exception shpuld 
be placed inside the except clause. 

#Syntax 

try:
    # code which can raise an exception 
except:
    # code to execute if we get an error or 
    # exception in the try block 
    
a, b = 10, 0

try:
    division = a/b 
    print(division)
except:
    print('Program after ZeroDivisionError Exception!')
    

# try...except with specific exception 
whenever we use the except clause outhout specifying 
the particular exception name, it will handel all 
exceptions in the same way. 

To handel the different types of exceptions, we can 
use the specific exception name with except caluse. 

A try clasue can have any number of except caluse 
to handel different exceptions. However only one 
will be executed with the exception occurs. 
We can also use a tuple of exception name to 
specify multiple exceptions in an except clause. 


# Syntax 
try:
    # code which can raise an exception 
except ExceptionName:
    # code to execute if we get an error or 
    # exception in the try block 
except(Exception 1,Exception 2, ..., Exception n ):
    # code to execute of we get an error or 
    # exception in the try block 
    
    
try:
    a, b = 10, 0 
    division = a/b 
    print(division)
except NameError:
    print("Name Error")
except (ZeroDivisionError, ArithmeticError):
    print("ZeroDivisionError or ArithmeticError")
    
    
# try...except...finally 
The finally clause can be used along with the 
try...except, when we have a specific block of 
code that is to be executed irrespective of wheather 
the try clause raise an exception or not. 

try:
    a, b = 10, 0 
    division = a / b 
    print(division)
except:
    print("Program after ZeroDivisionError Exception!")
finally:
    print("This is finally block.")
    
    
# try...except...else 
Sometimes we might want to execute a specific 
block of code only if the code inside the try clause 
execute without any error. for this case, we can 
use the else clause with the try caluse 

try:
    a, b = 10, 5 
    division = a/b 
    print(division)
except:
    print("Program after ZeroDivisionError Exception!")
else:
    print("This is else block")
    
    
#------------------------------------------------------------------------------

Tuple = (5, 10, 20)
Tuple.insert(2, 15) # Error
print(Tuple) 

# Output :
#    AttributeError: 'tuple' object has no attribute 'insert'

#Tuples are immutable we can not insert a new element ot it.
#so it will raise an Error. 


#------------------------------------------------------------------------------


# Powerful One-Lines in Python 
1. Swap two numbers 
n1, n2 = n2, n1 

2. Reverse a String 
reversed_string = input_string[::-1]

3. Factorial of a Number
fact = lambda n:[1, 0][n > 1] or fact(n-1)*n 

4. Prime Numbers 
primes = list(filter(lambda x:all(x%y!=0 for y in range(2, x)), range(2, 10)))

5. String Palindrome 
palindrome = input_string == input_string[::-1]


#------------------------------------------------------------------------------

List1 = [10, 20, 30, 40, 50]
List2 = [n%30 for n in List1]
print(List2) 




    
    
    
    
    

 

