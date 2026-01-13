from func_connect_db import connect_db
from func_select_table import select_data

#connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432')

#select_table="SELECT * FROM professions"
select_table="SELECT p2.first_name, p1.name FROM personal p2 JOIN professions p1 ON p2.personal_id = p1.profession_id"


data=select_data(connect_db('prof_db', 'prof', '2105', '127.0.0.1', '5432'), select_table)

for d in data:
    print(d)