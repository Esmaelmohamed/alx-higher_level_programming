#!/usr/bin/node

// Import the request module
const request = require('request');

// Make an HTTP request to the URL provided as a command-line argument
request(process.argv[2], function (_err, res) {
  // Print the response status code if a response was received
  console.log('code:', res.statusCode);
});

