import psycopg2
import os
from create_tables_querries import create_table_querries
from drop_table_querries import drop_tables_querries

def create_database_connection():
    db_user = os.getenv("USER")
    db_password = os.getenv("DB_PASSWORD")
    try:
        conn = psycopg2.connect(f"host=127.0.0.1 dbname=hotjar_task user={db_user} password={db_password}")
        conn.set_session(autocommit=True)
        curr = conn.cursor()
    except psycopg2.Error as e:
        print("Error: could not make connection to the database")
        print(e)
    return curr, conn
    
def drop_tables(curr):
    for querry in drop_tables_querries:
        curr.execute(querry)
        

def create_tables(curr):
    for querry in create_table_querries:
        curr.execute(querry)

def main():
    curr = create_database_connection()
    drop_tables(curr)
if __name__ == "__main__":
    main()