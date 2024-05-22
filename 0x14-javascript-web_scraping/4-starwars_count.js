#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the Star Wars API URL from command-line arguments
const starWarsUri = process.argv[2];
let times = 0;

// Make an HTTP request to the provided URL
request(starWarsUri, function (_err, _res, body) {
  // Parse the response body as JSON
  const results = JSON.parse(body).results;

  // Iterate over each movie in the results
  for (let i = 0; i < results.length; ++i) {
    const characters = results[i].characters;

    // Iterate over each character URL in the movie
    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      // Extract the character ID from the URL
      const characterId = character.split('/')[5];

      // Count the occurrences of character ID 18
      if (characterId === '18') {
        times += 1;
      }
    }
  }

  // Print the total count of character ID 18 appearances
  console.log(times);
});

