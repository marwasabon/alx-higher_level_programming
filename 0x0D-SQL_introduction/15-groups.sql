#!/usr/bin/env bash
# this is my sql 
-- Write a script that prints thei full description of the 
-- table first_table from thei database hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
