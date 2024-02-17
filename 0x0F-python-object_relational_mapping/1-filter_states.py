#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
# set connection
import MySQLdb as mysql
import sys



if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    mydb = mysql.connect(
        host='localhost',
        db=database,
        user=username,
        passwd=password,
        port=3306
    )

    # establish connection
    cursor = mydb.cursor()

    cursor.execute("""
        SELECT *
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # close connections
    cursor.close()
    mydb.close()
