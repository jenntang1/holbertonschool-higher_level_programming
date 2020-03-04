-- Lists all tv shows and all their genre id's.
SELECT c.title, b.genre_id
FROM tv_show_genres b
RIGHT JOIN tv_shows c
ON b.show_id = c.id
GROUP BY c.title, b.genre_id
ORDER BY c.title, b.genre_id ASC;
