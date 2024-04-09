#!/usr/bin/node

// Check the number of arguments passed to the script
const argsLength = process.argv.length;

// Print message based on the number of arguments
if (argsLength === 2) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
