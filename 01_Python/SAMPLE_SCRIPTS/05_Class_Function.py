# Write a Function to get the factorial of a given number:
# LOGIC:  5 > 1 > 1
#             2 > 2
#             3 > 6
#             4 > 24
#             5 > 120
#             6 > 720



def fact(num1):
    fact = 1
    for i in range(1,  num1+1):
        fact = fact * i
        #print(f"Factorail of {i} is: {fact}")        

    return fact

n1 = int(input('Enter a number to get the factorial: '))
for i in range(1, n1+1):
    result = fact(i)
    print(f"Factorail of {n1} is: {result}")



             
