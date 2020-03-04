-- Lists all tv shows without a genre.
SELECT c.title, b.genre_id
FROM tv_show_genres AS b
RIGHT JOIN tv_shows AS c
ON b.show_id = c.id
WHERE b.genre_id IS NULL
ORDER BY c.title, b.genre_id ASC;
