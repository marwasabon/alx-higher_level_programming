#!/usr/bin/env bash
# this is my sql
-- Creating  the user script
CREATE USER 'read_user'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Granting  SELECT privilege
GRANT SELECT ON database_name.* TO 'read_user'@'localhost';

-- changes take effect
FLUSH PRIVILEGES;
