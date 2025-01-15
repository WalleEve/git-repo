# Using Bind Variables to Pass Data to and from Oracle Database.

# IF we want to pass data to and from the Oracle database, we use placeholders in the SQL statements as 

"""
sql = ('select name '
        'from customers '
        'where customer_id = :customer_id' )
"""

# In this query, the :customer_id is a placeholder
# It is also known as bind variable or bind parameter
# when we execute a query using the cursor object, we need to pass the value of the bind variable 
# cursor.execute(sql, [100])

"""
Bind variables make the code more secure and help avoid SQL injection security issues because user data is never treated as a part of the executable SQL statement.

If user data is concatenated with a SQL statement, it will be vulnerable to a SQL injection attack:
sql = ('select name ' 
      'from customers '
      'where customer_id = ' + customer_id)
"""

# The following example illustrate how to find the customer's name by ID using bind variables 

import cx_Oracle 
import config 

def find_customer_by_id(customer_id):
    """
    Find customer name by id
    :param customer_id: id of the customer
    :return: customer name
    """
    sql = ('select name '
           'from customers '
           'where customer_id = :customer_id')
    
    customer_name = None 

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
                cursor.execute(sql, [100])
                row = cursor.fetchone()
                if row:
                    customer_name = row[0]
    except cx_Oracle.Error as error:
        print(error)
    return customer_name 

print(find_customer_by_id(100))



