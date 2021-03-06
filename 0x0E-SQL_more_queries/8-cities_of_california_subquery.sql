-- Lists all cities of California that's in the database.
SELECT cities.id, cities.name
FROM states, cities
WHERE states.name = 'California'
AND states.id = cities.state_id
ORDER BY cities.id ASC;
