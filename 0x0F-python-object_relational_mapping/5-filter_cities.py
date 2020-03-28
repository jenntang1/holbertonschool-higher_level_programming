#!/usr/bin/python3
""" 5. All cities by state """


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

    query = ("SELECT cities.name "
             "FROM states, cities "
             "WHERE cities.name IS NOT NULL "
             "AND states.id = cities.state_id "
             "AND states.name = '%s' "
             "ORDER BY cities.id" % argv[4])

    cursor.execute(query)

    data = cursor.fetchall()

    string = ', '.join([result[0] for result in data])

    print(string)

    cursor.close()

    connection.close()
