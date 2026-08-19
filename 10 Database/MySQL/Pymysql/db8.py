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


row = cur.fetchmany(3)
print(row)

cur.scroll(1, mode='relative')
'''for navigation scroll() method takes argument as cursor required
positional no. to navigate in relative/ absolute mode from current cursor
position'''

con.close()
# To close the connectivity of database
