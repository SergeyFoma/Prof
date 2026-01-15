import psycopg2
from psycopg2 import OperationalError

from func_connect_db import connect_db

# from insert_user import v

connect_db("prof_db", "prof", "2105", "127.0.0.1", "5432")

v_first_name = input("Фамилия: ")
v_name = input("Имя: ")
v_last_name = input("Отчество: ")
v_profession_id = input("Профессия: ")
v_razryad = input("Разряд: ")
v_birth_year = input("Год рождения: ")
v_year_company = input("Дата приёма: ")
v = (
    v_first_name,
    v_name,
    v_last_name,
    v_profession_id,
    v_razryad,
    v_birth_year,
    v_year_company,
)

def insert_table(connection):
    """The function for loading data into a table."""
    connection.autocommit = True
    cursor = connection.cursor()
    # values=[
    #     ('SPЗейбольд', 'Руслан', 'Федорович', 2, 4, '07.09.1997', '22.22.2222'),
    #     ('SKКабов', 'Виктор', 'Владимирович', 1, 6, '16.06.1986', '22.22.2222')
    # ]

    values = [v]
    val = ",".join(["%s"] * len(values))
    cursor.execute(
        f"INSERT INTO personal(first_name, name, last_name, profession_id, razryad, birth_year, year_company) VALUES {val}",
        values,
    )
    
    print("Еhe data has been added successfully!")
   

insert_table(connect_db("prof_db", "prof", "2105", "127.0.0.1", "5432"))
