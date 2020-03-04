-- Lists all tv shows that belongs to the Comedy genre.
SELECT c.title
FROM tv_genres a, tv_show_genres b, tv_shows c
WHERE a.name = "Comedy"
AND b.show_id = c.id
AND b.genre_id = a.id
GROUP BY c.title
ORDER BY c.title ASC;
