# Insert BLOB into a table 

import psycopg2 
from config import config 


def write_blob(part_id, path_to_file, file_extension):
    """ Insert a BLOB into a table """

    conn = None 
    try:
        # read data from a picture 
        drawing = open(path_to_file, 'rb').read()

        # read database configuration 
        params = config()

        # conncet to the PostgreSQL databse 
        conn = psycopg2.connect(**params)

        # creaate a new cursor object 
        cur = conn.cursor()

        # execute the insert statement 
        #print(cur)
        #print(drawing)
        cur.execute("INSERT INTO part_drawings(part_id, file_extension, drawing_data)" +
                    "VALUES(%s, %s, %s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        print('insert successfully')
        # commit the changes to the databse 
        conn.commit()

        # close the communication with the PostgreSQL databse 
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()





if __name__ == "__main__":
    print("function calling for first record")
    write_blob(1, 'D:\\Code\\git-repo\\PostgreSQLDBServer\\images\\simtray.jpg', 'jpg')
    print("function calling for second record")
    write_blob(2, 'D:\\Code\\git-repo\\PostgreSQLDBServer\\images\\speaker.jpg', 'jpg')


    