# Updating Data in Oracle Database from Python

import cx_Oracle
import config 

def updating_billings(billing_no, amount):
    """
    update now amount for a billing
    :param billing_no:
    :param amount:
    :return:
    """

    sql = ('update billing_headers '
           'set amount = :amount '
           'where billing_no = :billing_no')
    
    try:
        # establish a new connection 
        with cx_Oracle.connect(
            config.username, 
            config.password,
            config.dsn,
            encoding = config.encoding
        ) as connection:
            #create a cursor 
            with connection.cursor() as cursor:
                cursor.execute(sql, [amount, billing_no])

                connection.commit()

    except cx_Oracle.Error as error:
        print(error)


if __name__ == "__main__":
    updating_billings(1, 2000)