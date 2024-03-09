-- QUERRY THAT SEARCHES TEMPERATURES TABLE, CALC AVERAGE,  AND ORDER BY AVG.
-- group by city
SELECT city, AVG(value) as `avg_temp`
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
