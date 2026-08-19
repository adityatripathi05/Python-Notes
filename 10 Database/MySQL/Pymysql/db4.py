from pymysql import *

# establish connection with MySQL database
con = connect(host='localhost', user='root', password='mapa0594',
              database= 'table1' ,port=3306)
''' host takes ip address as an argument where the required database is stored
since my databse is in my system hence we can give 'localhost'''

cur = con.cursor()
'''cursor() is a method return a object of cursor type. It act as a buffer for
queries'''

count = cur.execute("select * from student ")
# execute() method return count of no.of rows selected from table
print(count, 'row selected')
'''execute() on select query may work inappropriate with different databases'''


'''commit() method is not required when fetching data from database'''

con.close()
# To close the connectivity of database
