#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:
script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
code should not be executed when imported
"""
import MySQLdb as mysql
mydb = mysql.connect(
    host='localhost',
    user='root',
    password='31006569',
    db='hbtn_0e_0_usa'
)

# create cursor
cursor = mydb.cursor()

cursor.execute('SELECT * FROM states')

rows = cursor.fetchall()

if __name__ == '__main__':
    for row in rows:
        print(row)
