#!/usr/bin/node

// Define the add function
function add(a, b) {
    return a + b;
  }
  
  // Get the first and second integers from the arguments
  const firstInteger = parseInt(process.argv[2]);
  const secondInteger = parseInt(process.argv[3]);
  
  // Check if the arguments are valid integers
  if (!isNaN(firstInteger) && !isNaN(secondInteger)) {
    // Call the add function and print the result
    console.log(add(firstInteger, secondInteger));
  } else {
    console.log("Invalid input. Please provide two integers as arguments.");
  }
  