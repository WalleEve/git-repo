# Steps for deleting data from the PostgreSQL table in Python

# The following delete_part() function deletes a row in the parts table specified by the part_id.

import psycopg2 
from config import config 


def delete_part(part_id):
    """ delete part by part_id """
    conn = None 
    row_deleted = 0 

    try:
        # read databse configuration 
        params = config()

        # coonect to the postgreSQL Database 
        conn = psycopg2.connect(**params)

        # create a new cursor 
        cur = conn.cursor()

        # execute the DELETE Statement 
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))

        # get the number of deleted rows 
        row_deleted = cur.rowcount

        # commit the changes to the databse 
        conn.commit()

        # close the communication with the postgreSQL database 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return row_deleted


if __name__ == "__main__":
    deleted_rows = delete_part(9)
    print('The number of deleted rows: ', deleted_rows)


    