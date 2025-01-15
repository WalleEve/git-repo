# Function Can Return Multiple Vales
"""
def cal(num1, num2):
    return num1 + num2, num1 * num2, num1 // num2


n = int(input("Enter  first number: "))
n2 = int(input("Enter second number: "))

add, mul, div = cal(n, n2)
print(f"Addition of {n} + {n2} = {add}")
print(f"Multiplication of {n} * {n2} = {mul}")
print(f"Division of {n} // {n2} = {div}")


"""

"""
def range_add(num1, num2):
    addList = []
    
    for i in range(num1, num2+1):
        addList.append(num1 + i)

    return addList

n = 5
n2 = 10
func_return = range_add(n, n2)
print(func_return)

"""

def range_add(num1, num2):
    global addList
    addList = [1]
    
    for i in range(num1, num2+1):
        print(addList)
        return addList.append(i) 

n = 5
n2 = 10
func_return = range_add(n, n2)
print(func_return)
print(f"addList: {addList}")


       
        
