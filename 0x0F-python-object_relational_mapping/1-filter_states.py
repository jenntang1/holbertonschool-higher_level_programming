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

    query = ("SELECT * "
             "FROM states "
             "ORDER BY id")

    cursor.execute(query)

    data = cursor.fetchall()

    for result in data:
        if 'N' == result[1][0]:
            print(result)

    cursor.close()

    connection.close()
