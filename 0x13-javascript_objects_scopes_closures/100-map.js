#!/usr/bin/node

// Importing the 'list' array from the './100-data' module
const { list } = require('./100-data');

// Logging the original 'list' array
console.log(list);

// Using the 'map' method to create a new array where each element is the product of the original element and its index
console.log(list.map((element, idx) => element * idx));

