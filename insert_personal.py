import psycopg2
from psycopg2 import OperationalError

from func_connect_db import connect_db

connect_db("prof_db", "prof", "2105", "127.0.0.1", "5432")

def insert_table(connection):
    connection.autocommit=True
    cursor=connection.cursor()
    values=[
        (5, 'PЗейбольд', 'Руслан', 'Федорович', 2, 4, '07.09.1997', '22.22.2222'),
        (6, 'KКабов', 'Виктор', 'Владимирович', 1, 6, '16.06.1986', '22.22.2222')
    ]
    val = ','.join(['%s']*len(values))
    cursor.execute(f"INSERT INTO personal(personal_id, first_name, name, last_name, profession_id, razryad, birth_year, year_company) VALUES {val}", values)
    print('Еhe data has been added successfully!')

insert_table(connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432'))