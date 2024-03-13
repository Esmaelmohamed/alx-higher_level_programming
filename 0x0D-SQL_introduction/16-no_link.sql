-- Script to list all records of the table second_table with a name value in descending score order

-- Select the score and name fields from second_table where name is not null, ordered by score (descending)
USE `hbtn_0c_0`;
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

