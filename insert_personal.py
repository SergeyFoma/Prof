import psycopg2
from psycopg2 import OperationalError

def connect_db(db_name, db_user, db_password, db_host, db_port):
    connection=None
    try:
        connection=psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
        )