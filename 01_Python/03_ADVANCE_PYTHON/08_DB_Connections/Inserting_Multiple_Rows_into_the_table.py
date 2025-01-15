# Inserting Multiple Rows into the table 
# If we want to insert multiple rows into a table once, we can use the cursor.executemany() method.

# The cursor.executemany() is more efficient than calling the cursor.execute() method
# multiple times because it reduces network transfer and database load.

import cx_Oracle
import config 

from datetime import datetime 

def insert_billings(billings):
    """
    insert multiple billings
    :param billings: a list of billings 
    :return:
    """

    # construct an insert statement that add a new row to the billing_headers table 

    sql = ('insert into billing_headers(billing_date, amount, customer_id, note) ' 
           'valeus(:billing_date, :amount, :customer_id, :note)')
    

    try:
        # establish a new connection 
        with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding = config.encoding
        ) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(sql, billings)
                # commit the work 
                connection.commit()
    except cx_Oracle.Error as error:
        print("Error occurred")
        print(error)



if  __name__ == "__main__":
    billings_docs = [
        (datetime.now(), 1000, 1, None),
        (datetime.now(), 1500, 2, None),
        (datetime.now(), 1700, 3, None)
    ]

    # insert multiple billings 
    insert_billings(billings_docs)


    