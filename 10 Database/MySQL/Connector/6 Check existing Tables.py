import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594",
  database="Ducat"
)
cursor = conn.cursor()
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)
