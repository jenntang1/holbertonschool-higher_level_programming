#!/usr/bin/python3
""" 2. Filter states by user input. """


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

    query = ("SELECT * "
             "FROM states "
             "WHERE name = '{}' "
             "ORDER BY id".format(argv[4]))

    cursor.execute(query)

    data = cursor.fetchall()

    for result in data:
        print(result)

    cursor.close()

    connection.close()
