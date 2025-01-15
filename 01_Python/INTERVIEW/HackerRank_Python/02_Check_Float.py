"""
	You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  
"""

for i in range(int(input())):
    N = input()
    float_check = False
    try:
        float(N)
        float_check=True
        if(int(N) == 0):
            float_check=False
    except:
        pass
    print(float_check)