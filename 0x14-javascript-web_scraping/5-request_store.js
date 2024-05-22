#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');
// Import the filesystem module for file operations
const fs = require('fs');

// Make an HTTP request to the URL provided as the first command-line argument
request(process.argv[2], function (_err, _res, body) {
  // Write the response body to the file specified as the second command-line argument
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    // Check for an error during the file write operation
    if (err) {
      // Print the error message if an error occurred
      console.log(err);
    }
  });
});

