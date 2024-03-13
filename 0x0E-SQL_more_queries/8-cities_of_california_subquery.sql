-- Select the id and name of cities
SELECT id, name
-- Filter the cities where the state_id matches the id of the state named "California"
FROM cities
WHERE state_id = (
      -- Subquery to find the id of the state named "California"
      SELECT id
      FROM states
      WHERE name = "California")
-- Order the results by the city id in ascending order
ORDER BY id;

