-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

SELECT * FROM second_table WHERE score > 0;
SELECT * FROM second_table WHERE name IS NOT NULL AND name <> '';
