# Unpacking a Sequence into Separate Variables:

# Problem 
"""
We have an N-element tuple or sequence that we would like to unpack into a collection of N variable.

tpl1 = ("sayed", 28, "08-JAN-1991")
v1 = "sayed"
v2 =  28
v3 =  "08-JAN-1991"
"""

tuple_t1 = ("sayed", 28, "08-JAN-1991")
name, age, dob = tuple_t1
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Dob: {dob}")


tpl2 = ('a', 'b', 'c',('d', 'e', 'f'), (1, 2, 3))
print(tpl2[3][0])

t1 , t2, t3, t4, t5 = tpl2 
t4t1 , t4t2, t4t3 = t4 
t5t1 , t5t2, t5t3 = t5 
print("t1 %s" %t1)
print("t2 %s" %t2)
print("t3 %s" %t3)
print(f"t4 {t4}")
print(f"t5 {t5}")
print(f"t4t1 {t4t1}")
print(f"t4t2 {t4t2}")
print(f"t4t3 {t4t3}")
print(f"t5t1 {t5t1}")
print(f"t5t2 {t5t2}")
print(f"t5t3 {t5t3}")


t1 , t2, t3, (t4t1 , t4t2, t4t3), (t5t1 , t5t2, t5t3) = tpl2 

print("t1 %s" %t1)
print("t2 %s" %t2)
print("t3 %s" %t3)
print(f"t4t1 {t4t1}")
print(f"t4t2 {t4t2}")
print(f"t4t3 {t4t3}")
print(f"t5t1 {t5t1}")
print(f"t5t2 {t5t2}")
print(f"t5t3 {t5t3}")


lst = [1, 2, 3, 4, 5, 6]
a, b, c , d, e, f = lst 
print(a , b, c, d, e, f)

dic = {"a":1, "b":2, "c":3}
k1, k2, k3 = dic 
print(k1, k2, k3)

# Note: If there is a mismatch in the number of elements , we will get an error.

"""
Unpacking actually works with any objects that happens to be iterable, not just tuple or list.
This includes strings, file, iteratora and generators.
"""

s = "Hello"
a, b, c, d, e = s 
print(a, b, c , d, e)

"""
When unpacking we may sometimes want to discard certain values.
Python has no special syntax for this but we can just pick a 
throwaway variable name for it.
"""
# For Example:
data = ["ACME", 50, 91.1, (2012, 12, 21)]
_, share, price, _ = data 
print(share, price)

6281484238 jio 
9698115169 jio
