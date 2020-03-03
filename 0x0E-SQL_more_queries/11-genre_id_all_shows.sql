-- Lists data given one requirement.
SELECT c.title, b.genre_id
FROM tv_show_genres b
LEFT JOIN tv_shows c
ON b.show_id = c.id
OR b.show_id IS NULL
GROUP BY c.title, b.genre_id
ORDER BY c.title, b.genre_id ASC;
