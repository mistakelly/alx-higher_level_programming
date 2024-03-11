-- a script that lists all the cities of California that can be found in the database 
-- The database name will be passed as an argument of the mysql command

SELECT id, name FROM cities WHERE state_id = 
    (
        SELECT id FROM states
        where name = 'California'
    )
ORDER BY cities.id ASC;
