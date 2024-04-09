#!/usr/bin/node

// Define a function to compute factorial recursively
function factorial(n) {
    // Base case: factorial of 0 or 1 is 1
    if (isNaN(n) || n === 1 || n === 0) {
      return 1;
    }
    // Recursive case: compute factorial of n-1 and multiply by n
    return n * factorial(n - 1);
  }
  
  // Get the integer from the first argument
  const integer = parseInt(process.argv[2]);
  
  // Print the factorial of the integer
  console.log(factorial(integer));
  