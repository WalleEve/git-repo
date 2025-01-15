import cx_Oracle 
import config 

connection = None 

try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding
    )

    print(connection.version)

except cx_Oracle.Error as error:
    print(error)

finally:
    if connection:
        connection.close()

        