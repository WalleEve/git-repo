#!/usr/bin/python

# Updating data 

import psycopg2 
from config import config 


def update_vendor(vendor_id, vendor_name):
    """ Update vendor name nased on the vendor id """

    sql = """ UPDATE vendors 
              SET vendor_name = %s 
              WHERE vendor_id = %s"""
    
    conn = None 
    updated_rows = 0 

    try:
        # read databse configuration 
        params = config()

        # connect to the PostgreSQL database 
        conn = psycopg2.connect(**params)

        # create a new cursor 
        cur = conn.cursor()

        # execute the UPDATE statement 
        cur.execute(sql, (vendor_name, vendor_id))

        # get the number of updated rows 
        updated_rows = cur.rowcount 

        # Commit the changes to the database
        conn.commit()

        # Clsoe communication with the PostgreSQL databse 
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows 


if __name__ == "__main__":
    # udpate vendor id 1 
    update_vendor(1, '3m Copr')
