#!/usr/bin/node

// Import the filesystem module
const fs = require('fs');

// Read the file specified in the command line arguments using UTF-8 encoding
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  // Check for an error during the file read operation
  if (err) {
    // Print the error message if an error occurred
    console.log(err);
  } else {
    // Write the content of the file to the standard output if no error occurred
    process.stdout.write(data);
  }
});

