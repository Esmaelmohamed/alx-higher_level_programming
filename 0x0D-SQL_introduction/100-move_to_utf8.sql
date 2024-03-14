-- Switch to the specified database
USE `hbtn_0c_0`;

-- Alter the character set and collation of the table 'first_table'
ALTER TABLE `first_table`
-- Convert the character set to utf8mb4
CONVERT TO CHARACTER SET utf8mb4
-- Set the collation to utf8mb4_unicode_ci for proper Unicode support
COLLATE utf8mb4_unicode_ci;

