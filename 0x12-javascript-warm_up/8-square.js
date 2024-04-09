#!/usr/bin/node

// Get the size of the square from the first argument
const size = parseInt(process.argv[2]);

// Check if the size is a valid number
if (!isNaN(size)) {
  // Loop to print each row of the square
  for (let i = 0; i < size; i++) {
    // Create a string with 'X' repeated 'size' times
    const row = 'X'.repeat(size);
    // Print the row
    console.log(row);
  }
} else {
  console.log("Missing size");
}
