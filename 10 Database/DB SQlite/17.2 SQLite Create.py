import sqlite3
conn= sqlite3.connect('Storage.db')
print('Connection Established')

############
# Create cursor object
'''
- cursor(): Create cursor object which is used to invoke
methods that execute SQLite statements in DB.
- sqlite3 cursor is a method of the connection object.
'''
cur= conn.cursor()
print('Cursor Object Created')

###########
# Create Table:
'''
- execute(): Using cursor object executes an SQL statement.
- SQL statement may be parameterized
(i,e. placeholders instead of SQL literals).
- The sqlite3 module supports two kinds of
placeholders: question marks and named placeholders
(named style).
'''
cur.execute('''CREATE TABLE Student
(Roll INT PRIMARY KEY,
FName VARCHAR(25) NOT NULL,
LName VARCHAR(25) NOT NULL,
Address Text,
Percentage REAL NOT NULL)''')
print('Table Created')

############
# Make Changes in DB:
'''
- commit(): This method commits the current
transaction i.e, this method saves all the changes we
make.
- If you don't call this method, anything you did
since the last call to commit() is not visible from
other database connections.
'''
conn.commit()

############
# Drop Table:
'''
cur.execute('DROP TABLE student')
print('Table Dropped')
conn.commit()
'''
conn.close()

