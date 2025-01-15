import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors


DB_CONFIG = {
    'dbname': 'myDB_080631',
    'user': 'postgres',
    'password': 'Postgres',
    'host': 'localhost',
    'port': '5432'
}

def print_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

def save_to_db():
        try:
            # Connect to PostgreSQL and insert the encrypted image
            conn = psycopg2.connect(**DB_CONFIG)
            cur = conn.cursor()
            print(f"connection: {cur}")
            # Ensure the table exists
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS images2 (
                id SERIAL PRIMARY KEY,
                image_data TEXT NOT NULL
            );
            '''
            cur.execute(create_table_query)
            conn.commit()

            insert_query = "INSERT INTO images2 (image_data) VALUES (%s)"
            cur.execute(insert_query, ('HELLO',))
            conn.commit()

            cur.close()
            conn.close()

        except OperationalError as err:
            # pass exception to function
            print_psycopg2_exception(err)

save_to_db()