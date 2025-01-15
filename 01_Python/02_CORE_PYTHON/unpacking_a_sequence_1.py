# 1.1: Unpacking a Sequence into Separate Variables

# Problem
"""
We have an N-element tuple or sequence that we would like to unpack into a collection ot N variables.

"""

# Solution:
"""
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement is that the number of variables and structures and structure match the sequence.

"""

p = (4, 5)
x, y = p

print(f"x: {x}")
print(f"y: {y}")

data = ['ACME', 50, 91.1, (2019, 12, 21)] 
name, shares, price, date = data

print("Name: ", name)
print(f"Date: {date}")

name, shares, price, (year, month, day)  = data

print(f"Name: {name}")
print(f"Year: {year}, Month: {month}, day: {day}")


# Discussion:
"""
Unpacking actually works with any object that happens to be iterable, not just tuples or lists, This includes strings, files, iterators and generators.
"""
s = "Hello"
a, b, c, d, e = s

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")


"""
When unpacking, we may sometimes want to discard certain values. Python has no special syntax for this, but we can often just pick a throwaway variable name for it.
"""
data = [ 'ACME', 50, 91.1, (2019, 12, 21) ]
_, shares, price, _ = data

print(f"shares: {shares}")
print(f"price: {price}")

# Check:
print(f"_: {_}")


