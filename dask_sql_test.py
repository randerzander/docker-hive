from pyhive import hive
cursor = hive.connect('hive-server').cursor()
cursor.execute('SELECT * FROM testdb.employee')
print(cursor.fetchall())
