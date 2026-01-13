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
    cursor.execute(f"INSERT INTO personal(first_name, name, last_name, ) VALUES {prof}", profs)
    print("Insert +++")