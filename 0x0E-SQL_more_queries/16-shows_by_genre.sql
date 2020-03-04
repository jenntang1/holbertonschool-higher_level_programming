-- Lists all tv shows and all the genres they belong to.
SELECT c.title, a.name
FROM tv_genres a
RIGHT JOIN tv_show_genres b ON a.id = b.genre_id
RIGHT JOIN tv_shows c ON b.show_id = c.id
ORDER BY c.title, a.name ASC
