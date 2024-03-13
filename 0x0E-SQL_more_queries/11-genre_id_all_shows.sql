-- shows contained in the database hbtn_0d_tvshows.

-- Each record should display: tv_shows.title - tv_show_genres.genre_id
--Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--You can use only one SELECT statement
--The database name will be passed as an argument of the mysql command

SELECT tv_shows.title AS `title`, IFNULL(tv_show_genres.genre_id, 'NULL'), tv_show_genres.genre_id as `genre_id`
FROM tv_shows JOIN tv_show_genres ON tv_shows.id =  tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;