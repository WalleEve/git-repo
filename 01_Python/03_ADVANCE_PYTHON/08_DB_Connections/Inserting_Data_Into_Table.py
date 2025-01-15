# Inserting Data Into Table from Python
# Inserting a single row into the table 

import cx_Oracle 
import config as cfg 
from datetime import datetime 

def insert_belling(billing_date, amount, customer_id, note):
    """
    Insert a row to the billing_headers table 
    :param amount:
    :param customer_id:
    :param note:
    :return:
    """

    # construct an insert statement that add a new row to the billing_headers table 

    sql = ("insert into billing_headers(billing_date, amount, customer_id, note)"
           "values(:billing_date, :amount, :customer_id, :note)")
    
    try:
        # establish a new connection 
        with cx_Oracle.connect(
            cfg.username,
            cfg.password,
            cfg.dsn,
            encoding = cfg.encoding
        ) as connection:
            
            # create a cursor 
            with connection.cursor() as cursor:
                # execute the inser statement
                cursor.execute(sql, [billing_date, amount, customer_id, note])
                # commit work 
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occured:')
        print(error)
        

if __name__ == '__main__':
    insert_belling(datetime.now(), 1200, 1, None)
