# Introduction to the tansaction in psycopg 

"""
In psycopg, the connection class is responsible for handling transactions. when we issue the 
first SQL statement to the PostgreSQL database using a cursor object, psycopg creates new transaction.

Form that moment, psycopg executes all the subsequent statements in the same transaction. If any statement fails, psycopg will abort the transaction.

The connection class has two methods for ending a transaction: 
commit() and rollback().
If we want to commit all changes to the PostgreSQL datbase permanently, we call the commit() method. and in case we want to cancel the chagnes, we call the rollback() method.
Closing the connection object or destroying it using the del will also result in  an 
implicit rollback.

We can set the autocommit attribute of the connection object to True. This 
ensures that psycopg executes every statement and cimmits it immediatly.

The autocommit mode is also useful when we execute statements required to execute outside a transaction wich as CREATE DATABASE and VACUUM.

# typical pattern

import psycopg2 

conn = None 

try:
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    cur.execute(statement_1)
    cur.execute(statement_1)

    conn.commit()
    cur.close()
except psycopg2.DatabseError as error:
    print(error)
finally:
    if conn  is not None:
        conn.close()


"""

import psycopg2
from config import config 

def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table 

    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"

    # statement for inserting a new row into the vendor_parts table 
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    conn = None 

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # insert a new part 
        cur.execute(insert_part, (part_name,))

        # get the part id 
        part_id = cur.fetchone()[0]

        # assign parts provided by vendors 
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # commit changes 
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == "__main__":
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))

    print("Invalid Call")
    add_part('Power Amplifier', (99,))


"""
conn = psycopg2.connect(dsn)

# transaction 1
with conn:
    with conn.cursor() as cur:
        cur.execute(sql)

# transaction 2
with conn:
    with conn.cursor() as cur:
        cur.execute(sql)

conn.close()
"""