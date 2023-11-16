#!/usr/bin/env bash
# this is my sql
-- lists all privileges
SET @comedy_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- List all shows that are not of the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
  SELECT tv_show_genres.show_id
  FROM tv_show_genres
  WHERE tv_show_genres.genre_id = @comedy_id
)
ORDER BY tv_shows.title ASC;
