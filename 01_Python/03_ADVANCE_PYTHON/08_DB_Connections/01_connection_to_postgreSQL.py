# Note Before running this script please check if the Postgres is installed in localhost and check the port number.
# For postgreSQL default available database is postgres
# For PostgreSQL commonly used user is postgres and password is postgres 
# and to connect PostgreSQL database we need psycopg2 module installed.
#installation
# pip install psycopg2 
# Run this pip command in CMD

import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5432")


cursor  = conn.cursor()

cursor.execute("select count(1) from information_schema.tables t where t.table_schema='Public'")

record_count = cursor.fetchone()

cursor.close()

cursor = conn.cursor()

cursor.execute("select * from information_schema.tables t where t.table_schema='public'")

#print(cursor.fetchone())
row_count = cursor.rowcount

print(f"Table count: {row_count}")

for i in range(1, row_count+1):
    data_string = cursor.fetchone()
    print(f"Data String: {data_string} ")

