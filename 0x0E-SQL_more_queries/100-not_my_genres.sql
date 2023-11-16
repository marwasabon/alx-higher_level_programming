#!/usr/bin/env bash
# this is my sql
-- lists all privileges
SELECT DISTINCT tv_genres.name 
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title <> 'Dexter'
AND tv_genres.name IS NOT NULL
ORDER BY tv_genres.name ASC;
