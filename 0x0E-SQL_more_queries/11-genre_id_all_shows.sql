-- shows contained in the database hbtn_0d_tvshows.

SELECT tv_shows.title AS `title`, tv_show_genres.genre_id from tv_shows
INNER JOIN tv_show_genre_id ON tv_shows.id = tv_show_genres.show_id
CASE 
    WHEN tv_show_genres.show_id  IS NULL THEN 'NULL'
    ELSE  
END
ORDER BY tv_shows.tiltle, tv_show_genres.genre_id ASC;