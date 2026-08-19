'''
Python needs a MySQL driver to access the MySQL database.
cmd: pip install mysql-connector-python
'''
# Create Connection:
import mysql.connector
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
)
print(conn)

''' host takes ip address as an argument where the
database is required to stored since my database will be
in my system hence we can give 'localhost
'''



