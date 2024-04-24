#!/usr/bin/node

/**
 * Reverses the elements of an array.
 * @param {Array} list - The array to reverse.
 * @returns {Array} - The reversed array.
 */
exports.esrever = function (list) {
  // Use reduceRight to iterate over the list in reverse order and build a new array with reversed elements
  return list.reduceRight(function (array, current) {
    array.push(current); // Add each element to the end of the new array
    return array; // Return the new array
  }, []);
};

