-- Lists all tv shows and their ratings.
SELECT c.title, SUM(d.rate) AS rating
FROM tv_shows AS c
LEFT JOIN tv_show_ratings AS d
ON c.id = d.show_id
GROUP BY c.title
ORDER BY rating DESC;
