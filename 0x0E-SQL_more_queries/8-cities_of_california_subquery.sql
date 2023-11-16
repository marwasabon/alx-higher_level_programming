#!/usr/bin/env bash
# this is my sql 
-- lists all privileges
SELECT * FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
