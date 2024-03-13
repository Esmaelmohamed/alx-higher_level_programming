-- Select the name of TV genres and the count of TV shows associated with each genre
SELECT name AS genre, COUNT(*) AS number_of_shows
-- Join the tv_genres table with the tv_show_genres table based on the id and genre_id columns, respectively
FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
-- Group the results by tv_show_genres.genre_id to count the number of shows for each genre
GROUP BY tv_show_genres.genre_id
-- Order the results by the number of shows in descending order
ORDER BY number_of_shows DESC;

