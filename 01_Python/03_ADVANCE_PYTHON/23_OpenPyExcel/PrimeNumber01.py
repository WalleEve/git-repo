# prime number

flag = False

def get_factorial(end_range, start_range=2):
    flag = False
    while start_range <= end_range//2:
        if end_range % start_range == 0:
            flag = True
            return flag
        start_range = start_range + 1 
        
    return flag

n = int(input("Enter a number: "))

for i in range(2, n+1):
    if get_factorial(i):
        print(f"{i} is not a prime number!")
    else:
        print(f"{i} is a prime number")
