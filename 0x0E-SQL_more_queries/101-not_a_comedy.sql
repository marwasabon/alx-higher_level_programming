#!/usr/bin/env bash
# this is my sql
-- lists all privileges
-- List all shows that are not of the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_show_id
    FROM tv_genres
    WHERE name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
