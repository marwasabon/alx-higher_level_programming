#!/usr/bin/env bash
# this is my sql 
-- lists all privileges the database if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Check if the table exists and create the table if not
CREATE TABLE IF NOT EXISTS states (
	  id INT AUTO_INCREMENT,
	  name VARCHAR(256) NOT NULL,
	  PRIMARY KEY (id)
	);
