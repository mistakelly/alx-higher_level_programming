#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb as mysql
from sys import argv


def connection(connect, username, password, database, prt, state):
    mydb = mysql.connect(
        host=connect,
        user=username,
        passwd=password,
        db=database,
        port=prt
    )

    cursor = mydb.cursor()
    query = "SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name=%s) ORDER BY cities.id ASC"
    cursor.execute(query, (state,))

    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(map(str, row)))

    cursor.close()
    return mydb


if __name__ == '__main__':
    mydbase = connection('localhost', argv[1], argv[2], argv[3], 3306, argv[4])
    mydbase.close()

