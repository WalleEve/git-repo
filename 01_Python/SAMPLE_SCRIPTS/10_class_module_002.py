# Getting Modules 
# "C:\Users\Sayed\Desktop\PythonRoadMap Dec 2022\PythonClass_Dec2022\10_class_module_001.py"
# import cal as c
from cal import addition as a

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second number: "))

print(__name__)
result = a(num1, num2)
print(result)

