
# Underscore for large numbers
number = 10_000_000_000 
print(f"{number:,}")

# List and Dict Comprehension 

# List Comprehension 
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

# Dict Comprehension 
numbers = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
squares = {k:v*v for (k,v) in numbers.items()}
print(squares)

# Most Frequent element in a List 
numbers = [1, 1, 2, 3, 4, 1]
mostFrequent = max(set(numbers), key = numbers.count)
print(mostFrequent) 

# Covert Mutable in Immutable 
numbers = [1, 2, 3, 4] 
numbers = frozenset(numbers)
#numbers[0] = 5  
print(numbers) 

# Print Monthly Calender 
import calendar  
print(calendar.month(2020, 11)) 

# Quiz 
x = 1_2_3 
y = 4  
print(x * y) # 1  8  12  

x = 1_2 
y = 3 
print(x * y) 





