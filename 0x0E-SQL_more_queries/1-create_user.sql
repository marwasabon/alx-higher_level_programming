#!/usr/bin/env bash
# this is my sql
-- Creating  the user script
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Granting  SELECT privilege
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- changes take effect
FLUSH PRIVILEGES;
