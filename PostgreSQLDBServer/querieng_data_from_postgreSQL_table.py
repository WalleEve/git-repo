# The steps for quering data from PostgreSQL table in Python


# The following get_vendor() function selects data from the vendor table and fetches the rows 
# using the fetchone() method.

import psycopg2 
from config import config 


def get_vendors():
    """ quering data from the vendor table """

    conn = None 

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# Querying data using fetchall() method 
# The following get_parts() function uses the fetchall() method of the curosr object to fetch
# rows from the result set and displays all the parts in the parts table.            

def get_parts():
    """ query parts from the parts table """
    conn = None 

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)

        for row in rows:
            print(row)
            
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



# Querying data using fetchmany() method 

# The following get_supliers() function selects parts and vendors data using the fetchmany() method.

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break 
        
        for row in rows:
            yield row

def get_paert_vendors():
    """ query part and vendor data from multiple tables """

    conn = None 
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""
            SELECT part_name, vendor_name
            FROM parts 
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id 
            ORDER BY part_name 
                    
        """)

        for row in iter_row(cur, 10):
            print(row)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()









if __name__ == "__main__":
    get_vendors()
    get_parts()
    get_paert_vendors()

