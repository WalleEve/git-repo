# Managing Transaction in Python 
# When we call the cursor.execute() to insert, update, or update data from a table.
# The cx_Oracle does not automatically commit the change to the database.

# Autocommiting mode 
# The connection object has an attribute called autocommit that allows us to commit the 
# transaction automatically. by default is set to False.
# To instruct cx_Oracle to commit the transaction automatically, 
# we set the value of the connection.sutocommit ti True.


# Starting a transaction explicitly 
# A transaction starts implicitly. To explicitly start a transaction, we use the connection.begin() method 
# A transaction can be local or global. 
# The connection.begin() method without any parameter starts a local transaction.

import cx_Oracle 
import config as cfg 
from datetime import datetime 

def insert_billing_header(billing_header, cursor):
    """
    Insert a new row into the billing_header table and 
    return the inserted billing no
    :param billing_header:
    :return:
    """

    sql = ('insert into billing_headers(billing_date, amount, customer_id) '
           'values(:billing_date, :amount, :customer_id) '
           'returning billing_no into :billing_no')
    
    billing_no = cursor.var(int)
    # add the variable to billing_header list
    billing_header.append(billing_no)
    # execute the insert statement 
    cursor.execute(sql, billing_header)
    # return the inserted value 
    return billing_no.getvalue()[0]


def insert_billing_items(billing_no, billing_items, cursor):
    """
    insert billing items 
    :param billing_nol:
    :param billing_items:
    :param cursor:
    :return:
    """

    # insert into billing items 
    sql = ('insert into billing_items(billing_no, product_id, price) '
           ' valeus (:billing_no, :product_id, :price)')
    
    items = [] 

    for item in billing_items:
        items.append((billing_no, item[0], item[1]))

    cursor.executemany(sql, item)



def insert_billing_doc(billing_header, billing_items):
    """
    Insert a billing document 
    :param billing_header:
    :param billing_items:
    :return:
    """

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
                # insert the billing header 
                billing_no = insert_billing_header(billing_header, cursor)
                # rollback the transaction if no billing no is generated
                if not billing_no:
                    connection.rollback()

                # insert the billing items 
                insert_billing_items(billing_no, billing_items, cursor)
                # commit the transaction 
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)



if __name__ == "__main__":
    insert_billing_doc(
        [datetime.now(), 1, 1000],
        [(1, 200),
         (2, 300),
         (3, 500)]
    ) 


