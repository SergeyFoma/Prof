from func_connect_db import connect_db
from func_create_table import create_table

table_create = """
    CREATE TABLE IF NOT EXISTS personal(
    personal_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    profession_id INT NOT NULL,
    FOREIGN KEY (profession_id) REFERENCES professions(profession_id),
    razryad INT NOT NULL,
    birth_year VARCHAR(50) NOT NULL,
    year_company VARCHAR(50) NOT NULL
);
"""

# create_connect('sm_app', 'sm_app_user', '2105', '127.0.0.1', '5432')

create_table(
    connect_db("prof_db", "prof", "2105", "127.0.0.1", "5432"),
    table_create
)