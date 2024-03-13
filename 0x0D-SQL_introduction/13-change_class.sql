-- Script to remove all records with a score <= 5 in the table second_table

-- Delete records with a score <= 5
USE `hbtn_0c_0`;
DELETE FROM second_table WHERE score <= 5;

