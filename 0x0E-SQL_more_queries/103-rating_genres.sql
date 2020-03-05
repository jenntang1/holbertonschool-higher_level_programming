-- Lists all genres and their ratings.
SELECT a.name, SUM(d.rate) AS rating
FROM tv_genres AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.genre_id
LEFT JOIN tv_shows AS c
ON b.show_id = c.id
LEFT JOIN tv_show_ratings AS d
ON c.id = d.show_id
GROUP BY a.name
ORDER BY rating DESC;
