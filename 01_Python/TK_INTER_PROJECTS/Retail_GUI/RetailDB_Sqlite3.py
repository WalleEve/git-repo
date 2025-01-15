# Database: SQLITE3
# Tables:
"""----------------------------------------------------------------------------
| USERS: keeps user details for login
| STOCK: keeps products of the store
| sale : Keeps the sale details
| purchase: keeps the purchase Details to the Store
| Stoke: Keeps the total stokes Details of the store
----------------------------------------------------------------------------"""
import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE users
         (ID INT PRIMARY KEY     NOT NULL,
         user_name      TEXT  UNIQUE   NOT NULL,
         password TEXT NOT NULL
         );''')
conn.execute("INSERT INTO users (ID,user_name,password) \
      VALUES (1, 'sayed', 'sayed' )");
print('Record Inserted')
conn.execute('''CREATE TABLE stock
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         total_qty real,
         total_value real
         );''')

conn.execute('''CREATE TABLE purchase
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         qty_per_unit real,
         total_qty real
         );''')

conn.execute('''CREATE TABLE sales
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         qty_per_unit real,
         total_qty real,
         total_amt real
         );''')
print ("Table created successfully");

conn.close()
