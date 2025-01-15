# Database: SQLITE3
# Tables:
"""----------------------------------------------------------------------------
| USERS: keeps user details for login
| STOCK: keeps products of the store
| sale : Keeps the sale details
| purchase: keeps the purchase Details to the Store
| Stoke: Keeps the total stokes Details of the store
----------------------------------------------------------------------------"""
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
conn.autocommit = True
cursor.execute('''CREATE TABLE users
         (ID INT PRIMARY KEY     NOT NULL,
         user_name      TEXT  UNIQUE   NOT NULL,
         password TEXT NOT NULL
         );''')
cursor.execute("INSERT INTO users (ID,user_name,password) \
      VALUES (1, 'sayed', 'sayed' )");
print('Record Inserted')
cursor.execute('''CREATE TABLE stock
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         total_qty real,
         total_value real
         );''')

cursor.execute('''CREATE TABLE purchase
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         qty_per_unit real,
         total_qty real
         );''')

cursor.execute('''CREATE TABLE sales
         (ID INT PRIMARY KEY     NOT NULL,
         ent_date      TEXT  UNIQUE   NOT NULL,
         item TEXT NOT NULL,
         qty_per_unit real,
         total_qty real,
         total_amt real
         );''')
print ("Table created successfully");

conn.close()
