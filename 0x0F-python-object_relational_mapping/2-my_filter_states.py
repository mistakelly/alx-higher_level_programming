#!/usr/bin/python3
"""
Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument.
Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running
on localhost at port 3306
You must use format to create the SQL query
with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


# import MySQLdb as mysql
import MySQLdb as mysql
from sys import argv
if __name__ == '__main__':
    username, password, database, searched = argv[1], argv[2], argv[3], argv[4]

    mydb = mysql.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    command = f'SELECT * FROM states WHERE name LIKE BINARY' \
              f' %s ORDER BY states.id'

    # create cursor
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(searched))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close connections
    cursor.close()
    mydb.close()
