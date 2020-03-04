-- Lists all cities in the database.
SELECT cities.id, cities.name, states.name
FROM states, cities
WHERE states.id IS NOT NULL
AND states.id = cities.state_id
ORDER BY cities.id ASC;
