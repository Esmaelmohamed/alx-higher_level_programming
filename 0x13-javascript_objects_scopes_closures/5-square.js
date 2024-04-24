#!/usr/bin/node

/**
 * Represents a square, which is a special case of a rectangle.
 */
class Square extends require('./4-rectangle.js') {
  /**
   * Creates a square with the given size.
   * @param {number} size - The size of the square (both width and height).
   */
  constructor(size) {
    super(size, size); // Calls the constructor of the Rectangle class with the same size for width and height
  }
}

module.exports = Square;

