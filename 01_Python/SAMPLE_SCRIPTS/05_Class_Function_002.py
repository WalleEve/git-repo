# Write a Program to find the prime number

#  2, 3, 5, 7, 11

def prime(num1):
    # prm=2
    flag = False
    for i in range(2, num1 +1):
        for j in range(2, i):
            if i % j == 0:
                falg = True

    return flag

n1 = int(input("Enter a Number: "))
flag = prime(n1)
if flag:
    print(f"{n1} is not a prime number")
else:
    print(f"{n1} is a prime number")
    
            
        

            
            
    


