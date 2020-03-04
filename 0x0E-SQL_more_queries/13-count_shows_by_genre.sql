-- Lists the genre and the number of tv shows that belongs to the genre.
SELECT a.name, COUNT(b.show_id) AS number_of_shows
FROM tv_genres a
LEFT JOIN tv_show_genres b
ON a.id = b.genre_id
GROUP BY a.name
ORDER BY number_of_shows DESC;
