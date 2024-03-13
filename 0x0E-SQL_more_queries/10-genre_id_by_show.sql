-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_shows.title AS title, COUNT(title) AS `genre_id` FROM tv_shows
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
GROUP BY tv_shows.title;


CREATE TABLE `tv_shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) 

CREATE TABLE `tv_show_genres` (
  `show_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  KEY `show_id` (`show_id`),
  KEY `genre_id` (`genre_id`),
  FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`),
  FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
) 
-