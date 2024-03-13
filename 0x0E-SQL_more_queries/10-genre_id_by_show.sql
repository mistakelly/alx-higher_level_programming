-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id COUNT(*) FROM hbtn_0d_tvshows
ORDER BY tv_shows.title, tv_show_genres.genre_id
GROUP BY tv_shows.title, tv_show_genres.genre_id;
