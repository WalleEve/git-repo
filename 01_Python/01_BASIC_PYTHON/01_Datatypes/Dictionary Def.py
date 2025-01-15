Dictionary:
A Dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and we can use a key to access the value associated with that key.
A key's value can be a number, a string, a list, or even aother dictionary. In fact, we can use any object that we cann create in Python as a value in a dictionary.

In Python, a dictionary is wrapped in braces {}, with a series of key-value pairs inside the braces
Example:
alian_0 = { 'color': "green", 'points': 5}

A Key-Value pair is a set of values associated with each other. When we provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon ":", and individual Key-Value pairs are separated by commas, we can store n number Key-Value pairs in a dictionary.

The simplest dictionary has exactly one Key-Value pairs.
alien_0 = {'color': "green"}

alien_0 = {'color': "green", 'pounts': 5}
print(alien_0)

#   GEEKSFORGEEKS:
Dictionary: In Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only singe value as an element, Distionary holds key:value pair.
Key value is provided in the dictionary to make it more optimized.

Note: Keys in a dictionary doesn't allows Polymorphism.

Creating a Dictionary: In Python, a Dictionary can be created by placing sequence of elements within curly{} braces, separated by 'comma'.
Dictinary holds a pair of values, one being the key and the other corresponding pair element being its Key:Value. Values in a dictionary can be of any datatype and can be duplicate, whereas keys can't be repeated and must be immutable.

Note: Dictionary keys are case sensitive, same anme but different cases of Key will be treated distinctly.

# Creating a Dictionary:
# With Interger Keys

Dict = {1: 'Geeks', 2: 'For', 3:'Geeks'}
print("\nDictionary with the sue of Inter Kaeys:")
print(Dict)

# Output:
Dictionary with the sue of Inter Kaeys:
{1: 'Geeks', 2: 'For', 3: 'Geeks'}


# Creating a Dictinary
# With Mixed Keys
Dict = {'name': "Geeks", 1:[1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys")
print(Dict)
# Output:
Dictionary with the use of Mixed Keys
{'name': 'Geeks', 1: [1, 2, 3, 4]}

Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing two curly braces{}.

# Creating an Empty Dictionary
Dict = {}
print("\nEmpty Dictionary:")
print(Dict)

# Output:
Empty Dictionary:
{}

# Creating a Dictionary with Dict() method
Dict = dict({1: "Geeks", 2: "For", 3: "Geeks"})
print("\nDictionary with the use of dict():")
print(Dict)

# Output:
Dictionary with the use of dict():
{1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Creating a Dictionary with each item as a Pair
Dict = dict([(1, "Geeks"), (2, "For")])
print("\nDictionary with each item as a Pair")
print(Dict)

# Output:
Dictionary with each item as a Pair
{1: 'Geeks', 2: 'For'}
