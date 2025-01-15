# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:25:41 2022

@author: Sayed
"""

# Dictionary 
"""
A dictionary in python is a collection of key-value pairs. 
Each key is connected to a value, and we can use a key to access the value 
associated with the key. 
A keys value can be a number, a string, a list , a tuple or even another dictionary.
In Python a dictionary is wrapped in braces, {}
with a seria of key-value pairs inside the brinside:
"""   
# The simplest dictionary has exactly one key-value pair.

alien_0 = {"color": "green"}

# A Simple Dictionary 

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])   # "color" is represent as key and "green" represent as value to the key
print(alien_0["points"])  # "points" represent as key and 5 represent as value to the key


# Accessing Values in a Dictionary 

# To get the value associated with a key, 
# give the name of the dictionary and then place the key inside a set of square brackes 

alien_0 = {"color": "green"}
print(alien_0["color"])

# We can have an unlimited number of key-value pairs in a dictionary.

alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print("You have earned "+ str(new_points) + " points!")


# Adding New Key-Value Pairs:

# Dictionaries are dynamic structures, and we can add new key-value pairs
# to a dictionary at any point of time. 

alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0 
alien_0["y_position"] = 25 

print(alien_0)

# Starting with an Empty Dictionary 

alien_0 = {} 

alien_0["color"] = "green"
alien_0["points"] = 5 

print(alien_0)


# Modifying Values in a Dictionary 
"""
To modify a value in dictionary, give the name of the dictionary with the key 
in sqare brakets and then the new value we want to associated with that key. 
"""

alien_0 = {"color": "green"}
print("The Alien is "+alien_0["color"]+".")

alien_0["color"] = "yellow"
print("The Alien is now "+alien_0["color"]+".")


alien_0 = {"x_position":0, "y_position": 25, "speed": "medium"}
print(f"Original x-position {alien_0['x_position']} ")

# Move the alien to the right 
# Determine how far to move the alien based on its current speed. 
if alien_0['speed']=='slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    x_increment = 3 
    
# The new position is the old position plus the increment .
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print("New x-position: " + str(alien_0['x_position']))

# REMOVING KEY-VALUE PAIRS:
"""
When we no longer need a pices of information that's stored in a dictionary
we can use the del statement to compltely remove a key-value pair.
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)





# Note: the deleted key-value pair is removed permanently 

# A DICTIONARY OF SIMILAR OBJECTS:

favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }

print("Sarah's favorite language is "+
      favorite_languages['sarah'].title() +
      '.')

# LOOPING THROUGH A DICTIONARY:

# Looping Through All Key-Value Pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }

for key, value in user_0.items():
    print("\nKey: "+ key)
    print("Value: "+value)


# The method items() return a list of key-value paires
# The for loop then store each of these pairs in the two variables provided.

favorite_language = {
    'jen': 'Python', 
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }
for name, language in  favorite_languages.items():
    print(name.title() + "'s Favorite Language is "+
          language.title())
    
# Looping Through All the Keys in a Dictionary:

# The keys() method id useful when we do not need to work with  
# all the values in a dictionary.   

favorite_language = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'Phil': 'Python',
    'sam': 'Java'
    } 
for name in favorite_language.keys():
    print(name.title())

# or 

for name in favorite_language:
    print(name.title())
    
# We can choose to use the keys() method explicitly if  
# it makes our code easier to read


favorite_languages ={
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("Hi "+name.title()+
              ", I see ypur favorite language is "+
              favorite_languages[name].title() + '!')
        
        
if 'erin' not in favorite_languages.keys():
    print("Erin, Please take our  poll!")


# The keys() method isn't just for looping, 
# It actually returns a list of all the keys

# Looping Through a Dictionary's Keys in Order 

favorite_languages ={
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# Looping Through All values in a Dictionary:
favorite_languages ={
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }

print("The following languages have been mentioed!")
for language in favorite_languages.values():
    print(language.title())    

# To see each language choosen without repetation.
# We can use set() 
# A set is similar to a list except that 
# each item in the set must be unique.

favorite_languages ={
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'sam': 'Java'
    }
print("The following languages have been mentioed!")
for language in set(favorite_languages.values()):
    print(language)


# NESTING 
# Sometimes we want to store a set of dictionaries in a list
# or a list of items as a value in a Dictionary.
# This is called nesting, 
# We can nest a set of dictionaries inside a set,
# A list of items inside a dictionary
# Or even a dictionary inside another dictionary 

# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
    


# Built-in Dictionary Methods

# clear()
# Clears a dictionary 
# d.clear() empties dictionary d of all key-value pairs

d = {'a': 10, 'b': 20, 'c': 30}
print("Dictionary: "+ str(d))
d.clear()
print("Dictionry After execution of clear(): "+ str(d))




# get(<key>[, <default>])
Returns the value for a key if exists in the dictionary. 
The python dictionary .get() method provides a convenient way of 
getting the value of a key from a dictionary without checking ahead 
of time whether the key exists, and without raising an error 

d.get(<key>) searches dictionary d for <key> and returns the 
associated value if it found. If <key> not found, it returns None. 


d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b')) 
print(d.get('z'))

if <key> is not found and the optional <default> argument is :
specified, that value is returned instead of None 

print(d.get('z', -1))
    
    

# items()
Returns a list of key-value pairs in a dictionary. 

d.items() returns a list of tuples containing the key-value pairs in d. 
The first item in each tuple is the key and the second item is the 
key's value. 

d = {'a': 10, 'b': 20, 'c': 30}
print(d)

print(list(d.items()))

print(list(d.items())[1][0])

print(list(d.items())[1][1])

 


# keys()
Returns a list of keys in a dictionary 

d.keys() returns a list of all keys in d 

d = {'a': 10, 'b': 20, 'c': 30}

print(d)

print(list(d.keys()))




# values()
Returns a list of values in a dictionary. 

d.values() returns a list of all values in d 

d = {'a':10, 'b': 20, 'c': 30}
print(d)

print(list(d.values()))

Any duplicate values in d will be returned as many times as they are occur. 

d = {'a':10, 'b': 20, 'c': 30, 'd':10, 'e': 30, 'f': 20}
print(d) 
print(list(d.values()))


# Technical Note: 
    The .items(), .keys(), and .values() 
    method actually return something called a view object. 
    A dictionary view objects is more or less like a window 
    on the keys and values. For practical purposes, we can 
    think of these methods aws returning list of the dictionary's keys and values.
    
    

# pop(<key>[, <default>])
Removes a key from a dictionary, if it is present, and returns it value. 
if <key> is presented in d, d.drop(<key>) removes <key>  and return its 
associate value 

d = {'a':10, 'b': 20, 'c': 30, 'd':10, 'e': 30, 'f': 20}

poped_key_value = d.pop('b')
print(d)
print(poped_key_value)


d.pop(<key>) raise a KeyError exception if <key> is not in d 

d = {'a':10, 'b': 20, 'c': 30, 'd':10, 'e': 30, 'f': 20}

d.pop('z')

if <key> is not in d, and the optional <default> argument is specified,
then that value is returned, and no exception is raised. 

d = {'a':10, 'b': 20, 'c': 30, 'd':10, 'e': 30, 'f': 20}

popped_item = d.pop('z', -1)
print(d)
print(popped_item)







# popitem()
Removes a key-value pair from a dictionary 
d.popitem() removes the last key-value pair added from  d and 
returns it as a tuple. 

d = {'a':10, 'b': 20, 'c': 30, 'd':10, 'e': 30, 'f': 20}
popped_item = d.popitem()
print(d)
print(popped_item)

if d is empty, d.popitem() raise a KeyError exception :
    

d = {} 
popped_item = d.popitem() # KeyError: 'popitem(): dictionary is empty'

# Note: 
    In Python versions less than 3.6 popitem() would return a arbitary (random)
    key-value pair since Python dictionaries were unordered before version 3.6 
    




# update(<obj>)
Merges a dictionary with another dictionary or with an 
iterable of key-value  pairs. 

If <obj> is a dictionary, d.update(<obj>) merges the entries from 
<obj> into d. For each key in <obj>.

if the key is not present in d, the key-value pair from <obj> is :
    added to d. 
    
if the key is already present in d, the corresponding value in d :
    for that key is updated to the value from <obj>:
        
        
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
print(d1)

In this example key 'b' already exists in d1, so its value is updated to 200, 
the value for the that key from d2.
However, there is no key 'd' in d1  so that key-value pair is added from d2.

<obj> may also be a sequence of key-value pairs, 
similar to when the dict() function is used to define a dictionary. 

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update([('b', 200), ('d', 400)])
print(d1) 

Or the values to merge can be specified as a list of keyword arguments: 
    
d1= {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
print(d1) 







    









 



