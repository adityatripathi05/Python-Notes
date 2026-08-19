##############
# Database:
'''
- DB is an organized collection of structured and
unstructured data to make it easily accessible, manageable
and update.
- In simple words, a DB in a place where the data is stored
- Following types of DB available in the market:
    - Centralised DB
    - Distributed DB
    - Personal DB
    - End-user DB
    - Commercial DB
    - NoSQL DB
    - Operational DB
    - Relational DB
'''

############
# Relational DB
'''
- The data is stored in the form of relations.
- Popular relational DB systems are SQLite, MySQL,
SQL Server or PostgreSQL.
- The standard user and application program interface(API)
of a relational DB is the Structured Query Language
(SQL).
'''

############
# SQL: Structure Query Language
'''
- SQL is a computer language for storing, manipulating and
retrieving data stored in a relational DB.
'''

#############
# SQLite:
'''
- SQLite is embedded relational DB management system.
- It is self-contained, serverless, zero configuration
and transactional SQL DB engine.
'''

##############
# DB Browser for SQLite
'''
https://sqlitebrowser.org/dl/
'''

##############
# Load python sqlite module
import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)
'''
- version of the pysqlite, which is the binding of the
Python language to the SQLite DB.
- sqlite_version gives us the version of the SQLite
DB library
'''

##############
# Connecting to DB
'''
- connect(): create a connection object that represents
the DB.
- If the DB does not exist, then it will be created and
finally a DB object will be returned.
'''
conn= sqlite3.connect('Storage.db')
print('Connection Established')

#############
# Or, Create Temproary DB
'''
- Use argument ":memory:" to create a temporary DB in the
RAM:
'''
#db= sqlite3.connect(':memory:')
#print('Connection Established')

#############
# Close DB Connection
'''
- close(): This method closes the DB connection.
- NOTE: This doesn't automatically call commit().
If we just close our database connection without calling
commit() first, our changes will be lost!
'''
#db.close()
conn.close()


