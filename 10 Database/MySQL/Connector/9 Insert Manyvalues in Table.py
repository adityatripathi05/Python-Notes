import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594",
  database="Ducat"
)
cursor = conn.cursor()
cursor.executemany("INSERT INTO student VALUES,\
               [('Tonu',2,13,380),\
                ('Monu',3,16,435),\
                ('Sonu',4,16,388),]")

conn.commit()

print(cursor.rowcount, "record inserted.")

conn.close()
