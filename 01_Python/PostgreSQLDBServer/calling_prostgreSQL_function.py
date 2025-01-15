# Calling a PostgrSQL function in Python

import  psycopg2 
from config import config 


def get_parts(vendor_id):
    """get parts provoded by a vendor specifyed by the vendor_id """

    conn = None 

    try:
        # read databse configuration 
        params = config()

        # connect to the PostgreSQL databse 
        conn = psycopg2.connect(**params)

        # create a cursor object for execution 
        cur = conn.cursor()

        # another wey to call a function 
        # cur.execute("SELECT * FROM get_parts_by_vendor(%s);", (vendor_id,))

        cur.callproc('get_parts_by_vendor', (vendor_id,))

        # process the result set 

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        # close the communication with the PostgreSQL databse server 
            
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




if __name__ == "__main__":
    get_parts(1)