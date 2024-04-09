#!/usr/bin/node

// Get the first argument passed to the script
const x = parseInt(process.argv[2]);

// Check if the argument is a valid number
if (!isNaN(x)) {
  // Loop x times and print "C is fun" each time
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
