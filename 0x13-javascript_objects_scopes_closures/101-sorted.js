#!/usr/bin/node

// Importing the 'dict' object from the './101-data' module
const { dict } = require('./101-data');

// Converting the 'dict' object into an array of key-value pairs
const convertedArr = Object.entries(dict);

// Creating a new object to store the reversed key-value pairs
const newObj = {};

// Iterating over each key-value pair in the converted array
convertedArr.forEach(element => {
  // If the value already exists as a key in the new object, push the current key to its corresponding array
  // Otherwise, create a new array with the current key as its only element
  newObj[element[1]] ? newObj[element[1]].push(element[0]) : newObj[element[1]] = [element[0]];
});

// Logging the new object containing reversed key-value pairs
console.log(newObj);

