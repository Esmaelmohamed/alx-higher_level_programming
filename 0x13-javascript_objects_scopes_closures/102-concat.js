#!/usr/bin/node

// Importing the 'fs' module for file system operations
const fs = require('fs').promises;
// Importing the 'argv' object from the 'process' module for accessing command line arguments
const { argv } = require('process');

// Reading the contents of the file specified by the third command line argument
fs.readFile(argv[2], 'utf8')
  // Writing the read data to the file specified by the fourth command line argument
  .then(data => fs.writeFile(argv[4], data, 'utf8'))
  // Handling any errors that occur during the file operations
  .catch(err => console.error(err));

// Reading the contents of the file specified by the fourth command line argument
fs.readFile(argv[3], 'utf8')
  // Appending the read data to the file specified by the fourth command line argument (using 'flag: 'a'')
  .then(data => fs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  // Handling any errors that occur during the file operations
  .catch(err => console.error(err));

