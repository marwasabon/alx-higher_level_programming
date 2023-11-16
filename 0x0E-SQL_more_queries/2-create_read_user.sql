#!/usr/bin/env bash
# this is my sql 
-- lists all privileges
-- Checks if the database exists and create the database if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Grants the user 
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
--- Grants Select to the user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
