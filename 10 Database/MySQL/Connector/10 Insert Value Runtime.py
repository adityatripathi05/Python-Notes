import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="python",
  database="Shilpi"
)

cursor = conn.cursor()

# user input data:
name = input('enter name: ')
roll = int(input('enter roll no.: '))
age = int(input('enter age: '))
marks = int(input('enter marks out of 500: '))

cursor.execute(f"insert into student values\
                    ('{name}',{roll},{age},{marks})")

con.commit()

con.close()
