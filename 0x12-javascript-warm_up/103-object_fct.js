#!/usr/bin/node

const myObject = {
    type: 'object',
    value: 12,
    // Define the incr function
    incr: function() {
      this.value++;
    }
  };
  
  console.log(myObject);
  
  // Call the incr function
  myObject.incr();
  console.log(myObject);
  
  // Call the incr function again
  myObject.incr();
  console.log(myObject);
  
  // Call the incr function once more
  myObject.incr();
  console.log(myObject);
  