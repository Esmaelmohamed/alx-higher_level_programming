-- Select the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join the tv_shows table with the tv_show_genres table based on the show_id column
-- to get the genre IDs associated with each TV show
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results first by the title of the TV show and then by the genre ID
ORDER BY tv_shows.title, tv_show_genres.genre_id;

