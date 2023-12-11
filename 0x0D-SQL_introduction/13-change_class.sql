#!/usr/bin/env bash
# this is my sql 
-- Write a script that prints thei full description of the 
-- table first_table from thei database hbtn_0c_0 in your MySQL server.
SELECT `state`, MAX (`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
