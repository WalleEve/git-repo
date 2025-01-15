# Querying data using the cursor fetchmany() method 
# If we want to process rows in batches, we can use the cursor.fetchmany() method.
# In this case we can pass the batch size to the Cursor.fetchmany() method.
# The batch size default to Cusor.arraysize.

import cx_Oracle
import config 

sql = "SELECT empno, ename, sal, hiredate from emp order by empno"

batch_size = 20

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
                # fetch rows 
                rows = cursor.fetchmany(batch_size) # rows = cursor.fetchall()
                if not rows:
                    break 
                # display rows 
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error) 
