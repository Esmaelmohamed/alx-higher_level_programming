#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if no arguments are passed or only one argument is passed
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and remove duplicates
  const integers = [...new Set(args.map(Number))];

  // Sort the integers in descending order
  const sortedIntegers = integers.sort((a, b) => b - a);

  // Print the second biggest integer
  console.log(sortedIntegers[1]);
}
