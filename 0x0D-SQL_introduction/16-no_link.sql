-- Lists records with specific requirements from the second_table table.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
