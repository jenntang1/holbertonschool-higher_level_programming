-- Lists data given one requirement.
SELECT c.title, b.genre_id
FROM tv_show_genres b
RIGHT JOIN tv_shows c
ON b.show_id = c.id
WHERE b.genre_id IS NULL
ORDER BY c.title, b.genre_id ASC;
