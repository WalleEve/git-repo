# Problem:
"""
We want to make a list of the largest or smallest N items in a collection.

"""

# Solution:
"""
The heapq module has two functions- nlargest() and nsmallest() that do exactly 

"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints[42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints[-4, 1, 2]

# Both functions also accepts a key parameter that allows them to be used with more complicated data structures.

portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'APPLE', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YAHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}
	]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(f"Cheap: {cheap}")
print(f"Expensive: {expensive}")


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
print(f"Heap: {heap}")
heapq.heapify(heap)
print(f"heap: {heap}")
min = heapq.heappop(heap)
print(f"min: {min}")
min = heapq.heappop(heap)
print(f"min: {min}")
min = heapq.heappop(heap)
print(f"min: {min}")

print(f"HEAP: {heap}")




