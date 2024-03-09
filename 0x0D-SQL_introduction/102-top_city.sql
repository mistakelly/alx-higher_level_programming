-- select the city with the highest temperature
-- in the month of july
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY AVG(value) DESC LIMIT 3
