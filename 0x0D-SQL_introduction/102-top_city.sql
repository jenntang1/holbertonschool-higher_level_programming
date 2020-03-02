-- Displays top 3 cities with highest average temperature.
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month between '07' and '08' GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
