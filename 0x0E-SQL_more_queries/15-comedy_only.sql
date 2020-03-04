-- Lists all tv shows that belongs to the Comedy genre.
SELECT c.title
FROM tv_genres AS a, tv_show_genres AS b, tv_shows AS c
WHERE a.name = "Comedy"
AND b.show_id = c.id
AND b.genre_id = a.id
GROUP BY c.title
ORDER BY c.title ASC;
