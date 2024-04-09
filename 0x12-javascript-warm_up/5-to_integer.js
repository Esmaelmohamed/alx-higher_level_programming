#!/usr/bin/node

// Get the first argument passed to the script
const firstArgument = process.argv[2];

// Convert the first argument to an integer
const firstArgumentInt = parseInt(firstArgument);

// Check if the conversion was successful
if (!isNaN(firstArgumentInt)) {
  console.log(`My number: ${firstArgumentInt}`);
} else {
  console.log('Not a number');
}
