-- Lists the genre and the number of tv shows that belongs to the genre.
SELECT a.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres a
LEFT JOIN tv_show_genres b
ON a.id = b.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
