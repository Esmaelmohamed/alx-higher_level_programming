-- Select the title of TV shows and the name of their corresponding genres
SELECT title, tv_genres.name
-- Perform a LEFT JOIN between the tv_shows table and the tv_show_genres table based on the id and show_id columns, respectively
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Perform a LEFT JOIN between the resulting table and the tv_genres table based on the genre_id and id columns, respectively
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Order the results first by the title of the TV show and then by the name of the genre
ORDER BY title, tv_genres.name;

