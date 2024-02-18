#!/usr/bin/python3
"""
prevent sql injection
"""
if __name__ == '__main__':
    # receive command line arguments
    import MySQLdb as mysql
    from sys import argv
    username, password, database, searched = argv[1], argv[2], argv[3], argv[4]

    # establish connection

    mydb = mysql.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
    )


    # create a cursor
    cursor = mydb.cursor()

    cursor.execute('SELECT * FROM states WHERE name LIKE BINARY %s', (searched,))
    # fetch all data
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # close connections
    cursor.close()
    mydb.close()
