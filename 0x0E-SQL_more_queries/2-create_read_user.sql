#!/usr/bin/env bash
-- lists all privileges
-- Checks if the database exists and create the database if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user exists and create the user if not
DELIMITER $$
CREATE PROCEDURE CreateUserIfNotExists(IN p_user VARCHAR(16), IN p_password VARCHAR(41))
BEGIN
  IF NOT EXISTS (SELECT 1 FROM mysql.user WHERE user = p_user) THEN
    CREATE USER p_user@'localhost' IDENTIFIED BY p_password;
  END IF;
END$$
DELIMITER ;

-- Call the stored procedure to create the user
CALL CreateUserIfNotExists('user_0d_2', 'user_0d_2_pwd');

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Make the changes take effect
FLUSH PRIVILEGES;
