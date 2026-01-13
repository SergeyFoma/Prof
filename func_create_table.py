from psycopg2 import OperationalError
from func_connect_db import connect_db

#connect_db("prof_db", "prof", '2105', '127.0.0.1', '5432')

def create_table(connection, query):
    connection.autocommit=True
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successful.")
    except OperationalError as e:
        print("The error {e} occurred.")





