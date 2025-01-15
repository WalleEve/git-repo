# 1.2: Unpacking Elements from Iterable of Arbitrary Length

# Problem:
"""
We need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many value to unpack" exception.
"""

# Solution:
"""
Python "star expression" can be used to address this problem. 
"""
# Funcation for drop first and last value and return  the middle values.
import statistics as st
def drop_first_last(grades):
	first, *middle, last = grades
	print(f"Middle Valus: {st.mean(middle)}")
	return 0

# Execute the function with some random values:
drop_first_last([45, 75, 96, 48, 58, 32])


#Example:
"""
Suppose we have user records that consist of a name and email, address, followed by an  arbitrary number of phone numbers.

"""
record = ('Sayed', 'sayed@live.in', 'Hyd', '9692392243', '7799876552')
name, email, address, *phone_number = record

print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone Number: {phone_number}")
print(f"Phone Number 1:{phone_number[0]} ")
print(f"Phone Number 2:{phone_number[1]}")


# Suppose we have list of values we need to fetch the last value
*traling, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(f"Current: {current}")

# Discussion

records = [
	('foo', 1, 2),
	('bar', "Hello"),
	('foo', 3, 4)
	]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)


# Star unpacking can also be useful when combined with certain kinds of string processing operations, such as spliting.

# Example:
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *body, homedir, sh = line.split(':')
print(f"Uname: {uname}")
print(f"home dir: {homedir}")
print(f"sh: {sh}")

# Sometimes we might want to unpack values and throw them away. We can't just specify a bare * when unpacking, but we could use a common throwaway variable name, such as _ or ign(ignore) :

record = ('ACME', 50, 123.24, (12, 18, 2019))
name, *_, (*_,year) = record

print(f"Name: {name}")
print(f"Year: {year}")

# If we have a list, we can easily split it into head and tail components like this:

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(f"Head: {head}")
print(f"Tail: {tail}")

# Writing functions that perform such splitting in order to carry out some kind of clever  recursive algorithm.

def sum_(items):
	head, *tail = items
	return head + sum(tail) if tail else head

result = sum_(items)
print(f"Resut: {result}")




