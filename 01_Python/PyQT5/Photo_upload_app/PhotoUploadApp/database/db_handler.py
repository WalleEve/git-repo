import psycopg2
from psycopg2 import Error
from config.settings import DB_CONFIG

def create_table():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        image_data BYTEA NOT NULL
    );
    '''
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

def save_image_to_db(image_data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        insert_query = "INSERT INTO images (image_data) VALUES (%s)"
        cur.execute(insert_query, (image_data,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
        return False

def retrieve_image_from_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        select_query = "SELECT image_data FROM images ORDER BY id DESC"
        cur.execute(select_query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        # Return a list of all retrieved images
        return [result[0] for result in results] if results else []
    except Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
        return []

def retrieve_all_images_from_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        select_query = "SELECT image_data FROM images ORDER BY id"
        cur.execute(select_query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return [result[0] for result in results] if results else []
    except Error as e:
        print(f"Database error: {e.pgcode} - {e.pgerror}")
        return []
