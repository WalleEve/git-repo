# Querying Data Uisng fetchone(), fetchmany(), and fetchall() Method 

import cx_Oracle
import config 

sql = 'SELECT ename, sal '\
'from emp '\
'order by sal'

try:
    with cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break 
                print(row)
except cx_Oracle.Error as error:
    print(error)