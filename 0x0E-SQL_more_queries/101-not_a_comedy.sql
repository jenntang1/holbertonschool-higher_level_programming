-- Lists all tv shows that doesn't belong to the genre Comedy.
SELECT c.title
FROM tv_shows AS c
WHERE c.title NOT IN
	(SELECT c.title
	FROM tv_shows AS c
	JOIN tv_show_genres AS b
	ON c.id = b.show_id
	JOIN tv_genres AS a
	ON a.id = b.genre_id
	WHERE a.name = 'Comedy')
ORDER BY c.title ASC;
