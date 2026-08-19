import sqlite3
conn= sqlite3.connect('Storage.db')
cur= conn.cursor()
try:
    cur.execute('''CREATE TABLE Student
(Roll INT PRIMARY KEY,
FName VARCHAR(25) NOT NULL,
LName VARCHAR(25) NOT NULL,
Address Text,
Percentage REAL NOT NULL)''')
    print('Table Created')
except:
    pass

##########
# Insert Record in Same Order:
cur.execute('''INSERT INTO student VALUES
(101,'Aditya','Tripathi','Noida',88.6)''')
conn.commit()

#############
# Insert Record in custom Order
cur.execute('''INSERT INTO student
(FName, LName,Roll, Address, Percentage) VALUES
('Sumit','Sharma',102,'Noida',67.5)''')
conn.commit()

##############
# Insert only NOT NULL records
cur.execute('''INSERT INTO student
(FName, LName, Roll, Percentage) VALUES
('Rohit','Sharma',103,88)''')
conn.commit()

############
# Insert value from variable: Use the "?" placeholder
data=(104,'Amit','Rana','UP',81.6)
cur.execute('''INSERT INTO student VALUES
(?,?,?,?,?)''',data)
conn.commit()

############
# Insert record using dictionary as ":keyname" placeholder
cur.execute('''INSERT INTO student
(FName,LName,Roll,Address,Percentage) VALUES
(:FName,:LName,:Roll,:Address,:Percentage)''',
{'FName':'Mark','LName':'Zuker','Roll':105,
 'Address':'Delhi','Percentage':78})
conn.commit()

##############
# Insert several data: Use executemany and a list with tuples
data=[(106,'Prem','Shukla','Delhi',88.6),
      (107,'Rohit','Raina','UP',71.6)]
cur.executemany('''INSERT INTO student VALUES
(?,?,?,?,?)''',data)
conn.commit()

print('Record Inserted')

############
# Check total changes
'''
- total_changes(): This routine returns the total
number of database rows that have been modified,
inserted, or deleted since the database connection
was opened.
'''
changes=conn.total_changes
print("Total no. of rows inserted:", changes)

conn.close()
