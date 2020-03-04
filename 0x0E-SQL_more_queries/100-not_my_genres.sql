-- Lists all genres that the tv show Dexter doesn't belong to.
SELECT a.name
FROM tv_genres AS a
WHERE a.name NOT IN
	(SELECT a.name
	FROM tv_genres AS a
	JOIN tv_show_genres AS b
	ON a.id = b.genre_id
	JOIN tv_shows AS c
	ON c.id = b.show_id
	WHERE c.title = 'Dexter')
ORDER BY a.name ASC;
