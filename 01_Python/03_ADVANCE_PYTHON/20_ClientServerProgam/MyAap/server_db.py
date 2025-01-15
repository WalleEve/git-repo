# SERVER SIDE DB SCRIPTS
import psycopg2

try:
    global conn
    global cur
    # Connect to an existing database
    conn = psycopg2.connect("dbname=myaap user=postgres password=postgres host = localhost port=5432")
    print("Conncetion Established With DB!")
    # open a cursor to perform database operations
    if conn != None:
        cur = conn.cursor()
        print("DB Object is Created!")
        
except Exception as err:
    print(err)


def execute_string(sql_string):
    global conn
    global cur
    cur.execute(sql_string)
    data = cur.fetchone()

    if data:
        print(data[1])



execute_string("select * from myaap_users where user_name='admin'")    



