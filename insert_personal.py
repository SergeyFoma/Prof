import psycopg2
from psycopg2 import OperationalError

from func_connect_db import connect_db

connect_db("prof_db", "prof", "2105", "127.0.0.1", "5432")