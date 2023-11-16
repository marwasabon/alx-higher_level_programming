#!/usr/bin/env bash
# this is my sql 
-- lists all privileges
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California from the cities table
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id ASC;
