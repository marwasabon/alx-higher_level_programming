#!/usr/bin/env bash
# this is my sql 
-- lists all privileges
SET @comedy_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- List all Comedy shows
SELECT tv_shows.title FROM tv_genres INNER JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON
tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
