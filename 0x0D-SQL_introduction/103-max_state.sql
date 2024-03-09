-- select state with highest temperature
-- order by state

SELECT state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state
