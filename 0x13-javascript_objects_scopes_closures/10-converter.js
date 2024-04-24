#!/usr/bin/node

/**
 * Returns a function that converts a number to a string representation in the specified base.
 * @param {number} base - The base to convert the number to (e.g., 2 for binary, 16 for hexadecimal).
 * @returns {function} - A function that converts a number to a string representation in the specified base.
 */
exports.converter = function (base) {
  // Return a function that converts a number to a string representation in the specified base
  return num => num.toString(base);
};

