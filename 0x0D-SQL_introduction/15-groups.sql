-- Count the occurrences of each score and order by the count in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

