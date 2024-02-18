#!/usr/bin/python3
"""
Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

$ ~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$
What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb as mysql
from sys import argv


def connection(connect, username, password, database, search, prt):
    """
        lists all row in states table
        connect:port,
        username: username of the user,
        password: password of the database,
        database: the database to use,
        prt: port to connect.
    """
    mydb = mysql.connect(
        host=connect,
        user=username,
        passwd=password,
        db=database,
        port=prt
    )

    # create cursor
    cursor = mydb.cursor()
    command = "SELECT * FROM states WHERE name LIKE BINARY %s"

    cursor.execute(command, (search, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close connections
    cursor.close()
    return mydb


if __name__ == '__main__':
    mydbase = connection('localhost', argv[1], argv[2], argv[3], argv[4], 3306)
    mydbase.close()
