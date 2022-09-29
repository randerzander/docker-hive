from pyhive import hive
from dask_sql import Context
cursor = hive.connect('hive-server').cursor()
cursor.execute('SELECT * FROM testdb.employee')

# validates container's ability to query from hive
print(cursor.fetchall())

c = Context()
c.create_table("employee", cursor, hive_table_name="testdb.employee")
