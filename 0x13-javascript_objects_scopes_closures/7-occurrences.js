#!/usr/bin/node

/**
 * Counts the number of occurrences of a specified element in a list.
 * @param {Array} list - The list to search for occurrences.
 * @param {*} searchElement - The element to count occurrences of.
 * @returns {number} - The number of occurrences of the specified element in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  // Use reduce to iterate over the list and count occurrences of the searchElement
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};

