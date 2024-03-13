-- Select the title of TV shows
SELECT title
-- Join the tv_shows table with the tv_show_genres table based on the id and show_id columns, respectively
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Join the resulting table with the tv_genres table based on the id and genre_id columns, respectively
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Filter the results to only include records where the name of the TV genre is 'Comedy'
WHERE tv_genres.name = 'Comedy'
-- Order the results by the title of the TV show
ORDER BY title;

