# Deleting Data From Oracle Database in Python

import cx_Oracle 
import config 


def delete_billings(billing_no, amount):
    """
    Delete a billing base on a billing no.
    :param billing_no:
    :return:
    """ 

    sql = ('delete fromm billing_headers '
           'where billing_no = :billing_no')
    

    try:
        # Establish a new connection 
        with cx_Oracle.connect(
            config.username, 
            config.password,
            config.dsn,
            encoding = config.encoding
        ) as connection:
            
            # create a cursor 
            with connection.cursor() as cursor:
                cursor.execute(sql, [amount, billing_no])

                connection.commit()

    except cx_Oracle.Error as error:
        print(error)



if __name__ == "__main__":
    delete_billings(1)