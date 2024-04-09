#!/usr/bin/node

// Get the first argument passed to the script
const firstArgument = process.argv[2];

// Check if an argument is passed
if (firstArgument === undefined) {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
