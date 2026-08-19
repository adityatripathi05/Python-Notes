import sqlite3
conn= sqlite3.connect('Storage.db')
cur= conn.cursor()

##########
# Read all Data:
'''
- Use * to select all the columns from a table.
'''
'''
cur.execute('SELECT * FROM student')
print(cur) # Iterator
for col in cur:
    print(col[0],col[1],col[2],col[3],col[4])
'''

##########
# Read few columns:
'''
cur.execute('SELECT FName,LName FROM student')
for col in cur:
    print(col[0],col[1])
'''

#############
# Represent Read Data: fetchall,fetchmany,fetchone
'''
cur.execute('SELECT * FROM student')

print('Fetch first data')
data1=cur.fetchone()
print(data1)

print('Fetch first three data')
data2=cur.fetchmany(3)
print(data2)

print('Fetch all data')
data3= cur.fetchall()
print(data3)
'''

############
# Read Distinct Data:
'''
cur.execute("SELECT DISTINCT ADDRESS FROM student")
data= cur.fetchall()
for col in data:
    print(col[0])
'''

############
# Conditional Data Reading: 'WHERE'
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Address='Delhi'")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

##############
# Retrieving Data with "?":
'''
r= int(input("Enter roll no.: "))
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Roll=?", (r,))
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

##############
# Multiple Conditional Data Reading: 'WHERE','AND','OR'
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Address='Delhi' AND Percentage>80")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

##
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Address='Delhi' OR Percentage>80")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

##############
# Multiple Data Reading: 'WHERE','IN','BETWEEN'
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Address IN ('Delhi','UP')")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

##
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE Percentage BETWEEN 85 AND 95")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

#############
# LIKE Operator:
# Select employee whose name starts with 'A'
'''
cur.execute("SELECT FName,Percentage FROM student\
            WHERE FName LIKE 'A%'")
data= cur.fetchall()
for col in data:
    print(col[0],'-->',col[1])
'''

conn.close()




