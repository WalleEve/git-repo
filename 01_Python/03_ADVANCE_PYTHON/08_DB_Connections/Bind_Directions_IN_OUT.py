# Bind Directions 
# Bind varibales can be IN OR OUT
# The IN bind variables allow us to pass data from Python to Oracle database
# while OUT bind variables allow us to get back from the Oracle Database to Python.

# To have the Oracle Database return data to Python, we need to create a variable by using the cursor.var() method 

import cx_Oracle
import config 

# construct a PL/SQL anomymous block 

plsql = ('begin '
         'select count(*) into :customer_count '
         'from customers; '
         'end;')

try:
    # establish a new connection 
    with cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding
    ) as connection:
        # create a cursor 
        with connection.cursor() as cursor:
            # create a variable 
            customer_count = cursor.var(int)
            # execute the pl/sql anonymous block 
            cursor.execute(plsql, customer_count = customer_count)
            # show the value of the variable 
            print(f"The number of customer is {customer_count.getvalue()}")
except cx_Oracle.Error as error:
    print(error)