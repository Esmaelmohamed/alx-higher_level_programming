-- Select the name of TV genres
SELECT name
-- Join the tv_genres table with the tv_show_genres table based on the id and genre_id columns, respectively
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Join the resulting table with the tv_shows table based on the id and show_id columns, respectively
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
-- Filter the results to only include records where the title of the TV show is 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Order the results by the genre name
ORDER BY name;

