#!/usr/bin/node

// Initialize a counter variable
let count = 0;

/**
 * Logs an item along with a count.
 * @param {*} item - The item to be logged.
 */
exports.logMe = function (item) {
  // Log the item along with the current count
  console.log(`${count++}: ${item}`);
};

