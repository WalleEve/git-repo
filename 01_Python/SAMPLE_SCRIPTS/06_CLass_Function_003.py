# Write a function to get a prime number:
# While


def get_prime(num, start_range = 2):
    flag = False
    #start_range = 2
    while start_range <= (num//2):  
        #print(start_range)
        if num % start_range == 0:
            flag = True
            return flag

        start_range = start_range +1
    return flag  # True 
    
"""
n = int(input("Enter a Number: "))

flag =  get_prime(n)
if flag:
    print(f"Number {n}  is not a Prime Number")
else:
    print(f"Number {n} is a prime number")



n1 = int(input("Enter a Number: "))
n2 = int(input("Enter second Number: "))

for i in range(n1, n2+1):
    flag =  get_prime(i) # 5..10
    if not flag:
        print(f"Number {i}  is a Prime Number")



n1 = int(input("Enter a Number: "))
n2 = int(input("Enter second Number: "))
for i in range(n1, n2+1):
    flag = get_prime(i)
    if not flag:
        print(f"Number {i} is a Prime Number")

"""


n1 = int(input("Enter a Number: "))
n2 = int(input("Enter second Number: "))
flag = get_prime(n1, n2)
if not flag:
    print(f"{n1} - {n2} is a Prime Number")

    
