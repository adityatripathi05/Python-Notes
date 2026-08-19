from pymysql import *

# establish connection with MySQL database
con = connect(host='localhost', user='root', password='mapa0594',
              database= 'table1' ,port=3306)
''' host takes ip address as an argument where the required database is stored
since my databse is in my system hence we can give 'localhost'''

cur = con.cursor()
'''cursor() is a method return a object of cursor type. It act as a buffer for
queries'''

cur.execute("select * from student")
# execute() method return count of no.of rows selected from table
print(cur.rowcount, 'row selected')
'''Since cursor is a python , so seleted columns of table from database
comes as each row of it as tuple of tuple in cursor() object. Hence we have
a special method to count no. of rows in cursor'''


row = cur.fetchone()
print(row)
'''fetchone() method will fetch one row of table inside the cursor and return
row as a tuple and cursor is positioned one step ahead from its previous
position'''

row = cur.fetchone()
print(row)

con.close()
# To close the connectivity of database
