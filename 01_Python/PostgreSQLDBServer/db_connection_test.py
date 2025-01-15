#!/usr/bin/python

# connection test for postgres

import psycopg2

from config import config 

def connect():
    """ Connect to the PostgreSQL databse server """
    conn = None 

    try:
        # read connection parameters 
        params = config()

        # connect to the PostgreSQL server 
        print('Connecting to the PostgreSQL databse...')

        conn  = psycopg2.connect(**params)

        # create a cursor 
        cur = conn.cursor()

        # execute a statement 
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL databse server version

        db_version = cur.fetchone()
        print(db_version)

        # close the communincation with the Pos     tgreSQL 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Databse connection closed')




    
if __name__ == '__main__':
    print("Trying to connect DB...")
    connect()
        