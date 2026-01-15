from func_connect_db import connect_db 

#connect_db("prof_db", "prof", "2105", "localhost", "5432")

def update_table(connection):
    '''The function update table'''
    connection.autocommit=True
    cursor=connection.cursor()
    cursor.execute(
        """UPDATE personal SET first_name='Халилов', name='Асиф', last_name='Зохраб оглы', profession_id=1, razryad=6, birth_year='18.04.1972', year_company='00.00.0000' WHERE personal_id=14"""
    )

update_table(connect_db("prof_db", "prof", "2105", "localhost", "5432"))