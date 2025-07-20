# What will happen with this code? def func(lst=[]): lst.append(1) return lst print(func()) print(func())
# Explanation:
# This is the mutable default argument trap! The empty list [] is created once when the function is defined, not each time it's called. So the same list gets modified each time.

# What will this code output? my_list = [1, 2, 3] print(my_list * 2)

# Which of these will create a dictionary with keys 'a', 'b', 'c' and values 1, 2, 3?

# What does this list comprehension create? [x**2 for x in range(5) if x % 2 == 0]

x= [1, 2, 3]
y = x 

y.append(4)

print(x)


# What's the time complexity of this function?

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates


# What will this code output?

def modify_list(lst):
    lst = lst + [4]
    return lst

original = [1, 2, 3]
result = modify_list(original)
print(original)
print(result)



# Which approach is most efficient for checking if an item exists in a collection of 1 million items?
# Sets use hash tables for O(1) average case lookup. Lists and tuples require O(n) linear search. Checking dict.values() is also O(n) since it searches through all values.


# What's wrong with this code?

class BankAccount:
    balance = 0
    
    def __init__(self, name):
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount

# balance = 0 is a class variable shared by ALL instances. Each account would share the same balance! It should be self.balance = 0 in __init__ to make it an instance variable.

# What will this generator function produce?

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

result = list(fibonacci(5))

# The generator yields 'a' first (0), then updates a,b. Sequence: yield 0, then a=1,b=1; yield 1, then a=1,b=2; yield 1, then a=2,b=3; yield 2, then a=3,b=5; yield 3.


# How would you handle this potential error in a production system?

user_input = input('Enter a number: ')
result = 10 / int(user_input)

# Production code needs robust error handling. try/except catches both ValueError (invalid int conversion) and ZeroDivisionError (division by zero). Other options miss edge cases.

# What will this code output?

my_dict = {'a': 1, 'b': 2}
for key in my_dict:
    if key == 'a':
        my_dict['c'] = 3
print(my_dict)