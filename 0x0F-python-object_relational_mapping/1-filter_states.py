#!/usr/bin/python3
""" 1. Filter states """


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    connection = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    all_states = cursor.fetchall()

    for one_state in all_states:
        print(one_state)

    cursor.close()

    connection.close()
