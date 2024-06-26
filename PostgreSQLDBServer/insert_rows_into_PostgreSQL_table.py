#!/usr/bin/python

# The following insert_vendor() function inserts a new row into the vendor table and returns the newly generated vendor_id value 

import psycopg2 
from config import config 

def insert_vendor(vendor_name):
    """ insert a new vendor into the vendor table"""

    sql = """INSERT INTO vendors(vendor_name)
             VALUES (%s) RETURNING vendor_id;"""
    
    conn = None 
    vendor_id = None 

    try:
        # read database configuration 
        params = config()

        # connect to the PostgreSQL databse 
        conn = psycopg2.connect(**params)
        # create a new cursor 
        cur = conn.cursor()

        # execute the INSERT statement 
        cur.execute(sql, (vendor_name,))
        # get the generated id back 
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database 
        conn.commit()
        # close communication with the database 
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        
    return vendor_id 


# Inserting multiple rows into a PostgreSQL table 

def insert_vendor_list(vendor_list):
    """ Insert multiple vendors into the vendors table"""

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None 

    try:
        # read database configuration 
        params = config()

        # connect to the PostgreSQL database 
        conn = psycopg2.connect(**params)

        # create a new cursor 
        cur = conn.cursor()

        # execute the INSERT statement 
        cur.executemany(sql, vendor_list)

        # commit the changes to the databse 
        conn.commit()

        # clsoe communication with the database 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()



if __name__ == "__main__":
    # isnert one vendor 
    insert_vendor('3M Co.')

    # insert multiple vendors 
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asshi Class Co Ltd.',),
        ('Daikin Insdustries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltc.',),
        ('VIP Industries Ltd.',)
    ])

