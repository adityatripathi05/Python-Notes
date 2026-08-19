import sqlite3
conn= sqlite3.connect('Storage.db')
cur= conn.cursor()

###########
# Modify Table Structure: Add Column
'''
cur.execute('ALTER TABLE student ADD Age INT')
conn.commit()
print('Age Column Added')
'''

###########
# Update row in Table:
'''
cur.execute("UPDATE student SET address='Delhi', Age=15\
            WHERE Roll=107")
conn.commit()
print('Record Updated')
'''

###########
# Update row using ?:
'''
a= int(input("Enter age: "))
r= int(input("Enter roll: "))
cur.execute("UPDATE student SET Age=? WHERE Roll=?",(a,r))
conn.commit()
print('Record Updated')
'''

#############
# Delete row in Table:
'''
cur.execute("DELETE FROM student WHERE Roll=107")
conn.commit()
print('Record Deleted')
'''

#############
# Drop all Data but not structure of Table
'''
cur.execute("DELETE FROM student")
conn.commit()
print('All Record Deleted')
'''

conn.close()
