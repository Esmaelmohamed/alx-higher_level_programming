-- Calculate the average temperature for each city in July and August, order by average temperature descending, and limit to top 3 cities
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;

