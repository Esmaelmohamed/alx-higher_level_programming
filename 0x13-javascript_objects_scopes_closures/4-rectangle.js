#!/usr/bin/node

/**
 * Represents a rectangle.
 */
class Rectangle {
  /**
   * Creates a rectangle with positive width and height.
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  /**
   * Prints a visual representation of the rectangle.
   */
  print() {
    // Print each row of the rectangle with 'X' characters
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
   * Rotates the rectangle by swapping its width and height.
   */
  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * Doubles the dimensions of the rectangle.
   */
  double() {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

module.exports = Rectangle;

