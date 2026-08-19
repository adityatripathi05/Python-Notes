import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594",
  database="Ducat"
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE student\
               (name VARCHAR(25),\
               roll INTEGER(15) PRIMARY KEY,\
               age INTEGER(3))")

'''
Primary Key: When creating a table, you should also
create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY"
which will insert a unique number for each record.
Starting at 1, and increased by one for each record.
'''
'''
cursor.execute("CREATE TABLE student\
               (name VARCHAR(25),\
               roll INT AUTO_INCREMENT PRIMARY KEY,\
               age INTEGER(3)")
'''
