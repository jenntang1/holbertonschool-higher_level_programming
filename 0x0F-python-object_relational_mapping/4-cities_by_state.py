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
             "WHERE cities.name IS NOT NULL I"
             "AND states.id = cities.state_id "
             "ORDER BY citiesid")

    cursor.execute(query)

    all_cities = cursor.fetchall()

    for one_city in all_cities:
        print(one_city)

    cursor.close()

    connection.close()
