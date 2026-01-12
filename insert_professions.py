import psycopg2
from psycopg2 import OperationalError

# create connection db

def connect_db(db_name, db_user, db_password, db_host, db_port):
    connection=None
    try:
        connection=psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f'Connect database {db_name} executed successful.')
    except OperationalError as e:
        print("The error {e} ocurred!")

    return connection
# connect_db('prof_db', 'prof', '2105', 'localhost', '5432')

def insert_table(connection):
    connection.autocommit=True
    cursor=connection.cursor()
    profs=[
        ('Слесарь-ремонтник',),
        ('Электрогазосварщик',),
        ('Стропальщик',),
        ('Оператор ТУ',),
        ('Сливщик-разливщик',),
        ('Оператор товарный',)
    ]
    prof = ','.join(['%s']*len(profs))
    cursor.execute(f"INSERT INTO professions(name) VALUES {prof}", profs)
    print("Insert +++")

insert_table(connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432'))