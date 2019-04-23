import pymysql

conn2 = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '1234'
)

cursor = conn2.cursor()
create_database = 'create database johntable default charset utf8'
cursor.execute(create_database)
conn2.commit
cursor.close()
conn2.close()
