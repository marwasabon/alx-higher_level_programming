#!/usr/bin/env bash
# this is my sql 
-- Write a script that prints thei full description of the 
-- table first_table from thei database hbtn_0c_0 in your MySQL server.
SELECT 'city', AVG ('value') AS 'avg_temp'
FROM 'temperatures'
WHERE 'month' = 7 OR 'month' = 8
GROUP BY 'city'
ORDER BY 'avg_temp' DESC
LIMIT 3;
