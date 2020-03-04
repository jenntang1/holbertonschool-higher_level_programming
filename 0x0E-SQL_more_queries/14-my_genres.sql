-- Lists the genres the tv show Dexter belongs to.
SELECT a.name
FROM tv_genres AS a, tv_show_genres AS b, tv_shows AS c
WHERE c.title = "Dexter"
AND b.genre_id = a.id
AND b.show_id = c.id
GROUP BY a.name
ORDER BY a.name ASC;
