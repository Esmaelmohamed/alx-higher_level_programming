#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Make an HTTP request to the URL provided as the first command-line argument
request(process.argv[2], function (err, _res, body) {
  // Check for an error during the request
  if (err) {
    console.log(err);
  } else {
    // Object to store the count of completed tasks by each user
    const completedTasksByUsers = {};
    // Parse the response body as JSON
    body = JSON.parse(body);

    // Iterate over each task in the response
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      // Initialize the count for the user if not already done
      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      // Increment the count for the user if the task is completed
      if (completed) {
        ++completedTasksByUsers[userId];
      }
    }

    // Print the completed tasks count by each user
    console.log(completedTasksByUsers);
  }
});

