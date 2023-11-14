#!/usr/bin/env bash
# this is my sql 
-- Write a script that prints thei full description of the 
-- table first_table from thei database hbtn_0c_0 in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (
	    id INT,
	    name VARCHAR(256),
	    score INT
	);
	INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
	INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
	INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
	INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);

