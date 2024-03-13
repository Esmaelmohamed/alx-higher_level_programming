-- Create database 'hbtn_0d_2' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user 'user_0d_2' if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on all tables within the 'hbtn_0d_2' database to user 'user_0d_2' at localhost
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Refresh the privileges to apply the changes
FLUSH PRIVILEGES;

