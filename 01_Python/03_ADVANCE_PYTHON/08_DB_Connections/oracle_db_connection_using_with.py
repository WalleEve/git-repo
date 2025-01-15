import cx_Oracle 
import config 

connection = None 

try:
    with cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding = config.encoding
    ) as connection:
        print(connection.version)
except cx_Oracle.Error as error:
    print(error)
