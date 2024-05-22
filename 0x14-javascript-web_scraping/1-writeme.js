#!/usr/bin/node

// Import the filesystem module
const fs = require('fs');

// Write the specified content to the file provided as a command-line argument
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  // Check for an error during the file write operation
  if (err) {
    // Print the error message if an error occurred
    console.log(err);
  }
});

