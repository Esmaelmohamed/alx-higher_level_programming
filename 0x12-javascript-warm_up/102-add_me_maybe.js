#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe(number, theFunction) {
    number++;
    theFunction(number);
  }
  
  // Export the addMeMaybe function
  module.exports.addMeMaybe = addMeMaybe;
  