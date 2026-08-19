import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mapa0594"
)

cursor = conn.cursor()
'''cursor() is a method which act as a buffer for queries.
It return a object of cursor type.
'''

cursor.execute("CREATE DATABASE Ducat")

'''If the above code was executed with no errors, you have
successfully created a database'''
