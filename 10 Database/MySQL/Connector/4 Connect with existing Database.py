import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594",
  database="Ducat"
)

#If the database does not exist, you will get an error.
