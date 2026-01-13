import psycopg2
from psycopg2 import OperationalError

from func_connect_db import connect_db


#connect_db('prof_db', 'prof', '2105', 'localhost', '5432')

def insert_table(connection):
    connection.autocommit=True
    cursor=connection.cursor()
    values=[
        (1, 'Слесарь-ремонтник',),
        (2, 'Электрогазосварщик',),
        (3, 'Стропальщик',),
        (4, 'Оператор ТУ',),
        (5, 'Сливщик-разливщик',),
        (6, 'Оператор товарный',)
    ]
    val = ','.join(['%s']*len(values))
    cursor.execute(f"INSERT INTO professions(profession_id, name) VALUES {val}", values)
   

insert_table(connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432'))