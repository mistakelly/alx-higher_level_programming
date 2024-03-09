-- select state with highest temperature
-- order by state

select state, MAX(value) AS 'max_temp'
from temperatures
GROUP BY state
ORDER BY state
