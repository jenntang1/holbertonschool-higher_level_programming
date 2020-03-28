#!/usr/bin/python3
""" 4. Cities by states """


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

    query = ("SELECT cities.id, cities.name, states.name "
             "FROM states, cities "
             "WHERE cities.name IS NOT NULL "
             "AND states.id = cities.state_id "
             "ORDER BY cities.id")

    cursor.execute(query)

    data = cursor.fetchall()

    for result in data:
        print(result)

    cursor.close()

    connection.close()
