-- Script to list all records with a score >= 10 in the table second_table

-- Select the score and name fields from second_table where score >= 10, ordered by score
USE `hbtn_0c_0`;
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

