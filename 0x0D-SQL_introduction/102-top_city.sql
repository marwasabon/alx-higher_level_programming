#!/usr/bin/env bash
# this is my sql 
-- Write a script that prints thei full description of the 
-- table first_table from thei database hbtn_0c_0 in your MySQL server.
SELECT city, AVG(temperature) as avg_temperature
FROM hbtn_0c_0
WHERE date_part('month', date) IN (7, 8)
GROUP BY city
ORDER BY avg_temperature DESC
LIMIT 3;
