-- shows contained in the database hbtn_0d_tvshows.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
--Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--You can use only one SELECT statement
--The database name will be passed as an argument of the mysql command

SELECT tv_shows.title AS `title`, tv_show_genres.genre_id from tv_shows
INNER JOIN tv_show_genre_id ON tv_shows.id = tv_show_genres.show_id
CASE 
    WHEN tv_show_genres.show_id  IS NULL THEN 'NULL'
    ELSE  
END
ORDER BY tv_shows.tiltle, tv_show_genres.genre_id ASC;