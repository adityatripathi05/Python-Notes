import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
'''
- all SQL queries are executed through cursor object
- execute() method return count of no.of rows inserted
in table
'''
for x in cursor:
  print(x)
