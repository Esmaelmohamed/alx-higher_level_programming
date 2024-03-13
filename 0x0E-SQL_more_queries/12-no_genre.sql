-- Select the title of TV shows and their corresponding genre IDs
SELECT title, tv_show_genres.genre_id
-- Perform a LEFT JOIN between the tv_shows table and the tv_show_genres table
-- based on the id and show_id columns, respectively
FROM tv_shows
LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
-- Filter the results to only include records where there is no matching record in the tv_show_genres table
WHERE tv_show_genres.show_id IS NULL
-- Order the results first by the title of the TV show and then by the genre ID
ORDER BY title, tv_show_genres.genre_id;

