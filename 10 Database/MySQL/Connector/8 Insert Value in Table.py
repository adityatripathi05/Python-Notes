import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mapa0594",
  database="Ducat"
)
cursor = conn.cursor()
cursor.execute("INSERT INTO student VALUES\
               ('Sonu',1, 15, 400)")

conn.commit()
'''commit() method internally establish link between
connect() and cursor() and reflect all the queries into
curson() onto connect() and is reflected back on to
the table/db'''

print(cursor.rowcount, "record inserted.")

# Get Address of last recent row inserted
print("1 record inserted, ID:", cursor.lastrowid)

conn.close()
