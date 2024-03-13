-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select the city ID, city name, and state name
SELECT cities.id, cities.name, states.name AS state_name
-- Join the cities table with the states table based on the state_id column
-- to get the corresponding state name for each city
FROM cities
JOIN states ON cities.state_id = states.id
-- Order the results by the city ID in ascending order
ORDER BY cities.id ASC;

