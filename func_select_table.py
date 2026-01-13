from psycopg2 import OperationalError
from func_connect_db import connect_db

#connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432')

def select_data(connection, query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error {e} occurred")


