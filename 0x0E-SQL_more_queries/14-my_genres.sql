#!/usr/bin/env bash
# this is my sql 
-- lists all privileges
SET @dexter_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- List all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = @dexter_id
ORDER BY tv_genres.name ASC;
