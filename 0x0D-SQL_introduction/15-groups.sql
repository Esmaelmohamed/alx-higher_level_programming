-- Script to list the number of records with the same score in the table second_table

-- Count records for each score and sort by the number of records (descending)
USE `hbtn_0c_0`;
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

