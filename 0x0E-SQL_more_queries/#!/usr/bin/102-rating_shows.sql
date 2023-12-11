#!/usr/bin/env bash
# this is my sql
-- lists all privileges
-- lists all the shows 
SELECT `title`, SUM (`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r
ON t.`id` = r.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
