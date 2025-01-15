Write an algorithm to order the list with numbers
list = ["2", "6", "9", "4", "8", "0", "7"]
print(list)

#list = [int(i) for i in list]
print(list)
list.sort()
print(list)


What will be the output of the following Python code?
str1 = "helloworld"
str1[::-1]
print(str1)
print(str1[::-1])


#Python Multi Assignment
a = [1, 2, 3] # list
b = (4, 5, 6) # tuple
c = {7, 8, 9} # set

p, q, r = a
s, t, u = b
x, y, z = c

print(p, q, r)
print(s, t, u)
print(x, y, z)

What is the output of the following assignment operator
y = 10
x = y += 2 # SyntaxError: invalid syntax
print(x)
#-------- Analyze
y = 10
x = y = 2
print(x) # 2

y = 10
y += 2
x = y
print(x) # 12

y = 10
x = y =+ 2
print(x) # 2

#--------------------------------

FORMAT VS FSTRING

myName = "Python"
myCity = "London"
mySal = "$50000"

print("My name is {}, my city is {}, my salary is {}".format(myName, myCity, mySal)) # format

print(f"My name is {myName}, my City is {myCity}, my Salary is {mySal}") # fstring

# Remove Duplicate values
list1 = [1, 2, 3, 4, 5, 4, 3, 4, 3, 2, 1, 5, 7 , 6, 8, 9, 3, 5]
print(list1)
list1 = set(list1)
print(list1)
print(list(list1))


# What is pip?
# Ans: Pip is the standard package manager for python. It allows us to install and manage additional package that are not part of the Python standard library.



# What data type is the object below:
L = [1, 23, 'hello', 1]
a) list
b) dictionary
c) array
d) tuple
Ans: a
L = [1, 23, 'hello', 1]
print(type(L))
# pip install wmi
# Windows Management Instrumentation
# To get system Information

import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system.Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")


a = '123456'
z = a[1] + a[4]
print(z) # 25

z = a[1] * a[4]
print(z) # Error





import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");

conn.close()


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print "Records created successfully";
conn.close()



#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print "Total number of rows updated :", conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print "Total number of rows deleted :", conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()



import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


from tkinter import *

master = Tk()

stock_dashboard = Toplevel(master)
stock_dashboard.title("Stock Dashboard")
# ENTRY FRAME:
stock_frame = Frame(stock_dashboard)
stock_frame.grid(row=2, sticky=W)

# Labels
Label(stock_dashboard, text="STOCK DASHBOARD", font=("Calibri", 15), width=30, ).grid(row=0, sticky=N, pady=10)
Label(stock_dashboard, text="Stock Entry", font=("Calibri", 13), width=30).grid(row=1, sticky=N, pady=5)


Label(stock_frame, text="Entry Date:", font=("Calibri", 11)).grid(row=3, sticky=W, padx=2, pady=2)
Label(stock_frame, text="Item:", font=("Calibri", 11)).grid(row=4, sticky=W, padx=2, pady=2)
Label(stock_frame, text="Total Quantity:", font=("Calibri", 11)).grid(row=5, sticky=W, padx=2, pady=2)
Label(stock_frame, text="Toal Value:", font=("Calibri", 11)).grid(row=6, sticky=W, padx=2, pady=2)

# Entry
Entry(stock_frame, width=30).grid(row=3, column=1, sticky=W, padx=2, pady=2)
Entry(stock_frame, width=30).grid(row=4, column=1, sticky=W, padx=2, pady=2)
Entry(stock_frame, width=30).grid(row=5, column=1, sticky=W, padx=2, pady=2)
Entry(stock_frame, width=30).grid(row=6, column=1, sticky=W, padx=2, pady=2)

master.mainloop()
