import sqlite3
conn= sqlite3.connect('Storage.db')
cur= conn.cursor()

##########
# Count Record
'''
cur.execute('SELECT COUNT (Roll) FROM student')
print(cur.fetchone())
'''

##########
# Calculate Sum of Numeric Record
'''
cur.execute('SELECT SUM (Percentage) FROM student')
print(cur.fetchone())
'''

##########
# Calculate Average of Numeric Record
'''
cur.execute('SELECT AVG (Percentage) FROM student')
print(cur.fetchone())
'''

##########
# Find Minimum of Numeric Record
'''
cur.execute('SELECT MIN (Percentage) FROM student')
print(cur.fetchone())
'''

##########
# Find Maximum of Numeric Record
'''
cur.execute('SELECT MAX (Percentage) FROM student')
print(cur.fetchone())
'''

##########
# Order Record in ascending and descending
'''
cur.execute('SELECT * FROM student ORDER BY Percentage')
for i in cur.fetchall():
    print(i)
'''

# In descending
'''
cur.execute('SELECT * FROM student ORDER BY Percentage DESC')
for i in cur.fetchall():
    print(i)
'''

conn.close()




