# Binding by names 
# If bind variables are associated with names, we have named binds.
# The named binds required the keyword parameter names oe ky of the dictionary to match the bind variable names.

import cx_Oracle 
import config 

sql = ('select product_name '
       'from products '
       'where list_price > :price and '
       'standard_cost <= :cost')

try:
    with cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding
    ) as connection:
        cursor = connection.cursor()
        # for row in cursor.execute(sql, {price:600, cost:500})
        for row in cursor.execute(sql, price=600, cost=500):
            print(row)
        cursor.close()
except cx_Oracle.Error as error:
    print(error)


sql = ('select product_name '
       'from products '
       'where list_price > :price and '
       'standard_cost <= :cost')

try:
    with cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding
    ) as connection:
        cursor = connection.cursor()
        for row in cursor.execute(sql, [600, 500]):
            print(row)
        cursor.close()

except cx_Oracle.Error as error:
    print(error)


    

        