from pymysql import *

# establish connection with MySQL database
con = connect(host='localhost', user='root', password='mapa0594',
              database= 'table1' ,port=3306)
''' host takes ip address as an argument where the required database is stored
since my databse is in my system hence we can give 'localhost'''

cur = con.cursor()
'''cursor() is a method return a object of cursor type. It act as a buffer for
queries'''

count1 = cur.execute("insert into student values('chintu', 5, 700)")
count2 = cur.execute("update student set marks = marks+ 20")
count3 = cur.execute("delete from student where marks<400")

# all SQL queries are executed through cursor object
# execute() method return count of no.of rows inserted in table
print(count1, 'row inserted')
print(count2, 'row updated')
print(count3, 'row deleted')
# But uptill now the executed queries are not reflected back to the table

con.commit()
'''commit() method internally establish link between connect() and cursor() and
reflect all the queries into curson() onto connect() and is reflected back on to
the table/db'''

con.close()
# To close the connectivity of database
